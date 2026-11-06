# Phase 17 verification and owner-fact handoff

Checked 16 October 2026 on `arena/48320ee5-ilmerastudyabroad`.
PR: https://github.com/fawazbhseo/ilmerastudyabroad/pull/1 (open, unmerged).
Phase start: `d398a22`. Task commits: `31dd953`, `c5a8a5b`, `1731585`, then
the final audit commit in branch history. No main push, merge or deployment.

## Decision

**The authorized owner/site fixes are implemented. Global acceptance remains
blocked, not falsely confirmed.** The default strict discovery/publication
commands still fail on restricted pre-existing LLM names, and the global
wording scan still fails in those same unchanged files. No permission was
inferred to edit either LLM file. No page status changed. Native Apache,
external raw transport and actual contact delivery are not proven locally.

The editable published HTML, metadata, schema, FAQ, alt/link text and Contact
surfaces pass the maintained name/wording scans. Online-presence checks pass
across these surfaces and both public LLM files. No new named university,
prohibited wording or em dash was introduced. Earlier historical reports and
blockers remain intact except for the two explicitly superseded owner inputs.

## 1. Final operating model and postal/schema decision

Owner's final statement, recorded 16 October 2026: ILMERA operates virtually,
with no physical office and no in-person counselling location anywhere.
All 17 guides now identify online counselling in their unique titles,
headings and metadata and each contains this plain sentence in its authored
section, with its actual audience name:

> Counselling is online, and students from [place] do not need to travel to an office.

The shared contact/footer wording and the Coorg article's metadata, headline,
body and generated incoming link labels identify online delivery. The last
audit also clarified the Contact directory and footer audience headings,
without changing their targets. No institution, local venue or meeting place
was invented. Official embassy interview procedures remain attributed to the
responsible body, not rewritten as online ILMERA counselling.

The old contact data contained a **locality-only PostalAddress**: Coorg;
Kodagu, Karnataka; country IN. It did not contain a street/building, postcode,
delivery address or coordinates. Retained it only in the Contact organisation,
with the label `Postal locality only; not a counselling location` and matching
visible limitations. Removed schema address copies elsewhere, including the
personal home-location copy, and the duplicate legacy contact node. No
registered-address or postal-delivery service was inferred from a locality.

Location pages use **Service with an Organization provider**. Both have the
actual place in areaServed; serviceType states online counselling. Neither
has storefront type, street address, address property or geo coordinates.
The sitewide organisation types were simplified to Organization. Existing
phone/WhatsApp/video channels were retained, with no city-specific contact.

### Location quality and unchanged status

- All 17 remain published, with unchanged status flags.
- Authored prose: **382-396 words**, excluding headings/FAQs/shared contact text.
- All 136 city-normalised five-token comparisons pass: **6.410%**
  maximum authored overlap and **13.476562%** maximum fresh
  full rendered-main overlap, each below 15%.
- Unique titles, H1s, meta descriptions and FAQs remain; evidence hashes and
  both overlap records were refreshed, not bypassed to preserve indexability.
- Nine destination summaries/provenance and all page statuses are unchanged.

## 2. Final GCC notes

First visible note, owner-confirmed business scope:

> ILMERA supports students applying to universities in all six GCC countries: UAE, Saudi Arabia, Qatar, Kuwait, Oman and Bahrain.

Second visible note, separately limited official-source scope:

> Official-source information on this page currently covers the UAE, Qatar, Saudi Arabia, Oman and Bahrain; Oman and Bahrain coverage is limited to student registration. Kuwait information is not yet available here from a verified official source, so students should confirm Kuwait requirements directly with the relevant institution and authority.

The owner confirms university partnerships across all six listed countries.
The page claims no partnership with a government or embassy and names no
university. Metadata and WebPage/Service descriptions exactly use both visible
notes. Service areaServed lists six business countries, not six sets of
verified student rules. The existing UAE-only intro is left unchanged and
still explicitly attributed to its UAE source.

