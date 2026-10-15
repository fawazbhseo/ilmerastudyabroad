# ILMERA Study Abroad: Site Source

Plain PHP marketing site served by Apache for ILMERA Study Abroad, based in
Coorg, Kodagu, Karnataka. ILMERA has no physical office or branch anywhere.
The founders are from Coorg, Kodagu, and counselling is by phone, WhatsApp
and video call.

## Structure and routes

There is no build step, CMS or database dependency in this repository.
Page content is maintained directly in PHP, text and XML files.

| URL | Source file |
|---|---|
| `/` | `index.php` |
| `/services` | `services.php` |
| `/about` | `about.php` |
| `/contact` | `contact.php` |
| `/privacy-policy` | `privacy-policy.php` |
| `/terms` | `terms.php` |
| `/study-abroad-consultants-in-karnataka` | `study-abroad-consultants-in-karnataka.php` |
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
  Root pages include them using `__DIR__ . '/includes/...'`; blog pages
  use `__DIR__ . '/../includes/...'`.
- All 9 image files are in `assets/images/`. There are no files directly
  inside `assets/` and no `blogs/` directory or root `blog.php`.
- Unused root `header.php`, `footer.php`, `download` and `_import/` were
  removed. `google10fa7a4178242a1f.html` remains unchanged.
- `sitemap.php` redirects to `sitemap.xml`, the sitemap referenced by
  `robots.txt`. Its 11 entries cover 6 main/legal pages, the blog listing
  and 4 indexable articles. `lastmod` dates are taken from the latest Git commit
  affecting each source file at the sitemap repair commit, not the article
  bylines or filesystem timestamps.

## Phase 2: Karnataka hub and district drafts

Four new root-level PHP pages use the existing article layout, CSS
variables, fonts, FAQ styling and `__DIR__` shared-include pattern:

- The Karnataka hub opens with a 48-word answer, followed by call-based
  counselling, a neutral consultant-selection checklist, all nine service
  destination anchors, Karnataka document notes, eight FAQs and district links.
- Belagavi focuses on issuing-institution checks, transcript requests and
  matching funding evidence to the application.
- Shivamogga separates document availability, updated records and funding
  timelines from the appointment journey.
- Udupi and Manipal distinguish qualification issuers, document delivery
  formats and loan/scholarship evidence.

The district guides have different substantive paragraphs and questions.
They do not invent local colleges, client origins, document procedures,
lenders or travel connections. Those facts and the owner's fee model
remain explicit `[VERIFY: ...]` placeholders. All **23 distinct items** are
checklisted by page in `flagged-items-for-verification.md`, section 14.

Each page has `noindex, follow` with a comment pointing to that inventory.
The four pages are **not** in `sitemap.xml`, `llms.txt` or `llms-full.txt`;
the sitemap still contains 11 URLs. The footer Navigation list and the
homepage Coorg service-area section link to the hub, but the main header
navigation is unchanged. The district pages and hub link to each other.
Noindex does not prevent direct access to a deployed page.

Each page defines WebPage, BreadcrumbList, FAQPage and Service JSON-LD.
Service `areaServed` is Karnataka, India. Only the required nested
ListItem, Question, Answer and AdministrativeArea objects are added;
team mentions reference the existing `#jabir`, `#zaheer` and `#fawaz` IDs.
There is no new review/rating, business-location or author-endorsement claim.
All eight FAQ question/answer pairs per page match the visible text exactly.

**Publication:** fact-check and resolve the page's placeholders, remove its
noindex tag, add its URL to `sitemap.xml` with an accurate Git-based lastmod,
and add it to `llms.txt` in the same commit. Edit the visible FAQ and its
JSON-LD together when replacing a placeholder. Do not publish a draft just
because it is already linked internally.

### Phase 2 validation

- All 22 PHP files passed PHP 8.5 WebAssembly lint; all 19 full pages
  rendered without PHP warnings or errors, including shared templates.
- All new-page links and service anchors resolve to files/IDs in the repo.
  Schema/visible FAQ parity, noindex, lead length, placeholder/checklist
  coverage, existing CSS reuse and newline preservation passed checks.
- The four new pages passed 16 real Chromium cases at 375px and 1280px,
  with JavaScript enabled and disabled. Native FAQ toggles worked in both
  modes; mobile menu open/close worked with JavaScript. No horizontal
  overflow or JavaScript page errors were detected.
- Browser checks used rendered PHP output and local image responses, with
  external font requests blocked. Hosting-stack redirects, real CDN font
  loading and final visual review still need staging checks under Apache.
- New pages use CRLF; modified existing files retain their original line
  endings. No test packages, generated HTML or screenshots were added to Git.

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
- The initial repair checks covered 18 PHP files, 14 JSON-LD blocks and
  6 inline scripts. Phase 2 adds 4 PHP pages, 4 JSON-LD blocks and 4 inline
  menu scripts; see the Phase 2 validation above.
- Native PHP and Apache are not installed in the workspace. The isolated
  PHP-WASM and Chromium checks do not replace hosting-stack validation.
- After deployment, verify `/blog` redirects to `/blog/`, `/blog/` renders
  the listing, all 7 article routes resolve, shared templates and images
  load, sitemap XML parses, and both sets of stats show final values with
  JavaScript disabled and enabled.

Production domain: `https://ilmerastudyabroad.com/`. Deployment is managed
outside this repository. See `CHANGELOG.md` for repair details. No ranking
position or visa/scholarship outcome is guaranteed by these repairs.
