#!/usr/bin/env python3
"""Check a running PHP site; optional publication fixtures use a separate docroot."""
import argparse
from collections import Counter
from datetime import date
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import shutil
import subprocess
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
            return r.status, dict(r.headers), r.read()
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


def expected_llm_bytes(root, name):
    """Phase 16 permits only removal of the two withheld-article link lines."""
    before = subprocess.check_output(['git', 'show', 'c2c8b9f:' + name], cwd=root)
    held = [b'https://ilmerastudyabroad.com/blog/study-in-germany-free-aps-certificate',
            b'https://ilmerastudyabroad.com/blog/italy-dsu-scholarship-eligibility']
    return b''.join(line for line in before.splitlines(keepends=True)
                    if not any(url in line for url in held))


def check(base, root):
    inventory = routes(root)
    pages, blocked = {}, set()
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
        for target in blocked:
            assert not re.search(re.escape(HOST + target) + r'(?:[)#?\s]|$)', text), ('LLM link to withheld page', name, target)
    assert all(inbound[p] > 0 for p in expected), 'Indexable orphan'
    status, _, robots = fetch(base, '/robots.txt')
    assert status == 200 and ('Sitemap: ' + HOST + '/sitemap.xml').encode() in robots
    assert not re.search(rb'^Disallow:\s*(?:/\s*$|/sitemap)', robots, re.M), 'Sitemap blocked by robots'
    return {'sitemap': urls, 'indexable': len(expected), 'blocked': len(blocked), 'routes': len(inventory)}, pages


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
