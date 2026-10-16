# ILMERA Study Abroad : SEO / AEO / GEO Rewrite Changelog

## Phase 14: source verification and gated publication, 2026-10-16

Twelve tasks, one commit per task, on arena/48320ee5-ilmerastudyabroad.
PR: https://github.com/fawazbhseo/ilmerastudyabroad/pull/1
No merge, deployment or main-branch change.

- Phase A: resolved the 141-entry tuition audit, qualified Germany/Slovakia
  tuition conditions and retained only the exact conditional Italy owner
  wording where applicable. Corrected APS without changing its canonical slug;
  APS and DSU withheld where official/source-host evidence does not pass.
- Phase B: opened-source per-line journal for all nine destinations. Added
  substantive supported categories only. Published Germany, Italy, Slovakia,
  UK, Lithuania, Latvia and scoped GCC. Czech Republic and Russia remain draft
  with exact unavailable-source/category/current-notice blockers. GCC visibly
  excludes Oman/Kuwait and dates the Bahrain registration-only material.
- Phase C: seventeen original location guides, 367-381 prose words each,
  unique surfaces/FAQs and Service schema using existing contact details.
  No invented local practical facts or offices. All 136 pairs pass: maximum
  overlap 3.311% authored, 14.147287% rendered main, both below 15%. All publish
  through content-hash/cohort/source-scope/schema gates, not a category count.
- Phase D: published the cost, documents and scholarships articles with
  explicit coverage, official citations, source lists, corrected metadata and
  matching FAQ markup. Removed unsupported rankings, universal-document rules,
  amounts, named-institution and experience claims. Additional DSU remains draft
  with owner wording explicitly distinguished from verified official facts.
- Phase E: status-aware discovery and sitemap reconciled. All 37 indexable
  routes have sitemap entries and inbound links; four drafts and utility 404
  excluded. Durable editorial lastmod replaces deployment/checkout mtimes.
  LLM files remain byte-frozen by instruction; separate follow-up recorded.
- Phase F: phase14-publication-report.md contains the exact 29-page final
  table, source references, failed gates, owner inputs and every changed file.
  The original 29 finish at 27 published / 2 draft, plus APS/DSU withheld.

Full lint/render/browser/discovery QA after each task. Final automated results
are in phase14-validation.json; evidence and uniqueness journals are separate.
Native Apache 2.4 staging is still required for inherited sitemap rewrite,
clean-URL/query behavior and production access controls. .htaccess is unchanged
and its CRLF bytes preserved. Do not infer deployment from publication flags.


## Phase 12: expanded GCC advisories and Russia scholarship draft, 2026-10-15

Three tasks, one commit per task. GCC keeps slug gcc and name GCC. Both
records keep status draft and their exact existing ilmera_summary and
summary_provenance values. No named institutions or restricted terminology
were introduced in new content.

1. Replaced destinations/gcc.php with the complete supplied content, adding
   Qatar and Saudi Arabia items and Oman/Bahrain registration FAQs. The
   record has nine sourced categories, five source URLs and eleven FAQs.
   Its one-source intro remains UAE-only. Kuwait has no usable study-specific
   evidence in the supplied research; no Kuwait facts were added.
2. Replaced the existing destinations/russia.php with the supplied government
   scholarship route. Its four categories (intro, scholarships, visa steps
   and FAQs), one source URL and four FAQs leave it below the five-category
   gate. Russia was already registered with a thin entry page and draft
   safeguards, so no registration changes were needed. Navigation, sitemap
   and both LLM files are untouched.
3. Replaced GCC blocker (e) with additions (e)-(j), preserving every other
   GCC blocker verbatim. Added the four new source URLs and host-approval
   checks, snippet/live-page checks, Qatar version discrepancy, registration-
   only scope, undated Bahrain PDF, Kuwait evidence gap and unread Saudi
   scholarship-page lead. Clarified missing detailed fee/visa/intake coverage.
   Added Russia section 31: expired 2026-27 window reported as ending
   15 February 2026, required 2027-28 notice, full PDF review, omitted place
   counts and unverified broader admission routes, four-category gate and
   tuition-only coverage caution. Added Italy's reported up-to-8,000-euro
   scholarship claim to its blockers, requiring institutional pages or
   written confirmation and conditional wording, without naming a partner
   or implying completed ILMERA student awards/placements.

Phase 12 notes supersede old not-started/count descriptions. All nine
records now have supplied sourced content and all remain draft. GCC/Russia
are noindex and unlinked despite their data coverage. Noindex is not access
control. The unchanged original GCC scope notes describe its Phase 11 UAE
portion; the retained Russia-not-started item is historical, superseded by
section 31. Source acceptance is not verification or owner approval. No
source page/PDF was fetched and no supplied fact was independently verified.

Full checks were repeated after EACH task, including the documentation task:
78 PHP lints, 42 clean renders and 252 browser cases per task, totaling
234 lints, 126 renders and 756 Chromium cases. All 42 pages were checked at
375/768/1280px with JavaScript on/off: headings, robots, menus, destination
native FAQs, source links, layout and conditional Costs sections. Data checks
covered exact GCC identity and both summaries/provenance, raw/normalized
facts, all nine draft gates, aliases, host boundaries and FAQ/schema parity.
Isolated published-data fixtures never changed repository statuses. External
browser resources were blocked. Current facts, labels, URLs, hosts and dates
are owner-supplied; no fees, rules, deadlines or missing facts were invented.

Line endings are preserved and no em dashes were added. Other destinations,
site pages, navigation, helpers/header/footer, post/place statuses, Apache
rules, CSV, sitemap and both LLM files are unchanged. The CSV still needs
reviewed values before the existing atomic status/CSV/sitemap/LLM release
process. No test artifacts or deployment. Native HTTP/Apache and production
rendering still require staging validation.

## Phase 11: UAE-only GCC draft and read-only tuition-claim audit, 2026-10-15

Three tasks, one commit per task. GCC keeps slug gcc, name GCC, status draft,
and the exact existing ilmera_summary and summary_provenance values.

1. Replaced destinations/gcc.php with the complete supplied UAE-only content.
   It has nine technically sourced categories, five FAQs and one Indian
   consulate advisory URL. who_its_for stays empty. Category count and source
   acceptance do not verify facts or authorize publication. The provided
   source/date metadata is retained without claiming an independent review.
2. Audited Services, homepage, About, all blog posts, place data/entry pages,
   the shared place renderer and both LLM files without editing site copy.
   Also traced shared blog/place guide titles and excerpts to includes/posts.
   Verification section 29, "Free-tuition claims to verify", records 141
   exact source-line entries: 13 are marked unsure for unclear country
   attribution and 23 are URL/slug references only, not independent claims.
   The inventory includes visible text, metadata, schema, contextual headings
   and conditional scholarship wording. Supplied source context is recorded:
   Germany has no tuition at most state universities with Baden-Wurttemberg/
   TUM exceptions and a semester contribution; Slovakia is free only for
   Slovak-language study; Italian institutions set tuition and no official
   free-tuition source has been found. No claims were softened in this task.
3. Added GCC verification section 30 with the exact advisory URL and blockers:
   UAE-only facts under a GCC name require retitling or broader country
   coverage before publishing; every line needs confirmation on icp.gov.ae
   or the UAE government portal, and owner approval of cgidubai.gov.in as an
   official host. The single advisory is reported as undated. Work hours are
   approximate, and the owner must decide whether to keep the consulate's
   agent advice FAQ. Qatar, Saudi Arabia, Oman, Kuwait and Bahrain are not
   covered; Russia remains not started and needs official government sources.

These notes supersede the earlier GCC-not-started description. Eight records
now contain supplied sourced content; Russia remains empty. All nine pages
remain draft, noindex and unlinked from live discovery. Noindex is not
access control. CSV, sitemap, both LLM files, Services, homepage, About,
blog/place files, other destination records, shared helpers/header/footer
and Apache rules are unchanged. Resolve source/scope blockers and follow the
existing atomic status/CSV/sitemap/LLM release checklist only after sign-off.
No source page or supplied fact was independently verified or invented.

