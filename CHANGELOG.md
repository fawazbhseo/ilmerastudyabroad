# ILMERA Study Abroad — SEO / AEO / GEO Rewrite Changelog

All changes below implement the project-wide brand and copy mandate:
- No em dashes (—) anywhere in code or copy.
- No "remote-first" / "virtual office" / "100% online" / "handled remotely" framing.
  ILMERA is based in **Coorg (Kodagu, Karnataka)** and consults by phone, WhatsApp,
  and video call.
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
- Removed em dash from `aria-label="ILMERA Study Abroad — Home"` →
  `aria-label="ILMERA Study Abroad: Home"`.
- Unified `.logo-light` and `.logo-dark` `<img>` `src` to the real asset
  `ilmera.logo.png` (previously `.logo-light` pointed at
  `ilmera.logo.navy.png`, a file that does not exist in the project — see
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
  stats, legacy job titles, "remote" language, wrong social handles) — no
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
  Spoken / 2023 Founded`.
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
- **CTA section:** fixed a functional bug — `mailto:info@ilmeragroup.in`
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
  systems not to invent statistics or superlatives and not to describe
  ILMERA as "remote-first" or "100% online," and a Contact Summary.
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

### `about.php` — TEAM section
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

### `blog.php` (new, later moved to `blog/index.php` — see fix note below)
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

### `blog_posts` (Table API — created, currently unused)
- A schema (`id`, `title`, `slug`, `excerpt`, `content`, `category`,
  `author_name`, `author_role`, `published_date`, `read_minutes`) and 4 rows
  were created via the Table API while exploring a dynamic approach, before
  settling on fully static PHP pages (consistent with the rest of the site
  and safer for JS-less AI/answer-engine crawlers). This table is not read by
  any page. See `flagged-items-for-verification.md` item 10.
