#!/usr/bin/env python3
"""Check a running PHP site; optional publication fixtures use a separate docroot."""
import argparse
from collections import Counter
from datetime import date
from html import unescape
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import shutil
import subprocess
import unicodedata
from urllib.error import HTTPError
from urllib.parse import unquote, urljoin, urlsplit
from urllib.request import urlopen
import xml.etree.ElementTree as ET

HOST = 'https://ilmerastudyabroad.com'


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.links, self.canonical, self.robots, self.ids = [], [], [], set()
        self.footer_links, self.content_links = [], []
        self.footer = False
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a:
            self.ids.add(a['id'])
        if tag == 'a' and 'name' in a:
            self.ids.add(a['name'])
        if tag == 'footer':
            self.footer = True
        if tag == 'a' and 'href' in a:
            self.links.append(a['href'])
            (self.footer_links if self.footer else self.content_links).append(a['href'])
        if tag == 'link' and 'canonical' in a.get('rel', '').split():
            self.canonical.append(a.get('href', ''))
        if tag == 'meta' and a.get('name', '').lower() in ('robots', 'googlebot'):
            self.robots.append(a.get('content', ''))

    def handle_endtag(self, tag):
        if tag == 'footer':
            self.footer = False


def fetch(base, path):
    try:
        with urlopen(base.rstrip('/') + path, timeout=30) as r:
            body = r.read()
            if r.status == 200 and 'text/html' in r.headers.get('Content-Type', ''):
                from phase30.duplicates import assert_no_repeated_answer
                assert_no_repeated_answer(body.decode(), path)
            return r.status, dict(r.headers), body
    except HTTPError as e:
        return e.code, dict(e.headers), e.read()


def routes(root):
    result = {}
    posts = (root / 'includes/posts.php').read_text()
    for file in sorted(list(root.glob('*.php')) + list((root / 'blog').glob('*.php'))):
        rel = file.relative_to(root).as_posix()
        if rel == 'sitemap.php':
            continue
        path = '/' if rel == 'index.php' else '/blog/' if rel == 'blog/index.php' else '/' + rel[:-4]
        status = 'published'
        text = file.read_text()
        kind = 'page'
        thin = re.search(r'\$(destination|place)\s*=\s*[\'"]([^\'"]+)', text)
        if thin:
            kind, slug = thin.groups()
            folder = 'destinations' if kind == 'destination' else 'places'
            status = re.search(r"'status'\s*=>\s*'([^']+)'", (root / folder / (slug + '.php')).read_text()).group(1)
        elif rel.startswith('blog/') and rel != 'blog/index.php':
            slug = file.stem
            block = re.search(r"^        '" + re.escape(slug) + r"' => \[(.*?)^        \],", posts, re.S | re.M)
            assert block, 'Missing article metadata'
            status = re.search(r"'status'\s*=>\s*'([^']+)'", block[1]).group(1)
        result[path] = {'file': rel, 'status': status, 'kind': kind}
    return result


def internal_url(current, href):
    u = urlsplit(urljoin(HOST + current, href))
    if u.scheme not in ('http', 'https') or u.netloc not in ('ilmerastudyabroad.com', 'www.ilmerastudyabroad.com'):
        return None
    return unquote(u.path) or '/', unquote(u.fragment)


