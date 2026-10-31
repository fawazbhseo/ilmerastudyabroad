# ILMERA Study Abroad: Site Source

Plain PHP marketing site served by Apache for ILMERA Study Abroad, based in
Coorg, Kodagu, Karnataka. ILMERA was founded in 2026 and has no physical
office or branch anywhere.
The founders are from Coorg, Kodagu, and counselling is by phone, WhatsApp
and video call.

## Structure and routes

There is no build step, CMS or database dependency in this repository.
Page content is maintained directly in PHP, text and XML files. Place-page
content lives in returning PHP arrays under `places/`; its spreadsheet is
`places-facts-template.csv`. Blog metadata and publication status live in
`includes/posts.php`; shared link eligibility lives in `includes/links.php`.
Destination content lives in `destinations/`, rendered by
`includes/destination-page.php`, with `destinations-facts-template.csv`
for source review.

| URL | Source file |
|---|---|
| `/` | `index.php` |
| `/services` | `services.php` |
| `/about` | `about.php` |
| `/contact` | `contact.php` |
| `/privacy-policy` | `privacy-policy.php` |
| `/terms` | `terms.php` |
| `/all-pages` | `all-pages.php` |
| `/study-in-germany` | `study-in-germany.php` |
| `/study-in-italy` | `study-in-italy.php` |
| `/study-in-uk` | `study-in-uk.php` |
| `/study-in-czech-republic` | `study-in-czech-republic.php` |
| `/study-in-lithuania` | `study-in-lithuania.php` |
| `/study-in-latvia` | `study-in-latvia.php` |
| `/study-in-slovakia` | `study-in-slovakia.php` |
| `/study-in-russia` | `study-in-russia.php` |
| `/study-in-gcc` | `study-in-gcc.php` |
| `/study-abroad-consultants-in-karnataka` | `study-abroad-consultants-in-karnataka.php` |
| `/study-abroad-consultants-in-kodagu` | `study-abroad-consultants-in-kodagu.php` |
| `/study-abroad-counselling-madikeri` | `study-abroad-counselling-madikeri.php` |
| `/study-abroad-counselling-virajpet` | `study-abroad-counselling-virajpet.php` |
| `/study-abroad-counselling-kushalnagar` | `study-abroad-counselling-kushalnagar.php` |
| `/study-abroad-counselling-gonikoppal` | `study-abroad-counselling-gonikoppal.php` |
| `/study-abroad-counselling-somwarpet` | `study-abroad-counselling-somwarpet.php` |
| `/study-abroad-counselling-ponnampet` | `study-abroad-counselling-ponnampet.php` |
| `/study-abroad-counselling-siddapura` | `study-abroad-counselling-siddapura.php` |
| `/study-abroad-counselling-mysuru` | `study-abroad-counselling-mysuru.php` |
| `/study-abroad-counselling-mangaluru` | `study-abroad-counselling-mangaluru.php` |
| `/study-abroad-counselling-hassan` | `study-abroad-counselling-hassan.php` |
| `/study-abroad-counselling-chikkamagaluru` | `study-abroad-counselling-chikkamagaluru.php` |
| `/study-abroad-counselling-bengaluru` | `study-abroad-counselling-bengaluru.php` |
| `/study-abroad-counselling-belagavi` | `study-abroad-counselling-belagavi.php` |
| `/study-abroad-counselling-shivamogga` | `study-abroad-counselling-shivamogga.php` |
| `/study-abroad-counselling-udupi-manipal` | `study-abroad-counselling-udupi-manipal.php` |
| `/blog/` | `blog/index.php` |
| `/blog/study-in-germany-free-aps-certificate` | `blog/study-in-germany-free-aps-certificate.php` |
| `/blog/italy-dsu-scholarship-eligibility` | `blog/italy-dsu-scholarship-eligibility.php` |
| `/blog/study-abroad-with-academic-backlogs` | `blog/study-abroad-with-academic-backlogs.php` |
| `/blog/study-abroad-counselling-from-coorg` | `blog/study-abroad-counselling-from-coorg.php` |
| `/blog/cost-of-studying-abroad-for-indian-students` | `blog/cost-of-studying-abroad-for-indian-students.php` |
| `/blog/documents-needed-to-study-abroad-from-india` | `blog/documents-needed-to-study-abroad-from-india.php` |
| `/blog/scholarships-for-indian-students-study-abroad` | `blog/scholarships-for-indian-students-study-abroad.php` |
| `/sitemap.xml` | `sitemap.xml` |
| `/robots.txt` | `robots.txt` |
| `/llms.txt` | `llms.txt` |
| `/llms-full.txt` | `llms-full.txt` |

