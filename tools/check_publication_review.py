#!/usr/bin/env python3
"""Audit all clean routes, structured data, source policies and authorized LLM content."""
import argparse
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import subprocess
from urllib.parse import urlsplit

from check_discovery import HOST, Page, check, validate_llm_text, fetch, routes


class Content(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.graphs, self.visible, self.buffer = [], [], []
        self.script, self.style, self.in_script = False, False, False
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'script':
            self.in_script = True
            self.script = a.get('type') == 'application/ld+json'
            self.buffer = []
        if tag == 'style':
            self.style = True

    def handle_endtag(self, tag):
        if tag == 'script':
            if self.script:
                value = json.loads(''.join(self.buffer))
                self.graphs.extend(value.get('@graph', [value]))
            self.script = False
            self.in_script = False
        if tag == 'style':
            self.style = False

    def handle_data(self, text):
        if self.script:
            self.buffer.append(text)
        elif not self.style and not self.in_script:
            self.visible.append(text)


def approved(url, hosts):
    u = urlsplit(url)
    h = (u.hostname or '').lower()
    return u.scheme == 'https' and not u.username and not u.password and (
        h.endswith('.gov.in') or h.endswith('.nic.in') or
        any(h == x or h.endswith('.' + x) for x in hosts))


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--base-url', required=True)
    p.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    p.add_argument('--report', type=Path)
    args = p.parse_args()
    root = args.root
    result, _ = check(args.base_url, root)
    checked = []
    for route, info in routes(root).items():
        status, headers, body = fetch(args.base_url, route)
        page, content = Page(body.decode()), Content(body.decode())
        assert status == 200, route
        if route != '/404':
            assert page.canonical == [HOST + route], (route, 'self canonical')
        noindex = any('noindex' in d.lower() for d in page.robots + [v for k, v in headers.items() if k.lower() == 'x-robots-tag'])
        assert noindex == (info['status'] == 'draft' or route == '/404'), (route, 'publication/robots mismatch')
        assert '\u2014' not in ''.join(content.visible), (route, 'visible punctuation')
        for graph in content.graphs:
            assert graph.get('@type'), (route, 'schema type')
            if info['kind'] == 'place' and graph['@type'] == 'Service':
                assert graph['provider']['telephone'] == '+919019557427', route
                assert graph['provider']['@id'] == HOST + '/#organization', route
                assert 'address' not in graph and 'address' not in graph['provider'], route
        if info['kind'] == 'place':
            assert any(g['@type'] == 'Service' for g in content.graphs), route
        checked.append({'route': route, 'status': status, 'indexable': not noindex, 'self_canonical': page.canonical == [HOST + route], 'utility': route == '/404', 'schema_graphs': len(content.graphs)})
    destination = json.loads((root / 'phase14-source-review.json').read_text())
    for slug, entry in destination['destinations'].items():
        for row in entry['retained_line_reviews']:
            assert row['confirmed_text'] and row['checked_on'] == '2026-10-16', (slug, row)
            assert approved(row['source_url'], destination['approved_hosts'][slug]), (slug, row)
    articles = json.loads((root / 'phase14-article-review.json').read_text())
    for slug, entry in articles['articles'].items():
        assert hashlib.sha256((root / 'blog' / (slug + '.php')).read_bytes()).hexdigest() == entry['file_sha256'], slug
        for source in entry['sources']:
            assert approved(source['url'], articles['approved_hosts']), (slug, source)
        if entry['verified']:
            assert not entry['failed_gates'] and all(c['verified'] and c['source_urls'] for c in entry['retained_claims']), slug
    llm_checks = {}
    for name in ['llms.txt', 'llms-full.txt']:
        now = (root / name).read_bytes()
        status, _, served = fetch(args.base_url, '/' + name)
        assert status == 200 and served == now, (name, 'Served/working copy parity')
        llm_checks[name] = validate_llm_text(root, name, now.decode())
        llm_checks[name]['sha256'] = hashlib.sha256(now).hexdigest()
    snapshot = (root / 'sitemap.xml').read_bytes()
    assert snapshot == fetch(args.base_url, '/sitemap.xml')[2], 'Static/runtime sitemap mismatch'
    output = {'checked_on': '2026-10-16', 'environment': 'PHP 8.5 WASM HTTP adapter, not native Apache', 'discovery': result, 'routes': checked, 'llm_content_checks': llm_checks, 'sitemap_snapshot_matches_runtime': True}
    if args.report:
        args.report.write_text(json.dumps(output, indent=2)+'\n')
    print('PASS', len(checked)-1, 'editorial self-canonicals;', len(checked), 'route status/robots, JSON-LD, Service contact, visible punctuation, approved source records, LLM content policy/served parity and sitemap parity')


if __name__ == '__main__':
    main()