class PublishedContent(HTMLParser):
    """Collect public text, metadata, alt/link text and decoded JSON-LD."""
    def __init__(self, text, include_government_citations=False):
        super().__init__(convert_charrefs=True)
        self.include_government_citations = include_government_citations
        self.parts, self.script_data = [], []
        self.skip, self.ldjson, self.government_citation = None, False, False
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ('script', 'style'):
            self.skip, self.ldjson = tag, tag == 'script' and a.get('type') == 'application/ld+json'
            self.script_data = []
            return
        if tag == 'a':
            host = (urlsplit(a.get('href', '')).hostname or '').lower()
            # Only government citation anchors may retain institution names.
            self.government_citation = not self.include_government_citations and (host.endswith(('.gov.in', '.nic.in', '.gov.uk', '.gov.cz', '.mfa.gov.lv', '.esteri.it')) or host in ('gov.uk', 'education.ec.europa.eu', 'www.mzv.sk', 'mzv.sk'))
        if not self.skip and not self.government_citation:
            self.parts.extend(value for key, value in attrs if value and key in ('content', 'alt', 'title', 'aria-label', 'href', 'src'))

    def handle_data(self, text):
        if self.ldjson:
            self.script_data.append(text)
        elif not self.skip and not self.government_citation:
            self.parts.append(text)

    def handle_endtag(self, tag):
        if tag == 'script' and self.ldjson:
            self.parts.append(json.dumps(json.loads(''.join(self.script_data)), ensure_ascii=False))
        if tag == self.skip:
            self.skip, self.ldjson = None, False
        if tag == 'a':
            self.government_citation = False


# Physical-presence denials and official immigration procedures are not offers
# of ILMERA premises. Keep these narrowly scoped; do not waive whole paragraphs.
PRESENCE_SAFE_CONTEXTS = [
    r"\b(?:no|not(?: an?| any)?|without(?: an?| any)?) (?:physical |local |walk[- ]in )?office(?: or branch(?: anywhere)?)?\b",
    r"\bdoes not operate a (?:physical )?office(?: or branch(?: anywhere)?)?\b",
    r"\bdo not need to travel to an office\b",
    r"\b(?:no|not(?: an?| any)?|without(?: an?| any)?) counselling location\b",
    r"\boffice of citizenship and migration affairs\b",
    r"\bissuing[- ]office\b",
    r"\badmissions offices?\b",
    r"\b(?:international )?branch campus(?:es)?\b",
    r"\b(?:video or )?in[- ]person interview with the embassy\b",
]
PRESENCE_BLOCKED = re.compile(
    r"\b(?:offices?|branch|(?:our|local) branches|branches in|ilmera(?:'s)?(?: \w+){0,4} branches|walk[- ]?ins?|near[- ](?:you|me)|in[- ]person|"
    r"visit (?:us|ilmera|our (?:premises|branch|office))|counselling location)\b", re.I)


def physical_presence_matches(text):
    value = re.sub(r"[\s_]+", " ", unicodedata.normalize('NFKC', unescape(unquote(text)))).casefold()
    for safe in PRESENCE_SAFE_CONTEXTS:
        value = re.sub(safe, ' ', value)
    return sorted(set(m.group(0) for m in PRESENCE_BLOCKED.finditer(value)))


def blocked_name_matches(text, names):
    value = re.sub(r'[\s_]+', ' ', unicodedata.normalize('NFKC', unescape(unquote(text)))).casefold()
    # Adrex Media School is a training institute, not a university. Only the
    # exact Fawaz full bio (including matching schema/FAQ/LLM text)
    # receive an allow-entry. The university blocklist is unchanged and is
    # still checked against the complete, unmasked publication text.
    from team_bio_policy import APPROVED_BIOS
    remaining = value
    for bio in APPROVED_BIOS:
        approved = re.sub(r'[\s_]+', ' ', unicodedata.normalize('NFKC', bio)).casefold()
        remaining = remaining.replace(approved, ' ')
    hits = [name for name in names if name.casefold() != 'adrex media school' and re.search(r'(?<!\w)' + re.escape(name.casefold()) + r'(?!\w)', value)]
    if re.search(r'(?<!\w)adrex media school(?!\w)', remaining):
        hits.append('Adrex Media School')
    return hits


def blocked_names(root):
    path = root / 'tools/blocked-names.txt'
    return [line.strip() for line in path.read_text().splitlines() if line.strip() and not line.startswith('#')]


def prohibited_wording_matches(text):
    """Scan publication copy, decoded URLs and structured data consistently."""
    value = unicodedata.normalize('NFKC', unescape(unquote(text))).casefold()
    value = re.sub(r'[\s_\u2010\u2011]+', ' ', value)
    return sorted(set(m.group(0) for m in re.finditer(r'\bfree\b|\btuition[-\s]*free\b', value)))


