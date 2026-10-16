#!/usr/bin/env python3
"""Maintain published-page LLM entries from actual rendered title/description.

No existing LLM generator preceded Phase 18. Only directory entries are rebuilt;
the document structure, policy copy and owner caveats remain hand-maintained.
"""
import argparse
import json
from html.parser import HTMLParser
from pathlib import Path
import re
from urllib.parse import urlsplit

from check_discovery import HOST, Page, fetch, routes, validate_llm_text


class Metadata(HTMLParser):
    def __init__(self, html):
        super().__init__(convert_charrefs=True)
        self.title, self.descriptions, self.in_title = [], [], False
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'title':
            self.in_title = True
        if tag == 'meta' and a.get('name', '').lower() == 'description':
            self.descriptions.append(a.get('content', ''))

    def handle_endtag(self, tag):
        if tag == 'title':
            self.in_title = False

    def handle_data(self, text):
        if self.in_title:
            self.title.append(text)


def directory_entries(base, root):
    result = []
    for route, info in routes(root).items():
        if info['status'] != 'published' or route == '/404':
            continue
        kind = ('destination' if info['kind'] == 'destination' else
                'location' if info['kind'] == 'place' else
                'blog' if route.startswith('/blog/') and route != '/blog/' else
                'index' if route in ('/blog/', '/all-pages') else None)
        if kind is None:
            continue  # Existing company/services/contact/legal URLs are retained.
        status, headers, body = fetch(base, route)
        page, meta = Page(body.decode()), Metadata(body.decode())
        assert status == 200 and page.canonical == [HOST + route], (route, 'Status/canonical')
        directives = page.robots + [v for k, v in headers.items() if k.lower() == 'x-robots-tag']
        assert not any('noindex' in d.lower() for d in directives), (route, 'Not indexable')
        title = ''.join(meta.title)
        assert title and len(meta.descriptions) == 1 and meta.descriptions[0], (route, 'Missing metadata')
        assert not any(c in title for c in '\n[]') and '\n' not in meta.descriptions[0], route
        result.append({'route': route, 'kind': kind, 'title': title,
                       'description': meta.descriptions[0],
                       'line': '- [' + title + '](' + HOST + route + '): ' + meta.descriptions[0]})
    return result


def section(text, heading, content):
    """Replace one existing section body, leaving heading/order intact."""
    start = text.index(heading) + len(heading)
    end = text.find('\n---\n', start)
    if end < 0:
        end = len(text)
    return text[:start] + '\n\n' + content.rstrip() + '\n' + text[end:]


def rebuild(text, name, entries):
    by_route = {row['route']: row for row in entries}
    for row in entries:
        if row['kind'] != 'destination':
            continue
        slug = row['route'].removeprefix('/study-in-')
        if name == 'llms.txt':
            labels = {'germany': 'Germany:', 'italy': 'Italy:', 'uk': 'United Kingdom:',
                      'lithuania': 'Lithuania:', 'latvia': 'Latvia:', 'slovakia': 'Slovakia:', 'gcc': 'GCC Countries:'}
            heading = '### ' + labels[slug]
        else:
            labels = {'germany': 'Germany', 'italy': 'Italy', 'uk': 'UK', 'lithuania': 'Lithuania',
                      'latvia': 'Latvia', 'slovakia': 'Slovakia', 'gcc': 'GCC'}
            match = re.search(r'^### 4\.\d+ ' + re.escape(labels[slug]) + r'[^\n]*', text, re.M)
            assert match, ('Missing country section', slug)
            heading = match[0]
        start = text.index(heading)
        end = text.find('\n### ', start + 1)
        if end < 0:
            end = text.index('\n---\n', start)
        block = text[start:end]
        if name == 'llms.txt':
            block, count = re.subn(r'^- \[[^\n]+\]\(https://ilmerastudyabroad\.com/[^)\n]+\)(?::[^\n]*)?$',
                                   lambda _: row['line'], block, count=1, flags=re.M)
            assert count == 1, (slug, 'Missing original destination entry')
        else:
            lines = block.splitlines()
            if len(lines) > 1 and lines[1].startswith('- ['):
                lines[1] = row['line']
            else:
                lines.insert(1, row['line'])
            block = '\n'.join(lines) + ('\n' if block.endswith('\n') else '')
        text = text[:start] + block + text[end:]
    locations = '\n'.join(r['line'] for r in entries if r['kind'] == 'location')
    blog = '\n'.join([by_route['/blog/']['line']] + [r['line'] for r in entries if r['kind'] == 'blog'])
    index = by_route['/all-pages']['line']
    if name == 'llms.txt':
        if '## Location Guides\n' not in text:
            text = text.replace('## Blog (guides for Indian students)', '## Location Guides\n\n' + locations + '\n\n---\n\n## Blog (guides for Indian students)', 1)
        else:
            text = section(text, '## Location Guides', locations)
        text = section(text, '## Blog (guides for Indian students)', blog)
        if '\n## Page Index\n' not in text:
            text = text.rstrip() + '\n\n---\n\n## Page Index\n\n' + index + '\n'
        else:
            text = section(text, '## Page Index', index)
    else:
        for heading, body in [('## 8. Published Location Guides', locations),
                              ('## 9. Published Blog Guides', blog), ('## 10. Page Index', index)]:
            if heading + '\n' not in text:
                text = text.rstrip() + '\n\n---\n\n' + heading + '\n\n' + body + '\n'
            else:
                text = section(text, heading, body)
    return text


