# Phase 20 bounded release cycles

Maximum: four full cycles. Stop early when a cycle has nothing in scope to fix; stop on any failure repeated twice. No policy, source, publication or wording check is waived to obtain a pass.

## Cycle 1, Task 6: PASS, stop early

- Starting commit: `714a646` (completed Task 5).
- Fresh suite duration: 402.23 seconds.
- PHP: 90 syntax checks, including maintained source/publication/proof gates and the new seven-boundary ItemList test.
- Renders: all 43 current routes, 38 published/indexable, four held editorial routes and the separate noindex utility page. No status change.
- Browser: 258 cases, three widths (375, 768, 1280), JavaScript off/on, 1,110 FAQ interactions; final-layout and expanded-answer readability passed. Fresh local page requests, external resources blocked.
- All published sitemap URLs self-canonical and indexable; no held URL in discovery, links, sitemap or either LLM directory. Internal target/fragment checks pass. No orphan; maximum click depth three.
- Visible FAQ questions/answers exactly match FAQPage data. The unordered state-hub list exactly matches its four visible labels and URLs; no ranking claim.
- Unique titles/descriptions, title length under 60, description length under 155, H1/opening alignment and existing social/page-schema parity pass for all 38.
- Names, restricted cost wording, physical-presence claims, business-superiority claims, em-dash and recursive prohibited-schema checks pass. No rating/review/premises schema added.
- All 17 locations remain above 350 authored prose words. All 136 authored pairs and 136 full-rendered pairs pass. Maximum full-rendered shared coverage: 13.242009 percent, strictly below 15.
- Both LLM files pass the existing generator's idempotence/rendered-metadata checks without a rewrite. Existing format and publication-only coverage retained.
- All 33 protected data/journal/entity/proof files remain byte-identical. This protects every destination fact, all nine summaries/provenance values and all prior publication statuses.
- Maps: 38 unique primaries, 2-3 secondaries each; all 50 prompts, 6 answered / 15 partly answered / 29 gap with exact missing facts.

Failures found: **0**. Fixes required: **0**. Repeated failures: **0**. Cycles 2-4 not run because Cycle 1 was clean. Do not use absent owner/source inputs to rerun an unchanged local cycle.

Evidence: `reports/phase-20-checks.json`, task 6, and the fresh task6 route captures/browser logs in the external evidence directory. No historical browser result is substituted for this cycle.

## Setup attempts and other task checks

Task 1's runtime, parser and browser setup/debug attempts are described in tools/phase20/README.md, including a reverted duration shortcut that stalled JavaScript-off stylesheet loading. They preceded bounded release cycles and are not claimed as clean cycles. Tasks 1-5 each ultimately had a separate full passing suite; Task 7 receives another fresh full suite for sign-off.

## Unverified owner/live boundary

No live deployment, native Apache rewrite/redirect/query/access-control acceptance, raw external-source HTTP status, form delivery, independent review, ranking or AI citation measurement was performed. The 29 factual gaps and 15 partial prompts remain open for their exact evidence, not waived. Empty proof is still empty. Owner-only actions need real consent/access/evidence. Deployment remains complete-live-backup first, owner direct-live upload and live smoke checks, with restoration of every backed-up file and setting on error; no staging or partial rollback.
