#!/usr/bin/env python3
"""Independent policy checks on the just-captured full-suite render set."""
import argparse
from html.parser import HTMLParser
import json
from pathlib import Path
import re

from check_discovery import PublishedContent, blocked_name_matches, blocked_names, prohibited_wording_matches


class Graphs(HTMLParser):
    def __init__(self, html):
        super().__init__(convert_charrefs=True)
        self.graphs, self.buffer, self.collect = [], [], False
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        if tag == 'script' and dict(attrs).get('type') == 'application/ld+json': self.collect, self.buffer = True, []

    def handle_data(self, text):
        if self.collect: self.buffer.append(text)

    def handle_endtag(self, tag):
        if tag == 'script' and self.collect:
            self.graphs.append(json.loads(''.join(self.buffer))); self.collect = False


def allowed_schema(value):
    if isinstance(value, dict):
        assert 'aggregateRating' not in value and 'review' not in value, 'Disallowed rating/review property'
        types = value.get('@type', [])
        if isinstance(types, str): types = [types]
        assert not set(types) & {'Review','AggregateRating','LocalBusiness'}, 'Disallowed schema type'
        for item in value.values(): allowed_schema(item)
    elif isinstance(value, list):
        for item in value: allowed_schema(item)


def check(root, captures):
    snapshots = json.loads((captures / 'snapshots.json').read_text())
    public = 0
    for path, item in snapshots.items():
        if item['info']['status'] != 'published' or path == '/404': continue
        html = (captures / item['file']).read_text()
        parts = ' '.join(PublishedContent(html).parts)
        assert not blocked_name_matches(parts, blocked_names(root)), (path, 'Institution aliases')
        assert not prohibited_wording_matches(' '.join(PublishedContent(html, include_government_citations=True).parts)), (path, 'Wording')
        assert '\u2014' not in html, (path, 'Punctuation')
        for graph in Graphs(html).graphs: allowed_schema(graph)
        public += 1
    assert public == 38, ('Unexpected publication cohort', public)
    prompts = ' '.join((root / 'reports/prompt-map.md').read_text().split())
    assert 'Document prompt inventory: unknown' in prompts and 'No AI prompts are fabricated' in prompts
    assert 'fee' in prompts.lower() and 'gap' in prompts and 'No public fee schedule' in prompts
    assert '3 answered, 0 partly answered, 1 gap' in prompts
    identity = json.loads((root / 'data/entity.json').read_text())
    for name in ('llms.txt','llms-full.txt'):
        text = (root / name).read_text()
        assert identity['description'] in text and all('- '+s in text for s in identity['services']), name
    return {'published_captures':public,'recursive_schema_policy':'PASS','names_wording_punctuation':'PASS',
            'prompt_status_reasons':'PASS','canonical_entity_llm_parity':'PASS',
            'strategy_prompt_inventory':'unknown; owner source access required',
            'external_http_status_verified':False,'live_rankings_verified':False}


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--captures', type=Path, required=True)
    p.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    args = p.parse_args(); print('PASS',json.dumps(check(args.root,args.captures)))