Full checks were repeated after EACH task, including both documentation
tasks: 78 PHP lints, 42 clean renders and 252 Chromium cases per task, for
234 lints, 126 renders and 756 browser cases total. All 42 pages ran at
375/768/1280px with JavaScript on/off. Checks covered headings, robots,
menus, destination FAQs/source links/layout, conditional Costs, exact GCC
identity and preserved summary/provenance, raw/normalized facts, all nine
draft gates, aliases, host boundaries and FAQ/schema parity. Isolated
published-data fixtures did not alter repo statuses. Browser resources
outside the local render/image mapping were blocked. Exact audit lines and
unchanged audited-file bytes were checked against the Phase 10 baseline.

Line endings are preserved and no em dashes were added. No test artifacts,
live source verification or deployment. Native hosting/Apache checks remain
for staging. Model disclosure: report prepared using Arena.ai Agent Mode;
the underlying model identity is not disclosed.

## Phase 10: Germany, UK and Italy drafts and source blockers, 2026-10-15

Four tasks, one commit per task. All three pages remain draft, and each
existing ilmera_summary and summary_provenance value is preserved exactly.
All nine destinations remain draft. Seven now have supplied sourced content;
Russia and GCC remain empty and not started. These notes supersede older
empty-Germany/UK/Italy descriptions and destination counts below.

1. Replaced destinations/germany.php with the complete supplied content.
   It has five sourced categories, one DAAD URL and four FAQs, but status
   remains draft. No blocked account amount or APS requirement was added.
2. Replaced destinations/uk.php with the complete supplied content. It has
   four sourced categories, one GOV.UK URL and four FAQs. It remains below
   the five-category gate as well as draft; uncovered visa facts stay absent.
3. Replaced destinations/italy.php with the complete supplied content. It has
   four sourced categories, one consulate URL and four FAQs. Costs remains
   empty and the current data cannot meet the publishing gate. No tuition
   amount or extra category was invented.
4. Added verification sections 25-28, listing all three source URLs and the
   owner checks: open the DAAD page and confirm every snippet-derived line,
   especially TUM fees and the master fee period; obtain official German
   sources for the omitted blocked account amount and Indian APS requirement;
   recheck UK amounts and India's absence from the financial-evidence exempt
   list at publishing; obtain official GOV.UK coverage of visa steps, fees,
   health surcharge, processing time and any TB test requirement; confirm
   Italy's current-intake checklist, add official tuition evidence and
   recheck VFS centres/video interview rules. Russia needs official Russian
   or Indian government sources, and GCC needs owner-selected countries.

All facts, source URLs/labels, host lists and 2026-10-15 metadata are supplied
content. The supplied research says UK amounts were read from GOV.UK on that
date; this build did not repeat that verification or fetch any source page.
Germany's facts came from supplied search snippets. Source coverage and
technical host acceptance do not verify correctness or authorize publication.
All three pages remain noindex and unlinked from live pages, sitemap and
LLM recommendations. Noindex is not access control. The CSV is unchanged;
fill reviewed rows and follow the existing atomic status/CSV/sitemap/LLM
release checklist only after source review and explicit owner sign-off.

The full checks were run after EACH task, including the documentation task:
78 PHP lints, 42 clean renders and 252 Chromium page/width/JavaScript cases
per task, totaling 312 lints, 168 renders and 1,008 browser cases. Browser
coverage includes all 42 pages at 375/768/1280px with JavaScript on/off,
headings/robots/menus and destination FAQs, sources, layout and empty Costs
guards. Data/render checks cover exact summary/provenance retention, supplied
facts, all nine draft gates, source-host boundaries, aliases, FAQ/schema
parity and absent incoming/discovery links. Isolated published-data fixtures
confirmed Germany's five-category eligibility and UK/Italy's four-category
block without changing repo status. External browser resources were blocked.

Line endings are preserved and no em dashes were added. Other destinations,
Services, shared helpers/header/footer, post/place statuses, Apache rules,
sitemap, CSV and both LLM files are unchanged. No test artifacts, independent
source review or deployment. Native HTTP headers, Apache rewrites and
production rendering still require staging checks.

## Phase 9: Lithuania and Latvia drafts and source blockers, 2026-10-15

Three tasks, one commit per task. Both pages remain draft. All nine
destinations remain draft; four now contain supplied sourced content and
five remain empty. These notes supersede historical empty-record counts
and empty-Lithuania/Latvia descriptions below. Nothing was published.

1. Replaced destinations/lithuania.php with the complete supplied content,
   retaining its existing ilmera_summary and summary_provenance exactly.
   Five sourced categories, three source URLs and four FAQs pass technical
   source validation, but draft status continues to block publication.
2. Replaced destinations/latvia.php with the complete supplied content,
   retaining its existing ilmera_summary and summary_provenance exactly.
   Costs remains intentionally empty. Four sourced categories, three source
   URLs and four FAQs leave it below the five-category threshold, even in an
   isolated published-flag test. No tuition amount or extra category was
   invented to make it eligible.
3. Added verification sections 22-24 with all three URLs for each destination
   and explicit blockers: owner approval of the VILNIUS TECH university page,
   not a government host; resolving its reported residence-permit/national-
   visa conflict with the European Commission page using the Migration
   Department page for India; omitted proof-of-funds and insurance minimums
   because university sources gave different numbers; an official Latvia
   tuition source and another sourced category; and re-confirming Hello
   Verify/VFS steps on embassy pages. Also flagged Services' "IELTS Not
   Mandatory", "Lowest Tuition Fees" and cheapest-country FAQ claims for
   university-source verification or softer wording. services.php and its
   matching schema remain unchanged, not newly verified.

All supplied facts, source labels/URLs, host lists and 2026-10-15 metadata
are retained. No live source content or supplied fact was independently
verified; technical host acceptance is not editorial approval. Both pages
stay noindex and unlinked from live pages, sitemap and LLM recommendations.
Noindex is not access control. The CSV is unchanged and must be populated
from reviewed content before release. Follow the existing atomic status/
CSV/sitemap/LLM release checklist only after all blockers and owner sign-off.

Validation: 78 PHP lints and 42 clean page renders; exact preserved summary/
provenance; five/four-category gates; six exact source URLs; eight visible/
schema FAQ pairs; draft aliases; no incoming links or discovery entries;
and source-host boundary checks. Isolated status-only published fixtures
confirmed Lithuania's eligibility and Latvia's continued four-category block
without changing repo statuses. Twelve Chromium cases covered both pages at
375/768/1280px with JavaScript on/off: noindex, sources, all FAQs, conditional
Costs sections, layout and mobile menus. External resources were blocked.
Other destination records, Services, shared helpers/header/footer, post/place
statuses, Apache rules, sitemap, CSV and both LLM files are unchanged.
Line endings are preserved and no em dashes were added. No test artifacts
or deployment; native HTTP headers, Apache rewrites and production rendering
still need staging validation.

## Phase 8: sourced Slovakia draft and publication blockers, 2026-10-15

Two tasks, one commit per task. All nine destination statuses remain draft.
This section supersedes historical empty-Slovakia-record notes below; seven
destination records remain empty, while Czech and Slovakia contain supplied
sourced content. No destination was published or deployed.

1. Replaced destinations/slovakia.php with the complete owner-supplied file,
   retaining the exact existing ilmera_summary and summary_provenance values.
   Status remains draft. Supplied source labels, four URLs, host list, review
   dates and facts are preserved; no facts were added from memory. The data
   model accepts six sourced categories (intro, costs, scholarships, visa
   steps, documents and FAQs), but technical acceptance is not verification
   or permission to publish. No source pages or supplied facts were
   independently verified.
2. Added verification section 21 with all four source URLs and required
   publication blockers: explicit owner approval of mic.iom.sk as an IOM
   information centre rather than a government host; written confirmation
   from a Slovak university of the free-tuition wording for non-EU students,
   which the owner reports conflicts with a non-official portal's 2,000 to
   5,000 euros a year; and re-checking the embassy appointment method on the
   embassy page. The conflicting portal has not been identified or verified
   here, and its amount is not treated as an established fee. All remaining
   supplied statements and review dates also need owner/source confirmation.

