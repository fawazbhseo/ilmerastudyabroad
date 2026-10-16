# Phase 18 release check

Date: 2026-10-16. Repository baseline: `05e63e9`.
Branch: `arena/48320ee5-ilmerastudyabroad`.
PR: https://github.com/fawazbhseo/ilmerastudyabroad/pull/1

## Direct-live readiness

**Ready for owner-controlled deployment directly to live, after a complete
backup of the current live site. All local release gates PASS.** Follow
[the one-page backup and live checklist](post-deploy-checklist.md). There is
no staging requirement. The owner reports that Phase 13 `.htaccess` is
already live; this phase does not reapply it or certify its live execution.

**Final live acceptance is not signed off.** I cannot verify that the new
page addresses work on the actual live server, certify raw external citation
HTTP status, or confirm live message/phone/WhatsApp delivery. Deployment,
post-deployment checks, rollback and Search Console submission are owner
actions. No deployment, main-branch push or PR merge was performed.

## Local checks

Every row below is mandatory, without a name/wording/discovery/publication
waiver. Current recorded results and complete command output are in
`phase-18-checks.json`; each task has its own fresh run. Current LLM hashes
identify the checked bytes, not a historical edit prohibition.

| Check | Result |
| --- | --- |
| PHP lints | PASS |
| renders and schema | PASS |
| university names | PASS |
| prohibited wording | PASS |
| em dashes | PASS |
| schema draft links | PASS |
| online presence | PASS |
| GCC business/source scope and schema parity | PASS |
| discovery | PASS |
| name-guard-tests | PASS |
| whole-site-wording-tests | PASS |
| LLM-directory-tests | PASS |
| LLM-directory-idempotence | PASS |
| LLM-policy-tests | PASS |
| online-presence-tests | PASS |
| citation-inventory-tests | PASS |
| italy-claim-tests | PASS |
| italy-exact-claims | PASS |
| publication | PASS |
| check_destination_sources.php | PASS |
| check_place_publication.php | PASS |
| check_place_contact.php | PASS |
| data-export | PASS |
| location-content | PASS |
| stored source records and sitemap parity | PASS |
| destination summary provenance and status preservation | PASS |
| Phase 18 unchanged statuses and GCC protected fields | PASS |
| fresh rendered location overlap | PASS |
| line endings and LLM permission | PASS |
| browser | PASS |

Strict failures remaining: **none**. No unresolved strict-failure file/line
references remain. Eight families of regression checks cover names, wording,
LLM policy, LLM metadata directories, online presence, citation inventory,
Italy attribution/caution and PHP publication/source gates.

Per completed run: 83 PHP parses; 42 fresh route renders; 41 editorial
self-canonicals; visible FAQ/JSON-LD parity; 252 browser cases across widths
375/768/1280 with JavaScript on and off. Discovery checks all published inward
links, internal resources, fragments, robots and exact sitemap membership.
Location guides have 382-396 authored words, maximum authored shared coverage
6.410 percent, and maximum freshly rendered main shared coverage 13.476562
percent over 136 pairs, within the 15 percent limit.

### Fresh runs by task

| Task | Full local suite | Seconds |
| --- | --- | --- |
| 1 | PASS | 86.41 |
| 2 | PASS | 96.05 |
| 3 | PASS | 94.14 |
| 4 | PASS | 103.79 |
| 5 | PASS | 98.33 |

The initial task 3 attempt stopped when the long-running WASM test adapter
exhausted its resources. The adapter was restarted; the complete fresh task 3
run passed without a publication change or a waived failure. An earlier
policy-test fixture was corrected to remove online-only wording in both
letter cases, then rerun successfully; the policy itself was not relaxed.

## Live confirmations still outstanding

Here, FAIL means required live evidence is missing, **not** that a broken
live feature was observed. These checks cannot be substituted with local
renders or a successful page-extraction wrapper.

| Required confirmation | Result | Required owner action |
| --- | --- | --- |
| Complete current live-site backup and restore readiness | FAIL: not verified | Back up and inspect the saved files before deployment |
| Actual new live page addresses and native server behavior | FAIL: not verified | Open the live pages, redirects, not-found response and sitemap after upload |
| Raw external-citation HTTP health and relevant content | FAIL: not verified | Perform the no-cost browser link check in the checklist |
| Live contact/enquiry receipt and phone/WhatsApp delivery | FAIL: not verified | Make clearly labelled tests and confirm receipt |
| Search Console sitemap submission and processing | FAIL: not verified | Submit after live tests pass and monitor the property |

If errors occur, restore the backed-up live files and relevant settings,
not only `.htaccess`, clear caches and repeat the live checks.

