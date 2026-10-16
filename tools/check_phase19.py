#!/usr/bin/env python3
"""Phase 19 rendered metadata, policy and preservation checks."""
import argparse
import json
from pathlib import Path
import re
import subprocess
from html.parser import HTMLParser

from check_discovery import fetch, routes, PublishedContent


class Surface(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.titles, self.h1s, self.openings, self.descriptions = [], [], [], []
        self.direct = []
        self.target = None
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ('title', 'h1'):
            self.target = self.titles if tag == 'title' else self.h1s
            self.target.append('')
        if tag == 'p' and a.get('class') == 'seo-opening':
            self.target = self.openings
            self.target.append('')
        if tag == 'p' and a.get('class') == 'direct-answer':
            self.target = self.direct
            self.target.append('')
        if tag == 'meta' and a.get('name') == 'description':
            self.descriptions.append(a.get('content'))

    def handle_data(self, text):
        if self.target is not None:
            self.target[-1] += text

    def handle_endtag(self, tag):
        if tag in ('title', 'h1', 'p'):
            self.target = None


def check(base, root):
    mapping = json.loads((root / 'data/seo-map.json').read_text())
    inventory = routes(root)
    expected = {p for p, i in inventory.items() if i['status'] == 'published' and p != '/404'}
    assert set(mapping) == expected, 'Mapping must cover every published page only'
    seen_titles, seen_desc = set(), set()
    for path, entry in mapping.items():
        status, _, body = fetch(base, path)
        assert status == 200, path
        html = body.decode()
        surface = Surface(html)
        assert surface.titles == [entry['title']] and len(entry['title']) < 60, (path, 'Title')
        assert surface.descriptions == [entry['description']] and len(entry['description']) < 155, (path, 'Description')
        assert surface.h1s == [entry['h1']] and entry['primary'].casefold() in entry['h1'].casefold(), (path, 'H1')
        assert surface.openings == [entry['opening']] and entry['primary'].casefold() in entry['opening'].casefold(), (path, 'Opening')
        assert entry['title'] not in seen_titles and entry['description'] not in seen_desc, (path, 'Duplicate metadata')
        seen_titles.add(entry['title']); seen_desc.add(entry['description'])
        if (root / 'data/answer-map.json').exists() and entry['kind'] in ('place', 'destination', 'article'):
            assert len(surface.direct) == 1 and 40 <= len(surface.direct[0].split()) <= 60, (path, 'Direct answer')
            assert len(re.findall(r'<details class="il-faq"', html)) >= 4, (path, 'Four visible FAQs')
        if (root / 'data/entity.json').exists():
            graphs = []
            for raw in re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.S):
                value = json.loads(raw); graphs.extend(value.get('@graph', [value]))
            orgs = [g for g in graphs if g.get('@type') == 'Organization' and g.get('@id') == 'https://ilmerastudyabroad.com/#organization']
            entity = json.loads((root / 'data/entity.json').read_text())
            assert len(orgs) == 1, (path, 'One canonical Organization')
            for key in ('name','url','logo','description','areaServed','sameAs'):
                assert orgs[0][key] == entity[key], (path, key)
            assert orgs[0]['telephone'] == '+919019557427' and orgs[0]['knowsAbout'] == entity['services'], path
            if entry['kind'] in ('destination','article'):
                assert '<time datetime="2026-10-16">' in html, (path, 'Visible review date')
                for g in graphs:
                    if g.get('@type') in ('WebPage','Article','BlogPosting'):
                        assert g.get('dateModified') == '2026-10-16', (path, 'Review/schema date parity')
        text = ' '.join(PublishedContent(html, include_government_citations=True).parts)
        assert not re.search(r'\bILMERA(?: Study Abroad)?\s+(?:is\s+)?(?:India.s\s+|the\s+)?(?:best|top|leading|no\.?\s*1)\b', text, re.I), (path, 'Superlative claim')
        assert not re.search(r'"(?:aggregateRating|@type"\s*:\s*"(?:Review|LocalBusiness))', html), (path, 'Disallowed proof schema')
    for file in (root / 'destinations').glob('*.php'):
        assert file.read_bytes() == subprocess.check_output(['git', 'show', 'a083aff:destinations/' + file.name], cwd=root), ('Destination data changed', file)
    return {'published_pages': len(mapping), 'unique_short_metadata': True, 'one_h1': True,
            'primary_in_heading_and_opening': True, 'destination_data_byte_identical': True}


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--base-url', required=True)
    p.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    args = p.parse_args()
    print('PASS', check(args.base_url, args.root))