def validate_llm_text(root, name, text):
    """Phase 18 permits edits, not policy exceptions or draft promotion."""
    from check_italy_claims import check_parts
    assert name in ('llms.txt', 'llms-full.txt'), name
    assert text.startswith('# ILMERA') and '\n## ' in text and '\n- ' in text, (name, 'Markdown structure')
    assert not blocked_name_matches(text, blocked_names(root)), (name, 'Institution name')
    assert not prohibited_wording_matches(text), (name, 'Prohibited cost wording')
    assert '\u2014' not in text, (name, 'Prohibited punctuation')
    assert not physical_presence_matches(text), (name, 'Physical-presence implication')
    assert re.search(r'\bonline[ -]only\b', text, re.I), (name, 'Explicit online-only model missing')
    assert check_parts([text]) >= 1, (name, 'Exact conditional Italy sentence missing')
    gcc = json.loads((root / 'phase14-source-review.json').read_text())['destinations']['gcc']
    for key in ('scope_note', 'review_notice'):
        assert gcc[key] in text, (name, 'GCC scope mismatch', key)
    inventory = routes(root)
    for route, info in inventory.items():
        if info['status'] == 'draft':
            assert not re.search(re.escape(HOST + route) + r'(?:[)#?\s]|$)', text), (name, 'Draft URL', route)
    policy_text = text
    scope_path = root / 'data/service-scope.json'
    if scope_path.exists() and (root / 'reports/phase-22-map.json').exists():
        scope = json.loads(scope_path.read_text())
        assert scope['reviewed_on'] == '2026-10-22'
        # Exempt only exact owner-confirmed business sentences, never a section,
        # arbitrary country prose, a partial match or a withheld route URL.
        approved = list(scope['services'].values())
        approved.append(json.loads((root / 'data/entity.json').read_text())['description'])
        for sentence in approved:
            policy_text = policy_text.replace(sentence, '')
    assert not re.search(r'\b(?:Czech Republic|Russia|Russian|APS|DSU)\b', policy_text, re.I), (name, 'Unpublished destination/article information')
    return {'content_policy': 'PASS', 'italy_exact_occurrences': check_parts([text]),
            'online_only': True, 'gcc_scope_parity': True, 'draft_information_absent': True}