- There are **7 article files** in `blog/`, plus the listing `blog/index.php`.
  The listing currently shows the original 4 articles. The cost, documents
  and scholarships drafts are not live yet per the owner and retain
  `noindex, follow`. This repair does not publish them or add listing cards.
  Only the 4 indexable article URLs are in the sitemap. Add each draft back
  in the same commit that fact-checks it, changes registry status to
  published and adds its verified `llms.txt` summary. Robots follow the
  registry; do not remove their conditional guards.
- `.htaccess` requires Apache `mod_rewrite` and permission to apply these
  directory overrides. It preserves the existing PHP-to-extensionless
  redirect and internal rewrite rules and sets
  `DirectoryIndex index.php index.html`.
- Apache redirects `/blog` to `/blog/` on the live server. The listing's
  canonical, Open Graph, JSON-LD, breadcrumbs, sitemap and internal links
  use `/blog/`. Article URLs remain extensionless, without a trailing slash.
- Shared layout templates are `includes/header.php` and `includes/footer.php`.
  Existing root pages use `__DIR__ . '/includes/...'`; blog pages use
  `__DIR__ . '/../includes/...'`. Thin place entry files include
  `includes/place-page.php`, which loads the shared header and footer
  relative to its own `__DIR__`. Destination entries use the same thin-file
  pattern with `includes/destination-page.php`.
- All 9 image files are in `assets/images/`. There are no files directly
  inside `assets/` and no `blogs/` directory or root `blog.php`.
- Unused root `header.php`, `footer.php`, `download` and `_import/` were
  removed. `google10fa7a4178242a1f.html` remains unchanged.
- `sitemap.php` redirects to `sitemap.xml`, the sitemap referenced by
  `robots.txt`. Its 11 entries cover 6 main/legal pages, the blog listing
  and 4 indexable articles. `lastmod` dates are taken from the latest Git commit
  affecting each source file at the sitemap repair commit, not the article
  bylines or filesystem timestamps.

## Place fact spreadsheet and publication

`places-facts-template.csv` has one row for each of the 17 place records.
Every data field has a matching `_source` column. Lists and FAQs use JSON
arrays inside CSV cells; empty lists are `[]` and unknown scalar facts are
empty cells. Keep the headers and slug stable when saving from a spreadsheet.
The source columns document provenance and owner review; they are not public
page content. Existing-content sources point to the pre-migration Git revision.

Fill a row with confirmed facts and current sources, then transfer its values
into the returning PHP array in `places/{slug}.php`. Decode list/FAQ cells to
PHP arrays, not JSON strings. This is a manual review workflow, not an automatic
CSV import. Keep unknown values empty; never put verification placeholders in
public data. FAQ entries have `question` and `answer` keys.

To publish a filled row, follow the one-commit release workflow below. Set
status to published only after owner review and at least five valid fact
categories. The renderer still forces noindex below that threshold.
Footer, breadcrumbs, related links and the directory update automatically;
do not add manual footer or homepage links to bypass the gate.

All current records remain drafts. Noindex is not access control: draft
URLs can be opened directly, but draft targets are not linked by the shared
helpers, including from other drafts.

## Phase 3: data-driven place pages

There are 17 place records and 17 clean-URL entry files. Each entry contains
only `$place = 'slug';` and the shared renderer include. The existing Apache
rules are unchanged. The two hubs use `/study-abroad-consultants-in-{slug}`;
other places use `/study-abroad-counselling-{slug}`.

`includes/place-page.php` loads `places/{slug}.php`, which returns an array.
The required keys are `slug`, `name`, `type`, `district` and `status`.
`type` is `district-hub`, `town` or `city`; these are editorial page types,
not claims about statutory municipal classification. `status` is `draft`
or `published`. The `district` key can be an empty string while unknown;
only the owner-provided Kodagu grouping has been populated. Unknown
metadata must not be guessed.