The local environment is a PHP 8.5 WASM HTTP adapter, not native Apache.
Browser cases replay fresh rendered pages with local images and abort
external requests. Stored official-source journals, approved hosts, content
hashes and citation inventory were checked; official pages were not newly
recertified as raw HTTP successes. No external source fact was added.

## Content and publication preservation

Both LLM documents state the online-only model, omit institution names and
prohibited claims, and carry the exact visible six-country business / five-
country official-source GCC notes. Oman and Bahrain remain registration-only;
Kuwait requirements remain unsourced. Government/ministry/official portal
labels are not university endorsements or government affiliation claims.
The exact Italy sentence retains immediate owner attribution and the
written-award caution. It is not official proof of a scholarship or partner.

No PHP publication copy, page metadata, status, protected destination field,
source journal or sitemap was edited. Existing LF/CRLF/mixed line endings
are preserved. Historical blocker records were not rewritten.

| Accounting | Published | Held / separate |
| --- | --- | --- |
| Whole site HTML | 37 indexable | 4 editorial drafts plus 1 noindex 404 utility |
| Destinations | 7 | 2 drafts |
| Location guides | 17 | 0 |
| Blog articles | 5 | 2 drafts |
| Other indexable pages | 8 | Utility counted separately above |
| Expanded original target set, including two held articles | 27 | 4 drafts |

The original-target accounting excludes two earlier published articles and
eight core pages; it is not the whole-site count. The two held destinations
and two held articles remain absent from published navigation, schema,
sitemap and both LLM files. Noindex/discovery exclusion is not access control.

## Task 1: every changed LLM line

[The complete line-by-line record](phase-18-task-1-lines.md) enumerates every
removed/replaced baseline line and every new/replacement line with its exact
text and task 1 number, before task 2 changes shifted later lines. It uses
baseline `05e63e9` and task 1 commit `7d45837`, with SHA-256 snapshots. Removed
restricted names/claims are not repeated in the handoff. This record is not
silently regenerated from the final files.

## Task 2: page listings

Each file has **31 exact title/meta-description entries**: all seven
published destinations, 17 location guides, five articles, the blog index
and page index. All 37 published addresses are represented, with existing
company/contact/services/legal URLs retained in their established sections.
There was no earlier generator; `tools/build_llms_directory.py` now maintains
these entries from fresh rendered metadata and checks idempotence by default.
No draft information or new editorial claim was added to the directory.

New canonical addresses: **28 in llms.txt and 31 in llms-full.txt**. The two
already-listed short-file article entries were refreshed; the blog index
was normalized to its existing canonical address, not counted as a new page.
`phase-18-llm-pages.json` records exact titles/descriptions and new-by-file
flags. All listed routes below appear in both files.

### Destinations

- `/study-in-gcc`
- `/study-in-germany`
- `/study-in-italy`
- `/study-in-latvia`
- `/study-in-lithuania`
- `/study-in-slovakia`
- `/study-in-uk`

### Location guides

- `/study-abroad-consultants-in-karnataka`
- `/study-abroad-consultants-in-kodagu`
- `/study-abroad-counselling-belagavi`
- `/study-abroad-counselling-bengaluru`
- `/study-abroad-counselling-chikkamagaluru`
- `/study-abroad-counselling-gonikoppal`
- `/study-abroad-counselling-hassan`
- `/study-abroad-counselling-kushalnagar`
- `/study-abroad-counselling-madikeri`
- `/study-abroad-counselling-mangaluru`
- `/study-abroad-counselling-mysuru`
- `/study-abroad-counselling-ponnampet`
- `/study-abroad-counselling-shivamogga`
- `/study-abroad-counselling-siddapura`
- `/study-abroad-counselling-somwarpet`
- `/study-abroad-counselling-udupi-manipal`
- `/study-abroad-counselling-virajpet`

### Published articles

- `/blog/cost-of-studying-abroad-for-indian-students`
- `/blog/documents-needed-to-study-abroad-from-india`
- `/blog/scholarships-for-indian-students-study-abroad`
- `/blog/study-abroad-counselling-from-coorg`
- `/blog/study-abroad-with-academic-backlogs`

### Published indexes

- `/all-pages`
- `/blog/`

## Every changed file since Phase 18 baseline

- `flagged-items-for-verification.md`
- `llms-full.txt`
- `llms.txt`
- `reports/phase-18-checks.json`
- `reports/phase-18-llm-pages.json`
- `reports/phase-18-release-check.md`
- `reports/phase-18-strict-check.md`
- `reports/phase-18-task-1-lines.md`
- `reports/post-deploy-checklist.md`
- `tools/README.md`
- `tools/blocked-names.txt`
- `tools/build_llms_directory.py`
- `tools/check_discovery.py`
- `tools/check_publication_review.py`
- `tools/test_llm_directory.py`
- `tools/test_llm_policy.py`
- `tools/test_wording.py`
