# Phase31 before/after contact sheet

**Scope:** local full-page comparison of the Phase30 baseline at `75f355fd4dfda0a61ddbda5b45fc2944c8503e76` and Phase31 rendered source at `49efa0aa1e929c9359bc6e2abc3ba656d8e19753`. These are branch evidence, not live-host screenshots. Each source has a frozen rendered HTML archive; current assets are unchanged from the baseline.

**Capture method:** 32 raw PNGs, eight requested pages at 360px and 1280px, 900px viewport height, Chromium 143.0.7499.0, Playwright 1.58.2, JavaScript on, normal motion. Each page was slowly scrolled, allowed a 3-second settle, returned to the top and captured full page. All 32 responses were HTTP 200, all returned to top, and there were no unexpected request failures. Google Fonts requests were blocked by the local harness. The raw-image hashes, sizes, page heights and capture conditions are in [`phase-31-contact-sheet-captures.json`](phase-31-contact-sheet-captures.json).

Links below point to the original full-page PNG files committed in the branch. The sizes shown in parentheses are the image width by full-page pixel height, followed by the PNG file size.

## Before/after screenshot index

| Page | Width | Before raw PNG | After raw PNG | Document height before -> after |
|---|---:|---|---|---:|
| Home | 360px | [before-home-360.png (360x16015, 1.65 MiB)](screenshots/phase-31-contact-sheet/before-home-360.png) | [after-home-360.png (360x15957, 1.65 MiB)](screenshots/phase-31-contact-sheet/after-home-360.png) | 16,015 -> 15,957 (-58px) |
| Home | 1280px | [before-home-1280.png (1280x10977, 3.30 MiB)](screenshots/phase-31-contact-sheet/before-home-1280.png) | [after-home-1280.png (1280x10977, 3.29 MiB)](screenshots/phase-31-contact-sheet/after-home-1280.png) | 10,977 -> 10,977 (+0px) |
| Services | 360px | [before-services-360.png (360x23222, 1.93 MiB)](screenshots/phase-31-contact-sheet/before-services-360.png) | [after-services-360.png (360x23222, 1.93 MiB)](screenshots/phase-31-contact-sheet/after-services-360.png) | 23,222 -> 23,222 (+0px) |
| Services | 1280px | [before-services-1280.png (1280x17711, 3.96 MiB)](screenshots/phase-31-contact-sheet/before-services-1280.png) | [after-services-1280.png (1280x17711, 3.97 MiB)](screenshots/phase-31-contact-sheet/after-services-1280.png) | 17,711 -> 17,711 (+0px) |
| About | 360px | [before-about-360.png (360x14983, 1.68 MiB)](screenshots/phase-31-contact-sheet/before-about-360.png) | [after-about-360.png (360x14803, 1.66 MiB)](screenshots/phase-31-contact-sheet/after-about-360.png) | 14,983 -> 14,803 (-180px) |
| About | 1280px | [before-about-1280.png (1280x9275, 2.79 MiB)](screenshots/phase-31-contact-sheet/before-about-1280.png) | [after-about-1280.png (1280x9275, 2.78 MiB)](screenshots/phase-31-contact-sheet/after-about-1280.png) | 9,275 -> 9,275 (+0px) |
| Contact | 360px | [before-contact-360.png (360x9113, 1.18 MiB)](screenshots/phase-31-contact-sheet/before-contact-360.png) | [after-contact-360.png (360x9113, 1.18 MiB)](screenshots/phase-31-contact-sheet/after-contact-360.png) | 9,113 -> 9,113 (+0px) |
| Contact | 1280px | [before-contact-1280.png (1280x6064, 1.63 MiB)](screenshots/phase-31-contact-sheet/before-contact-1280.png) | [after-contact-1280.png (1280x6064, 1.63 MiB)](screenshots/phase-31-contact-sheet/after-contact-1280.png) | 6,064 -> 6,064 (+0px) |
| Germany | 360px | [before-germany-360.png (360x8059, 0.41 MiB)](screenshots/phase-31-contact-sheet/before-germany-360.png) | [after-germany-360.png (360x8059, 0.47 MiB)](screenshots/phase-31-contact-sheet/after-germany-360.png) | 8,059 -> 8,059 (+0px) |
| Germany | 1280px | [before-germany-1280.png (1280x5937, 0.46 MiB)](screenshots/phase-31-contact-sheet/before-germany-1280.png) | [after-germany-1280.png (1280x5937, 0.65 MiB)](screenshots/phase-31-contact-sheet/after-germany-1280.png) | 5,937 -> 5,937 (+0px) |
| Mysuru | 360px | [before-mysuru-360.png (360x6860, 0.43 MiB)](screenshots/phase-31-contact-sheet/before-mysuru-360.png) | [after-mysuru-360.png (360x6860, 0.46 MiB)](screenshots/phase-31-contact-sheet/after-mysuru-360.png) | 6,860 -> 6,860 (+0px) |
| Mysuru | 1280px | [before-mysuru-1280.png (1280x4538, 0.54 MiB)](screenshots/phase-31-contact-sheet/before-mysuru-1280.png) | [after-mysuru-1280.png (1280x4538, 0.66 MiB)](screenshots/phase-31-contact-sheet/after-mysuru-1280.png) | 4,538 -> 4,538 (+0px) |
| Article: How to Choose a Study Abroad Consultant | 360px | [before-article-360.png (360x12537, 0.97 MiB)](screenshots/phase-31-contact-sheet/before-article-360.png) | [after-article-360.png (360x12537, 1.03 MiB)](screenshots/phase-31-contact-sheet/after-article-360.png) | 12,537 -> 12,537 (+0px) |
| Article: How to Choose a Study Abroad Consultant | 1280px | [before-article-1280.png (1280x7976, 0.97 MiB)](screenshots/phase-31-contact-sheet/before-article-1280.png) | [after-article-1280.png (1280x7976, 1.07 MiB)](screenshots/phase-31-contact-sheet/after-article-1280.png) | 7,976 -> 7,976 (+0px) |
| Blog index | 360px | [before-blog-index-360.png (360x6400, 0.39 MiB)](screenshots/phase-31-contact-sheet/before-blog-index-360.png) | [after-blog-index-360.png (360x6400, 0.43 MiB)](screenshots/phase-31-contact-sheet/after-blog-index-360.png) | 6,400 -> 6,400 (+0px) |
| Blog index | 1280px | [before-blog-index-1280.png (1280x3400, 0.44 MiB)](screenshots/phase-31-contact-sheet/before-blog-index-1280.png) | [after-blog-index-1280.png (1280x3400, 0.55 MiB)](screenshots/phase-31-contact-sheet/after-blog-index-1280.png) | 3,400 -> 3,400 (+0px) |