### Optional content fields

| Field | PHP value | Rendering rule |
|---|---|---|
| `intro_answer` | String | Optional 40-60 word opening; invalid lengths are omitted |
| `local_institutions` | List of strings | Local institutions section only when populated |
| `transcript_and_moi_steps` | List of strings | Transcript/MOI section only when populated |
| `local_loan_options` | List of strings | Loan section only when populated |
| `visa_appointment_route` | String | Appointment route section only when populated |
| `local_notes` | List of strings | Place-owned planning notes only when populated |
| `faqs` | List of question/answer arrays | Incomplete pairs omitted; visible text generates FAQPage |
| `nearby` | List of other record slugs | Related guide links, subject to publication checks |

Use plain text, not raw HTML. List text and visa-route text may contain
internal links in `[label](/path#anchor)` form; external link syntax is not
converted. FAQ questions/answers and intros remain plain text. Placeholder
markers, empty items and incomplete FAQs are filtered before rendering or
counting. Invalid/missing required records return a noindex 404. Slugs are
validated before a file is loaded.
For an additional place, add a matching PHP record, CSV row and thin root
entry file using the same URL pattern; a data record alone is not a route.

The seven fact categories are the content rows above except `nearby`. Each
valid non-empty category counts once, regardless of its item count. Metadata,
links and the shared counselling block never count. The renderer allows
indexing only for `status = published` **and at least five valid fact
categories**. Otherwise it forces both robots meta and X-Robots-Tag noindex.
There is no manual robots-tag removal in a thin entry file.

### Current content and links

- All 17 records remain `draft`. The four migrated records retain their
  existing intros, confirmed FAQs and planning guidance. The 23 former
  verification items are unresolved empty facts or unanswered FAQ entries,
  not visible marker text. Each migrated record has only three filled fact
  categories. There are 10 complete FAQs across the four migrated records.
- The 13 new records have empty fact fields. This includes Kodagu, seven
  Kodagu town guides and five city guides. No local institutions, loan
  products, transcript procedures or visa travel routes were invented.
- Each of the seven town records relates to Kodagu, Karnataka and two other
  town records. Kodagu lists its seven town guides plus Karnataka. `nearby`
  is an editorial related-guide list, not verified distance or travel advice.
- One clearly separated shared block explains the standard ILMERA process:
  based in Coorg, Kodagu, no physical office, counselling by phone, WhatsApp
  and video call. Local fact sections come only from the place array.
  Navigation and related guide lists use the shared publication registries.
- WebPage, BreadcrumbList and Service are emitted; FAQPage is emitted only
  for complete FAQ pairs. Service areaServed is AdministrativeArea Karnataka,
  India. Nested breadcrumb/FAQ types only; no new business, rating or review
  schema. No author endorsement is inferred from the shared template.
- Related, breadcrumb and inline links suppress unpublished or unready
  targets on all pages, including drafts. Noindex is not access control.
- No live page or shared navigation links to these drafts. Phase 4 changes
  the shared footer and homepage but keeps the 11-URL sitemap, existing
  header, place facts, spreadsheet and both LLM context files unchanged.

### Phase 3 validation

All 53 PHP files passed PHP 8.5 WASM lint; all 32 full pages rendered without
warnings/errors. Checks cover thin entry syntax, valid routes and anchors,
empty-section omission, placeholder suppression, FAQ/schema parity, CSV/PHP
parity, the town link graph and unchanged live-site files. Isolated test
fixtures cover the 4/5-category boundary, draft status, whitespace, encoded
markers, incomplete FAQs, count inflation, unsafe slugs and ready-to-draft
link suppression. All 68 Chromium combinations of 17 pages, two widths and
JavaScript enabled/disabled passed without overflow or JavaScript errors.

Tests used rendered PHP and local images, with external font requests
blocked. Native Apache rewrites, production fonts and hosting-specific
behavior still need staging checks. No testing packages or generated
fixtures, rendered HTML or screenshots were added to Git. New data and
renderer files use LF; root entries preserve CRLF; existing docs retain LF.

### Earlier Phase 2 drafts

