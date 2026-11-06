#!/usr/bin/env python3
"""Report the measured Phase31 main-content target bounds and 44px exceptions."""
from __future__ import annotations
import argparse
import json
import pathlib
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parents[2]
BASELINE = ROOT / 'reports/phase-31-target-baseline.json'


def below44(target):
    return float(target['width']) < 44 or float(target['height']) < 44


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--browser-matrix', type=pathlib.Path, required=True)
    ap.add_argument('--out', type=pathlib.Path, required=True)
    args = ap.parse_args()
    browser = json.loads(args.browser_matrix.read_text(encoding='utf-8'))
    baseline = json.loads(BASELINE.read_text(encoding='utf-8'))
    current = browser.get('target_dimensions', {})
    old = baseline.get('targets', {})
    if browser.get('normal_cases') != 258 or browser.get('total_cases') != 306:
        raise SystemExit('Browser matrix does not contain the expected 258 normal plus 48 reduced-motion cases')

    current_below = [(key, value) for key, value in current.items() if below44(value)]
    base_below = [(key, value) for key, value in old.items() if below44(value)]
    shared = set(current) & set(old)
    new_below = []
    new_targets_below = []
    resolved_below = []
    shrunk = []
    for key, value in current.items():
        before = old.get(key)
        now_small = below44(value)
        if before is None:
            if now_small:
                new_targets_below.append({'key': key, 'current': {'width': value['width'], 'height': value['height']}})
            continue
        was_small = below44(before)
        if now_small and not was_small:
            new_below.append({'key': key, 'baseline': {'width': before['width'], 'height': before['height']}, 'current': {'width': value['width'], 'height': value['height']}})
        if was_small and not now_small:
            resolved_below.append(key)
        dw = float(value['width']) - float(before['width'])
        dh = float(value['height']) - float(before['height'])
        if dw < -0.5 or dh < -0.5:
            shrunk.append({'key': key, 'width_delta': round(dw, 2), 'height_delta': round(dh, 2)})

    per_route = Counter(key.split('|', 1)[0] for key, _ in current_below)
    failures = []
    for key, value in current_below:
        failures.append({
            'key': key,
            'tag': value.get('tag'),
            'href': value.get('href'),
            'text': value.get('text'),
            'width': value.get('width'),
            'height': value.get('height'),
        })
    examples = failures[:40]
    baseline_relative_pass = not new_below and not new_targets_below and not shrunk
    # The requested 44px bound is evaluated literally on the recorded element rectangles.
    # Existing small boxes remain visible failures and are not waived by baseline parity.
    status = 'PASS' if not current_below and not new_targets_below and not shrunk else 'FAIL'
    report = {
        'phase': '32c',
        'check': '44px_interactive_target_rectangles',
        'status': status,
        'baseline_relative_status': 'PASS' if baseline_relative_pass else 'FAIL',
        'rule': 'Each measured visible interactive element rectangle must be at least 44 CSS px wide and 44 CSS px high. This conservative check does not infer extra pointer area from pseudo-elements.',
        'scope': 'The inherited Phase31 browser-suite target inventory: visible main-content anchors, buttons, summaries, inputs, selects, textareas and role=button elements. Header, navigation, footer, hidden accordion children and scroll indicators are excluded by that runner and are not claimed as covered here.',
        'matrix': {
            'normal_cases': browser.get('normal_cases'),
            'reduced_motion_cases': browser.get('reduced_motion_cases'),
            'total_cases': browser.get('total_cases'),
            'current_target_rectangles': len(current),
            'phase31_target_rectangles': len(old),
            'shared_identities': len(shared),
        },
        'current_below_44_count': len(current_below),
        'phase31_below_44_count': len(base_below),
        'below_44_delta': len(current_below) - len(base_below),
        'new_below_44_existing_identity_count': len(new_below),
        'new_target_below_44_count': len(new_targets_below),
        'resolved_below_44_count': len(resolved_below),
        'baseline_relative_shrink_count': len(shrunk),
        'below_44_by_route': dict(sorted(per_route.items())),
        'remaining_failures': failures,
        'failure_examples': examples,
        'additional_new_below_44': new_below[:40],
        'new_target_failures': new_targets_below[:40],
        'interpretation': 'PASS_BASELINE_RELATIVE is not a 44px conformance pass. Every measured rectangle below 44px remains a literal finding; this report keeps existing failures visible and authorizes no layout change.',
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f"{status} 44px target rectangles: {len(current_below)}/{len(current)} below 44; baseline {len(base_below)}; newly below {len(new_below)+len(new_targets_below)}; shrunk {len(shrunk)}")
    return 0 if status == 'PASS' else 1


if __name__ == '__main__':
    raise SystemExit(main())
