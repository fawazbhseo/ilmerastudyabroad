#!/usr/bin/env python3
"""Validate and summarize the current 516-case Phase31 blank-space scan."""
from __future__ import annotations
import argparse
import hashlib
import json
import pathlib
import re
from collections import Counter, defaultdict

ROOT = pathlib.Path(__file__).resolve().parents[2]
INVENTORY = ROOT / 'reports/phase-25-baseline-renders.json'
PHASE31_AFTER = ROOT / 'reports/phase-31-after-blank-space-audit.json'
CONTACT_NOTE = ROOT / 'reports/phase-32-contact-minihero-tail-summary.md'
EXPECTED_WIDTHS = (360, 768, 1280)
EXPECTED_JS = ('on', 'off')
EXPECTED_MOTION = ('normal', 'reduced')
SCROLL_HINTS = {'/': 'Explore', '/services': 'Explore', '/about': 'Explore', '/contact': 'Reach Out'}


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def focused_contact_reference():
    rows = {}
    for line in CONTACT_NOTE.read_text(encoding='utf-8').splitlines():
        if not line.startswith('|'):
            continue
        cols = [part.strip() for part in line.strip().strip('|').split('|')]
        if cols and cols[0] in {'360px', '768px', '1280px'} and len(cols) > 3:
            width = int(cols[0].removesuffix('px'))
            match = re.search(r'([0-9]+(?:\.[0-9]+)?)\s*px', cols[3])
            if match:
                rows[width] = float(match.group(1))
    return rows


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--scan-dir', type=pathlib.Path, required=True)
    ap.add_argument('--out', type=pathlib.Path, required=True)
    args = ap.parse_args()
    scan_dir = args.scan_dir.resolve()
    summary_path = scan_dir / 'summary.json'
    summary_bytes = summary_path.read_bytes()
    summary = json.loads(summary_bytes)
    inventory = json.loads(INVENTORY.read_text(encoding='utf-8'))
    previous = json.loads(PHASE31_AFTER.read_text(encoding='utf-8'))
    routes = sorted(inventory.get('routes', {}))
    expected_matrix = {(route, width, js, motion) for route in routes for width in EXPECTED_WIDTHS for js in EXPECTED_JS for motion in EXPECTED_MOTION}
    listed = {(case['route'], case['width'], case['javascript'], case['motion']) for case in summary.get('cases', [])}
    if len(routes) != 43 or len(expected_matrix) != 516:
        raise SystemExit('Frozen 43-route matrix input is invalid')

    case_hashes = []
    pixel_candidates = 0
    hidden_reveals = []
    scroll_cues = []
    dom_findings = []
    contact_tails = []
    incomplete = []
    statuses = Counter()
    request_failures = 0
    for entry in summary.get('cases', []):
        case_path = scan_dir / 'cases' / (entry['id'] + '.json')
        if not case_path.is_file():
            incomplete.append({'id': entry['id'], 'reason': 'missing_case_json'})
            continue
        raw = case_path.read_bytes()
        case_hashes.append({'id': entry['id'], 'sha256': sha(raw)})
        case = json.loads(raw)
        statuses[str(case.get('http_status'))] += 1
        scroll = case.get('scroll', {})
        if case.get('http_status') not in (200, 404):
            incomplete.append({'id': entry['id'], 'reason': 'unexpected_http_status', 'status': case.get('http_status')})
        if not scroll.get('returned_to_top') or scroll.get('settle_ms') != 3000:
            incomplete.append({'id': entry['id'], 'reason': 'incomplete_scroll_or_settle', 'scroll': scroll})
        request_failures += len(case.get('request_failures', []))
        pixel_candidates += len(case.get('pixel_scan', {}).get('interior_candidates', []))
        dom = case.get('dom', {})
        for item in dom.get('hidden_text', []):
            is_hint = case.get('route') in SCROLL_HINTS and item.get('text_sample') == SCROLL_HINTS[case['route']] and item.get('y', 9999) < 1200
            if is_hint:
                scroll_cues.append({'case': entry['id'], 'route': case['route'], 'width': case['width'], 'javascript': case['javascript'], 'motion': case['motion'], 'selector': item.get('selector'), 'text': item.get('text_sample'), 'y': item.get('y')})
            else:
                hidden_reveals.append({'case': entry['id'], 'route': case['route'], 'width': case['width'], 'javascript': case['javascript'], 'motion': case['motion'], 'selector': item.get('selector'), 'text': item.get('text_sample'), 'y': item.get('y')})
        for item in dom.get('empty_or_spacing_nodes', []):
            row = {'case': entry['id'], 'route': case['route'], 'width': case['width'], 'javascript': case['javascript'], 'motion': case['motion'], **item}
            dom_findings.append(row)
        tail = dom.get('contact_minihero_tail')
        if case.get('route') == '/contact':
            if not tail:
                incomplete.append({'id': entry['id'], 'reason': 'missing_contact_minihero_tail'})
            else:
                contact_tails.append({
                    'case': entry['id'],
                    'width': case['width'],
                    'javascript': case['javascript'],
                    'motion': case['motion'],
                    'section_height': tail['height'],
                    'min_height': tail['min_height'],
                    'last_visible_flow_bottom': tail['last_visible_flow_bottom'],
                    'flow_tail_to_section_bottom': tail['flow_tail_to_section_bottom'],
                    'scroll_indicator': tail['scroll_indicator'],
                })

    if summary.get('case_count') != 516 or summary.get('expected_case_count') != 516 or not summary.get('complete') or listed != expected_matrix:
        incomplete.append({'reason': 'scan_matrix_incomplete', 'listed_cases': summary.get('case_count'), 'expected': 516})

    prior_counts = previous.get('finding_counts', {})
    current_dom_counts = Counter(item.get('kind', 'unknown') for item in dom_findings)
    current_counts = {
        'pixel-quiet-band': pixel_candidates,
        'intentional-scroll-indicator-dismissed': len(scroll_cues),
        'hidden-reveal-text': len(hidden_reveals),
        **dict(current_dom_counts),
    }
    contact_other_tails = [item for item in dom_findings if item.get('kind') == 'unused-min-height-tail' and not (item.get('route') == '/contact' and item.get('selector') == '#miniHero')]
    empty_nodes = [item for item in dom_findings if item.get('kind') in {'empty-content-wrapper', 'hidden-content-wrapper'}]
    focused = focused_contact_reference()
    phase31_tails = {}
    for item in previous.get('findings', []):
        if item.get('kind') == 'unused-min-height-tail' and item.get('route') == '/contact' and item.get('selector') == '#miniHero':
            phase31_tails.setdefault(int(item['width']), item['height'])
    by_width = defaultdict(list)
    for item in contact_tails:
        by_width[item['width']].append(item['flow_tail_to_section_bottom'])
    contact_width_summary = {
        str(width): {
            'current_scan_min_px': round(min(values), 2) if values else None,
            'current_scan_max_px': round(max(values), 2) if values else None,
            'state_count': len(values),
            'phase31_after_scan_px': phase31_tails.get(width),
            'phase32_focused_inspector_px': focused.get(width),
        }
        for width, values in sorted(by_width.items())
    }

    unexplained_tail_failures = [
        item for item in dom_findings
        if item.get('kind') == 'unused-min-height-tail'
        and not (item.get('route') == '/contact' and item.get('selector') == '#miniHero')
    ]
    status = 'PASS' if not incomplete and not hidden_reveals and not empty_nodes and not unexplained_tail_failures else 'FAIL'
    report = {
        'phase': '32c',
        'check': 'current_phase31_blank_space_scan',
        'status': status,
        'source_head': summary.get('source_head'),
        'route_count': len(routes),
        'case_count': summary.get('case_count'),
        'expected_case_count': 516,
        'matrix': '43 routes x 3 widths x JavaScript on/off x normal/reduced motion',
        'scroll_and_settle': 'Every case must complete the slow full-page scroll, wait 3000ms, and return to scrollY 0.',
        'screenshot_method': 'A full-page PNG was captured and scanned in memory in each case; per-case SHA-256 is retained. Crops were disabled for this scan. Quiet-band counts are screening candidates, not proof of removable space.',
        'http_status_counts': dict(statuses),
        'pixel_quiet_band_candidates': pixel_candidates,
        'previous_phase31_after_pixel_candidates': prior_counts.get('pixel-quiet-band'),
        'pixel_candidate_delta': pixel_candidates - prior_counts.get('pixel-quiet-band', 0),
        'intentional_scroll_indicator_dismissals': len(scroll_cues),
        'previous_phase31_after_scroll_indicator_dismissals': prior_counts.get('intentional-scroll-indicator-dismissed'),
        'hidden_reveal_text_findings': hidden_reveals,
        'dom_findings_by_kind': dict(sorted(current_dom_counts.items())),
        'empty_content_findings': empty_nodes,
        'unexplained_min_height_tails': unexplained_tail_failures,
        'contact_minihero_disposition': 'Retain. This is the existing 88vh first-fold hero and its existing bottom scroll cue. No layout change is authorized by this scan.',
        'contact_minihero_tail_by_width': contact_width_summary,
        'contact_minihero_state_measurements': contact_tails,
        'case_completeness_failures': incomplete,
        'request_failure_event_count': request_failures,
        'case_sha256': case_hashes,
        'scan_summary_sha256': sha(summary_bytes),
        'prior_phase31_report': 'reports/phase-31-after-blank-space-audit.json',
        'prior_contact_inspector': 'reports/phase-32-contact-minihero-tail-summary.md',
        'interpretation': 'The scan is complete only if all 516 cases satisfy the scroll/settle contract. Pixel quiet bands are candidates. Contact #miniHero tails are retained and reported separately; no blank-space or content removal is authorized here.',
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f"{status} blank-space scan: {summary.get('case_count')}/516 cases, {pixel_candidates} pixel candidates, {len(hidden_reveals)} hidden reveal groups, {len(dom_findings)} DOM candidates, {len(contact_tails)} Contact tail captures")
    return 0 if status == 'PASS' else 1


if __name__ == '__main__':
    raise SystemExit(main())