Phase 2 originally created four standalone drafts with 23 visible VERIFY
items and matching FAQs. Its footer/homepage links were removed before
Phase 3. That static implementation is now superseded by the data records,
empty unresolved fields and dynamic publication gate above. Section 14 of
`flagged-items-for-verification.md` preserves the pending owner checklist;
sections 15 and 16 describe readiness and the current release workflow.

## Phase 4: publication-aware navigation

### Blog metadata

`includes/posts.php` contains all seven records with `slug`, `title`,
`excerpt`, `category`, `readMinutes`, `datePublished`, `dateModified`,
`status` and `related` (post slugs). Four existing guides are published.
The cost, documents and scholarships posts remain draft pending the owner
checks in section 13 of `flagged-items-for-verification.md`.

The registry controls listing cards and Blog schema membership, article
robots directives, JSON-LD dates, related-guide selection, latest guides,
footer guides and the directory. Draft articles also send an X-Robots-Tag
header. Do not remove a robots tag or edit a card to publish a post. The
article route must exist as well as having published status. Related guides
prefer the configured slugs, then fill from other published records, without
self-links or duplicates. The homepage selects up to three published guides
by publication date, newest first, with slug as the deterministic tie-break.

### Shared breadcrumbs and links

- `includes/place-data.php` contains the pure place loader, normalization,
  escaping and five-of-seven readiness check, extracted from the renderer.
- `includes/links.php` provides publication-gated page, post and place
  anchors, static-page groups, place groups and relevant guide selection.
  Existing inline article links and place-note Markdown use the same gate,
  including direct PHP, query-string and encoded draft-path aliases.
- `includes/breadcrumbs.php` emits the visible breadcrumb and one
  BreadcrumbList from one trail array on every full HTML page, including
  Home and 404. Unpublished ancestors are skipped in both outputs; the
  current page is plain text. Ready town trails use Home / Karnataka /
  Kodagu / Town; ready city trails use Home / Karnataka / City. Unknown
  districts are not invented. Head schema references the same breadcrumb id.
- Every article ends with up to three other published guides, a relevant
  services-section link and contact. The Coorg process article links to
  `/services#process`, not an arbitrarily chosen country. General planning
  guides in country sections are labelled as planning guides, not falsely
  described as country-specific articles. Draft guides become eligible
  automatically once published; no country guide content was invented.
- About and Contact link contextually to services, the blog and
  `/about#team`. Place pages link to ready parent hubs and ready entries in
  their existing editorial `nearby` array, plus relevant published guides.
  These related entries are not verified physical-nearest-place claims.
- Footer Guides and Locations columns exist only when they have published
  items. Locations are grouped in order: Karnataka, districts, towns/cities.
  No current place qualifies, so no Locations column is emitted.
- `/all-pages` lists published pages by type using these same helpers.
  It currently lists 12 distinct content/directory URLs: the existing 11
  sitemap URLs plus itself. It is footer-linked, but deliberately **not
  included in `sitemap.xml`**. Empty location groups are omitted.

### Release a post or place in one commit

1. Verify the article's claims or the place's sources with the owner. Keep
   unresolved content draft. For a place, transfer reviewed CSV fields and
   sources into `places/{slug}.php`, with at least five valid categories,
   a matching thin entry file and complete visible/schema FAQs.
2. Set the post's status in `includes/posts.php`, or the place's status in
   its PHP record and CSV row, to `published`. For posts, set accurate
   `datePublished` (actual first publication) and `dateModified` (actual
   substantive review/change) dates. Draft scaffold dates are not evidence
   of publication or verification. The guards generate index/noindex;
   never manually remove their conditional logic.
3. In that **same commit**, add the clean canonical URL to `sitemap.xml`
   with accurate `lastmod` reflecting the actual substantive change/release.
   Use the relevant content/data Git history and reviewed change date, not
   filesystem mtimes or a blanket date replacement. Keep dates consistent
   with article metadata. Do not add `/all-pages` to the XML sitemap.
4. In that **same commit**, add the verified page and a factual summary to
   `llms.txt`. Keep `llms-full.txt` consistent if its content is affected;
   neither LLM file should recommend unpublished pages.
5. Render the page and affected lists. Check robots meta and HTTP headers,
   canonical URL, visible/schema breadcrumb and FAQ parity, related/latest
   guides, services, footer and `/all-pages`. Links populate automatically;
   no manual footer, related-list or directory edits are needed. Verify
   Apache routing and browser behavior on staging before deployment.