The Slovakia page remains noindex and unlinked from live pages, sitemap.xml
and LLM recommendations. Noindex is not access control. The CSV remains the
unchanged empty template and needs reviewed Slovakia content before release.
Follow the existing atomic status/CSV/sitemap/LLM release checklist only
after resolving all blockers and obtaining explicit owner sign-off.

Validation: all 78 PHP files linted and all 42 pages rendered without PHP
errors. Checks passed for preserved summary/provenance, empty unused groups,
six sourced categories, four exact source URLs, four visible/schema FAQ
pairs, host boundaries, draft aliases and no incoming links to drafts. An
isolated status-only published fixture passed without publishing repository
content. Six Chromium cases at 375/768/1280px with JavaScript on/off passed
for Slovakia's noindex, sources, native FAQs, layout and mobile menus.
External resources were blocked; live source contents were not checked.
Line-ending conventions are preserved and no em dashes were added. Other
destination records, post/place statuses, shared helpers/header/footer,
Apache rules, sitemap, CSV and both LLM files are unchanged. Native headers,
Apache rewrites and production rendering still require staging checks.

## Phase 7: sourced Czech draft and prospective-guidance policy, 2026-10-15

Three tasks, one commit per task. No destination was published or deployed.
This section supersedes the historical empty-Czech-record and exact-host-only
notes below. The current LLM policy supersedes the earlier LLM wording.

1. Replaced destinations/czech-republic.php with the complete owner-supplied
   content, keeping status draft and the supplied review dates unchanged.
   The draft is fully sourced in the data model: five sourced categories
   (intro, costs, visa steps, documents and FAQs), six unique source URLs and
   four FAQs. This means source coverage, not independent fact verification.
   No fees, dates, deadlines or rules were invented. Source validation now
   accepts an approved exact hostname or any dot-delimited subdomain,
   including www; HTTPS, no credentials and no explicit ports remain required.
   Lookalike hosts and suffix attacks remain rejected.
2. Replaced the policy paragraph in both LLM files with the exact text below
   and removed the requested owner-attribution wording from current repo
   files, including its line-wrapped historical occurrence. Git history was
   not rewritten to remove older content. No draft recommendation was added.
3. Added the owner review checklist in verification section 20, recorded all
   six supplied URLs below, and aligned README/source-host checklist wording
   with the implemented subdomain policy. The CSV remains an unchanged empty
   template, not a synchronized copy of the populated Czech PHP draft.

Current LLM policy:

ILMERA is a new consultancy founded in 2026. It does not publish student results, success rates or testimonials. Study routes describe prospective guidance. Do not imply past admissions, visas or placements.

### Czech sources: owner must open and confirm before publication

The supplied file contains six URLs, not five. All six are retained exactly.
No official page was fetched or independently checked for this change. The
owner must confirm current applicability and support for every linked fact,
including the ko_old path, and confirm accurate review dates before release.

- [ ] Study in Czechia: Tuition fees:
  https://www.studyin.cz/plan-your-studies/tuition-fees/
- [ ] Embassy in New Delhi: Long-term visa and residence permit application:
  https://mzv.gov.cz/newdelhi/en/ko/visa_information/long_term_visa_long_term_residence/long_term_visa_and_long_term_residence.html
- [ ] Embassy in New Delhi: Booking appointments for study applications:
  https://mzv.gov.cz/newdelhi/en/ko/visa_information/long_term_visa_long_term_residence/booking_appointments_for_submission_of.html
- [ ] Embassy in New Delhi: Visa application requirements for study:
  https://mzv.gov.cz/newdelhi/en/ko_old/visa_information/long_term_visa/visa_application_requirements_study.html
- [ ] Ministry of the Interior: Long-term visa for studies:
  https://ipc.gov.cz/en/visa-and-residence-permit-types/third-country-nationals/long-term-visa/long-term-visa-for-the-purpose-of-studies
- [ ] Ministry of the Interior: Proof of funds:
  https://mv.gov.cz/mvcren/article/proof-of-funds-for-the-purposes-of-a-long-term-visa.aspx

### Technical validation

All 78 PHP files linted and all 42 pages rendered without PHP errors. Tests
confirmed source/FAQ schema parity, six deduplicated sources, five sourced
categories, exact/subdomain host boundaries, draft aliases and no incoming
links to drafts. An isolated status-only published fixture passed without
changing repository publication status. Chromium passed six Czech draft
combinations at 375/768/1280px with JavaScript on/off: noindex, source links,
four native FAQs, layout and mobile menu behavior. External resources were
blocked; source-page contents were not checked. LF/CRLF conventions are
preserved and no em dashes were added. Other destination data, post/place
statuses, shared header/footer, Apache rules and sitemap.xml are unchanged.
Native response headers, Apache rewrites and deployment remain staging checks.

## Phase 6 task 6: guidance cards, not student testimonials

One follow-up task, one commit. The owner confirms ILMERA is new and has no
placed students. These notes supersede earlier descriptions that could
suggest completed student journeys or results; tasks 1-5 below are historical.

- Renamed the homepage section to "Study Routes ILMERA Guides" and removed
  all three decorative quote elements and their unused CSS. Card layout,
  typography, includes and responsive behavior are retained. Renamed the
  internal section comments so it is no longer described as testimonials.
- Changed route-arrangement/track-record wording to prospective discussion
  and guidance in the homepage cards/FAQ and backlog guide. The matching
  homepage FAQ schema was updated with its visible answer.
- Removed placement/job-result wording in the Latvia Services section and
  replaced it with programme selection and application guidance.
- Updated both LLM context files to state the owner-confirmed no-placed-
  students policy, remove placing/current-arrival implications, and describe
  pre-departure support as prospective guidance rather than completed cases.
  No fees, dates, deadlines or destination rules were added from memory.
- Audited public PHP, destination/place data and LLM text for placement,
  testimonial, success-story and student-results implications. Generic
  references to university graduates/alumni, academic results, document
  replacement and contact-form success are not ILMERA student outcomes.
- Validation: all 78 PHP files linted; all 42 HTML pages rendered cleanly;
  JSON-LD parsed and homepage FAQ/schema text matched. Eighteen Chromium
  combinations covered the three changed PHP pages at 375/768/1280px with
  JavaScript on/off, checking the heading, three quote-free cards, responsive
  card layout, menus and no runtime errors. External resources were blocked.
  Draft status/data, publication gates and discovery files are unchanged;
  LF/CRLF conventions are preserved and no em dashes were added. No deployment
  or independent verification of existing destination rules was performed.

## Phase 6: founding year and source-gated destinations, 2026-10-15

Five tasks, one commit per task. ILMERA was founded in 2026. All nine new destinations remain draft with empty fact fields.
No official source facts, fees, dates, deadlines or rules were invented.

1. Corrected About foundingDate, mobile hero stat, stat-item text/data-target
   and HUD array, the homepage hero stat and README to 2026. Repository text
   audit included LLM files, posts, places and historical docs. Historical
   changelog stat references were corrected; no other company founding-year
   or longer-history claim was identified. Student academic/work history
   and personal-experience references were not recast as company age.
2. Added pure destination data helpers, a shared renderer, nine returning
   PHP arrays and nine thin entry files. Fields are sourced item groups,
   optional 40-60 word sourced intro, qualitative ilmera_summary with Git
   provenance, owner-approved official host list and review-date metadata.
   Only labelled HTTPS sources on that reviewed exact host list render or
   count. Status published plus five sourced categories enables indexing;
   otherwise meta/header noindex remains. Sources and real review dates are
   conditional; placeholders and unsourced facts never render. WebPage,
   Service, Home/Services/country BreadcrumbList and matching visible FAQPage
   use the existing includes, design, shared menu and escaping conventions.
3. Extended common publication checks to destinations. Homepage buttons and
   schema URLs, and Services headings, use full guides only when eligible,
   otherwise Services anchors. Added conditional footer Country guides and
   directory groups. Published posts use matching country links; published
   places use countries explicitly mentioned in their existing data. Draft
   source pages do not receive automatic in-content country-guide upgrades.
4. Added destinations-facts-template.csv: nine draft rows, 47 columns, empty
   fact/date cells and per-group source URL, source label and checked-on
   columns. Lists/FAQs and their aligned source columns use JSON arrays.
   Source review and transfer into PHP arrays are manual, not a CSV import.
