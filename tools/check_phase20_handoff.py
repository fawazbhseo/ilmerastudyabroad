#!/usr/bin/env python3
"""Append-only history, line-ending and final scope checks for the Phase 20 handoff."""
import json,pathlib,subprocess
r=pathlib.Path(__file__).resolve().parents[1]
def original(name):return subprocess.check_output(['git','show','ad09f84:'+name],cwd=r)
for name in ['CHANGELOG.md','flagged-items-for-verification.md','tools/README.md']:
 assert (r/name).read_bytes().startswith(original(name)),('Not append-only',name)
# These mixed/CRLF entry points must not have been rewritten at all.
for name in ['index.php','about.php','.htaccess']:
 assert (r/name).read_bytes()==original(name),('Protected line endings/entry point',name)
for name in ['llms.txt','llms-full.txt','data/seo-map.json']:
 assert (r/name).read_bytes()==original(name),('Unexpected directory/metadata rewrite',name)
answers=json.loads((r/'data/answer-map.json').read_text());old=json.loads(original('data/answer-map.json'))
assert set(answers)==set(old)
count=0;pages=0
for page,entry in answers.items():
 baseline=old[page]
 for field in ['question','answer','basis','reviewed_on']:assert entry[field]==baseline[field],(page,field)
 assert entry['extra_faqs'][:len(baseline['extra_faqs'])]==baseline['extra_faqs']
 delta=len(entry['extra_faqs'])-len(baseline['extra_faqs']);assert delta>=0
 count+=delta;pages+=bool(delta)
assert (count,pages)==(7,4),(count,pages)
recommendations=json.loads((r/'reports/phase-20-recommendations.json').read_text())
assert len(recommendations['recommendations'])==54
assert recommendations['counts']=={'owner-only':21,'already done':14,'rejected by a rule':16,'done in this phase':3}
for name in ['phase-20-release-check.md','phase-20-progress.md','phase-20-cycles.md']:
 assert (r/'reports'/name).is_file()
checks=json.loads((r/'reports/phase-20-checks.json').read_text())
assert all(str(i) in checks['tasks'] for i in range(1,7))
assert all(c['status']=='PASS' for t in checks['tasks'].values() for c in t['checks'].values())
print('PASS append-only histories, exact CRLF/mixed entry-point bytes, unchanged metadata/LLM files, seven additive FAQs on four pages, 54 classified actions and all prior task checks')