The protected `intro_answer`, `slug`, `name`, `ilmera_summary` and
`summary_provenance` are byte-preserved. Source approval lists were not
expanded. Oman now has the newly opened replacement registration page at
`https://www.indemb-oman.gov.in/registerstd/`, found through the same embassy's
navigation after the old path returned a missing-file body. Only its request
for Indian students residing in Muscat for education or training to register
was added, as an FAQ with checked_on `2026-10-16` and a matching review row.
It is not admission, visa or work-rule evidence. Bahrain's registration
notice remains explicitly dated 31 May 2022.

The Kuwait embassy directory was opened, but no usable current student-rule
content was accepted. **No Kuwait fact, verified citation or approved-host
expansion was added. Kuwait remains an open source blocker.** The note says
information is not yet available here from verified evidence, not that no
official rules exist anywhere. Fresh open outcomes and limits are recorded
in [phase-17-source-opens.json](phase-17-source-opens.json); wrapper success
is not represented as a raw HTTP-status certificate.

## 3. Targeted documentation closures

Only these owner-input blockers are closed in the dated append to
`flagged-items-for-verification.md`:

- **CLOSED:** confirmation of physical presence and the counselling model,
  resolved by the final virtual-only/no-premises statement.
- **CLOSED:** confirmation of the GCC country list and broad university
  partnership country scope, resolved for all six countries.
- **OPEN:** current official-source Kuwait student requirements.

Individual agreement/award evidence, attribution, other destination source
gaps, restricted LLM content, delivery and native-staging checks remain as
recorded. The original historical blocker paragraphs were not rewritten.
CHANGELOG and maintenance instructions append the current decisions.

## 4. Fresh checks after every task

[phase-17-checks.json](phase-17-checks.json) stores the fresh per-task summaries
without copying restricted names/wording into new documentation. No prior
phase's QA result is substituted for one of these executions.

| Task | PHP parses | Fresh renders | Chromium cases | Presence / core discovery | Default strict discovery/publication | Seconds |
|---|---|---|---|---|---|---|
| 1 | 83 PASS | 42 PASS | 252 PASS | PASS | FAIL: restricted LLM names | 84.97 |
| 2 | 83 PASS | 42 PASS | 252 PASS | PASS | FAIL: restricted LLM names | 85.65 |
| 3 | 83 PASS | 42 PASS | 252 PASS | PASS | FAIL: restricted LLM names | 85.71 |
| 4 | 83 PASS | 42 PASS | 252 PASS | PASS | FAIL: restricted LLM names | 85.63 |

Each browser run covers 42 routes at 375, 768 and 1280 pixels, JavaScript
on/off: 252 cases. It checks page errors, native/button FAQ interactions and
full-answer readability, mobile navigation, duplicate discovery links and
study-section overflow. Each new browser run replays that task's fresh HTML
captures and local images; other external requests were aborted. This is not
a production-network, native-Apache or external-resource certificate.

### Final matrix

| Requirement | Result | Scope / evidence |
|---|---|---|
| Every PHP file parses | PASS | 83 files using PHP 8.5 WASM TOKEN_PARSE; not native PHP CLI |
| Clean route renders/status/canonicals | PASS, local | 42 fresh responses; 41 editorial self-canonicals; four drafts and utility noindex |
| Browser cases | PASS, capture scope | 252 fresh cases with JS on/off and real FAQ/mobile controls |
| Online-only wording guard | PASS | Published surfaces plus both LLM files; nine current regression cases, including plural offers |
| Location note, postal/storefront/geo schema | PASS | 17 visible notes; Service/Organization with matching place areaServed; no local address/coordinates/storefront |
| Location uniqueness/prose/pairwise gates | PASS | 17 unique guides; all authored and full-main 136 pairs measured again |
| GCC visible/meta/schema scope consistency | PASS | Six business countries, five source countries; no Kuwait fact added; protected fields preserved |
| Structured data / FAQ parity | PASS | Every rendered JSON-LD block parses; FAQ questions/answers match visible content |
| Sitemap health/parity | PASS, local | 37 unique entries, each 200/self-canonical/not-noindex; committed XML matches runtime generation |
| Internal broken links/fragments/resources | PASS, core | Fresh route/resource/fragment scan, no indexable orphan or draft target |
| Draft URLs in discovery/schema/sitemap | PASS | All four drafts excluded, including both public LLM files |
| Em dash scan | PASS | Fresh published HTML/schema/meta plus both LLM files |
| Named-university scan | PASS in editable HTML; FAIL overall | Restricted existing LLM content remains; no new name introduced |
| Restricted-wording scan | PASS in editable HTML; FAIL overall | Both LLM files unchanged; global acceptance cannot be confirmed |
| Default strict discovery/publication | FAIL, not waived | Stops at restricted LLM naming; diagnostic core is not a release pass |
| Source/hash/contact/summary/status gates | PASS independently | Active exact records, hashes, known contacts and unchanged statuses/protected values |
| LLM permission / line endings | PASS | Both LLM files exactly phase-start bytes; existing LF/CRLF/mixed endings preserved |
| External transport and native staging | UNVERIFIED | No new all-source raw-200, external-asset, real-delivery or Apache certificate |
| Overall unconditional acceptance | **BLOCKED** | Restricted LLM failures and the open evidence/deployment limits remain explicit |

