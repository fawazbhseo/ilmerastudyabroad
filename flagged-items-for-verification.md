# Flagged Items for Manual Verification

These are assumptions or gaps introduced during the SEO/AEO/GEO rewrite that
the site owner should confirm before or shortly after publishing. None of
them block the site from working correctly, but they affect accuracy or
brand polish.

## 1. Logo asset path (RESOLVED)
- All pages now consistently reference `assets/images/ilmera.logo.png` for
  the header logo, favicon, and `og:image`/`twitter:image` social preview
  tags. **Action needed:** confirm this exact file exists on the live server
  and renders correctly both as a small favicon (square crop) and as a large
  1200x630 social preview image; a dedicated square favicon and a dedicated
  social-preview image are usually sharper than reusing one logo file for
  both purposes.
- The header no longer references a separate "light theme" logo variant,
  because the light/dark theme toggle itself has been removed from the site
  (see item 4 below) — there is now only one visual theme, so only one logo
  file is needed.

## 2. Team photo filenames (RESOLVED)
- Standardized across the whole site to exactly:
  - `assets/images/ilmera.logo.png` (logo)
  - `assets/images/jabirkj.png` (Jabir KJ, Founder)
  - `assets/images/zaheer.png` (Zaheer KJ, CFO — lowercase "z")
  - `assets/images/fawazbh.webp` (Fawaz BH, CMO)
- **Action needed:** confirm these four files exist at these exact paths
  (case-sensitive) on the live server. `zaheer.png` was previously
  referenced inconsistently as `Zaheer.png` (capital Z) in some places —
  if the live server's filesystem is case-sensitive (most Linux hosts are),
  only one of those casings will actually work.

## 3. About page team cards (RESOLVED)
- Removed a duplicated "Jabir KJ" name that previously appeared twice in
  his team card.
- Unified all three team cards (Jabir/Fawaz/Zaheer) to the same structure:
  avatar image, name heading, role, then a bio paragraph of comparable
  length (roughly 55-60 words each, down from Jabir's ~115 words vs. ~65
  for the other two).
- Unified the `alt` attribute pattern on all three avatar images to
  "[Name], [Role] of/at ILMERA Study Abroad".

## 4. Light/dark theme toggle removed
- The `theme-toggle` button, its sun/moon icons, and the associated
  `localStorage`-based theme-switch script were removed from `header.php`
  at the site owner's request. The `html[data-theme="light"]` CSS rules
  elsewhere in `header.php`, `about.php`, and `contact.php` were left in
  place (they simply never trigger now, since nothing sets
  `data-theme="light"` anymore) rather than being stripped out, to avoid
  making a large, form of unrequested changes across multiple files.
  **Action needed:** if a future editor wants to fully remove all traces of
  the old light-theme feature (not just the button that triggered it), the
  `html[data-theme="light"]` CSS blocks in those three files can be deleted
  as a follow-up cleanup; leaving them in has no visible effect on the
  current site.

## 5. sitemap.php added alongside sitemap.xml
- `sitemap.php` was created per the site owner's request. Rather than
  duplicating the URL list in two independently maintained places (a
  risk for drift and a potential duplicate-content signal), `sitemap.php`
  301-redirects to the canonical `/sitemap.xml`, which remains the single
  source of truth and the one referenced in `robots.txt`.
- **Action needed:** none, unless the site owner specifically wants
  `sitemap.php` to generate its own independent XML instead of redirecting
  — in that case, say so and the redirect can be replaced with a PHP-
  generated sitemap (a version of this was drafted and is easy to restore).

## 6. Destination/eligibility facts to confirm against current official sources
The following figures were kept or written based on prior site content and
general knowledge, not independently verified this session. They should be
checked against current official/government sources before relying on them
for compliance-sensitive claims:
- UK Graduate Route: "up to 2 years of post-study work after completing a
  degree" (correct as a general rule at time of writing, but visa rules
  change; verify current validity).
- Italy DSU scholarship: described as regional, income-based (ISEE) and
  merit-based, potentially covering tuition, stipend, and subsidised housing
  and meals. Amounts and eligibility thresholds vary by region and by year
  and are intentionally not quoted as fixed numbers, but should be confirmed
  each admissions cycle.
- Germany: "public universities charge little to no tuition" and the APS
  certificate being "mandatory for Indian applicants since 2022" — confirm
  current APS requirement status and any tuition changes in the state(s)
  ILMERA actually places students in.
- Czech Republic / Lithuania / Latvia / Slovakia: described qualitatively as
  "low-cost" / "some tuition-free programmes" without specific fee figures.
  If specific fee ranges are added later, they must be sourced and dated.
- GCC (UAE, Saudi Arabia, Qatar, Kuwait, Bahrain, Oman): described as hosting
  "international branch campuses of UK, US and Australian universities" —
  true in general but should be confirmed for whichever specific campuses
  ILMERA actually works with.

## 7. Social handles and contact details
- Instagram handle standardized to `ilmera.studyabroad`; Facebook/LinkedIn
  standardized to `ilmerastudyabroad`. **Action needed:** confirm these
  handles are live, correctly spelled, and actually owned/managed by ILMERA
  before the site goes live, since a broken or wrong social link is a poor
  trust signal (E-E-A-T) for both human visitors and AI answer engines.
- WhatsApp number `+421 944485186` (a non-Indian country code) is used
  site-wide for the WhatsApp channel. This was already present in the
  inherited content and was not changed. **Action needed:** confirm this is
  intentional (e.g., a WhatsApp Business number) and correct if it should be
  an Indian number instead.