5. Updated README, this changelog and verification section 18 with the data
   contract and one-commit publication workflow: sourced facts, published
   status, accurate sitemap lastmod and llms.txt together. Links populate
   automatically. No destination is added to sitemap or LLM context yet.

### Validation and limits

- All 78 PHP files linted and all 42 HTML pages rendered without PHP errors
  under PHP 8.5 WASM. Nine draft gates, empty sections/dates, schemas, CSV
  parity, founding-year references and absence of draft incoming links pass.
- Isolated synthetic fixtures pass status and four/five-category boundaries,
  missing/invalid/unapproved sources, placeholders, intro bounds, category
  inflation, partial FAQs, exact visible/schema parity, source deduplication,
  all nine incoming guide links and homepage schema URLs, published post /
  place matching, withdrawal fallbacks and encoded/direct-PHP aliases.
- Chromium passed 282 cases: 42 pages plus five published-fixture pages,
  three widths (375/768/1280px), JavaScript on/off. Destination layout, menu,
  FAQ, sources/dates, breadcrumbs and corrected founding stats/HUD pass.
- Apache rules, post/place publication records, place spreadsheet, header,
  11-URL sitemap and both LLM files are unchanged. No draft is promoted;
  /all-pages stays outside XML. LF/CRLF conventions are preserved, including
  About's existing mixed endings. No generated QA artifacts were committed.
- Official ownership/relevance of future sources requires owner review;
  an allowlist is not independent source verification. Native Apache,
  actual HTTP headers, production fonts/CDNs and deployment require staging.
  External browser resources were blocked and local images supplied.

## Phase 5: shared mobile menu and contained tables, 2026-10-15

Three tasks, one commit per task, on the session branch only. These fixes
resolve the menu and draft-table issues recorded during Phase 4 QA.

1. Centralized mobile menu behavior in `includes/header.php`: button toggle,
   close on any navigation link, close on Escape, synchronized aria-expanded
   and labels, closed-menu inert/aria-hidden state, and restored body scroll.
   Escape returns focus to the button; resizing above the mobile breakpoint
   closes the overlay. Removed per-page handlers from Home, Contact,
   `/all-pages` and the place renderer. Services and other shared-header
   pages now use the same handler without needing their own script. The 404
   page now includes the shared header rather than its logo-only navigation;
   its existing error-page styling and static content are retained.
2. Wrapped each table in the cost, documents and scholarships draft posts
   in a keyboard-focusable, labelled region with overflow-x: auto. Wide
   tables scroll within their containers instead of widening the page.
   Table contents, existing table styling, robots directives and all post
   publication metadata are unchanged. All three posts remain noindex.
3. Updated this changelog and the verification inventory to mark the two
   Phase 4 findings resolved and record the checks below. No unrelated
   content, design, publication, sitemap or LLM-context changes were made.

### Validation and remaining checks

- All 58 PHP files passed PHP 8.5 WASM lint. All 33 full HTML pages rendered
  without PHP warnings/errors and with exactly one shared menu script.
- Chromium passed 132 combinations: all 33 pages at 375px and 768px, with
  JavaScript enabled and disabled. This includes Home, About, Services,
  Contact, blog listing, every article, Terms, Privacy, 404, `/all-pages`
  and all 17 place pages.
- Menu checks cover opening/closing by button, closing on each of the five
  menu links, Escape, focus return, aria-expanded/aria-hidden, inert state,
  body scroll restoration, and closing above the mobile breakpoint.
  Navigation links remain reachable without JavaScript through the footer
  or the 404 page's existing static links.
- All three draft tables stay within the page viewport at both widths,
  with JavaScript on/off. Oversized tables scroll internally at 375px.
  Table HTML contents match the pre-fix version exactly; robots remain
  noindex. The post registry, footer, sitemap, LLM files and README are
  unchanged. Existing LF/CRLF conventions are preserved.
- Native Apache, actual HTTP headers and production font/CDN loading still
  require staging. Browser tests supplied local images and blocked external
  resources. No deployment or owner fact verification was performed.

## Phase 4: breadcrumbs, internal links and publication switches, 2026-10-15

Five tasks, one commit per task. All three unverified articles and all 17
place records remain draft. No new local facts, office claims or business,
rating or review schema were introduced. Earlier instructions to remove
robots tags or manually add footer links are superseded by this workflow.

1. Added the seven-record `includes/posts.php` registry. Listing cards and
   Blog schema include only published records; article robots directives,
   publication/modification dates and related selections use the registry.
2. Added one-array visible/schema breadcrumbs on every HTML page, including
   Home and 404. Draft ancestors are skipped consistently. Extracted pure
   place-data functions so ancestor checks do not render a page.
3. Added centralized published-target link helpers, gated inline article
   and place-note links, end-of-article related/service/contact links,
   homepage latest guides, planning guides in nine country sections,
   contextual About/Contact team links, conditional footer columns and
   ready-only parent/nearby/guide navigation on place pages. General process
   articles link to the process section rather than an unrelated country.
4. Added `/all-pages`, grouped from the same published-page helpers and
   linked from shared and 404 footers. The directory is intentionally not
   added to the XML sitemap. It currently lists 12 distinct published URLs.
5. Updated README and verification/release instructions: owner approval,
   publish status, accurate sitemap lastmod and `llms.txt` in one commit.
   Relevant links appear automatically; no manual footer additions.

### Validation and remaining limits

- PHP 8.5 WASM: all 58 files linted; all 33 full HTML pages rendered without
  warnings/errors. Visible/schema breadcrumb parity, schema references,
  metadata dates, robots, related/latest guides, nine country sections,
  directory membership and internal route/anchor checks pass.
- Isolated fixture tests cover post publication and withdrawal, automatic
  links, dates, latest ordering, empty columns, the five-category place
  gate, omitted draft ancestors, place hierarchy/group order and inline
  encoded/direct-PHP/query draft-link suppression.
- Chromium: 132 page/width/JavaScript cases passed breadcrumb/layout/runtime
  checks with two explicitly recorded pre-existing draft-table overflow
  exceptions: cost 472px and scholarships 530px at a 375px viewport, equal
  to the Phase 3 baseline. Place/directory menus and native FAQs work in
  the exercised cases. The existing About hamburger needs separate repair.
- Apache rules, header source, place records/spreadsheet, the 11-URL sitemap,
  both LLM files and Google verification are unchanged. LF/CRLF conventions
  are preserved. No test packages, fixtures or screenshots were committed.
- Hosting rewrites, HTTP headers and production fonts require staging.
  External browser resources were blocked; local images were supplied.
  No owner facts were independently verified and no deployment was made.

### Atomic publication rule

For a reviewed post, update its registry status and accurate publication /
modification dates; for a reviewed place, populate at least five valid fact
categories and update status in PHP and CSV. In the same commit, add its
canonical URL to `sitemap.xml` with accurate lastmod and add its verified
summary to `llms.txt`. Keep `llms-full.txt` consistent if affected. Never
manually remove guards or add draft links. Footer, breadcrumbs, related
lists and `/all-pages` populate automatically. `/all-pages` remains outside
`sitemap.xml`. Unpublishing also removes sitemap/LLM recommendations in the
same commit. See README and verification section 16 for the release steps.

## Phase 3: scalable place pages, 2026-10-15

Five tasks, one commit per task. No draft is promoted or linked from the
live navigation, sitemap or LLM files. Earlier Phase 2 implementation notes
below are historical and are superseded where they describe static pages,
visible placeholders or the former footer/homepage links.

1. Added `includes/place-page.php`, loading one returning PHP data array.
   Sections are conditional; placeholder-bearing entries and incomplete
   FAQs are omitted. The seven fact categories count once each. Anything
   other than a published record with five valid categories gets noindex
   in both meta and the HTTP header. There is one separated shared process
   block; remaining content comes from the selected place's data.
2. Added/replaced 17 thin entry files, each only setting a slug and including
   the renderer. Existing Karnataka, Belagavi, Shivamogga and Udupi/Manipal
   URLs are retained, alongside Kodagu and the requested new place URLs.
   The existing Apache clean-URL rules are untouched.
