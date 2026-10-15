# ILMERA Study Abroad — Site Source & SEO/AEO/GEO Rewrite

Static-hosted PHP marketing site for **ILMERA Study Abroad**, a study-abroad
consultancy based in Coorg (Kodagu, Karnataka) that guides Indian students
to universities in Germany, Italy, the UK, Czech Republic, Lithuania, Latvia,
Slovakia, Russia, and the GCC.

This repo has gone through a full-site SEO (Search Engine Optimization), AEO
(Answer Engine Optimization), and GEO (Generative Engine Optimization) audit
and rewrite. See `CHANGELOG.md` for the complete list of edits and
`flagged-items-for-verification.md` for open items the site owner should
confirm.

## 1. Currently completed features

- **Clean, consistent brand copy** across every page: no em dashes, no
  fabricated statistics or unverifiable superlatives, no "remote-first" /
  "100% online" framing. ILMERA is consistently framed as based in Coorg
  (Kodagu, Karnataka), reachable by phone, WhatsApp, and video call.
- **Standardized leadership titles**: Jabir KJ (Founder), Fawaz BH (CMO),
  Zaheer KJ (CFO) — applied in both visible HTML and JSON-LD structured data.
- **All blog article authors standardized to Fawaz BH (CMO)**, so every
  article under `/blog` credits the same, correctly titled author.
- **Standardized contact details**: Primary `+91 90195 57427`, Secondary
  `+91 94810 84038`, correct Instagram handle `ilmera.studyabroad`, correct
  Facebook/LinkedIn handle `ilmerastudyabroad`.
- **Standardized brand asset path**: `assets/images/ilmera.logo.png` used
  consistently for the logo, favicon, and Open Graph / Twitter Card images
  across all six pages.
- **Structured data (JSON-LD)** on every page: `EducationalOrganization` /
  `ProfessionalService`, `WebSite`, `WebPage`, `ContactPage`, `AboutPage`,
  `BreadcrumbList`, `FAQPage`, `Person` (leadership), `Service`, and
  `Organization` with `contactPoint`, `address`, and `sameAs` all present and
  consistent.
- **Clean, extension-less URLs** enforced via `.htaccess` mod_rewrite
  (`/about`, `/services`, `/contact`, `/privacy-policy`, `/terms` instead of
  `.php`-suffixed paths), matched consistently across `sitemap.xml`, internal
  links, canonical tags, and JSON-LD `@id`/URL fields.
- **AI-crawler access and context files**: `robots.txt` explicitly allows the
  major AI/LLM crawlers (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot,
  Google-Extended, ClaudeBot, Applebot-Extended, etc.); `llms.txt` and the new
  `llms-full.txt` give AI answer engines a structured, accurate summary of
  the company, leadership, services, destinations, and an explicit
  instruction not to invent statistics or "remote-first" language about
  ILMERA.
- **Two new legal pages**: `/privacy-policy` and `/terms`, matching the
  site's visual language, with JSON-LD `WebPage` + `BreadcrumbList` schema.
- **Local SEO/GEO consistency**: `geo.region` / `geo.placename` meta tags
  corrected to the precise `IN-KA` / "Coorg, Karnataka, India" on every page
  (previously inconsistent — some pages used a generic "India" tag).
- **System cleanup**: `htaccess` renamed to `.htaccess` so its rewrite rules
  actually apply; scratch `_import/tree.json` removed.
- **Simplified navigation**: removed the light/dark theme toggle button from
  the header (site now uses one consistent visual theme).
- **Standardized brand image paths** site-wide: `ilmera.logo.png` (logo),
  `jabirkj.png` (Jabir KJ), `zaheer.png` (Zaheer KJ), `fawazbh.webp`
  (Fawaz BH) — fixed inconsistent filenames/casing that existed in some
  JSON-LD blocks.
- **Cleaned up the About page team cards**: removed a duplicated name in
  Jabir KJ's card, unified all three cards to the same structure, and
  rebalanced bio lengths so all three read as similar length.
- **Added `sitemap.php`**, which redirects to the canonical `sitemap.xml`
  (kept as the single source of truth to avoid duplicate-content risk).
- **Added a Blog section**: a new `/blog` listing page plus 4 static article
  pages under `/blog/{slug}`, linked from both the header and footer
  navigation, with full SEO meta tags and `Blog`/`BlogPosting`/`BreadcrumbList`
  JSON-LD on every blog page. See section 2 for the full path list.

## 2. Functional entry points (paths)