Publish status, sitemap entry with accurate lastmod and `llms.txt` together,
not as separate release commits. Helpers do not write XML or text files for
you. If unpublishing, change status and remove sitemap/LLM recommendations
in one commit; dynamic lists and inline links stop linking the target.
New posts need both a registry record and an article file. New places need
a reviewed data record, spreadsheet row and thin entry file. New static
content pages must be registered in `ilmera_static_pages()` as appropriate.

### Phase 4 validation and limits

- All 58 PHP files passed PHP 8.5 WASM lint. All 33 full HTML pages rendered
  without PHP warnings/errors. Every page has one BreadcrumbList matching
  the visible trail and referenced id. Article metadata dates and robots,
  related/latest guides, all nine services sections, canonical paths and
  local anchors were checked. All three draft posts and 17 places remain
  excluded from public links, listing cards, sitemap and LLM context.
- Isolated synthetic fixtures passed post publication/unpublication,
  metadata date changes, latest ordering, empty-list/column suppression,
  place five-category boundaries, draft/underfilled ancestors, parent and
  nearby links, Karnataka/district/town-city group order and encoded/PHP
  draft-link aliases. No fixture facts or status changes enter this repo.
- Chromium covered all 33 pages at 375px and 1280px with JavaScript on/off
  (132 cases), checking breadcrumbs, layout and runtime errors. Place and
  new-directory menu behavior and native FAQ toggles were exercised.
- Phase 4 recorded mobile draft-table overflow and missing About menu
  wiring. Phase 5 resolved both with scrollable table containers and a
  single shared header menu script. See verification section 17.
- Native Apache, actual HTTP response headers, production fonts and hosting
  behavior still require staging checks. Browser tests blocked external
  resources and supplied local images. No official fact verification,
  deployment or outcome guarantee is implied. QA tools/artifacts remain
  outside Git. Existing byte-level newline conventions are retained.

## Phase 6: sourced destination pages and founding year

The owner confirms ILMERA was founded in **2026**. About JSON-LD, its hero
stat, stat-item text/data-target and HUD array, the homepage hero stat and
this README use that year. A repository-wide text audit covered the LLM
files, posts, places and historical docs. No other company founding year or
longer-history claim was found. Historical changelog stat references were
corrected too. Existing student academic/work history and personal-experience
references are not company-age claims; no older company history is implied.

### Destination data and source model

There are nine returning PHP arrays under `destinations/`, nine thin clean-URL
entry files, `includes/destination-data.php` for pure normalization/readiness,
and `includes/destination-page.php` for rendering with the existing design,
header, footer and menu. Apache rewrite rules are unchanged.

Each record contains `slug`, `name`, `status`, `intro_answer`, `who_its_for`,
`english_requirements`, `costs`, `scholarships`, `visa_steps`, `intakes`,
`documents`, `work_and_stay`, `faqs`, plus the review metadata below. All nine
start draft with empty fact groups, empty review dates and no approved source
hosts. Phase 7 adds owner-supplied sourced content to the Czech draft only;
see verification section 20 before publication. No facts were guessed.

- Each ordinary group is a list of arrays with `text`, `source_url`,
  `source_label` and `checked_on`. FAQ items use `question` and `answer`
  instead of `text`, plus the same source fields. Plain strings are not
  accepted as sourced items. Raw HTML is not public content.
- `intro_answer` is an optional 40-60 word string. It needs the sibling fields
  `intro_answer_source_url`, `intro_answer_source_label` and
  `intro_answer_checked_on`. Invalid-length or unsourced intros are omitted,
  including from page descriptions.
- `official_source_hosts` is an owner-reviewed list of exact official-source
  hostnames. Initially `[]`. Before adding a host, verify that the actual
  university, scholarship body or government authority owns it and that the
  linked page supports the exact statement. Host membership is an explicit
  editorial approval, not automatic proof of official ownership.
- Every fact item, even qualitative fact items, needs a nonempty source label
  and a valid HTTPS URL on a listed host or any dot-delimited subdomain of
  that host to render or count, including www. Missing, unapproved, malformed,
  credential-bearing or explicit-port URLs are rejected. Review parent-domain
  scope before approval. Placeholder-bearing text, blank items and incomplete
  FAQ pairs render nowhere and do not count.