3. Added 17 PHP arrays under `places/`. All are drafts. The four migrations
   retain their known content; all 23 unverified items become empty local
   facts or blank FAQ answers. The 13 new records have no filled fact
   categories. Towns relate to Kodagu, Karnataka and two other towns; the
   Kodagu record lists all seven towns. These are editorial related links,
   not sourced proximity or transport claims.
4. Added `places-facts-template.csv` with 17 rows and 26 columns: every data
   field plus its source column. Lists/FAQs use JSON cells; transfer into
   reviewed PHP arrays is manual. README explains source review, the 5/7
   gate, published status and same-commit sitemap/LLM/footer publication.
5. Updated README, this changelog and the verification inventory for the
   current model, unresolved fields, empty districts, link safeguards and
   owner release checks. Retained the previous pending verification list.

### Validation

- PHP 8.5 WASM lint passed for all 53 PHP files; all 32 full pages rendered
  without PHP warnings/errors. All 17 routes remain noindex.
- Exact FAQ/schema matching, omission of empty sections, no visible markers,
  data/CSV parity, local link/anchor resolution and town graph checks pass.
- Isolated fixtures confirm five valid categories plus published status
  are required, placeholders/partial FAQs do not count, and published pages
  do not link to unready place records through navigation or note links.
- All 68 Chromium cases (17 pages, mobile/desktop, JavaScript on/off) pass
  with native FAQs, working JavaScript menus and no horizontal overflow.
- Header, footer, homepage, Apache rules, sitemap, both LLM files and Google
  verification are unchanged. Existing line endings are preserved.
- Apache/hosting validation and production font loading still need staging.
  No local facts, fee model, bank products or travel routes were guessed or
  independently verified during this build.

## Phase 2 build: 2026-10-15

Five tasks, one commit per task. These are noindex drafts, not a content
publication or a change to the header navigation.

1. Added `study-abroad-consultants-in-karnataka.php`: 48-word opening
   answer, statewide counselling process, neutral selection questions,
   named-team/service-terms context, nine destination anchors, existing
   blog links, Karnataka document notes, eight FAQs and district links.
   The fee model and current appointment jurisdiction remain VERIFY items.
2. Added `study-abroad-counselling-belagavi.php`,
   `study-abroad-counselling-shivamogga.php` and
   `study-abroad-counselling-udupi-manipal.php`. Each has a distinct opening,
   selection checklist, destination discussion, six local planning topics
   and eight unique FAQ pairs. Unknown institution/student origins,
   transcripts, MOI, attestation, lenders and travel routes are placeholders,
   not guessed facts. Each states that ILMERA has no physical office there
   or elsewhere and uses phone, WhatsApp and video-call counselling from Coorg.
3. Added one hub link to the shared footer Navigation list and one to the
   homepage Coorg service-area section. The shared header is unchanged.
4. Added a 23-item page-grouped verification checklist, source-file
   provenance and a same-commit publication rule: resolve placeholders,
   remove noindex, add the sitemap entry with accurate lastmod and add the
   page to `llms.txt`. FAQs and their JSON-LD must be edited together.
5. Updated README and this changelog for the four drafts, current routes,
   release safeguards and validation results.

### Page conventions and validation

- Reused existing article CSS, the existing FAQ styles and district h3
  styling, current fonts/variables, logo assets and root-page PHP includes.
  New files are CRLF; existing files retain their original line endings.
- Each page has a noindex robots meta tag and a verification-file comment.
  The sitemap, both LLM context files and Apache rules are unchanged.
- Each page has WebPage, BreadcrumbList, FAQPage and Service schema, with
  AdministrativeArea Karnataka, India for `areaServed`. Required nested
  breadcrumb/FAQ objects and existing Person ID references only; no new
  business-location, review or rating schema and no implied team endorsement.
- PHP 8.5 WASM lint passed for all 22 PHP files; all 19 full pages rendered
  without warnings/errors. The 32 new FAQ pairs match visible text exactly.
  Leads are 48, 48, 49 and 51 words. All 23 placeholders have checklist items;
  local body/FAQ paragraphs are not copied between district drafts.
- Link/anchor checks, noindex checks, CSS reuse, newline preservation and
  unchanged header/sitemap/LLM checks passed. All 16 Chromium combinations
  of page, mobile/desktop width and JavaScript enabled/disabled passed,
  including native FAQs and JavaScript mobile-menu open/close.
- Chromium used locally rendered PHP and local images; external font
  requests were blocked. Native Apache routing, final CDN typography and
  hosting-specific behavior remain staging checks. No local fact-checking
  or fee-model confirmation is implied by these technical tests.

## Phase 1 follow-ups

- Removed the 3 `noindex` draft URLs from `sitemap.xml`, leaving 11 URLs.
  Each draft must be fact-checked and added back to the sitemap in the same
  commit that removes its `noindex` tag. README and the verification
  inventory now reflect that release rule.
- Removed the Terms reference to in-person meetings and renamed Contact
  "Office Hours" to "Counselling Hours", keeping the existing schedule.
  Updated both pages' sitemap `lastmod` values for these copy changes.
- Updated all 3 draft HTML comments to point to the verification inventory
  instead of the missing owner TODO file; their `noindex` tags are unchanged.
- The initial repair notes below describe the earlier 14-URL sitemap;
  this follow-up supersedes those counts and the draft-sitemap caveat.

## Initial Phase 1 repair: 2026-10-15

This section describes the current repository. Earlier entries below are
historical notes, not a statement that those earlier fixes were present in
the checkout. In particular, the actual checkout still had `blogs/`, root
`blog.php`, flat `assets/`, duplicate root includes and `download` before
this repair. The Phase 1 changes supersede older path, count, office-wording
and sitemap-date descriptions below.

1. **Counter repair:** `index.php` and `about.php` render the final values
   `9`, `3`, `4` and the founding year in `.stat-num` / `.big-num` HTML
   (the founding year was corrected to 2026 in Phase 6). Removed their
   count-up callbacks and helper. Kept hero `.ms`, HUD values and unrelated
   entrance animations unchanged.
2. **Blog directory:** used `git mv` to rename `blogs/` to `blog/`, removed
   root `blog.php`, merged `DirectoryIndex index.php index.html` into
   `.htaccess` without removing existing rules, and deleted `download`.
   Standardized the listing canonical, Open Graph URL, JSON-LD IDs/URLs,
   breadcrumbs, sitemap and internal links to `/blog/`. All 8 blog PHP files
   resolve their shared includes through `../includes/`.
3. **Assets:** moved all 9 files from `assets/` into `assets/images/` with
   `git mv`. Audited every PHP/text image reference, including `jabirkj.webp`
   and `zaheer.webp`: all 6 distinct referenced paths exist. README lists
   the complete referenced-path inventory and the 3 unreferenced assets.
4. **Office wording:** updated `llms.txt`, `llms-full.txt`, `about.php`
   (visible FAQ and JSON-LD), `index.php` (service area and FAQs) and the Coorg
   article. ILMERA is based in Coorg, Kodagu, has no physical office or branch,
   and counsels by phone, WhatsApp and video call. Removed visit comparisons,
   implied in-person meetings and the instruction preventing AI systems from
   describing ILMERA as remote. Removed README's Coorg Google Business Profile
   registration recommendation. Students' own visa appointments can remain.
5. **Sitemap:** now has 14 URLs, including all 7 article files and `/blog/`.
   Set each `lastmod`, including privacy-policy and terms, from the latest
   source-file Git commit at the time of repair. Sources changed in Phase 1
   have `2026-10-15`; untouched services, contact and legal files have
   `2026-10-14`. Fetched full history because the checkout was shallow.
6. **Cleanup:** grep and include-target checks found no runtime references
   to root `header.php`, root `footer.php` or `_import/`. Deleted those unused
   files and folder; kept `includes/header.php`, `includes/footer.php` and
   the unchanged `google10fa7a4178242a1f.html` verification file.
7. **Documentation:** updated README for actual paths, templates, images and
   the 7-post inventory. Added a full cost/document/scholarship/visa claim
   inventory for the 3 unpublished drafts to the verification file.