def check(base, root, enforce_names=True):
    inventory = routes(root)
    pages, blocked, public_text, presence_text = {}, set(), {}, {}
    for path, info in inventory.items():
        status, headers, body = fetch(base, path)
        assert status == 200, ('Editorial route HTTP status', path, status)
        assert not re.search(rb'(Fatal error|Parse error|Warning|Notice):', body), path
        page = Page(body.decode())
        directives = page.robots + [v for k, v in headers.items() if k.lower() == 'x-robots-tag']
        noindex = any('noindex' in d.lower() for d in directives)
        if noindex or info['status'] == 'draft' or path == '/404':
            blocked.add(path)
        else:
            assert page.canonical == [HOST + path], ('Canonical mismatch', path, page.canonical)
        pages[path] = page
        public_text[path] = ' ' .join(PublishedContent(body.decode()).parts)
        presence_text[path] = ' '.join(PublishedContent(body.decode(), include_government_citations=True).parts)
    status, _, xml = fetch(base, '/sitemap.xml')
    assert status == 200, 'Sitemap HTTP status'
    tree = ET.fromstring(xml)
    urls = [e.text for e in tree.findall('.//{*}loc')]
    assert len(urls) == len(set(urls)), 'Duplicate sitemap URLs'
    expected = set(inventory) - blocked
    assert set(urls) == {HOST + p for p in expected}, 'Sitemap/editorial inventory mismatch'
    for node in tree.findall('{*}url'):
        value = node.find('{*}lastmod')
        if value is not None:
            assert date.fromisoformat(value.text) <= date.today(), 'Future lastmod'
    assert not any(urlsplit(u).path in blocked for u in urls), 'Blocked sitemap target'
    inbound = Counter()
    resources = set()
    for source, page in pages.items():
        for href in page.links:
            target = internal_url(source, href)
            if target is None:
                continue
            path, fragment = target
            if path == source and href.startswith('#'):
                if fragment:
                    assert fragment in page.ids, ('Broken in-page fragment', source, fragment)
                continue
            assert path not in blocked, ('Link to draft/noindex', source, path)
            if path in pages:
                if fragment:
                    assert fragment in pages[path].ids, ('Broken fragment', source, path, fragment)
                if source != path:
                    inbound[path] += 1
            else:
                resources.add(path)
    for path in resources:
        status, headers, _ = fetch(base, path)
        assert status == 200, ('Broken internal resource', path, status)
        assert 'noindex' not in ' '.join(v for k, v in headers.items() if k.lower() == 'x-robots-tag').lower(), path
    for name in ['llms.txt', 'llms-full.txt']:
        status, _, body = fetch(base, '/' + name)
        assert status == 200, ('Public discovery text status', name, status)
        text = body.decode()
        validate_llm_text(root, name, text)
        public_text['/' + name] = text
        presence_text['/' + name] = text
        for target in blocked:
            assert not re.search(re.escape(HOST + target) + r'(?:[)#?\s]|$)', text), ('LLM link to withheld page', name, target)
    assert all(inbound[p] > 0 for p in expected), 'Indexable orphan'
    status, _, robots = fetch(base, '/robots.txt')
    assert status == 200 and ('Sitemap: ' + HOST + '/sitemap.xml').encode() in robots
    assert not re.search(rb'^Disallow:\s*(?:/\s*$|/sitemap)', robots, re.M), 'Sitemap blocked by robots'
    presence_failures = {path: hits for path, text in presence_text.items() if path not in blocked
                         and (hits := physical_presence_matches(text))}
    assert not presence_failures, ('Physical-presence phrases in published content', presence_failures)
    wording_failures = {path: hits for path, text in presence_text.items() if path not in blocked
                        and (hits := prohibited_wording_matches(text))}
    assert not wording_failures, ('Prohibited wording in published content', wording_failures)
    if enforce_names:
        names = blocked_names(root)
        failures = {path: hits for path, text in public_text.items() if path not in blocked
                    and (hits := blocked_name_matches(text, names))}
        assert not failures, ('Blocked institution names in published content', failures)
    from build_llms_directory import check as check_llm_directory
    llm_directory = check_llm_directory(base, root)
    return {'sitemap': urls, 'indexable': len(expected), 'blocked': len(blocked), 'routes': len(inventory), 'llm_directory': llm_directory}, pages


def assert_visibility(base, target, visible):
    _, _, xml = fetch(base, '/sitemap.xml')
    assert ((HOST + target).encode() in xml) == visible, 'Fixture sitemap visibility'
    for source in ['/', '/services', '/about', '/contact']:
        _, _, body = fetch(base, source)
        page = Page(body.decode())
        footer = {internal_url(source, h) for h in page.footer_links}
        content = {internal_url(source, h) for h in page.content_links}
        assert ((target, '') in footer) == visible, 'Fixture footer visibility'
        if source in ['/', '/services'] or target.startswith('/study-abroad-') and source == '/contact':
            assert ((target, '') in content) == visible, 'Fixture content visibility'
    if visible:
        _, _, body = fetch(base, target)
        page = Page(body.decode())
        targets = {internal_url(target, h) for h in page.content_links}
        assert ('/services', '') in targets and ('/contact', '') in targets, 'Missing contextual back-links'