- `checked_on` stores the actual review date for the item; `facts_last_checked`
  stores the owner's actual page-wide review date. Use valid ISO calendar
  dates and keep them consistent with the review evidence. Empty/invalid dates
  are not printed or replaced with invented dates. These metadata fields do
  not add fact categories. Fill them before release, even though the gate
  itself is based on published status and five sourced categories.
- `ilmera_summary` contains only cautious, nonnumeric qualitative/service
  wording migrated from existing Services/LLM text. `summary_provenance`
  records the source Git revision and section. This is not an official fact
  source. Never add an unsourced figure, date, fee or concrete rule here to
  bypass the source gate. Summary copy does not count toward readiness.

A destination is indexable only when status is `published` **and at least
five of the ten fact categories** contain a valid sourced item. The ten are
intro, the eight ordinary groups above and FAQs. Each group counts once;
multiple items in a group, summaries, metadata and shared counselling copy
cannot inflate the count. Otherwise robots meta and X-Robots-Tag force
noindex, follow, and shared links exclude the page. Noindex is not access
control: drafts remain directly accessible.

The renderer emits WebPage, Service, the shared Home / Services / Study in X
BreadcrumbList, and FAQPage only for valid visible FAQ pairs. FAQ citations
sit outside the answer text so schema answers exactly match visible answers.
Each rendered fact has a citation to the deduplicated Sources list with
labelled official links and optional recorded item review dates. The Facts
last checked field appears only when a valid page-wide date and sourced
facts exist. Empty sections, empty Sources/FAQ lists and placeholder review
dates are omitted rather than printed.

### Destination links

The existing link helpers enforce the same destination gate and require an
actual entry file. Homepage buttons and their ItemList schema URLs, plus
Services country headings, point to full guides only when eligible; otherwise
they retain `/services#country` targets. Existing contact CTAs are unchanged.

The footer adds a conditional Country guides column and `/all-pages` a
conditional group containing only eligible destinations. Existing footer
Services country anchors remain available. Published articles upgrade their
matching end-of-post country links; the country-neutral Coorg article keeps
its process link. Published/ready places link countries already mentioned in
their own data and upgrade their matching Services Markdown links. No country
association is invented for a place with no matching country text. Draft
source posts/places do not get these automatic in-content upgrades. Direct
PHP, encoded, trailing-slash and query aliases cannot bypass the target gate.

All nine destinations are currently excluded from public links, sitemap and
LLM context files. The three blog drafts and all 17 place drafts retain their
existing status. `/all-pages` remains outside `sitemap.xml`.

### Spreadsheet and atomic destination release

`destinations-facts-template.csv` has nine rows and 47 columns: metadata plus
one value column and `source_url`, `source_label`, `checked_on` columns for
each of the ten groups. Intro and its source/date cells are scalar strings.
Other groups use JSON arrays; source/date columns are parallel JSON arrays
aligned by item index. FAQs use JSON question/answer objects, with the same
parallel source arrays. Empty lists are `[]`; unknown scalar cells are empty.
Hosts use a JSON array. The summary/provenance cells mirror the PHP records.

1. Obtain owner-approved facts and official sources. Fill each reviewed CSV
   value and its aligned source URL, label and real checked-on date. Approve
   exact official hostnames only after checking ownership and relevance.
   Do not invent numeric claims or populate unknown fields with markers.
2. Manually transfer the reviewed data to `destinations/{slug}.php`, building
   sourced item arrays from the parallel CSV cells. This is not an automatic
   CSV import. Add valid intro/source fields if used, complete FAQs and an
   accurate page-wide `facts_last_checked` date. Verify the thin entry exists.
3. After owner sign-off and at least five valid sourced categories, set status
   to `published` in both the PHP record and CSV. Never remove conditional
   robots code or force links to a draft/underfilled page.
4. In that **same commit**, add the clean destination URL to `sitemap.xml`
   with accurate lastmod reflecting the actual substantive content/review
   change, supported by Git history and the release evidence, not filesystem
   timestamps or a blanket date replacement.
