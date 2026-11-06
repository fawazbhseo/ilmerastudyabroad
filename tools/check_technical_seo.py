#!/usr/bin/env python3
"""Audit fresh HTML, breadcrumbs, headings, images and click depth locally."""
import argparse
from collections import deque
from html.parser import HTMLParser
import json
from pathlib import Path
from urllib.parse import urljoin, urlsplit

from check_discovery import HOST, Page, fetch, routes, internal_url


class Technical(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.main, self.level = False, 0
        self.images, self.headings, self.crumbs, self.graphs, self.stylesheets = [], [], [], [], []
        self.breadcrumb = False
        self.crumb = None
        self.json_script, self.buffer = False, []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'main': self.main = True
        if self.main and tag in ('h1','h2','h3','h4','h5','h6'):
            level = int(tag[1]); assert level <= self.level + 1, ('Skipped heading level', tag)
            self.level = level; self.headings.append(level)
        if tag == 'img': self.images.append(a)
        if tag == 'link' and a.get('rel') == 'stylesheet': self.stylesheets.append(a.get('href',''))
        if tag == 'nav' and a.get('aria-label') == 'Breadcrumb': self.breadcrumb = True
        if self.breadcrumb and tag in ('a','span'):
            self.crumb = {'name':'', 'href':a.get('href')}; self.crumbs.append(self.crumb)
        if tag == 'script' and a.get('type') == 'application/ld+json': self.json_script, self.buffer = True, []

    def handle_data(self, text):
        if self.crumb is not None: self.crumb['name'] += text
        if self.json_script: self.buffer.append(text)

    def handle_endtag(self, tag):
        if tag == 'main': self.main = False
        if tag == 'nav': self.breadcrumb = False
        if tag in ('a','span'): self.crumb = None
        if tag == 'script' and self.json_script:
            value = json.loads(''.join(self.buffer)); self.graphs.extend(value.get('@graph',[value])); self.json_script = False


def check(base, root):
    inventory = routes(root)
    published = {p for p,i in inventory.items() if i['status'] == 'published' and p != '/404'}
    edges, images, font_sources = {}, 0, set()
    for route in sorted(published):
        status, headers, body = fetch(base, route)
        assert status == 200, route
        html = body.decode(); page = Page(html); technical = Technical(html)
        assert page.canonical == [HOST + route], (route, 'Self-canonical')
        assert technical.headings.count(1) == 1 and technical.headings[0] == 1, (route, 'One H1')
        assert not any('noindex' in r.lower() for r in page.robots), (route, 'Published noindex')
        crumbs = [g for g in technical.graphs if g.get('@type') == 'BreadcrumbList']
        assert len(crumbs) == 1, (route, 'One breadcrumb graph')
        items = crumbs[0]['itemListElement']
        assert len(items) == len(technical.crumbs), (route, 'Breadcrumb length')
        for pos, (item, visible) in enumerate(zip(items, technical.crumbs), 1):
            assert item['position'] == pos and item['name'] == visible['name'].strip(), (route, 'Breadcrumb label/order')
            assert item['item'] == (urljoin(HOST + route, visible['href']) if visible['href'] else HOST + route), (route, 'Breadcrumb URL')
        for index, image in enumerate(technical.images):
            assert image.get('alt','').strip(), (route, 'Image alt')
            assert int(image.get('width',0)) > 0 and int(image.get('height',0)) > 0, (route, 'Image dimensions')
            if index > 0: assert image.get('loading') == 'lazy', (route, 'Below-brand image loading', image.get('src'))
            images += 1
        font_sources.update(u for u in technical.stylesheets if u.startswith('https://'))
        edges[route] = {t[0] for href in page.links if (t := internal_url(route, href)) and t[0] in published}
    distance, pending = {'/':0}, deque(['/'])
    while pending:
        source = pending.popleft()
        for target in edges[source]:
            if target not in distance: distance[target] = distance[source] + 1; pending.append(target)
    assert set(distance) == published and max(distance.values()) <= 3, ('Click depth/orphan', distance)
    return {'pages':len(published),'heading_order':'PASS','breadcrumb_visible_schema_parity':'PASS',
            'image_instances':images,'image_alt_dimensions_loading':'PASS',
            'max_click_depth':max(distance.values()),'orphans':0,'canonical_targets_direct_200':True,
            'existing_external_font_stylesheets':sorted(font_sources),
            'native_redirect_chains_verified':False,'live_performance_verified':False}


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--base-url', required=True)
    p.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    p.add_argument('--report', type=Path)
    args = p.parse_args(); result = check(args.base_url, args.root)
    if args.report: args.report.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS',json.dumps(result))