def linked_routes(text):
    return {urlsplit(url.rstrip('.,;')).path or '/' for url in
            re.findall(re.escape(HOST) + r'(?:/[^\s)]*)?', text)}


def validate_directory(text, entries, inventory):
    for row in entries:
        assert text.count(row['line']) == 1, (row['route'], 'Missing, stale or duplicate title/description entry')
    # /blog is an existing alias; new entries must use the canonical /blog/.
    expected = {route for route, info in inventory.items() if info['status'] == 'published' and route != '/404'}
    assert expected <= linked_routes(text), ('Missing published URLs', sorted(expected - linked_routes(text)))
    return {'metadata_entries': len(entries), 'published_urls': len(expected),
            'destinations': sum(r['kind'] == 'destination' for r in entries),
            'locations': sum(r['kind'] == 'location' for r in entries),
            'blog_articles': sum(r['kind'] == 'blog' for r in entries)}


def entity_reference(root):
    data = json.loads((root / 'data/entity.json').read_text())
    return '\n\n---\n\n## Canonical entity reference\n\n' + data['description'] + '\n\n' + '\n'.join('- ' + item for item in data['services']) + '\n\n' + data['countries_note'] + '\n'


def rebuild_entity(text, root):
    marker = '\n\n---\n\n## Canonical entity reference\n'
    if marker in text:
        text = text.split(marker, 1)[0]
    return text.rstrip() + entity_reference(root)


def check(base, root):
    entries, inventory = directory_entries(base, root), routes(root)
    result = {}
    for name in ('llms.txt', 'llms-full.txt'):
        status, _, body = fetch(base, '/' + name)
        assert status == 200 and body == (root / name).read_bytes(), (name, 'Served parity')
        result[name] = validate_directory(body.decode(), entries, inventory)
        if (root / 'data/entity.json').exists():
            assert body.decode().endswith(entity_reference(root)), (name, 'Canonical entity mismatch')
    return result


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--base-url', required=True)
    p.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    p.add_argument('--write', action='store_true', help='Update only the directory entries in both files')
    args = p.parse_args()
    entries, inventory = directory_entries(args.base_url, args.root), routes(args.root)
    for name in ('llms.txt', 'llms-full.txt'):
        path = args.root / name
        raw = path.read_bytes()
        assert b'\r' not in raw, (name, 'Expected existing LF format')
        before = raw.decode()
        after = rebuild(before, name, entries)
        if (args.root / 'data/entity.json').exists():
            after = rebuild_entity(after, args.root)
        validate_llm_text(args.root, name, after)
        validate_directory(after, entries, inventory)
        if args.write:
            path.write_bytes(after.encode())
        else:
            assert before == after, (name, 'Directory needs regeneration; review then use --write')
    print('PASS', check(args.base_url, args.root))


if __name__ == '__main__':
    main()
