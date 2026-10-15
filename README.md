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
  All 7 article URLs are included in the sitemap as explicitly requested;
  review the draft sitemap entries before publication if they remain held.
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
  `robots.txt`. Its 14 entries cover 6 main/legal pages, the blog listing
  and 7 articles. `lastmod` dates are taken from the latest Git commit
  affecting each source file at the sitemap repair commit, not the article
  bylines or filesystem timestamps.

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
- Source validation passed with `php-parser` for all 18 PHP files, JSON
  parsing for all 14 JSON-LD blocks and JavaScript syntax checks for all
  6 inline script blocks. Include, image, stats, URL, sitemap/date and
  newline-preservation checks also passed.
- PHP and Apache are not installed in the repair workspace. Source-level
  checks cannot replace a staging check under the actual hosting stack.
- After deployment, verify `/blog` redirects to `/blog/`, `/blog/` renders
  the listing, all 7 article routes resolve, shared templates and images
  load, sitemap XML parses, and both sets of stats show final values with
  JavaScript disabled and enabled.

Production domain: `https://ilmerastudyabroad.com/`. Deployment is managed
outside this repository. See `CHANGELOG.md` for repair details. No ranking
position or visa/scholarship outcome is guaranteed by these repairs.
