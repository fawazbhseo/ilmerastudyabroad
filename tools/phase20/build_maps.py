#!/usr/bin/env python3
"""Render reviewed mapping data, without changing publication or SEO data."""
import argparse,collections,json,pathlib
r=pathlib.Path(__file__).resolve().parents[2];p=argparse.ArgumentParser();p.add_argument('--pages',type=int,default=38);a=p.parse_args();d=json.loads((r/'reports/phase-20-map.json').read_text());rows=d['keywords'][:a.pages]
s='''# Document-reviewed keyword map

Source inventory: strategy-doc-summary.md and strategy-doc-research.json, read 2026-10-16. Baseline: Phase 19 `ad09f84`. No numeric volumes or keyword-difficulty figures were supplied. Priority is intent and relevance, never fabricated demand. The 17 explicit document query strings/fragments remain separately inventoried; page-specific normalized targets and mandatory navigational labels are not additional measured research keywords.

'''
s+=f'Checkpoint coverage: **{len(rows)}/38 published pages**, one distinct primary and two or three secondaries each. '+('COMPLETE.\n' if len(rows)==38 else 'IN PROGRESS; remaining pages are not claimed complete.\n')
s+='''
| Published page | Primary | Secondary targets | Document basis and intent priority |
| --- | --- | --- | --- |
'''
for x in rows:s+=f"| `{x['page']}` | {x['primary']} | {'; '.join(x['secondary'])} | {x['document_basis']}; {x['priority']} |\n"
s+='''
## Comparison with Phase 19

Changed primary keywords: **0**. All 38 current primaries still fit the underlying page and the document's intent. The rules do not justify replacing a fitting target merely with a synonym or a superlative. No title/H1 changes are forced. Existing city targets are honest service-audience labels, not office claims. Each retained page and reason is in phase-20-map.json, with its baseline primary. The original provisional maps are archived byte-for-byte in phase-19-provisional-keyword-map.md and phase-19-provisional-prompt-map.md. Karnataka's secondary targets now explicitly include the document's overseas-education variant; this is a report assignment, not keyword stuffing in publication.

## Cannibalisation and gaps

- Karnataka owns statewide service intent; the selection article owns evaluation criteria, not a second statewide service landing page. Do not create the proposed self-ranking listicle.
- Kodagu guide concerns family coordination; Coorg article concerns the remote application process. Synonymous geography is an intentional risk to monitor, not evidence of measured cannibalisation. Preserve their different primary intent and internal-link roles.
- Home is brand identity, About is identity verification, Services is service scope, Contact is enquiry. They are not extra city-ranking pages.
- Existing location pages have different application-planning topics; the document's academic-issuer, bank and local-appointment workflows cannot replace them without official evidence.
- Hubballi-Dharwad, national expansion, scholarship procedure and loan/eligibility pages are research opportunities, not publication approvals. Insufficient supported new detail and duplication risk mean no new page is justified by this map alone.
- Held destinations and held APS/DSU articles remain excluded. Country subjects in section 5A do not override publication/source gates.
- Service-fee explainer remains an owner-input gap, separate from study-cost guidance. No public fee schedule is invented.
- Geographic query variants have neutral service phrasing here. Superlative query language in the research inventory is not an ILMERA superiority claim.
'''
(r/'reports/keyword-map.md').write_text(s)
counts=collections.Counter(x['status'] for x in d['prompts'])
s=f'''# Document prompt map

Source: strategy-doc-summary.md, section 3, all six intent groups. Exactly 50 numbered prompts, policy-safe transcription, no fabricated prompts. Keywords and source research are not proof of official rules. Counts: **{counts['answered']} answered, {counts['partly answered']} partly answered, {counts['gap']} gap**.

Answered means the requested factual or decision-check question is substantively covered. Partly answered identifies only the supported component and explicitly states the remainder. Gap means the requested fact is absent, even when a nearby generic planning section exists. An exact heading on a gap row is the nearest published review location, NOT a claim that it answers the question. No draft is a target. For compound prompts, every missing component stays visible; a disclaimer or generic advice does not turn a missing official fact into an answer.

The full question text, intent group and section reference are retained for every row in phase-20-map.json and the source inventory. Bracketed policy redactions follow Task 1. No new institution list, ranking or price is authorized.

| ID / source | Prompt | Published page / exact visible heading or FAQ | Status | Supported component / exact missing fact |
| --- | --- | --- | --- | --- |
'''
for x in d['prompts']:
 s+=f"| {x['id']} / {x['section']} | {x['text']} | `{x['page']}` / **{x['heading']}** | {x['status']} | {x['basis']}"+(f" Missing: {x['missing_fact']}" if x['missing_fact'] else ' No missing component for this scoped question.')+' |\n'
s+='''
## Separate owner and publication gaps

No public fee schedule is verified. This remains a gap independently of the 50 document prompts; it is not added as a 51st source prompt. Proof slots remain empty, not resolved by the research document. No country or local procedure is inferred from a competitor page, an AI prompt or a ranking claim. Current official evidence and any owner approvals must pass existing source/publication checks before future content work. Status-only edits cannot release held pages.
'''
(r/'reports/prompt-map.md').write_text(s)