## 8. Minor cosmetic whitespace in about.php
- Two blank lines remain inside Jabir KJ's team card in the HTML source
  (between the avatar `<img>` and the `<h3>` name), left over from removing
  the duplicate name div. They collapse to nothing when rendered in a
  browser and have no visible or functional effect; flagged only for
  source-code tidiness if a future editor wants to remove them.

## 9. On the "#1 ranking" goal
No legitimate SEO/AEO/GEO work (on-page structure, schema, content quality,
crawler access, technical hygiene) can guarantee a #1 ranking on Google,
Bing, or any AI answer engine, because rankings are also driven by
competitor content, backlink profiles, domain authority/age, and ongoing
algorithm changes that are outside any single site's control. This project
strengthened every on-page and structured-data lever within a static site's
control (accurate schema, consistent NAP/contact data, clean URLs, crawler
access for AI bots, no fabricated claims that could trigger trust penalties).
Further ranking improvement beyond this point typically requires off-page
work (backlinks, reviews, citations) and ongoing content additions, which are
outside the scope of a one-time static-site rewrite.

## 10. New Blog feature added (RESOLVED)
- `/blog` was added as a new listing page (originally `blog.php` at the site
  root; **moved to `blog/index.php` to fix a 404**, see item 12 below), linked
  from the main
  navigation (`header.php`, both desktop and mobile menus) and from the
  footer's Navigation list (`footer.php`). It is also included in
  `sitemap.xml`.
- Four initial articles were written as **individual static PHP pages** under
  `/blog/{slug}` (e.g. `/blog/study-in-germany-free-aps-certificate`), each
  with its own SEO meta tags, Open Graph/Twitter tags, and `BlogPosting` +
  `BreadcrumbList` JSON-LD. This matches the rest of the site's fully static,
  server-rendered approach (important for AI/answer-engine crawlers that do
  not execute JavaScript) and avoids the 404s that would have resulted from
  linking to detail pages that did not exist.
- A `blog_posts` table was also created via the Table API (schema + 4 rows)
  early in this work, before the static-page approach was finalized. **This
  table is currently unused** — no page reads from it. It can be deleted if
  the site owner does not plan to move the blog to a dynamic/database-backed
  model later, or kept as a head start if they do. Flagging so it is not
  mistaken for live content.
- **UPDATE:** all four articles are now attributed to a single author, **Fawaz
  BH, CMO**, per the site owner's explicit request (previously Zaheer KJ was
  credited on the Germany/APS article and Jabir KJ on the Italy/DSU article).
  **Action needed:** let us know if the site owner wants additional articles,
  a "read more" pagination system, or category filtering as the blog grows.

## 11. Jabir KJ's title corrected from "CEO" to "Founder" (RESOLVED)
- Jabir KJ is the Founder of ILMERA Study Abroad, not the CEO. Every "CEO"
  reference to him has been changed to "Founder" across `about.php`
  (meta tags, JSON-LD `Person.jobTitle` and `description`, FAQ answers,
  visible hero/story/Kodagu-section prose, and the visible team card),
  `index.php` (JSON-LD `founder`/`employee` Person objects, FAQ JSON-LD and
  its visible `<details>` duplicate, and the visible team card), `contact.php`
  (`ai-content-summary` meta tag), `llms.txt`, and `llms-full.txt`. The
  `Organization.founder` relationship (`{"@id": ".../#jabir"}`) itself was
  left unchanged, since that relationship was already correct.
- `llms-full.txt`'s leadership section previously stated that "Founder" was
  an informal, non-authoritative variant of Jabir KJ's title; that sentence
  was rewritten since Founder is now his standardized, authoritative title.
- **Action needed:** none — this is complete. Confirm no other internal
  documents or external listings (e.g. Google Business Profile, LinkedIn
  company page) still list Jabir KJ as "CEO".

## 12. Blog pages returning 404 (RESOLVED)
- **Root cause:** the site had both a `blog.php` file at the site root AND a
  `blog/` directory (holding the 4 article pages) at the same time. The
  `.htaccess` rewrite rule that maps `/blog` to `blog.php` only fires when
  `%{REQUEST_FILENAME}` is **not** an existing directory
  (`RewriteCond %{REQUEST_FILENAME} !-d`). Because `blog/` is a real
  directory on disk, that condition failed for every request to `/blog`, so
  Apache tried to serve the `blog/` directory itself instead of `blog.php`
  and found no index file there, resulting in a 404 (individual article
  pages like `/blog/study-in-germany-free-aps-certificate` were unaffected,
  since those exact paths are not directories).
- **Fix applied:** moved the listing page from `blog.php` to `blog/index.php`
  and added `DirectoryIndex index.php index.html` to `.htaccess`. Now a
  request for `/blog` resolves directly to the directory's own `index.php`
  through Apache's normal directory-index behavior, with no naming conflict.
  No links needed to change, since `header.php`, `footer.php`, `sitemap.xml`,
  and the JSON-LD `Blog`/`BreadcrumbList` entities all already pointed to the
  extension-less `/blog` path, not to `blog.php` directly.
- **Action needed:** after deploying, verify `/blog` and all 4
  `/blog/{slug}` article URLs load correctly (not just that they no longer
  404, but that they render the full page, since a clean console/absence of
  a 404 does not by itself confirm correct rendering).
