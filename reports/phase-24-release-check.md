# Phase 24 release check

Reviewed 2026-10-22. PR #1: https://github.com/fawazbhseo/ilmerastudyabroad/pull/1
Branch: `arena/48320ee5-ilmerastudyabroad`. Baseline: `9157825a90487f656b2b6c566405107a819f9857`.
No main push, merge, deployment, enquiry submission or live setting change.

## Decision

**Implementation passes executable local verification. Live deployment is NOT
CLEARED.** The actual private certificate file is unavailable: an address or
unknown-private-value comparison cannot be performed. No match/mismatch is
asserted. Native Apache/access control, public HTTP/MIME, complete backup/
restore readiness and real contact delivery are not independently verified.
Earlier source/status/live blockers remain intact.

## Check-by-check sign-off

| Check | Result | Evidence / limit |
| --- | --- | --- |
| Session-only resume safety and task checkpoints | PASS | Remote fetched; baseline bytes verified; one commit/push/PR checkpoint per task |
| PHP lint | PASS | 92 PHP files, PHP 8.5 WASM CLI |
| Unit/source/proof/citation/publication/location tests | PASS | Full task reports, exact registration field mutations and unchanged generic gates |
| Render, structured data and strict copy policy | PASS | 43 fresh renders; one canonical Organization and three exact Persons on each of 38 published routes; no prohibited schema/price fields |
| Browser, mobile/tablet/desktop, script on/off | PASS | 258 cases at 375/768/1280; 36 About/Home portrait checks; 1,278 FAQ interactions |
| FAQ visible/schema parity | PASS | 213 exact question/answer pairs |
| Sitemap, canonical, noindex and local links | PASS | 38 indexable self-canonical published entries; held pages excluded; local links/assets valid, zero orphans |
| Unique metadata and image attributes | PASS | 38 unique metadata records, 88 image instances checked; alt/dimensions/loading retained |
| LLM discovery/generator idempotence | PASS | Both files, 32 rendered metadata entries and 38 published URLs; no held discovery |
| Registration statement, caveat and identifier | PASS | Exact About/Contact block; one Udyam PropertyValue per canonical Organization; one statement/caveat per LLM |
| New certificate payload privacy | PASS | Exact allowlist; no certificate file or extra private field copied; no provenance/review date in public registration projection; no extra public file allowed |
| Certificate address/private-value cross-comparison | FAIL | Actual certificate unavailable; cannot compare its address or independently search for unknown private values. Existing contact/locality preserved, no invented mismatch |
| Zaheer approved bio everywhere active | PASS | Identical approved sentence in About/Home/team/Person/LLMs/FAQ; both legacy bio strings absent from active surfaces |
| Jabir/Fawaz bios, titles/alts and original portraits | PASS | Exact source and original asset-byte protection; historical inventories/negative tests preserved internally |
| Fawaz derivative encoding, dimensions and load | PASS | Genuine RIFF/WEBP, 384/192 square, below 60 KB; reproducible whole-square resize; HTTP bytes/local image/webp MIME and browser load checks |
| Original social-image references | PASS | No original-portrait og:image found in all 43 renders; all social metadata and blog author image references unchanged |
| Status, summaries/provenance, country facts, contact/address | PASS | All non-authorized website files byte-protected; exact legacy official-answer fields retained; no source gate relaxed |
| Actual baseline render comparison | PASS | Archived 9157825 baseline: 38 changed published renders; five held/utility renders byte-identical |
| Location distinctness | PASS | 17 locations, 136 rendered pairs, maximum 13.24200913242009 percent overlap; existing authored checks retained |
| Internal report/tool privacy configuration | PASS | Directory Apache deny rules and local adapter 403s; no published/held page-status or root rewrite change |
| Native access control, live HTTP/MIME/redirects | FAIL | Local adapter is not native Apache or independently verified public hosting |
| Existing Fawaz credential accuracy/currentness | FAIL | Owner confirmation pending; existing bios/FAQ not rewritten or independently re-verified |
| Backup/all-file-settings restore and contact delivery | FAIL | Not verified; no live upload or contact submission performed |
| Append-only logs, line endings and whitespace | PASS | Old log bytes remain prefixes; Home CRLF, About mixed CRLF plus three bare LF, root htaccess CRLF preserved; diff check clean |
| Bounded verification | PASS | Cycle 1 executable checks PASS 514.09s, early stop; cycles 2/3 not run; no repeated technical failure |
| Task 6 final full suite | PASS | 508.8 seconds; every executable check passed |

Executable local PASS is not a claim that the FAIL items above were verified.
External browser requests were aborted. No live rankings, performance, external
raw HTTP or enquiry-delivery assertion follows from these tests.

## Exact published registration text

On `/about` and `/contact`, in one visible shared-design block per page:

> ILMERA Study Abroad is registered under Udyam (MSME), registration number UDYAM-KR-18-0023330.

> Udyam registration is a business registration. It does not mean any authority has approved or endorsed ILMERA's services.

Both generator-maintained LLM files include the same statement/caveat. Canonical
Organization identifiers contain only `@type: PropertyValue`, `propertyID:
Udyam`, and the approved number. Enterprise name remains ILMERA Study Abroad.
Existing brand-name uses elsewhere remain unchanged. Private provenance and
review date remain backend evidence, not certificate facts rendered publicly.
Other four optional proof slots remain empty. No source URL is fabricated.

## Final Zaheer bio

> Zaheer KJ is the Chief Financial Officer of ILMERA Study Abroad, responsible for the company's finance function.

Seventeen words, one plain sentence, no extra background. Active About/Home,
team/Person data, both LLM files and About FAQ agree exactly. No student
advising, student-payment/loan duty or outcome is implied. Jabir/Fawaz source
biography variants, title labels and alt text remain exact. Historical audit
inventories and negative-test constants are internal evidence, not active bios.

## Fawaz image before and after

| File | Actual encoding/dimensions | Bytes | Treatment |
| --- | --- | ---: | --- |
| `assets/images/fawazbh.webp` | PNG, 1254 x 1254 | 1,541,656 | Original byte-identical, same path |
| `assets/images/fawazbh-384.webp` | WebP, 384 x 384 | 19,056 | New team src, canonical Person/LLM photo URL |
| `assets/images/fawazbh-192.webp` | WebP, 192 x 192 | 7,892 | New responsive srcset candidate |

Whole-square LANCZOS resize, WebP quality 82/method 6, no crop or retouching.
Both new files are below 60 KB and reproducible using Pillow 13.0.0 with
`tools/phase24/build_portraits.py`. Original SHA-256:
`9b2b087bd07f454a9dc54985ce4429ab11f92a7e00c3202ab87c297bbcd530dd`.
About keeps 88 x 88 attributes; Home keeps 96 x 96; loading and alt text stay.
No original-portrait og:image exists in the 43 renders. Original published
blog author portraits remain on the following routes, unchanged:

- `/blog/cost-of-studying-abroad-for-indian-students`
- `/blog/documents-needed-to-study-abroad-from-india`
- `/blog/scholarships-for-indian-students-study-abroad`
- `/blog/study-abroad-counselling-from-coorg`
- `/blog/study-abroad-with-academic-backlogs`

Two held author portraits also remain untouched. All existing social-image
metadata is unchanged. The original PNG-name/MIME issue outside the requested
team surfaces is not silently represented as fixed; live MIME needs checking.

## Owner-only inputs and live requirements

- Fee inclusions/exclusions, payment schedule/conditions, refund/cancellation
  terms and the actual written policy version. Nothing is inferred.
- Private activity correction: owner should ask a CA/check the Udyam portal,
  as documented only in the internal owner-input report. No activity code,
  certificate file or certificate-private field was published.
- Optional Zaheer background: none supplied, not a blocker for the minimal bio.
- Confirm accuracy/currentness of existing Fawaz Ahrefs Academy/Semrush
  certification claims and the Adrex Media School diploma statement in About FAQ.
- Future genuine feedback only when it exists, with written permission,
  verified video and factual review; no current feedback/result is invented.
- An actual private certificate is needed for the requested address-only
  comparison. Registration values themselves are supplied, not missing inputs.
- Complete backup and all-file/settings restore readiness before any separately
  authorized direct live upload, then native access/rewrite/public MIME/HTTP
  and actual contact-delivery verification. No staging/live deployment done.

## Every changed page

Exactly 38 published HTML routes change against the actual archived baseline.
All receive the approved canonical Organization identifier and Zaheer Person
bio/Fawaz Person image URL. Only Home/About have direct team bio/photo edits;
About/Contact additionally show the exact registration block. No other visible
country, service, price, policy or biography fact is changed. Shared changes
are atomic component updates, not 38 individual content rewrites.