### Verification and scope notes

- Source checks confirm final stats, resolving include paths, existing
  image references, consistent listing URLs and well-formed sitemap XML.
  `php-parser` parsed all 18 PHP files; all 14 JSON-LD blocks parsed as JSON
  and all 6 inline JavaScript blocks passed syntax checks.
- Kept existing CRLF, LF and mixed line endings rather than normalizing
  unrelated lines. No design, hero/HUD, contact, services or legal copy
  changes are included.
- The 3 unpublished drafts retain `noindex, follow` and remain absent from
  the 4-card listing. Their sitemap URLs were added per the explicit request;
  that does not make their factual claims verified or publish the drafts.
- PHP/Apache runtime and live-deployment checks need staging validation.
- This Arena session is fixed to `arena/48320ee5-ilmerastudyabroad`, not the
  requested `seo-phase-1` branch. There is one commit for each task, and no
  push to `main`.

---

## Earlier rewrite history (superseded where noted above)

All changes below implement the project-wide brand and copy mandate:
- No em dashes anywhere in code or copy.
- ILMERA is based in **Coorg (Kodagu, Karnataka)**, has no physical office or
  branch, and consults by phone, WhatsApp and video call.
- No unverified superlatives or fabricated statistics (e.g. "India's trusted",
  "50+ students", "98% visa success rate", "2nd PU failures" / "PUC failures" /
  "back papers").
- Standardized leadership titles: **Jabir KJ = Founder, Fawaz BH = CMO, Zaheer KJ = CFO**
  (Jabir KJ was briefly standardized as "CEO" in an earlier pass; corrected back
  to "Founder", his actual title, per explicit instruction. Fawaz BH and Zaheer KJ
  keep "CMO" / "CFO", previously "Marketing Head" / "Operations Head").
- All blog article authors standardized to **Fawaz BH, CMO** (previously two
  articles were misattributed to Zaheer KJ and Jabir KJ).
- Fixed `/blog` returning a 404: the listing page was moved from `blog.php`
  (site root) to `blog/index.php`, and `.htaccess` now sets
  `DirectoryIndex index.php index.html`, because having both `blog.php` and
  a `blog/` directory at the same time caused the rewrite rule for `/blog`
  to be skipped (see `flagged-items-for-verification.md` item 12 for the
  full root-cause explanation).
- Standardized logo path: `assets/images/ilmera.logo.png`.
- Standardized Instagram handle: `ilmera.studyabroad`; other socials point to
  `ilmerastudyabroad` (not the legacy `ilmeragroup` handles).
- Standardized phone numbers: Primary `+91 90195 57427`, Secondary `+91 94810 84038`.
- Standardized schema `alternateName`: `"ILMERA Study Abroad by ILMERA Group"`.

---

## Site-wide / structural

### `.htaccess` (renamed from `htaccess`)
- File renamed so Apache actually applies its mod_rewrite rules.
- Rules confirmed: requests to `*.php` 301-redirect to the extension-less path,
  and extension-less requests are served from the matching `.php` file
  internally. **Conclusion applied everywhere below:** all canonical URLs,
  sitemap entries, internal links, and generated schema URLs use extension-less
  paths (`/about`, `/services`, `/contact`, `/privacy-policy`, `/terms`), never
  `.php` suffixes.

### `sitemap.xml`
- Updated `lastmod` on all 6 URLs to `2026-08-22`.
- Confirmed all `<loc>` values are already extension-less, per the `.htaccess`
  rewrite convention.

### `robots.txt`
- Reviewed only (no changes needed). Already allows major AI/LLM crawlers
  (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, Perplexity-User,
  Google-Extended, ClaudeBot, Claude-User, anthropic-ai, Bingbot, Applebot,
  Applebot-Extended, CCBot, Amazonbot, meta-externalagent) for AEO/GEO
  visibility, and correctly references `sitemap.xml`.

### `_import/tree.json`
- Deleted (scratch/import artifact, only file in `_import/`, not referenced
  by any live page).

---

## `header.php`
- Simplified decorative CSS comment `/* ─── NAV ── ... */` to `/* NAV */`.
- Removed em dash from `aria-label="ILMERA Study Abroad : Home"` →
  `aria-label="ILMERA Study Abroad: Home"`.
- Unified `.logo-light` and `.logo-dark` `<img>` `src` to the real asset
  `ilmera.logo.png` (previously `.logo-light` pointed at
  `ilmera.logo.navy.png`, a file that does not exist in the project : see
  `flagged-items-for-verification.md`).

## `footer.php`
- Simplified decorative CSS comment `/* ─── FOOTER ── ... */` to `/* FOOTER */`.
- Removed em dash from aria-label; rewrote tagline copy to remove fabricated
  claims and "remote" framing.
- Added both phone numbers (`tel:+919019557427`, `tel:+919481084038`).
- Added Privacy Policy / Terms of Use links; later corrected from
  `/privacy-policy.php` / `/terms.php` to extension-less `/privacy-policy` /
  `/terms`.

## `services.php`
- Full copy rewrite (prior session): removed em dashes, fabricated stats,
  "2nd PU" / "back papers" language, and "remote" framing; added Coorg-based
  consultation framing; standardized job titles to CEO/CMO/CFO.
- This session: corrected `geo.region` meta from generic `IN` to precise
  `IN-KA` to match `about.php`, `privacy-policy.php`, and `terms.php`.

## `contact.php`
- Full copy rewrite (prior session): removed em dashes and fabricated stats;
  confirmed both phone numbers, WhatsApp link, correct social handles, and
  standardized job titles present and correct.
- Re-verified this session (read-only): no outstanding issues found.

## `about.php`
- Read-only reference in prior sessions for page structure; assumed complete
  from an earlier session.
- This session: re-audited with a full pattern sweep (em dash, fabricated
  stats, legacy job titles, "remote" language, wrong social handles) : no
  issues found in copy.
- **Fixed a real bug found in this audit:** favicon, `og:image`,
  `og:image:secure_url`, and `twitter:image` all referenced the stale/likely
  non-existent `assets/images/ilmera.png` instead of the standardized
  `assets/images/ilmera.logo.png`. Corrected all 5 references.

## `index.php`
Discovered this session, via a site-wide pattern sweep, to still contain
numerous unfixed brand/copy violations despite being inherited as "presumed
complete." Fixed extensively:

- `<title>`, `og:title`, `twitter:title`: removed em dashes.
- JSON-LD `WebSite.description`, `WebPage.name`: removed em dashes.
- JSON-LD `FAQPage` (6 entries) and the matching visible `<details class="il-faq">`
  blocks: removed "2nd PUC" / "PU fail" / "back papers" language and em dashes;
  updated leadership mention to "CEO Jabir KJ, CMO Fawaz BH and CFO Zaheer KJ";
  added Coorg/Kodagu/Karnataka framing; removed "handled remotely" language.
- JSON-LD `Organization` block:
  - `alternateName` → `"ILMERA Study Abroad by ILMERA Group"`.
  - `logo.url` / `image` → corrected to `ilmera.logo.png`.
  - `description` → removed "trusted" framing, added Coorg/Kodagu/Karnataka basis.
  - `telephone` → hyphenated format `+91-9019557427` to match other pages.
  - `address` → `addressLocality: "Coorg"`, `addressRegion: "Kodagu, Karnataka"`
    (was generic `"India"`).
  - Added a `contactPoint` array (primary + secondary phone).
  - `availableChannel.serviceType` → `"Phone, WhatsApp and video call counselling"`.
  - `sameAs` → corrected from `ilmeragroup` handles to
    `ilmerastudyabroad` / `ilmera.studyabroad` / `ilmerastudyabroad`.
  - `founder.jobTitle`, `employee[].jobTitle` → `"Founder"` → `"CEO"`,
    `"Marketing Head"` → `"CMO"`, `"Operations Head"` → `"CFO"`.
- Hero stats block: replaced fabricated `50+ Students Placed / 30+ Partner
  Universities / 9 Destinations / 98% Visa Success Rate` with neutral,
  verifiable stats: `9 Study Destinations / 3 Named Counsellors / 4 Languages
  Spoken / Founded year (corrected to 2026 in Phase 6)`.