## Plain-language page notes

### Home

The Home `#team` section is the only approved blank-space change on this page. Its mobile `min-height` is now `auto` at widths up to 600px. The pre-fix scan measured a 201px visible-child-to-section-bottom tail at 360px. In the full-page captures, the overall document height changes from 16,015px to 15,957px at 360px, a 58px document-height reduction; at 1280px it remains 10,977px. The 201px tail measure and 58px document-height delta are different quantities.

### Services

No blank-space CSS change was made to Services. The page height is unchanged at both captured widths: 23,222px at 360px and 17,711px at 1280px.

### About

The About `#team` section now uses `min-height:auto` at 360px and 768px. The pre-fix scan measured visible-child-to-section-bottom tails of 196px at 360px and 283px at 768px. Full-page document height changes from 14,983px to 14,803px at 360px (180px shorter) and from 9,628px to 9,361px at 768px (267px shorter, from the 516-case scan). The 1280px document remains 9,275px.

### Contact

No blank-space change was made to Contact. The existing 88vh `#miniHero` is retained for its bottom scroll cue. The remaining measured tails are 138px at 360px and 233px at 768px. Full-page document height is unchanged at 9,113px (360px) and 6,064px (1280px).

### Germany

The destination hero now has the approved static still background. This fills the hero visually without changing its vertical geometry: document height stays 8,059px at 360px and 5,937px at 1280px. No text, links, image content or page structure changed.

### Mysuru

The place-page hero now has the approved static still background. The document remains 6,860px tall at 360px and 4,538px at 1280px. No vertical blank space is claimed as removed.

### Article: How to Choose a Study Abroad Consultant

The article hero receives the approved static still background only. Document height is unchanged at 12,537px at 360px and 7,976px at 1280px.

### Blog index

The blog-index hero receives the approved static still background only. Document height is unchanged at 6,400px at 360px and 3,400px at 1280px.

## Total blank-height accounting

**Observed full-document height reduction across the three affected responsive widths: 505px** (Home 360px: 58px; About 360px: 180px; About 768px: 267px). The 768px value is from the fresh 516-case scan because the contact-sheet image set is intentionally limited to 360px and 1280px. All other page/width document heights in this contact sheet are unchanged.

The original blank-space audit measured 680px of visible-child-to-section-bottom tail across those three `#team` breakpoints (Home 201px at 360px; About 196px at 360px; About 283px at 768px). That is the pre-fix section-tail metric, not the measured full-document height change. Repeated JavaScript/motion observations are not added. The remaining Contact `#miniHero` tails (138px at 360px, 233px at 768px) are retained intentionally and are excluded from savings. Pixel quiet-band candidates are also excluded.

## Scope confirmation

The 43-route comparison against the Phase30 baseline passed the protected rendered-content invariants: visible/document text and order, title/meta, headings, FAQ text, link hrefs and attributes, image attributes, JSON-LD, canonicals, robots, HTTP status and exact sitemap bytes/38 entries. The recognized Phase31 presentation sources are limited to `index.php`, `about.php` and `includes/visual-system.php`; the Home/About changes are limited to the logged responsive `#team` `min-height` rules, and the shared visual-system change adds the approved static still backgrounds for destination/place/article/blog templates. No user-facing wording or image content was changed. See [`phase-31-task5-render-comparison.json`](phase-31-task5-render-comparison.json) and [`phase-31-task2-render-comparison.json`](phase-31-task2-render-comparison.json).

Task4 reference/control pages `/`, `/services`, `/about` and `/contact` are byte-identical between the local A/B arms. The four A/B target pages (Germany, Mysuru, the selected article and blog index) differ only by the exact logged Task3 static-still CSS block; removing that block makes each full rendered HTML byte-identical to the control arm. The still-image assets are byte-identical between arms. See [`phase-31-task4-ab-fixtures.json`](phase-31-task4-ab-fixtures.json).

This contact sheet records presentation differences only. It does not certify live performance, native hosting behavior or deployment.
