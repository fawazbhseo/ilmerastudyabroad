#!/usr/bin/env python3
"""Compare the current PHP-WASM route captures with the frozen Phase31b renders."""
from __future__ import annotations
import argparse
import gzip
import hashlib
from html.parser import HTMLParser
import json
import pathlib
import subprocess
import sys
import unicodedata

ROOT = pathlib.Path(__file__).resolve().parents[2]
BASE_INDEX = ROOT / 'reports/phase-32-before-render-index.json'
BASE_ARCHIVE = ROOT / 'reports/phase-32-before-renders.json.gz'


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def norm_text(parts) -> str:
    return ' '.join(unicodedata.normalize('NFC', ' '.join(parts)).split())


class RenderFacts(HTMLParser):
    def __init__(self, text: str):
        super().__init__(convert_charrefs=True)
        self.text_parts = []
        self.links = []
        self.images = []
        self.picture_sources = []
        self.json_ld = []
        self._ignore_depth = 0
        self._script_kind = None
        self._script_buffer = []
        self._anchor = None
        self._title_depth = 0
        self._title = []
        self._heading = None
        self.headings = []
        self.feed(text)
        self.close()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'script':
            self._script_kind = 'jsonld' if attrs.get('type', '').lower() == 'application/ld+json' else 'other'
            self._script_buffer = []
            if self._script_kind != 'jsonld':
                self._ignore_depth += 1
        elif tag in ('style', 'noscript', 'template'):
            self._ignore_depth += 1
        if tag == 'title':
            self._title_depth += 1
        if tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
            self._heading = {'tag': tag, 'parts': []}
        if tag == 'a':
            self._anchor = {
                'href': attrs.get('href'),
                'rel': attrs.get('rel'),
                'target': attrs.get('target'),
                'aria_label': attrs.get('aria-label'),
                'parts': [],
            }
        if tag == 'img':
            self.images.append({key: attrs.get(key) for key in ('src', 'srcset', 'sizes', 'alt', 'width', 'height')})
        if tag == 'source':
            self.picture_sources.append({key: attrs.get(key) for key in ('src', 'srcset', 'sizes', 'type', 'media', 'width', 'height')})

    def handle_endtag(self, tag):
        if tag == 'a' and self._anchor is not None:
            anchor = dict(self._anchor)
            anchor['text'] = norm_text(anchor.pop('parts'))
            self.links.append(anchor)
            self._anchor = None
        if tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6') and self._heading is not None:
            self.headings.append({'tag': self._heading['tag'], 'text': norm_text(self._heading['parts'])})
            self._heading = None
        if tag == 'title' and self._title_depth:
            self._title_depth -= 1
        if tag == 'script':
            if self._script_kind == 'jsonld':
                raw = ''.join(self._script_buffer).strip()
                if raw:
                    try:
                        parsed = json.loads(raw)
                        self.json_ld.append(parsed)
                    except json.JSONDecodeError:
                        self.json_ld.append({'_parse_error': raw})
            elif self._ignore_depth:
                self._ignore_depth -= 1
            self._script_kind = None
            self._script_buffer = []
        elif tag in ('style', 'noscript', 'template') and self._ignore_depth:
            self._ignore_depth -= 1

    def handle_data(self, data):
        if self._script_kind == 'jsonld':
            self._script_buffer.append(data)
            return
        if self._ignore_depth:
            return
        if data.strip():
            self.text_parts.append(data)
            if self._anchor is not None:
                self._anchor['parts'].append(data)
            if self._heading is not None:
                self._heading['parts'].append(data)
            if self._title_depth:
                self._title.append(data)

    def facts(self):
        return {
            'text': norm_text(self.text_parts),
            'title': norm_text(self._title),
            'headings': self.headings,
            'links': self.links,
            'images': self.images,
            'picture_sources': self.picture_sources,
            'json_ld': self.json_ld,
        }


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':'))


def parse_facts(raw: bytes):
    return RenderFacts(raw.decode('utf-8', errors='strict')).facts()


