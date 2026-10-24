#!/usr/bin/env python3
"""Inventory citations without a destination-host allowlist masking legacy links.

This opens local published pages, not their external citations. External raw HTTP
status and substantive source verification must be recorded separately. An unknown
non-social external host is included for review, never silently approved/dropped.
"""
import argparse
import json
import re
from collections import defaultdict
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
import check_discovery as discovery

# Contact, social profiles and the existing owner-biography attribution are not
# factual study-rule citations. These exclusions do not approve source hosts.
NON_CITATION_HOSTS = {'wa.me', 'facebook.com', 'instagram.com', 'linkedin.com', 'fawazbhseo.in'}


def external_reference(url):
    host = (urlsplit(url).hostname or '').lower().removeprefix('www.')
    return url.startswith('https://') and host not in NON_CITATION_HOSTS | {'ilmerastudyabroad.com'}


class References(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.urls = set()
        self.json_text = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'a' and external_reference(attrs.get('href', '')):
            self.urls.add(attrs['href'])
        if tag == 'script' and attrs.get('type') == 'application/ld+json':
            self.json_text = ''

    def handle_data(self, data):
        if self.json_text is not None:
            self.json_text += data

    def handle_endtag(self, tag):
        if tag == 'script' and self.json_text is not None:
            def walk(value, citation=False):
                if isinstance(value, dict):
                    for key, item in value.items():
                        walk(item, citation or key == 'citation')
                elif isinstance(value, list):
                    for item in value:
                        walk(item, citation)
                elif citation and isinstance(value, str) and external_reference(value):
                    self.urls.add(value)
            walk(json.loads(self.json_text))
            self.json_text = None


def inventory(base, root):
    references = defaultdict(set)
    for route, info in discovery.routes(root).items():
        if info['status'] == 'draft' or route == '/404':
            continue
        status, _, body = discovery.fetch(base, route)
        assert status == 200, (route, status)
        parser = References()
        parser.feed(body.decode())
        for url in parser.urls:
            references[url].add(route)
    for name in ('llms.txt', 'llms-full.txt'):
        status, _, body = discovery.fetch(base, '/' + name)
        assert status == 200, (name, status)
        for raw in re.findall(r'https://[^\s<>]+', body.decode()):
            url = raw.rstrip(').,;')
            if external_reference(url):
                references[url].add('/' + name)
    return [{'url': url, 'routes': sorted(routes)} for url, routes in sorted(references.items())]


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--base-url', default='http://127.0.0.1:8080')
    p.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    p.add_argument('--output', type=Path)
    args = p.parse_args()
    content = json.dumps(inventory(args.base_url.rstrip('/'), args.root), indent=2) + '\n'
    if args.output:
        args.output.write_text(content)
    else:
        print(content, end='')