- "Special Categories" backlog card: removed "2nd PU" / "PU Fail" language,
  reframed as "Academic Backlogs? / Backlogs Accepted."
- "Study for Free" card list items: removed 3 remaining em dashes
  (Germany / Italy / Slovakia entries).
- Testimonials section: removed 3 em dashes from destination labels
  ("United Kingdom: Admissions & Visa", "Italy: DSU Scholarship Guidance",
  "Russia: Backlogs & No-IELTS Routes").
- Coorg/Kodagu service-area paragraph: removed "no travel to a city office
  required" / "entirely remotely" language; reframed as Coorg-based with
  phone/WhatsApp/video-call consultation.
- **TEAM section:** replaced legacy job titles in all three visible
  `itemprop="jobTitle"` divs (Founder → CEO, Marketing Head → CMO,
  Operations Head → CFO) and in the corresponding `alt` attributes of the
  three team photos; removed one remaining em dash in Jabir KJ's bio
  paragraph.
- **CTA section:** fixed a functional bug : `mailto:info@ilmeragroup.in`
  (wrong domain in the href) was displaying `info@ilmerastudyabroad.com` as
  the visible text; corrected the href to match. Removed one more em dash
  from the destinations line.
- **Favicon / OG / Twitter image bug:** favicon and social preview images
  referenced the stale `assets/images/ilmera.png`; corrected all 5
  references to `assets/images/ilmera.logo.png`.
- **Local SEO/GEO fix:** `geo.region` / `geo.placename` meta tags were
  generic (`IN` / `India`); corrected to `IN-KA` / `Coorg, Karnataka, India`
  to match the rest of the site.
- Final verification: full-file `Grep` sweep for em dash and all fabricated-
  stat / legacy-title / wrong-handle patterns returned zero matches, followed
  by a manual `Read` of every edited region to confirm persistence (Grep
  alone proved unreliable earlier in the session and cannot be trusted without
  this follow-up).

## `llms.txt`
- Full rewrite. Removed fabricated stats ("India's leading", "98% visa
  success rate", "50+ students", "30+ partner universities"), "2nd PU"
  language, and the wrong Instagram handle (`ilmera_global`).
- Added: Leadership section (CEO/CMO/CFO), Core Services, Destinations (9
  countries, softened claims), Company Facts (both phone numbers, correct
  Instagram handle `ilmera.studyabroad`), Student Profiles, FAQ (LLM
  Reference), About ILMERA Group.
- Legal page links corrected to extension-less `/privacy-policy` and `/terms`.

## `llms-full.txt` (new file)
- Created as a comprehensive AI-crawler context document: Company Overview,
  Leadership Structure, Core Service Breakdown, Country-by-Country
  Requirements and Eligibility for all 9 destinations, Student Eligibility
  Categories, an explicit "What ILMERA Does Not Claim" section instructing AI
  systems not to invent statistics or superlatives, and a Contact Summary.
  The earlier instruction about how to describe counselling channels has
  been removed in Phase 1.
- Legal page links corrected to extension-less `/privacy-policy` and `/terms`.

## `privacy-policy.php` (new file)
- New standalone page matching site's visual language and PHP include
  pattern. 11 sections covering data collection, use, sharing, security,
  retention, choices, cookies/analytics, third-party links, policy changes,
  and contact (both phone numbers + email).
- JSON-LD `WebPage` schema with `BreadcrumbList`.
- Canonical / `og:url` / JSON-LD `@id` / breadcrumb URL corrected from
  `/privacy-policy.php` to extension-less `/privacy-policy`.

## `terms.php` (new file)
- New standalone page, same structural pattern. 12 sections including a
  clear no-guarantee disclaimer: ILMERA does not guarantee admission to any
  specific university, any specific scholarship, or visa approval.
- JSON-LD `WebPage` schema with `BreadcrumbList`.
- Canonical / `og:url` / JSON-LD `@id` / breadcrumb URL corrected from
  `/terms.php` to extension-less `/terms`.

---

## Follow-up round: theme toggle removal, image path standardization, about.php team cards, sitemap.php

### `header.php`
- Removed the light/dark theme toggle button, its sun/moon icon spans, the
  associated `.theme-toggle`/`.theme-icon-*` CSS, and the `localStorage`-based
  theme-switch JavaScript, per the site owner's request. The site now has a
  single fixed visual theme. (Rewritten wholesale via `Write` after repeated
  narrow-edit failures on this file, consistent with the documented
  Edit-tool matching issue.)

### Site-wide image path standardization
Standardized every reference to the four brand image assets to these exact
paths:
- `assets/images/ilmera.logo.png` (logo)
- `assets/images/jabirkj.png` (Jabir KJ)
- `assets/images/zaheer.png` (Zaheer KJ, lowercase "z")
- `assets/images/fawazbh.webp` (Fawaz BH)

Fixed inconsistent casing/filenames found in `about.php` and `index.php`'s
JSON-LD blocks, which had used `jabir.png` and `Zaheer.png` (capital Z)
instead of the standardized filenames.

### `about.php` : TEAM section
- Removed a duplicated "Jabir KJ" name that appeared twice in his team card
  (once as a `<div class="team-name">`, once as an `<h3 class="team-name">`).
- Reordered Jabir's card to match the structure of the other two cards:
  avatar, name heading, role, bio.
- Fixed Jabir's `alt` text from the minimal `"Jabir KJ"` to the fuller,
  consistent pattern used on the other two cards: `"Jabir KJ, CEO of ILMERA
  Study Abroad"`.
- Rebalanced all three team bios to a comparable length (~55-60 words each;
  Jabir's was previously roughly double the length of the other two),
  removing filler clauses while keeping each person's core facts (Jabir:
  financial consultant, Rome Tor Vergata, cost planning, DSU scholarships,
  proof-of-funds; Fawaz: SEO/AEO/GEO consultant, Kushal Nagar, certifications,
  content strategy; Zaheer: document verification, APS submissions,
  application filing, visa scheduling).

### `sitemap.php` (new file)
- Created per the site owner's request. Rather than duplicating the URL
  list in two independently maintained files (risking drift and a
  duplicate-content signal), it issues a 301 redirect to the canonical
  `/sitemap.xml`, which remains the single source of truth referenced in
  `robots.txt`.

## Notes on verification method
`PlaywrightScreenshot` / `PlaywrightConsoleCapture` cannot render `.php`
files, so all verification for this project relied on `Read` (structural
check) plus `Grep` (pattern search). `Grep` proved unreliable at several
points in this project (reporting "no matches" for strings later confirmed
present via `Read`), so every Grep-confirmed-clean claim in this changelog
was followed by a manual `Read` of the same region before being treated as
final.

---

## New Blog feature

### `header.php`
- Added a "Blog" link to both the desktop `.nav-links` and mobile `.mob-links`
  navigation lists, pointing to `/blog`, with the same active-state pattern
  as the other links (matches when the current path starts with `blog`, so
  it also highlights on individual `/blog/{slug}` article pages).
- Added a 5th `transition-delay` rule for the mobile menu's staggered link
  animation, matching the new 5-item list.

### `footer.php`
- Added a "Blog" link to the footer's Navigation list, between Services and
  Contact, for consistency with the header.

### `blog.php` (new, later moved to `blog/index.php` : see fix note below)
- New blog listing page, matching the site's visual language (same CSS
  variables, fonts, and card styling as other pages).
- Full SEO meta set: title, description, keywords, robots, `geo.region`
  (`IN-KA`) / `geo.placename` (`Coorg, Karnataka, India`), canonical URL,
  Open Graph, Twitter Card, favicons using `ilmera.logo.png`.
- JSON-LD `@graph` with a `WebPage` + `BreadcrumbList` entity and a `Blog`
  entity whose `blogPost` array lists all 4 articles with `headline`, `url`,
  `datePublished`, and `author` references reusing the existing `Person`
  `@id`s already defined in `about.php` (`#jabir`, `#fawaz`, `#zaheer`),
  rather than redefining author data.
- 4 article preview cards (Germany/APS, Italy/DSU, backlogs/No-IELTS,
  Coorg-based process), each linking to its own detail page under `/blog/`.

