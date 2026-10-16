#!/usr/bin/env python3
"""Measure authored prose and city-normalized shared five-word coverage."""
import argparse
import hashlib
import itertools
import json
from pathlib import Path
import re
import subprocess


def payload(d):
    return [d[k] for k in ['page_title', 'heading', 'meta_description', 'intro_answer', 'sections', 'faqs']]


def digest(d):
    return hashlib.sha256(json.dumps(payload(d), ensure_ascii=False, separators=(',', ':')).encode()).hexdigest()


def inspect(data):
    names = sorted([d['name'] for d in data.values()], key=len, reverse=True)
    pattern = re.compile('|'.join(re.escape(n) for n in names), re.I)
    records, tokens = {}, {}
    titles, headings, metas, questions = set(), set(), set(), set()
    for slug, d in data.items():
        prose = d['intro_answer'] + ' ' + ' '.join(p for s in d['sections'] for p in s['paragraphs'])
        words = len(prose.split())
        assert words >= 350, (slug, words)
        assert 40 <= len(d['intro_answer'].split()) <= 60, slug
        for value, seen in [(d['page_title'], titles), (d['heading'], headings), (d['meta_description'], metas)]:
            assert value and value not in seen, (slug, 'duplicate surface')
            seen.add(value)
        for f in d['faqs']:
            assert f['question'] not in questions and f['answer'], (slug, 'FAQ')
            questions.add(f['question'])
        assert d['local_facts_used'] is False and d['local_fact_sources'] == [], slug
        assert not any(d[k] for k in ['local_institutions', 'transcript_and_moi_steps', 'local_loan_options', 'visa_appointment_route', 'local_notes']), slug
        copy = prose + ' ' + ' '.join(s['heading'] for s in d['sections']) + ' ' + ' '.join(f['question']+' '+f['answer'] for f in d['faqs'])
        tokens[slug] = re.findall(r"[a-z0-9]+(?:'[a-z]+)?", pattern.sub('LOCATION', copy).lower())
        records[slug] = {'prose_words': words, 'content_sha256': digest(d), 'local_facts_used': False, 'local_fact_sources': [], 'copy_reviewed': True, 'schema_reviewed': True, 'checked_on': '2026-10-16'}
    pairs = []
    for a, b in itertools.combinations(sorted(tokens), 2):
        ta, tb = tokens[a], tokens[b]
        sa, sb = [tuple(ta[i:i+5]) for i in range(len(ta)-4)], [tuple(tb[i:i+5]) for i in range(len(tb)-4)]
        common = set(sa) & set(sb)
        def covered(shingles, total):
            positions = {j for i, s in enumerate(shingles) if s in common for j in range(i, i+5)}
            return len(positions) / total * 100
        ca, cb = covered(sa, len(ta)), covered(sb, len(tb))
        assert max(ca, cb) <= 15, (a, b, ca, cb)
        pairs.append({'a': a, 'b': b, 'percent_a': round(ca, 3), 'percent_b': round(cb, 3)})
    return {'checked_on': '2026-10-16', 'method': 'Shared contiguous five-word token coverage in either document, after case/punctuation and all city-name normalization. Intro, authored sections and FAQs included; sitewide navigation/contact boilerplate excluded. Prose minimum excludes FAQs and headings.', 'contact_basis': ['contact.php: existing phone, WhatsApp and video-call arrangements', 'services.php: existing profile/application/document support', 'terms.php: agreed scope and no guaranteed outcome'], 'locations': records, 'pairwise_overlap': pairs, 'max_shared_percent': max(max(p['percent_a'], p['percent_b']) for p in pairs)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data-json', type=Path)
    parser.add_argument('--write-report', type=Path)
    args = parser.parse_args()
    if args.data_json:
        data = json.loads(args.data_json.read_text())['places']
    else:
        code = '$out=[]; foreach(glob("places/*.php") as $file) { $d=include $file; $out[$d["slug"]]=$d; } echo json_encode($out);'
        data = json.loads(subprocess.check_output(['php', '-r', code], cwd=Path(__file__).resolve().parents[1]))
    report = inspect(data)
    if args.write_report:
        args.write_report.write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n')
    print('PASS', len(report['locations']), 'unique guides;', len(report['pairwise_overlap']), 'pairs; maximum shared coverage', report['max_shared_percent'], 'percent')
    print('Prose words:', min(r['prose_words'] for r in report['locations'].values()), 'to', max(r['prose_words'] for r in report['locations'].values()))


if __name__ == '__main__':
    main()