- `/about`: Registration block, Zaheer bio/FAQ and Fawaz responsive image, plus canonical updates.
- `/all-pages`: Shared canonical registration and Person updates only.
- `/blog/cost-of-studying-abroad-for-indian-students`: Shared canonical registration and Person updates only.
- `/blog/documents-needed-to-study-abroad-from-india`: Shared canonical registration and Person updates only.
- `/blog/how-to-choose-study-abroad-consultant-karnataka`: Shared canonical registration and Person updates only.
- `/blog/`: Shared canonical registration and Person updates only.
- `/blog/scholarships-for-indian-students-study-abroad`: Shared canonical registration and Person updates only.
- `/blog/study-abroad-counselling-from-coorg`: Shared canonical registration and Person updates only.
- `/blog/study-abroad-with-academic-backlogs`: Shared canonical registration and Person updates only.
- `/contact`: Registration block and shared canonical updates; contact/address untouched.
- `/`: Team Zaheer bio and Fawaz responsive image, plus shared canonical updates.
- `/privacy-policy`: Shared canonical registration and Person updates only.
- `/services`: Shared canonical registration and Person updates only.
- `/study-abroad-consultants-in-karnataka`: Shared canonical registration and Person updates only.
- `/study-abroad-consultants-in-kodagu`: Shared canonical registration and Person updates only.
- `/study-abroad-counselling-belagavi`: Shared canonical registration and Person updates only.
- `/study-abroad-counselling-bengaluru`: Shared canonical registration and Person updates only.
- `/study-abroad-counselling-chikkamagaluru`: Shared canonical registration and Person updates only.
- `/study-abroad-counselling-gonikoppal`: Shared canonical registration and Person updates only.
- `/study-abroad-counselling-hassan`: Shared canonical registration and Person updates only.
- `/study-abroad-counselling-kushalnagar`: Shared canonical registration and Person updates only.
- `/study-abroad-counselling-madikeri`: Shared canonical registration and Person updates only.
- `/study-abroad-counselling-mangaluru`: Shared canonical registration and Person updates only.
- `/study-abroad-counselling-mysuru`: Shared canonical registration and Person updates only.
- `/study-abroad-counselling-ponnampet`: Shared canonical registration and Person updates only.
- `/study-abroad-counselling-shivamogga`: Shared canonical registration and Person updates only.
- `/study-abroad-counselling-siddapura`: Shared canonical registration and Person updates only.
- `/study-abroad-counselling-somwarpet`: Shared canonical registration and Person updates only.
- `/study-abroad-counselling-udupi-manipal`: Shared canonical registration and Person updates only.
- `/study-abroad-counselling-virajpet`: Shared canonical registration and Person updates only.
- `/study-in-gcc`: Shared canonical registration and Person updates only.
- `/study-in-germany`: Shared canonical registration and Person updates only.
- `/study-in-italy`: Shared canonical registration and Person updates only.
- `/study-in-latvia`: Shared canonical registration and Person updates only.
- `/study-in-lithuania`: Shared canonical registration and Person updates only.
- `/study-in-slovakia`: Shared canonical registration and Person updates only.
- `/study-in-uk`: Shared canonical registration and Person updates only.
- `/terms`: Shared canonical registration and Person updates only.

Discovery documents: `/llms.txt` and `/llms-full.txt`, existing-generator
registration/leadership/photo references only. Five held/utility renders are
byte-identical; neither publication status nor sitemap membership changed.

## Every changed repository file

Exactly 30 files relative to `9157825`, including this report.
Runtime, dependency installations, baseline tree and HTML/browser captures
remain outside Git. Original image assets are not changed.

- `CHANGELOG.md`
- `about.php`
- `assets/images/fawazbh-192.webp`
- `assets/images/fawazbh-384.webp`
- `data/proof.php`
- `data/team.json`
- `flagged-items-for-verification.md`
- `includes/proof.php`
- `includes/site-presentation.php`
- `index.php`
- `llms-full.txt`
- `llms.txt`
- `reports/.htaccess`
- `reports/owner-inputs-needed.md`
- `reports/phase-24-checks.json`
- `reports/phase-24-cycles.md`
- `reports/phase-24-image-check.json`
- `reports/phase-24-progress.md`
- `reports/phase-24-registration-check.md`
- `reports/phase-24-release-check.md`
- `reports/phase-24-render-inventory.json`
- `tools/.htaccess`
- `tools/build_llms_directory.py`
- `tools/check_phase20.py`
- `tools/check_phase24.py`
- `tools/phase24/browser.cjs`
- `tools/phase24/build_portraits.py`
- `tools/phase24/run.py`
- `tools/phase24/server.cjs`
- `tools/test_proof.php`

## Task commits and evidence

1. `ba0a62c`: registration, full suite PASS 624.36s after two distinct harness fixes.
2. `57f4e54`: Zaheer bio, full suite PASS 528.04s after exact negative-string fix.
3. `ce62c61`: WebP derivatives, full suite PASS 531.28s.
4. `5542b0b`: owner inputs/private artifact rules, full suite PASS 518.10s.
5. `733b82f`: bounded verification/source/render safeguards, cycle 1 PASS 514.09s.
6. This release commit: append-only sign-off, final full-suite result above.

Each task is separately committed/pushed to the session branch and checkpointed
on PR #1. Fresh local check details: `reports/phase-24-checks.json`. Bounded
cycle/limits: `phase-24-cycles.md`. Original/derivative evidence:
`phase-24-image-check.json`. Actual route hash comparison:
`phase-24-render-inventory.json`. Resume/task log: `phase-24-progress.md`.