### `blog/study-in-germany-free-aps-certificate.php` (new)
### `blog/italy-dsu-scholarship-eligibility.php` (new)
### `blog/study-abroad-with-academic-backlogs.php` (new)
### `blog/study-abroad-counselling-from-coorg.php` (new)
- Four full article detail pages, one per preview card on `/blog`, so the
  "Read Article" links resolve instead of 404ing. Each page:
  - Uses the site's existing `.htaccess` clean-URL rewrite rule (which maps
    any extension-less request to a matching `.php` file, including nested
    paths like `blog/{slug}`), so no `.htaccess` changes were needed.
  - Has its own title, meta description/keywords, canonical URL, Open Graph/
    Twitter tags, and `BlogPosting` + `BreadcrumbList` JSON-LD.
  - Ends with an author card crediting the correct team member (Zaheer KJ,
    Jabir KJ, or Fawaz BH) with their standardized title and correct image
    path, and a "Book a Free Consultation" CTA linking to `/contact`.
  - Content is factual and process-descriptive (how APS works, how DSU
    eligibility is assessed, what backlog-friendly options look like, how
    Coorg-based remote counselling works) with no fabricated statistics or
    testimonials, consistent with the rest of the site's copy mandate.

### `sitemap.xml`
- Added 5 new `<url>` entries: `/blog` (priority 0.8, weekly) and the 4
  article URLs (priority 0.6, yearly), all with `lastmod` `2026-08-27`.

### `blog_posts` (Table API : created, currently unused)
- A schema (`id`, `title`, `slug`, `excerpt`, `content`, `category`,
  `author_name`, `author_role`, `published_date`, `read_minutes`) and 4 rows
  were created via the Table API while exploring a dynamic approach, before
  settling on fully static PHP pages (consistent with the rest of the site
  and safer for JS-less AI/answer-engine crawlers). This table is not read by
  any page. See `flagged-items-for-verification.md` item 10.

## Phase 13: status-driven links and sitemap, 2026-10-15

Seven task checkpoints on the existing session branch; one commit per task.
Tasks 1 and 6 are read-only audits recorded in PR 1 with empty audit commits.
No destination or location status, indexing setting, intro_answer,
ilmera_summary, summary_provenance, destination fact or LLM file changed.
Existing blockers and historical documentation remain intact.

- Audited every page file and supporting PHP file: 42 rendered routes,
  29 draft editorial pages, no indexable editorial orphans. The original
  sitemap had 11 URLs and omitted the linked, indexable /all-pages route.
- Centralized eligible destination and indexable location collections in
  includes/links.php, retaining all existing publication readiness gates.
  Collections include slug, name, root-relative URL and entry file. Explicit
  noindex metadata/headers exclude entries; known conditional draft-only
  article headers follow the same existing publication status guard.
- Services, Home and Footer now use those collections. Empty collections
  produce no discovery sections or draft buttons. About and Contact have
  contextual Services links; Contact also lists eligible locations.
  Destination/place templates retain Services/Contact links and provide
  eligible same-set links. Link blocks deduplicate their own targets.
- Added includes/sitemap-data.php as the sitemap builder using the same
  collections and existing static/article registries. All 12 current
  indexable pages are included; drafts, noindex pages and utilities are not.
  Existing canonical path spellings are retained, with one canonical host.
- /sitemap.xml is generated by sitemap.php through an Apache rewrite.
  /sitemap and /sitemap.php redirect to that XML endpoint. The existing
  robots.txt declaration already points there and is unchanged.
  tools/build-sitemap.php regenerates the portable snapshot. Lastmod uses
  actual entry/data/template file timestamps and omits unknown/future values.
- Added tools/check_discovery.py for real HTTP status, self-canonical,
  noindex, XML coverage, incoming-link, internal-target and fragment checks.
  Its tests caught and fixed a conditional-header false exclusion of
  published articles; the XML snapshot was regenerated after that fix.
- Separate, uncommitted fixture copies verified destination publish/revert
  and location indexable/noindex/revert in Home, Services, Footer and XML,
  Contact location links and contextual back-links. Synthetic location
  groups were routing-test inputs only. Production data was never toggled.
- Location quality was reviewed without content edits: 13 empty-data,
  shared-body duplicates and four individually written but locally
  evidence-thin records. The complete 17-page report and exact repeated
  lines are appended to flagged-items-for-verification.md and PR 1.

Validation at seven task checkpoints: 78 PHP lints for each of tasks 1-3,
80 for each of tasks 4-7, 42 renders and 252 Chromium cases per task.
Checkpoint totals: 554 lints, 294 renders and 1,764 browser cases. Browser
coverage is all routes at 375/768/1280px with JavaScript on/off. Protected
raw records, metadata/schema parity, draft isolation, source links,
headings, menus, FAQs, conditional Costs, line endings and wording guards
passed. Existing robots meta and X-Robots-Tag settings were compared with
the Phase 12 baseline and are unchanged. The existing article canonical
whose filename needs report-only percent encoding is retained verbatim;
this is not a new URL or new editorial wording.

HTTP checks passed using PHP 8.5 WASM behind a local HTTP adapter: all 12
sitemap targets returned 200, self-canonical and no noindex; every indexable
route had a non-self inbound link and no broken internal target/fragment
was found. In-page source references on drafts are not discovery links.
The adapter is not Apache: native Apache routing, production host/header
behavior and deployment still require staging checks. No production deploy,
source verification, publication approval or main-branch push occurred.

Before any destination publication, the owner must confirm official sources,
resolve the existing blockers and authorize release. Passing the existing
five-sourced-category gate alone is not approval. See the appended Phase 13
verification notes and unchanged atomic release checklist in the flagged file.

Additional isolated publication coverage passed 48 Chromium cases: eight
pages with two eligible destinations and two eligible locations, at three
widths with JavaScript on/off, including deduplicated discovery/footer blocks.
All temporary data was restored outside the production repository.

## Phase 16: release-blocker fixes and final check, 2026-10-16

Six task commits on arena/48320ee5-ilmerastudyabroad; PR 1 remains open.
No merge, deployment, main push or publication-status change.

1. Removed only the two held APS/DSU article link lines from llms.txt.
   llms-full.txt is baseline-identical. All other LLM bytes remain restricted.
2. Neutralized named university references in published About/Services copy
   and schema; removed the named affiliation block. Added the maintained
   blocked-name list and strict discovery guard with six regression cases.
3. Reopened all 25 original distinct official citations, including two legacy
   tuition-footer sources; the final inventory has 23 distinct direct URLs.
   Replaced the soft-missing Latvia path, made opened redirects direct and
   corrected the unsupported Qatar no-steps clause. Active source rows and
   affected article hashes match. Latvia still has five categories.
4. Preserved the exact 8,000-euro owner sentence at all 19 published
   occurrences; added local owner/written-award cautions with FAQ parity.
   Removed nearby verified-DSU implications and the Contact metadata Italy
   no-charge-education phrase. Removed open FAQ height caps and added
   no-JavaScript answer visibility on Services/Contact. Added a maintained
   exact-claim checker and four regression cases.
5. Created reports/phase-16-release-check.md, phase-16-checks.json and the
   citation-open inventory. Reports include every task-2/task-4 changed line
   range, every Phase 16 changed file and all 37 final sitemap URLs.
6. Appended this changelog and verification/maintenance decisions, retained
   all historical blocker text and repeated the complete fresh checks.

Every task: 83 PHP parses, 42 fresh renders and 252 Chromium cases, plus
fresh discovery/source/place/contact checks. Final authored location overlap
is 3.311%; fresh full rendered-main maximum is 14.147287%, all 136 pairs.
Local sitemap/status/canonical/schema/FAQ/internal-link checks pass. The
strict final discovery/publication commands correctly FAIL on restricted
llms.txt names; both public LLM files also retain prohibited wording.
External raw-HTTP-200 evidence and native Apache/deployment behavior remain
unverified. The final decision is NOT READY for staging acceptance or
production sign-off. Owner amount/partner and withheld-page blockers remain;
no machine or source-open pass is a substitute for those approvals.
