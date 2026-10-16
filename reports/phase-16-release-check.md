# Phase 16 release check

Checked 16 October 2026 on `arena/48320ee5-ilmerastudyabroad`.
PR: https://github.com/fawazbhseo/ilmerastudyabroad/pull/1 (open, unmerged).
Application changes end at `0aa08b6`; tasks 5 and 6 add release evidence and
handoff documentation. Phase 15 and all historical blocker text are retained.

**Decision: NOT READY for staging acceptance or production sign-off.**
The authorized fixes are implemented, but the strict release acceptance
criteria still fail on frozen public LLM content. Numeric external citation
HTTP 200 and native Apache/deployment behavior are not proven. No merge,
deployment, main push or status-only publication was performed.

## 1. Scope and counts

- Original 29 targets: **27 published, 2 draft**.
- With the separately held APS and DSU articles: **27 published, 4 draft**, 31 targets.
- Entire site: **37 indexable published HTML pages, 4 draft editorial pages**.
  There are 41 editorial routes plus the noindex 404 utility, 42 renders total.
- The sitemap has **37 unique URLs**, each 200, self-canonical and without
  noindex in the fresh local PHP adapter. This is not a production HTTP claim.
- No publication status changed anywhere during Phase 16. Latvia retains five
  genuine categories: intro, costs, visa steps, documents and FAQ.
- Destination category counts remain Germany 6, Italy 5, Slovakia 6, UK 6,
  Lithuania 5, Latvia 5, GCC 9, Czech Republic 4 and Russia 0.
- The nine destination summaries and their provenance were preserved exactly.
  All 17 location guides retain their content/review gates and existing contacts.

### Four held pages

| Page | Clean route | Status and discovery |
|---|---|---|
| APS | `/blog/study-in-germany-free-aps-certificate` | Draft; noindex robots/googlebot/header; absent from HTML/LLM discovery, schema and sitemap |
| DSU | `/blog/italy-dsu-scholarship-eligibility` | Draft; noindex robots/googlebot/header; absent from HTML/LLM discovery, schema and sitemap |
| Czech Republic | `/study-in-czech-republic` | Draft; four categories, below five; prior approved-source/booking blockers retained |
| Russia | `/study-in-russia` | Draft; no supported current notice or five categories; prior unavailable notice blocker retained |

Noindex is not access control. These four draft pages remain directly
requestable in the adapter; private staging must use real authentication.

## 2. Six tasks and fresh verification

One commit per task. Task commits 1-4 are `0004749`, `ce7e665`, `4ca8a0d`,
`0aa08b6`; the two documentation commits follow in branch history.
Every task had a new full parser/render/browser/discovery run. Results are
not substituted from Phase 14/15 or an earlier task. The final machine summary
is [phase-16-checks.json](phase-16-checks.json).

| Task | PHP lints | Fresh renders | Chromium cases | Core discovery | Strict discovery/publication | Seconds |
|---|---|---|---|---|---|---|
| 1 | 83 PASS | 42 PASS | 252 PASS | PASS | PASS before task-2 name guard existed | 211.58 |
| 2 | 83 PASS | 42 PASS | 252 PASS | PASS | FAIL: restricted LLM names | 80.76 |
| 3 | 83 PASS | 42 PASS | 252 PASS | PASS | FAIL: restricted LLM names | 78.44 |
| 4 | 83 PASS | 42 PASS | 252 PASS | PASS | FAIL: restricted LLM names | 93.04 |
| 5 | 83 PASS | 42 PASS | 252 PASS | PASS | FAIL: restricted LLM names | 86.48 |

Task 1's older CLI passed before the name guard was introduced in task 2;
its separate names/wording scans already failed. That older pass is not a
current release pass. Tasks 2 onward default to strict name enforcement and
correctly fail. Core discovery is separately labelled diagnostic only, with
`enforce_names=False`; it does not override either strict CLI result.
Tasks 3/4 were finalized only after repeating their complete QA on corrected
inventories/visibility fixes; this table records those last full executions.

### Final acceptance matrix