def fixtures(base, root, fixture_root):
    assert fixture_root.resolve() != root.resolve(), 'Fixture must have a separate docroot'
    fixture_root.mkdir(parents=True, exist_ok=True)
    for file in root.rglob('*'):
        if file.is_file() and not any(p in ('.git', 'tools') for p in file.relative_to(root).parts):
            target = fixture_root / file.relative_to(root)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(file, target)
    destination = fixture_root / 'destinations/germany.php'
    location = fixture_root / 'places/karnataka.php'
    entry = fixture_root / 'study-abroad-consultants-in-karnataka.php'
    originals = {p: p.read_bytes() for p in [destination, location, entry]}
    durl, lurl = '/study-in-germany', '/study-abroad-consultants-in-karnataka'
    try:
        check(base, fixture_root)
        assert_visibility(base, durl, True)
        assert_visibility(base, lurl, True)
        destination.write_bytes(originals[destination].replace(b"'status' => 'published'", b"'status' => 'draft'", 1))
        assert_visibility(base, durl, False)
        check(base, fixture_root)
        destination.write_bytes(originals[destination])
        assert_visibility(base, durl, True)
        changed = originals[destination].replace(b"'text' => '", b"'text' => 'Changed claim. ", 1)
        assert changed != originals[destination]
        destination.write_bytes(changed)
        assert_visibility(base, durl, False)
        check(base, fixture_root)
        destination.write_bytes(originals[destination])
        location.write_bytes(originals[location].replace(b"'status' => 'published'", b"'status' => 'draft'", 1))
        assert_visibility(base, lurl, False)
        check(base, fixture_root)
        location.write_bytes(originals[location])
        assert_visibility(base, lurl, True)
        entry.write_bytes(originals[entry].replace(b'include __DIR__', b"header('X-Robots-Tag: noindex, follow');\ninclude __DIR__", 1))
        assert_visibility(base, lurl, False)
        check(base, fixture_root)
        entry.write_bytes(originals[entry])
        assert_visibility(base, lurl, True)
        changed = originals[location].replace(b"'intro_answer' => '", b"'intro_answer' => 'Changed wording. ", 1)
        assert changed != originals[location]
        location.write_bytes(changed)
        assert_visibility(base, lurl, False)
        check(base, fixture_root)
        location.write_bytes(originals[location])
        article = fixture_root / 'blog/cost-of-studying-abroad-for-indian-students.php'
        article_original = article.read_bytes()
        try:
            article.write_bytes(article_original + b"\n<!-- Isolated evidence mismatch -->\n")
            assert_visibility(base, '/blog/cost-of-studying-abroad-for-indian-students', False)
            check(base, fixture_root)
        finally:
            article.write_bytes(article_original)
        posts_file = fixture_root / 'includes/posts.php'
        posts_original = posts_file.read_text()
        try:
            changed = posts_original
            for held in ['study-in-germany-free-aps-certificate', 'italy-dsu-scholarship-eligibility']:
                pattern = r"(^        '" + re.escape(held) + r"' => \[.*?^        \],)"
                changed = re.sub(pattern, lambda m: m[0].replace("'status' => 'draft'", "'status' => 'published'", 1), changed, count=1, flags=re.S | re.M)
            posts_file.write_text(changed)
            for held in ['study-in-germany-free-aps-certificate', 'italy-dsu-scholarship-eligibility']:
                assert_visibility(base, '/blog/' + held, False)
            check(base, fixture_root)
        finally:
            posts_file.write_text(posts_original)
        assert_visibility(base, lurl, True)
        assert_visibility(base, durl, True)
        check(base, fixture_root)
    finally:
        for p, value in originals.items():
            p.write_bytes(value)
    print('PASS isolated status, source mismatch, cohort mismatch, noindex header and article mismatch/revert')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base-url', required=True)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--fixture-base-url')
    parser.add_argument('--fixture-root', type=Path)
    args = parser.parse_args()
    result, _ = check(args.base_url, args.root)
    print(json.dumps(result, indent=2))
    if args.fixture_base_url or args.fixture_root:
        assert args.fixture_base_url and args.fixture_root, 'Both fixture options are required'
        fixtures(args.fixture_base_url, args.root, args.fixture_root)
    print('PASS HTTP statuses, canonicals, robots, sitemap coverage, inbound links, internal targets and fragments')


if __name__ == '__main__':
    main()
