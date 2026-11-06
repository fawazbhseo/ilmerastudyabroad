#!/usr/bin/env python3
"""Check the exact owner sentence, local attribution and written-award caution.

This is a copy regression check, not proof of an award or partner relationship.
FAQ parity and the independent names/prohibited-wording checks remain required.
"""
import argparse
import re
import unicodedata
from pathlib import Path
from urllib.parse import unquote
import check_discovery as discovery

EXACT = 'Tuition can be fully or largely covered at our partner universities through scholarships of up to 8,000 euros, subject to eligibility.'
OWNER = 'Owner-provided conditional guidance. '
CAUTION = ' Do not rely on funding until written award terms confirm eligibility, coverage and payment.'
AMOUNT = re.compile(r'(?<!\w)(?:8[,.\s]*000|8\s*k|eight[\s-]+thousand)(?!\w)', re.I)


def check_parts(parts):
    count = 0
    for raw in parts:
        text = unicodedata.normalize('NFKC', unquote(raw))
        occurrences = text.count(EXACT)
        assert text.count(OWNER + EXACT + CAUTION) == occurrences, 'Missing local owner label or written-award caution'
        assert not AMOUNT.search(text.replace(EXACT, '')), 'Non-exact 8,000-euro claim'
        count += occurrences
    return count


def check(base, root):
    findings = {}
    for route, info in discovery.routes(root).items():
        if info['status'] == 'draft' or route == '/404':
            continue
        status, _, body = discovery.fetch(base, route)
        assert status == 200, (route, status)
        try:
            count = check_parts(discovery.PublishedContent(body.decode()).parts)
        except AssertionError as error:
            raise AssertionError((route, str(error))) from error
        if count:
            findings[route] = count
    for name in ('llms.txt', 'llms-full.txt'):
        status, _, body = discovery.fetch(base, '/' + name)
        assert status == 200, (name, status)
        count = check_parts([body.decode()])
        if count:
            findings['/' + name] = count
    return findings


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--base-url', default='http://127.0.0.1:8080')
    p.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    args = p.parse_args()
    result = check(args.base_url.rstrip('/'), args.root)
    print('PASS exact owner-sentence occurrences (visible/schema/metadata):', result, 'total', sum(result.values()))