| Requirement | Result | Evidence and limit |
|---|---|---|
| Every PHP file parses | PASS | 83 files through PHP 8.5 WASM TOKEN_PARSE; native PHP/Apache not installed |
| All clean routes render | PASS, local scope | 42 fresh responses; 41 editorial self-canonicals; 4 drafts plus utility noindex |
| Browser coverage | PASS, captured-render scope | 42 pages x 3 widths (375/768/1280) x JS on/off = 252 cases; page errors, native FAQ toggles, mobile navigation, discovery duplicates and study-section overflow checked |
| Amount FAQ readability | PASS | Services/Contact button FAQs open/close and fit fully; JS-off answers visible; fixed height caps removed |
| Published JSON-LD / FAQ parity | PASS | Every rendered JSON-LD block parsed; every FAQ answer/question matched visible copy |
| Sitemap parity and URL health | PASS, local scope | Committed XML equals freshly generated runtime XML; all 37 entries 200, self-canonical, no noindex, no duplicate/draft |
| Internal links / fragments / resources | PASS, diagnostic core | All rendered link targets/fragments checked; resources 200, no indexable orphans, no draft links; default strict command still fails below |
| Robots / public discovery | PASS, diagnostic core | Sitemap declared and not blocked; public LLM responses 200; APS/DSU links absent |
| No draft URLs in schema | PASS | Fresh published JSON-LD scan; withheld routes excluded |
| No em dash in public content | PASS | Fresh HTML/schema/metadata and both public LLM files scanned |
| No university/institution names | FAIL overall | Published HTML/schema/meta/alt/link surfaces pass the maintained blocked-name list; `llms.txt:58` still fails; manual published institution-context sweep found no other university name |
| No free / tuition-free wording | FAIL overall | Published HTML surfaces pass; both restricted LLM files fail, including negative uses |
| Exact Italy owner sentence | PASS | 19 occurrences: Home 8, About 1, Contact 4, Services 6; exact sentence unchanged, local owner label and written-award caution; no other published Italy amount variant found |
| Strict discovery CLI | FAIL | Maintained names guard detects restricted `llms.txt`; six regression cases pass |
| Strict publication CLI | FAIL | Stops at the same strict discovery/name failure, not reported as passing later checks |
| Stored source/hash/sitemap checks | PASS independently | Active journal host/date/text gates, affected article hashes and snapshot parity independently executed; this is not fresh external HTTP proof |
| Fresh official source content opens | PASS, substantive-content scope | All 25 original distinct citations opened; one soft missing page replaced; 23 current distinct URLs inventoried including legacy footers and schema/LLM references |
| Every external citation raw HTTP 200 | UNVERIFIED, blocks acceptance | Fetch interface exposes content, not raw response headers/status on success; no invented 200 certificate |
| Location content/source/contact gates | PASS | 17 unique guides; 367-381 authored words; 136 pairs; authored maximum 3.311%; fresh full rendered-main maximum 14.147287% |
| LLM byte permission / line endings | PASS | Only the two authorized `llms.txt` link lines removed; `llms-full.txt` baseline-identical; existing CRLF/mixed About endings preserved |
| Native Apache and deployment behavior | UNVERIFIED, blocks sign-off | Real rewrite/redirect/query preservation/access controls/HTTPS-host rules and live asset/contact delivery need staging checks |
| Staging acceptance readiness | **FAIL / NOT READY** | LLM policy violations plus missing transport/deployment proof remain |

Browser tests replay newly rendered HTML and local image assets. Other
external network requests were aborted. This does not verify remote fonts,
third-party scripts, message delivery, native Apache or production behavior.
Button-FAQ clipping/JS-off assertions were added with task 4 and repeated in
the final audit; earlier browser tasks did not claim that added coverage.

## 3. Authorization decision and remaining blockers

1. **LLM permission conflict.** Task 1 explicitly permits only removing APS
   and DSU article link lines from the two LLM files, while task 2 also requests
   names/wording cleanup there. Conservatively retain all other bytes. The
   maintained guard must fail, not silently exempt these public files.
2. **Restricted names:** `llms.txt:58` retains Oxford, Cambridge, Imperial
   College London (including the Imperial alias), University of Manchester and
   UCL. Tor Vergata/Rome affiliation and UK named examples were neutralized
   only in the authorized published HTML/schema surfaces.
3. **Restricted wording:** `llms.txt` offending lines 3, 28, 34, 42, 44, 53, 94, 97, 99, 102, 137, 153, 161, 162, 183, 189, 192, 198;
   `llms-full.txt` offending lines 56, 57, 69, 76, 79, 107, 108, 111, 138.
   Broader Italy stipend/funding implications in these files are not new
   approvals and remain inconsistent with the release-wide wording request.
4. **External transport:** all current sources yielded substantive opened
   content, but raw numeric HTTP 200 is not exposed by the fetch interface.
   Recheck final direct URLs and redirects with an unrestricted staging runner.
5. **Native staging:** verify `.htaccess` behavior, query strings, clean URLs,
   `/sitemap`, `/sitemap.php`, `/sitemap.xml`, data/include/tool denial, HTTPS
   and canonical host, live resources and actual contact delivery.
6. **Owner/evidence:** the partner relationship and up-to-8,000 figure remain
   owner guidance, not officially verified awards. Existing business,
   attribution, service-scope and withheld-page evidence blockers in
   `flagged-items-for-verification.md` remain in force. No new partner,
   local office, statistic, history, address or author/reviewer was invented.