| Path | File | Purpose |
|---|---|---|
| `/` | `index.php` | Home page |
| `/services` | `services.php` | Services detail page |
| `/about` | `about.php` | About / leadership page |
| `/contact` | `contact.php` | Contact page |
| `/privacy-policy` | `privacy-policy.php` | Privacy policy (new) |
| `/terms` | `terms.php` | Terms of use (new) |
| `/blog` | `blog/index.php` | Blog listing page (new) |
| `/blog/study-in-germany-free-aps-certificate` | `blog/study-in-germany-free-aps-certificate.php` | Article: Germany APS certificate (new) |
| `/blog/italy-dsu-scholarship-eligibility` | `blog/italy-dsu-scholarship-eligibility.php` | Article: Italy DSU scholarship (new) |
| `/blog/study-abroad-with-academic-backlogs` | `blog/study-abroad-with-academic-backlogs.php` | Article: studying with backlogs (new) |
| `/blog/study-abroad-counselling-from-coorg` | `blog/study-abroad-counselling-from-coorg.php` | Article: Coorg-based counselling process (new) |
| `/sitemap.xml` | `sitemap.xml` | XML sitemap |
| `/robots.txt` | `robots.txt` | Crawler directives |
| `/llms.txt` | `llms.txt` | AI-crawler summary |
| `/llms-full.txt` | `llms-full.txt` | AI-crawler full context doc |

All `.php`-suffixed direct requests 301-redirect to their extension-less
equivalent via `.htaccess`; there are no query-parameter-driven routes.

## 3. Features not yet implemented

- No backend/CMS — all content is hand-authored static PHP with no database.
  The blog is static too: adding a new article currently means creating a
  new `.php` file under `blog/` and adding a card to `blog/index.php`, not
  filling in a form.
- No visible on-page display of the East African/other-market claims (site
  is India-focused only, by design).
- No automated build, lint, or test pipeline (plain PHP/HTML/CSS/JS, no
  build step).
- Off-page SEO (backlinks, business directory citations, Google Business
  Profile) is outside the scope of this static-site rewrite — see the
  ranking note in `flagged-items-for-verification.md`.

## 4. Recommended next steps

1. Confirm the open items in `flagged-items-for-verification.md`, especially:
   asset filenames (`ilmera.logo.png`, team photos), destination/eligibility
   facts, and social handle ownership.
3. The blog now exists with 4 articles; keep adding new posts periodically
   for ongoing content freshness (helps both classic SEO and AEO/GEO, since
   AI answer engines favor frequently updated, specific, well-sourced
   content). A `blog_posts` Table API schema was also created during this
   work but is not currently used by any page (see
   `flagged-items-for-verification.md` item 10) — delete it or wire it up to
   a dynamic blog later, whichever the site owner prefers.
4. Periodically refresh `llms.txt` / `llms-full.txt` and the JSON-LD
   `dateModified`/`lastmod` values whenever real content changes, so AI
   crawlers and search engines see it as current.
5. Set realistic ranking expectations: no legitimate technique guarantees a
   #1 ranking; continued off-page authority building and content additions
   are the main levers beyond this on-page/technical rewrite.

## 5. Project goals

Give ILMERA Study Abroad an accurate, consistent, and technically sound
static site that:
- Represents the business honestly (no fabricated stats/testimonials, no
  misleading "remote-first" framing).
- Is fully crawlable and well-structured for classic search engines (SEO),
  answer engines like Google's AI Overviews and Bing Copilot (AEO), and
  generative AI assistants like ChatGPT, Claude, and Perplexity (GEO).
- Uses consistent brand facts (leadership titles, contact numbers, logo,
  social handles, business location) everywhere they appear.

## 6. Data models / storage

This is a fully static PHP site — all page content lives directly in the
`.php`, `.txt`, and `.xml` files listed above. `header.php` and `footer.php`
are shared includes referenced from each page via
`include $_SERVER['DOCUMENT_ROOT'] . '/includes/header.php'` (or a relative
`include 'includes/header.php'` in `index.php`) — the live server is expected
to resolve these against its actual `DOCUMENT_ROOT`/`includes/` structure.

One RESTful Table API table, `blog_posts`, was created while exploring a
dynamic blog approach (fields: `id`, `title`, `slug`, `excerpt`, `content`,
`category`, `author_name`, `author_role`, `published_date`, `read_minutes`;
4 seed rows). The final blog implementation ended up fully static instead
(safer for JS-less AI/answer-engine crawlers and consistent with the rest of
the site), so **this table is not currently read by any page** — it is
unused infrastructure, flagged in `flagged-items-for-verification.md` item 10.

## 7. Public URLs

Production domain: `https://ilmerastudyabroad.com/` (deployment/hosting is
managed outside this static-file rewrite; see the Publish tab for one-click
publishing of this project if hosted from this workspace).
