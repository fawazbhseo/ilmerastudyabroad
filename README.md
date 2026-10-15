# ILMERA Study Abroad: Site Source

Plain PHP marketing site served by Apache for ILMERA Study Abroad, based in
Coorg, Kodagu, Karnataka. ILMERA has no physical office or branch anywhere.
The founders are from Coorg, Kodagu, and counselling is by phone, WhatsApp
and video call.

## Structure and routes

There is no build step, CMS or database dependency in this repository.
Page content is maintained directly in PHP, text and XML files. Place-page
content lives in returning PHP arrays under `places/`; its spreadsheet is
`places-facts-template.csv`.

| URL | Source file |
|---|---|
| `/` | `index.php` |
| `/services` | `services.php` |
| `/about` | `about.php` |
| `/contact` | `contact.php` |
| `/privacy-policy` | `privacy-policy.php` |
| `/terms` | `terms.php` |
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
- Shared templates are `includes/header.php` and `includes/footer.php`.
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

To publish a filled row, complete these steps in one commit:

1. Review the sources and fill at least five of the seven fact categories:
   `intro_answer`, `local_institutions`, `transcript_and_moi_steps`,
   `local_loan_options`, `visa_appointment_route`, `local_notes`, `faqs`.
   A non-empty intro must have 40 to 60 words. Only complete FAQs count.
   Each category counts once; metadata, related links and shared copy do not.
2. Set `status` to `published` in the PHP record and spreadsheet. The template
   still forces noindex if fewer than five valid categories are filled.
3. Add the clean page URL to `sitemap.xml` with an accurate Git-based `lastmod`.
4. Add the verified page to `llms.txt`.
5. Add the footer link only when its target is ready. Do not restore a homepage
   link to an unready hub. Published pages suppress links to unready place data.

All current records are drafts. This phase adds no live navigation, sitemap
or LLM-context links. Noindex is not access control: draft URLs can be opened
directly and may link to other drafts for editorial review.

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
  and video call. Every other content section comes from the place array.
- WebPage, BreadcrumbList and Service are emitted; FAQPage is emitted only
  for complete FAQ pairs. Service areaServed is AdministrativeArea Karnataka,
  India. Nested breadcrumb/FAQ types only; no new business, rating or review
  schema. No author endorsement is inferred from the shared template.
- Published/ready pages suppress related, breadcrumb and inline links to
  place records that fail the same publication gate. Draft pages can link
  to other drafts for editorial review. Noindex is not access control.
- No live page or shared navigation links to these drafts. The header,
  footer, homepage, 11-URL sitemap and both LLM context files are unchanged.

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
section 15 describes the current Phase 3 workflow.

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
- The initial repair checks covered 18 PHP files. Phase 3 now covers
  53 PHP files, including the 17 data records; see validation above.
- Native PHP and Apache are not installed in the workspace. The isolated
  PHP-WASM and Chromium checks do not replace hosting-stack validation.
- After deployment, verify `/blog` redirects to `/blog/`, `/blog/` renders
  the listing, all 7 article routes resolve, shared templates and images
  load, sitemap XML parses, and both sets of stats show final values with
  JavaScript disabled and enabled.

Production domain: `https://ilmerastudyabroad.com/`. Deployment is managed
outside this repository. See `CHANGELOG.md` for repair details. No ranking
position or visa/scholarship outcome is guaranteed by these repairs.