## 4. Citation repairs and evidence

The full fresh source-open inventory is
[phase-16-citations.json](phase-16-citations.json). The broader maintained
`tools/published_citations.py` covers all non-social external anchors plus
schema citation fields and both public LLM files; unknown hosts are included
for review, not dropped or automatically approved. Its three regression
cases cover legacy/unknown hosts, schema-only references and explicit
social/contact exclusions. The initial destination-only filter missed two
legacy tuition-footer sources; the final inventory and source opens include
both. Neither footer host was added to destination approval lists.

| Repair | Current outcome |
|---|---|
| Latvia short `/applying-for-a-long-stay-visa/indian-nationals` | Missing-page body rejected even though fetch wrapper said success. Documents article/schema/journal now cite the opened `/students/indian-nationals` page, with a precise student label and 16 October recheck. Supports Hello Verify before VFS, transaction number and identity/study/funds/accommodation/insurance paragraph. Latvia retains five categories. |
| Dubai landing URL | Redirected successfully in this fresh pass, unlike the earlier recorded HTTP 500. GCC/Costs now use the opened official `/content/Student-Advisory-2026.doc`, labelled as the 2026 document. No earlier failure was rewritten as success. |
| European Commission Latvia / Riyadh / Slovak national visa | Replaced known redirect aliases with their opened same-host direct URLs. Active row labels/dates and article hashes synchronized. |
| Qatar no-steps clause | Advisory does list an application link and usual documents. Removed the contrary implication and retained the visa applicability fact plus institution-confirmation advice. No external commercial application link endorsed. |
| Existing Ministry / Universitaly footer citations | Both freshly opened. Ministry supports language/duration tuition conditions; Universitaly supports current procedures, not an award amount/partners. Not new destination-host approvals. |

All active checked_on dates remain `2026-10-16` because the original review
and this recheck occurred on the same date; explicit Phase 16 recheck records
were appended. Historical original-field records and blockers were retained.
A substantive source-open result is deliberately distinct from raw HTTP 200.

## 5. Exact Italy sentence and change-line inventories

The exact sentence is preserved verbatim:

> Tuition can be fully or largely covered at our partner universities through scholarships of up to 8,000 euros, subject to eligibility.

Every published occurrence also has the local label `Owner-provided
conditional guidance.` and a separate caution to wait for written eligibility,
coverage and payment terms. Existing source-review owner disclaimers remain.
The Home unwritten-award FAQ says No; Services/Home labels do not present the
owner amount as a verified regional DSU figure. Contact metadata no longer
describes Italy as no-charge education. Metadata with no amount remains
amount-neutral. Full FAQ schema/visible parity passes. No named university
was added. The draft DSU article and frozen LLM wording were not edited here.

### Task 2: every changed line range

Numbers are at the named task commits, not historical source-audit numbers.
`zero lines` marks a pure insertion/deletion anchor. Every modified/deleted
line in that task is covered below, including the guard and decision files.
The removed named-affiliation block is About old lines 198-203; its deletion
has no new content line. Later task 4 adds one head line on Services, so its
neutralized programme-comparison line is finally 490 rather than 489.

| File | Before task 2 (`0004749`) | After task 2 (`ce7e665`) |
|---|---|---|
| `about.php` | 195; 199-203; 325; 595; 696; 733 | 195; after 198 (zero lines); 320; 590; 691; 728 |
| `flagged-items-for-verification.md` | after 2757 (zero lines) | 2758-2774 |
| `services.php` | 489 | 489 |
| `tools/blocked-names.txt` | after 0 (zero lines) | 1-10 |
| `tools/check_discovery.py` | after 5 (zero lines); after 11 (zero lines); after 88 (zero lines); 98; 100; after 112 (zero lines); after 152 (zero lines); after 158 (zero lines) | 6; 13; 91-136; 146; 148; 161; 202; 209-213 |
| `tools/test_discovery.py` | after 0 (zero lines) | 1-40 |

### Task 4: every changed line range

These final ranges cover all 19 exact-sentence contexts, matching FAQ schema,
nearby labels, the Contact metadata change, FAQ visibility CSS/fallbacks,
new guard/tests and the appended decision record. The sentence itself was
already exact; the changes strengthen attribution and surrounding cautions.

| File | Before task 4 (`4ca8a0d`) | After task 4 (`0aa08b6`) |
|---|---|---|
| `about.php` | 666 | 666 |
| `contact.php` | 16; 168; 171; after 211 (zero lines); 328; 515; 539 | 16; 168; 171; 212; 329; 516; 540 |
| `flagged-items-for-verification.md` | after 2817 (zero lines) | 2818-2846 |
| `index.php` | 172; 174; 178; 510; 512; 557; 590; 594; 602 | 172; 174; 178; 510; 512; 557; 590; 594; 602 |
| `services.php` | 141-142; 308; after 350 (zero lines); 439; 711; 760; 763-764 | 141-142; 308; 351; 440; 712; 761; 764-765 |
| `tools/check_italy_claims.py` | after 0 (zero lines) | 1-59 |
| `tools/test_italy_claims.py` | after 0 (zero lines) | 1-26 |