def runtime_paths_changed(source_head: str, current_head: str):
    ancestor = subprocess.run(['git', 'merge-base', '--is-ancestor', source_head, current_head], cwd=ROOT)
    if ancestor.returncode:
        raise SystemExit(f'Render source {source_head} is not an ancestor of suite HEAD {current_head}')
    changed = subprocess.check_output(['git', 'diff', '--name-only', source_head, current_head], cwd=ROOT, text=True).splitlines()
    root_runtime_files = {
        'index.php', 'services.php', 'about.php', 'contact.php', '404.php', 'all-pages.php',
        'privacy-policy.php', 'terms.php', 'sitemap.php', 'robots.txt', 'sitemap.xml',
        'llms.txt', 'llms-full.txt', 'favicon.ico', 'deploy-check.php',
    }
    runtime = []
    for name in changed:
        parts = pathlib.PurePosixPath(name).parts
        if not parts:
            continue
        if parts[0] in {'assets', 'data', 'includes', 'destinations', 'places', 'blog'} or name in root_runtime_files or parts[-1] == '.htaccess' or name.endswith('.php'):
            runtime.append(name)
    return runtime


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--current', type=pathlib.Path, required=True, help='PHP-WASM adapter evidence directory')
    ap.add_argument('--out', type=pathlib.Path, required=True)
    args = ap.parse_args()
    current_root = args.current.resolve()
    current_index_path = current_root / 'routes.json'
    if not current_index_path.is_file():
        raise SystemExit(f'Missing current render index: {current_index_path}')
    baseline_index = json.loads(BASE_INDEX.read_text(encoding='utf-8'))
    archive_bytes = BASE_ARCHIVE.read_bytes()
    if sha(archive_bytes) != baseline_index['render_archive_sha256']:
        raise SystemExit('Frozen Phase31b render archive hash does not match its index')
    baseline_archive = json.loads(gzip.decompress(archive_bytes).decode('utf-8'))
    expected_baseline = '796879d7b3d5ca0fa1e398562e937e9f364a5f62'
    if baseline_index.get('source_commit') != expected_baseline or baseline_archive.get('source_commit') != expected_baseline:
        raise SystemExit('Frozen render input is not the requested Phase31b source 796879d')

    current_index = json.loads(current_index_path.read_text(encoding='utf-8'))
    current_head = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip()
    source_head = current_index.get('source_head')
    runtime_delta = runtime_paths_changed(source_head, current_head)
    if runtime_delta:
        raise SystemExit(f'Production runtime files changed after capture: {runtime_delta}')
    current_entries = current_index.get('routes', [])
    baseline_routes = baseline_archive.get('routes', {})
    if len(current_entries) != 43 or len({entry.get('url') for entry in current_entries}) != 43:
        raise SystemExit(f'Expected 43 unique current renders, got {len(current_entries)}')
    if set(baseline_routes) != {entry['url'] for entry in current_entries}:
        raise SystemExit('Current and Phase31b route inventories differ')

    rows = []
    for entry in sorted(current_entries, key=lambda row: row['url']):
        route = entry['url']
        path = current_root / 'render-before' / entry['evidence']
        if not path.is_file():
            rows.append({'route': route, 'status': 'FAIL', 'differences': ['missing_current_render']})
            continue
        current_bytes = path.read_bytes()
        base = baseline_routes[route]
        base_bytes = base['html'].encode('utf-8')
        current_hash = sha(current_bytes)
        current_facts = parse_facts(current_bytes)
        baseline_facts = parse_facts(base_bytes)
        comparisons = {}
        for key in ('text', 'title', 'headings', 'links', 'images', 'picture_sources', 'json_ld'):
            left = canonical(current_facts[key])
            right = canonical(baseline_facts[key])
            comparisons[key] = {
                'identical': left == right,
                'current_count_or_chars': len(current_facts[key]) if isinstance(current_facts[key], (list, dict)) else len(current_facts[key]),
                'phase31b_count_or_chars': len(baseline_facts[key]) if isinstance(baseline_facts[key], (list, dict)) else len(baseline_facts[key]),
            }
        differences = [key for key, result in comparisons.items() if not result['identical']]
        if entry.get('status') != base.get('status'):
            differences.append('http_status')
        if entry.get('bytes') != len(current_bytes) or entry.get('sha256') != current_hash:
            differences.append('render_index_integrity')
        rows.append({
            'route': route,
            'status': 'PASS' if not differences else 'FAIL',
            'http_status_current': entry.get('status'),
            'http_status_phase31b': base.get('status'),
            'current_bytes': len(current_bytes),
            'phase31b_bytes': len(base_bytes),
            'current_sha256': current_hash,
            'phase31b_sha256': base.get('sha256'),
            'comparisons': comparisons,
            'differences': differences,
        })

    category_failures = {
        category: [row['route'] for row in rows if row.get('comparisons', {}).get(category, {}).get('identical') is False]
        for category in ('text', 'title', 'headings', 'links', 'images', 'picture_sources', 'json_ld')
    }
    status_failures = [row['route'] for row in rows if row.get('http_status_current') != row.get('http_status_phase31b')]
    integrity_failures = [row['route'] for row in rows if 'render_index_integrity' in row.get('differences', [])]
    failed_routes = [row['route'] for row in rows if row.get('status') != 'PASS']
    report = {
        'phase': '32c',
        'check': 'current_43_route_render_comparison_to_phase31b',
        'status': 'PASS' if len(rows) == 43 and not failed_routes and not any(category_failures.values()) and not status_failures and not integrity_failures else 'FAIL',
        'phase31b_source_commit': expected_baseline,
        'current_render_source_head': source_head,
        'current_suite_head': current_head,
        'production_runtime_changes_after_capture': runtime_delta,
        'route_count': len(rows),
        'status_mismatches': status_failures,
        'render_index_integrity_failures': integrity_failures,
        'failed_routes': failed_routes,
        'category_mismatches': category_failures,
        'category_route_counts': {
            category: sum(row.get('comparisons', {}).get(category, {}).get('identical') is True for row in rows)
            for category in ('text', 'title', 'headings', 'links', 'images', 'picture_sources', 'json_ld')
        },
        'rows': rows,
        'method': 'UTF-8 rendered HTML parsed with HTMLParser; script/style/noscript/template text excluded. Link attributes/text, img attributes, picture source attributes and parsed JSON-LD compared exactly after whitespace normalization for text and key sorting for JSON-LD.',
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f"{report['status']} 43-route Phase31b comparison; text={report['category_route_counts']['text']}/43 links={report['category_route_counts']['links']}/43 images={report['category_route_counts']['images']}/43 JSON-LD={report['category_route_counts']['json_ld']}/43")
    return 0 if report['status'] == 'PASS' else 1


if __name__ == '__main__':
    raise SystemExit(main())
