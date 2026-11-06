#!/usr/bin/env python3
"""Render the active reviewed prompt map without rewriting historical map JSON."""
import collections,json,pathlib
root=pathlib.Path(__file__).resolve().parents[2]
d=json.loads((root/'reports/phase-23-map.json').read_text())
c=collections.Counter(x['status'] for x in d['prompts'])
s=f'''# Document prompt map

Phase 23, reviewed 2026-10-22. Source: strategy-doc-summary.md section 3 and
strategy-doc-research.json. Exactly 50 source prompts; none invented.
Counts: **{c['answered']} answered, {c['partly answered']} partly answered, {c['gap']} gap**.

Answered means the requested question is substantively covered. Partly answered
means a factual/decision component is supported with the remainder explicit.
Gap means the requested fact is absent. An owner-approved business assistance
statement is not an official eligibility, approval, procedure or price answer.
Scope clarification alone does not close a factual gap or change a held gate.
The exact heading on each row locates the nearest useful answer, not proof of
full coverage. Full source questions and separate owner-scope status are in
phase-23-map.json; the Phase 20 map is retained unchanged as history.

| ID / source | Prompt | Published page / exact heading or FAQ | Status | Supported component and remaining fact |
| --- | --- | --- | --- | --- |
'''
for p in d['prompts']:
 detail=p['basis']+(' Missing: '+p['missing_fact'] if p['missing_fact'] else ' No missing component for this scoped question.')
 if p.get('owner_scope'):detail+=' Owner scope: '+p['owner_scope']
 s+=f"| {p['id']} / {p['section']} | {p['text']} | `{p['page']}` / **{p['heading']}** | {p['status']} | {detail} |\n"
s+='''
## Remaining boundaries

The owner confirms the student service-charge range, additional university
fees, actual payments from some partner universities, and the written-policy
existence. Per-service inclusions, payment schedule and refund terms are not
supplied. Existing team photos/bios and titles are verified. ILMERA is new and
has no student feedback yet; future feedback requires written permission and
verified video. No placement count, result or registration identifier is
published. Neither Udyam value is supplied. Official rules and individual
decisions still require their own current evidence; held destinations and
APS/DSU articles remain held. Counts are not raised by absent feedback or
business assistance: no artificial performance/official-rule coverage.
'''
(root/'reports/prompt-map.md').write_text(s)
print('PASS prompt map',dict(c))