5. In that **same commit**, add the verified destination and factual summary
   to `llms.txt`. Keep `llms-full.txt` consistent if affected. Do not recommend
   a draft in either file. The helpers do not edit these files for you.
6. Validate robots meta and actual HTTP headers, sources, dates, category
   count, visible/schema FAQ and breadcrumb parity, Services/homepage schema
   targets, footer/directory and matching article/place links on staging.
   Link placements update automatically; no manual footer edits are needed.

Sourced facts, published status, accurate sitemap entry and `llms.txt` belong
to **one release commit**. For withdrawal, change status and remove sitemap /
LLM recommendations together; links disappear or revert to Services anchors.
No destination is published by this build.

### Phase 6 validation and limits

- All 78 PHP files passed PHP 8.5 WASM lint. All 42 HTML pages rendered cleanly,
  with one shared menu and breadcrumb per page. Nine empty destination drafts,
  CSV/PHP parity, founding year and no incoming draft links were verified.
- Isolated synthetic fixtures covered draft/published and four/five-category
  boundaries; missing/invalid/unapproved sources; placeholders; category
  inflation; intro word bounds; complete/partial FAQs and exact visible/schema
  parity; all nine automatic link targets and homepage schema; matching
  published posts/places; withdrawals and encoded/direct-PHP draft aliases.
  No synthetic facts, dates, hosts or statuses enter Git.
- Chromium passed 282 combinations: 42 current pages plus five isolated
  published-fixture pages, 375/768/1280px, JavaScript on/off. Checks include
  breadcrumb parity, no runtime errors, destination layout, menus, native
  FAQs, source targets, dates, no-JS navigation and the corrected founding
  stats/HUD. Existing menu/table fixes remain in place.
- No official facts or URLs were provided for publication and none were
  independently verified. Owner source review remains essential; an approved
  host list cannot establish the truth of a claim by itself. Actual HTTP
  headers, native Apache rewrites, production fonts/CDNs and deployment still
  need staging. External resources were blocked in browser QA; local images
  were supplied. No QA fixtures, tools or screenshots were committed.

## Phase 1 repairs

The homepage and About stats render `9`, `3`, `4` and `2026` directly in
HTML. Their count-up code is removed. Hero `.ms` and HUD values and all
unrelated design and animation remain unchanged.

The About physical-office FAQ and its JSON-LD answer plainly say there is
no walk-in office. The homepage service-area content and FAQs, Coorg blog
article and both LLM context files describe phone, WhatsApp and video-call
counselling without implying visits or branches. The LLM context no longer
instructs AI systems not to describe ILMERA as remote.

### Referenced image audit

Every `assets/images/...` path referenced in PHP or text files exists:

- `assets/images/fawazbh.webp`
- `assets/images/ilmera.logo.png`
- `assets/images/jabirkj.png`
- `assets/images/jabirkj.webp`
- `assets/images/zaheer.png`
- `assets/images/zaheer.webp`

The other moved assets are `ilmera.logo.navy.png`, `ilmera.png` and
`ilmera.white.png`. No missing referenced image files were found.

## Editing and verification

- Preserve each file's existing line endings. The checkout contains CRLF,
  LF and one mixed-ending PHP file; avoid whole-file newline conversions.
- Write complete files when rewriting. Keep repairs scoped and avoid
  design changes, em dashes, invented facts, statistics, reviews or awards.
- Confirm destination costs, scholarships, document requirements and visa
  rules with current official sources before publication. The draft-post
  inventory is in `flagged-items-for-verification.md`.
- The initial repair checks covered 18 PHP files. Phase 3 covered 53;
  Phase 4 covered 58; Phase 6 covers 78 PHP files, including all data and
  shared helpers.
- Native PHP and Apache are not installed in the workspace. The isolated
  PHP-WASM and Chromium checks do not replace hosting-stack validation.
- After deployment, verify `/blog` redirects to `/blog/`, `/blog/` renders
  the listing, all 7 article routes resolve, shared templates and images
  load, sitemap XML parses, and both sets of stats show final values with
  JavaScript disabled and enabled.

Production domain: `https://ilmerastudyabroad.com/`. Deployment is managed
outside this repository. See `CHANGELOG.md` for repair details. No ranking
position or visa/scholarship outcome is guaranteed by these repairs.