## 6. Full final sitemap

All 37 URLs, in the freshly served sitemap order:

```text
https://ilmerastudyabroad.com/
https://ilmerastudyabroad.com/services
https://ilmerastudyabroad.com/about
https://ilmerastudyabroad.com/contact
https://ilmerastudyabroad.com/blog/
https://ilmerastudyabroad.com/privacy-policy
https://ilmerastudyabroad.com/terms
https://ilmerastudyabroad.com/all-pages
https://ilmerastudyabroad.com/blog/study-abroad-with-academic-backlogs
https://ilmerastudyabroad.com/blog/study-abroad-counselling-from-coorg
https://ilmerastudyabroad.com/blog/cost-of-studying-abroad-for-indian-students
https://ilmerastudyabroad.com/blog/documents-needed-to-study-abroad-from-india
https://ilmerastudyabroad.com/blog/scholarships-for-indian-students-study-abroad
https://ilmerastudyabroad.com/study-in-germany
https://ilmerastudyabroad.com/study-in-italy
https://ilmerastudyabroad.com/study-in-uk
https://ilmerastudyabroad.com/study-in-lithuania
https://ilmerastudyabroad.com/study-in-latvia
https://ilmerastudyabroad.com/study-in-slovakia
https://ilmerastudyabroad.com/study-in-gcc
https://ilmerastudyabroad.com/study-abroad-counselling-belagavi
https://ilmerastudyabroad.com/study-abroad-counselling-bengaluru
https://ilmerastudyabroad.com/study-abroad-counselling-chikkamagaluru
https://ilmerastudyabroad.com/study-abroad-counselling-gonikoppal
https://ilmerastudyabroad.com/study-abroad-counselling-hassan
https://ilmerastudyabroad.com/study-abroad-consultants-in-karnataka
https://ilmerastudyabroad.com/study-abroad-consultants-in-kodagu
https://ilmerastudyabroad.com/study-abroad-counselling-kushalnagar
https://ilmerastudyabroad.com/study-abroad-counselling-madikeri
https://ilmerastudyabroad.com/study-abroad-counselling-mangaluru
https://ilmerastudyabroad.com/study-abroad-counselling-mysuru
https://ilmerastudyabroad.com/study-abroad-counselling-ponnampet
https://ilmerastudyabroad.com/study-abroad-counselling-shivamogga
https://ilmerastudyabroad.com/study-abroad-counselling-siddapura
https://ilmerastudyabroad.com/study-abroad-counselling-somwarpet
https://ilmerastudyabroad.com/study-abroad-counselling-udupi-manipal
https://ilmerastudyabroad.com/study-abroad-counselling-virajpet
```

## 7. Every Phase 16 changed file

Relative to the Phase 15 handoff `c2c8b9f`; unchanged `llms-full.txt`,
`sitemap.xml`, robots, page statuses and historical reports are not listed.
This inventory includes the current release evidence/documentation files.

- `about.php`
- `blog/cost-of-studying-abroad-for-indian-students.php`
- `blog/documents-needed-to-study-abroad-from-india.php`
- `contact.php`
- `destinations/gcc.php`
- `destinations/latvia.php`
- `destinations/slovakia.php`
- `flagged-items-for-verification.md`
- `index.php`
- `llms.txt`
- `phase14-article-review.json`
- `phase14-source-review.json`
- `reports/phase-16-checks.json`
- `reports/phase-16-citations.json`
- `reports/phase-16-release-check.md`
- `services.php`
- `tools/blocked-names.txt`
- `tools/check_discovery.py`
- `tools/check_italy_claims.py`
- `tools/check_publication_review.py`
- `tools/published_citations.py`
- `tools/test_citations.py`
- `tools/test_discovery.py`
- `tools/test_italy_claims.py`

## 8. Handoff commands and next action

Use the maintained commands in `tools/README.md` against an authorized native
PHP/Apache staging copy. Run default strict discovery/publication commands;
never treat diagnostic core output as a release pass. Preserve both LLM files
until authorization explicitly expands beyond task-1 link removals. Re-run
all wording/names/discovery gates after any authorized LLM reconciliation.
Externally verify every URL from `tools/published_citations.py` with raw
status/redirect evidence and substantively confirm supporting text. Keep
Czech/Russia/APS/DSU withheld unless their specific evidence gates are met.
The current PR remains open for review, not merge/deploy authorization.
