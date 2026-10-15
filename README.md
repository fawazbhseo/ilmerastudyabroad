# ILMERA Study Abroad: Site Source

Plain PHP marketing site served by Apache for ILMERA Study Abroad, based in
Coorg, Kodagu, Karnataka. ILMERA has no physical office or branch anywhere.
The founders are from Coorg, Kodagu, and counselling is by phone, WhatsApp
and video call.

## Structure and routes

There is no build step, CMS or database dependency in this repository.
Page content is maintained directly in PHP, text and XML files. Place-page
content lives in returning PHP arrays under `places/`; its spreadsheet is
`places-facts-template.csv`. Blog metadata and publication status live in
`includes/posts.php`; shared link eligibility lives in `includes/links.php`.

| URL | Source file |
|---|---|
| `/` | `index.php` |
| `/services` | `services.php` |
| `/about` | `about.php` |
| `/contact` | `contact.php` |
| `/privacy-policy` | `privacy-policy.php` |
| `/terms` | `terms.php` |
| `/all-pages` | `all-pages.php` |
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
  in the same commit that fact-checks it and removes its `noindex` tag.
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
  relative to its own `__DIR__`.
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
- Two pre-existing draft tables still exceed the mobile viewport: cost
  (472px) and scholarships (530px), at 375px. Their widths match the Phase 3
  baseline. Existing About mobile-menu wiring also needs a separate repair;
  it predates this phase. See the verification inventory for follow-up.
- Native Apache, actual HTTP response headers, production fonts and hosting
  behavior still require staging checks. Browser tests blocked external
  resources and supplied local images. No official fact verification,
  deployment or outcome guarantee is implied. QA tools/artifacts remain
  outside Git. Existing byte-level newline conventions are retained.

## Phase 1 repairs

The homepage and About stats render `9`, `3`, `4` and `2023` directly in
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
  Phase 4 covers 58 PHP files, including the data and shared helpers.
- Native PHP and Apache are not installed in the workspace. The isolated
  PHP-WASM and Chromium checks do not replace hosting-stack validation.
- After deployment, verify `/blog` redirects to `/blog/`, `/blog/` renders
  the listing, all 7 article routes resolve, shared templates and images
  load, sitemap XML parses, and both sets of stats show final values with
  JavaScript disabled and enabled.

Production domain: `https://ilmerastudyabroad.com/`. Deployment is managed
outside this repository. See `CHANGELOG.md` for repair details. No ranking
position or visa/scholarship outcome is guaranteed by these repairs.