Name, citation-inventory and amount regression suites were rerun too. Strict
CLIs use default enforcement. A separate core discovery run isolates sitemap,
links, robots and physical-presence health, but does not override strict
failure. Stored source/hash checks were independently executed because the
strict publication command correctly stops at the earlier LLM failure.

## 5. Counts and sitemap

Original 29 targets: **27 published / 2 draft**. With separately held APS/DSU
articles: **27 published / 4 draft**, 31 targets. Whole site: **37 indexable
published HTML pages**, four draft editorial pages and a separate noindex
404 utility. No status, sitemap URL or canonical route was changed.
Noindex is not authentication; private staging needs real access control.

Full final sitemap, in freshly served order:

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

## 6. Every changed task-1a line

The complete before/after source-line table is
[phase-17-task-1-lines.md](phase-17-task-1-lines.md). It covers every changed
line in all 26 task-1 published-surface source files, including accompanying
postal/schema removals, metadata, generated link text and authored notes.
The appended final-audit supplement also covers `contact.php:849` and
`includes/footer.php:85` and the Home qualifier at `index.php:543`. Task-1 destination-template line 168 is finally
173 after the five task-2 scope/schema insertions above it. All other task-1
source positions remain as recorded. Deletions have their original line
ranges and zero-line anchors rather than fictitious new line numbers.

## 7. Every Phase 17 changed file

Relative to `d398a22`, including this final report and machine evidence:

- `CHANGELOG.md`
- `about.php`
- `blog/study-abroad-counselling-from-coorg.php`
- `contact.php`
- `destinations/gcc.php`
- `flagged-items-for-verification.md`
- `includes/destination-page.php`
- `includes/footer.php`
- `includes/place-page.php`
- `includes/posts.php`
- `index.php`
- `phase14-location-review.json`
- `phase14-source-review.json`
- `places/belagavi.php`
- `places/bengaluru.php`
- `places/chikkamagaluru.php`
- `places/gonikoppal.php`
- `places/hassan.php`
- `places/karnataka.php`
- `places/kodagu.php`
- `places/kushalnagar.php`
- `places/madikeri.php`
- `places/mangaluru.php`
- `places/mysuru.php`
- `places/ponnampet.php`
- `places/shivamogga.php`
- `places/siddapura.php`
- `places/somwarpet.php`
- `places/udupi-manipal.php`
- `places/virajpet.php`
- `reports/phase-17-checks.json`
- `reports/phase-17-source-opens.json`
- `reports/phase-17-task-1-lines.md`
- `reports/phase-17-verification.md`
- `services.php`
- `tools/README.md`
- `tools/check_discovery.py`
- `tools/test_presence.py`

Neither LLM file, `sitemap.xml`, robots, existing canonical routes or page
status flags is changed. Prior phase reports remain unchanged. The final
branch is for review only; PR #1 remains open, with no merge or deployment.
