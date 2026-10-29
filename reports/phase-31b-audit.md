# Phase31 Task2 post-fix blank-space audit

**Capture source:** `49efa0aa1e929c9359bc6e2abc3ba656d8e19753`. Exact Task2 source-scope validation passed for: `about.php, includes/visual-system.php, index.php`. Immutable content/render baseline: `75f355fd4dfda0a61ddbda5b45fc2944c8503e76`.

**Coverage:** 516 cases: 43 route entries × 3 widths (360, 768, 1280) × JavaScript on/off × normal/reduced motion. Every case scrolled through the document, waited 3 seconds, returned to the top, captured and analysed a full-page PNG in memory, recorded its SHA-256, and saved a crop for each thresholded candidate.

**Pinned local browser:** Chromium 143.0.7499.0 (`@sparticuz/chromium` 143.0.4), Playwright 1.58.2, GSAP 3.12.2, Three.js 0.128.0. Original Google Fonts stylesheet requests were blocked by the harness and recorded as expected request failures; no external font/CDN bytes were used. This is local browser evidence, not native-host testing.

## Reading the candidate counts

A pixel quiet band is a screening candidate, not proof that the design contains removable blank space. The metric detects a contiguous vertical band where horizontal grayscale edge occupancy stays below 0.6% at a scan width of at most 512px, with the requested route-specific minimum heights. Bands must be between visually active rows. Structural findings separately detect visible text/media, empty wrappers, hidden reveal text, and excess tail below the last visible child of an explicit `min-height`, after subtracting the declared bottom padding. Normal section padding, intentional backgrounds, and repeated views of the same gap are not counted as confirmed savings.

Total audit findings: **1026** (by kind: `{"intentional-scroll-indicator-dismissed": 16, "pixel-quiet-band": 1006, "unused-min-height-tail": 4}`). Hidden reveal-text findings: **0**; intentional scroll-cue dismissals: **16**; unused explicit-min-height tails: **4**; non-decorative empty wrappers: **0**.

## Before and after counts

| Finding kind | Task1 baseline | Task2 post-fix | Change |
|---|---:|---:|---:|
| intentional-scroll-indicator-dismissed | 16 | 16 | +0 |
| pixel-quiet-band | 1174 | 1006 | -168 |
| unused-min-height-tail | 16 | 4 | -12 |

Task2 changed only the two reviewed `#team` responsive `min-height` declarations. No revealed page-copy failure was found in Task1, so no reveal code was introduced. The Contact `#miniHero` first-fold cue space remains intentionally retained.

## Candidate route ranking

Ranking is by route-level vertical union across the width/state matrix, which avoids simply multiplying repeated screenshots. Cumulative pixels across cases are shown separately and are not a unique-area measurement.

| Rank | Route | Vertical union candidate px | Cumulative candidate px across cases | Pixel bands | Min-height tails | Hidden text | Empty wrappers |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `/services` | 8,414 | 34,635 | 148 | 0 | 0 | 0 |
| 2 | `/` | 2,916 | 12,130 | 60 | 0 | 0 | 0 |
| 3 | `/about` | 2,553 | 12,274 | 64 | 0 | 0 | 0 |
| 4 | `/contact` | 1,704 | 5,602 | 26 | 4 | 0 | 0 |
| 5 | `/study-in-uk` | 1,313 | 5,364 | 32 | 0 | 0 | 0 |
| 6 | `/study-in-germany` | 1,138 | 4,552 | 28 | 0 | 0 | 0 |
| 7 | `/study-in-lithuania` | 1,136 | 4,544 | 28 | 0 | 0 | 0 |
| 8 | `/study-in-italy` | 1,135 | 4,540 | 28 | 0 | 0 | 0 |
| 9 | `/study-in-latvia` | 1,002 | 4,008 | 24 | 0 | 0 | 0 |
| 10 | `/study-in-slovakia` | 1,001 | 4,004 | 24 | 0 | 0 | 0 |
| 11 | `/blog/` | 900 | 3,600 | 20 | 0 | 0 | 0 |
| 12 | `/all-pages` | 819 | 3,756 | 24 | 0 | 0 | 0 |
| 13 | `/study-abroad-counselling-mysuru` | 767 | 3,068 | 20 | 0 | 0 | 0 |
| 14 | `/study-abroad-counselling-madikeri` | 766 | 3,064 | 20 | 0 | 0 | 0 |
| 15 | `/study-abroad-counselling-mangaluru` | 766 | 3,064 | 20 | 0 | 0 | 0 |
| 16 | `/study-abroad-counselling-belagavi` | 765 | 3,060 | 20 | 0 | 0 | 0 |
| 17 | `/study-abroad-counselling-gonikoppal` | 765 | 3,060 | 20 | 0 | 0 | 0 |
| 18 | `/study-abroad-counselling-hassan` | 765 | 3,060 | 20 | 0 | 0 | 0 |
| 19 | `/study-abroad-counselling-ponnampet` | 765 | 3,060 | 20 | 0 | 0 | 0 |
| 20 | `/study-abroad-counselling-siddapura` | 764 | 3,056 | 20 | 0 | 0 | 0 |
| 21 | `/blog/study-abroad-with-academic-backlogs` | 763 | 3,052 | 20 | 0 | 0 | 0 |
| 22 | `/study-abroad-consultants-in-kodagu` | 763 | 3,052 | 20 | 0 | 0 | 0 |
| 23 | `/study-abroad-counselling-chikkamagaluru` | 763 | 3,052 | 20 | 0 | 0 | 0 |
| 24 | `/study-abroad-counselling-kushalnagar` | 763 | 3,052 | 20 | 0 | 0 | 0 |
| 25 | `/study-abroad-counselling-shivamogga` | 763 | 3,052 | 20 | 0 | 0 | 0 |
| 26 | `/study-abroad-counselling-virajpet` | 763 | 3,052 | 20 | 0 | 0 | 0 |
| 27 | `/study-abroad-counselling-bengaluru` | 761 | 3,044 | 20 | 0 | 0 | 0 |
| 28 | `/study-abroad-counselling-somwarpet` | 761 | 3,044 | 20 | 0 | 0 | 0 |
| 29 | `/study-abroad-consultants-in-karnataka` | 743 | 2,972 | 20 | 0 | 0 | 0 |
| 30 | `/blog/cost-of-studying-abroad-for-indian-students` | 663 | 2,652 | 16 | 0 | 0 | 0 |
| 31 | `/study-in-gcc` | 647 | 2,588 | 16 | 0 | 0 | 0 |
| 32 | `/blog/study-in-germany-free-aps-certificate` | 645 | 2,580 | 16 | 0 | 0 | 0 |
| 33 | `/study-in-czech-republic` | 626 | 2,504 | 16 | 0 | 0 | 0 |
| 34 | `/study-in-russia` | 626 | 2,504 | 16 | 0 | 0 | 0 |
| 35 | `/blog/study-abroad-counselling-from-coorg` | 602 | 2,408 | 16 | 0 | 0 | 0 |
| 36 | `/study-abroad-counselling-udupi-manipal` | 601 | 2,404 | 16 | 0 | 0 | 0 |
| 37 | `/blog/how-to-choose-study-abroad-consultant-karnataka` | 381 | 1,524 | 8 | 0 | 0 | 0 |
| 38 | `/404` | 341 | 1,364 | 8 | 0 | 0 | 0 |
| 39 | `/blog/scholarships-for-indian-students-study-abroad` | 313 | 1,252 | 8 | 0 | 0 | 0 |
| 40 | `/blog/documents-needed-to-study-abroad-from-india` | 309 | 1,236 | 8 | 0 | 0 | 0 |
| 41 | `/terms` | 273 | 1,092 | 8 | 0 | 0 | 0 |
| 42 | `/privacy-policy` | 152 | 608 | 4 | 0 | 0 | 0 |
| 43 | `/blog/italy-dsu-scholarship-eligibility` | 147 | 588 | 4 | 0 | 0 | 0 |

## Structural/reveal findings

These are measured structural candidates, not blanket authorization to remove spacing. Each row includes the saved crop and route/source location.

| Kind | Route | State | y | Height | Selector | Computed cause/evidence | Source | Crop |
|---|---|---|---:|---:|---|---|---|---|
| intentional-scroll-indicator-dismissed | `/` | 1280 / JS on / normal | 841 | 11 | `.scroll-ind span` | Existing scroll cue is initially visible and is intentionally faded after scrollY exceeds 80px; it remains dismissed when returning to the top. JavaScript-off pages do not run that dismissal. It is a cue, not revealed page content. | `index.php:398`; CSS `index.php:260` | `reports/screenshots/phase-31b-scan/home__1280__js-on__motion-normal-hidden-06.webp` |
| intentional-scroll-indicator-dismissed | `/` | 1280 / JS on / reduced | 841 | 11 | `.scroll-ind span` | Existing scroll cue is initially visible and is intentionally faded after scrollY exceeds 80px; it remains dismissed when returning to the top. JavaScript-off pages do not run that dismissal. It is a cue, not revealed page content. | `index.php:398`; CSS `index.php:260` | `reports/screenshots/phase-31b-scan/home__1280__js-on__motion-reduced-hidden-06.webp` |
| intentional-scroll-indicator-dismissed | `/about` | 1280 / JS on / normal | 579 | 11 | `.scroll-ind span` | Existing scroll cue is initially visible and is intentionally faded after scrollY exceeds 80px; it remains dismissed when returning to the top. JavaScript-off pages do not run that dismissal. It is a cue, not revealed page content. | `about.php:533`; CSS `about.php:397` | `reports/screenshots/phase-31b-scan/about__1280__js-on__motion-normal-hidden-07.webp` |
| intentional-scroll-indicator-dismissed | `/about` | 1280 / JS on / reduced | 579 | 11 | `.scroll-ind span` | Existing scroll cue is initially visible and is intentionally faded after scrollY exceeds 80px; it remains dismissed when returning to the top. JavaScript-off pages do not run that dismissal. It is a cue, not revealed page content. | `about.php:533`; CSS `about.php:397` | `reports/screenshots/phase-31b-scan/about__1280__js-on__motion-reduced-hidden-07.webp` |
| unused-min-height-tail | `/contact` | 360 / JS on / normal | 654 | 138 | `#miniHero` | Computed min-height creates a tail beyond the last visible text/media block after the declared bottom padding. Retain: the 88vh first-fold hero intentionally leaves room for its existing bottom scroll cue; no content or layout change authorized here. | `contact.php:325` | `reports/screenshots/phase-31b-scan/contact__360__js-on__motion-normal-dom-03.webp` |
| intentional-scroll-indicator-dismissed | `/contact` | 360 / JS on / normal | 725 | 11 | `.scroll-ind span` | Existing scroll cue is initially visible and is intentionally faded after scrollY exceeds 80px; it remains dismissed when returning to the top. JavaScript-off pages do not run that dismissal. It is a cue, not revealed page content. | `contact.php:331`; CSS `contact.php:247` | `reports/screenshots/phase-31b-scan/contact__360__js-on__motion-normal-hidden-04.webp` |
| unused-min-height-tail | `/contact` | 360 / JS on / reduced | 654 | 138 | `#miniHero` | Computed min-height creates a tail beyond the last visible text/media block after the declared bottom padding. Retain: the 88vh first-fold hero intentionally leaves room for its existing bottom scroll cue; no content or layout change authorized here. | `contact.php:325` | `reports/screenshots/phase-31b-scan/contact__360__js-on__motion-reduced-dom-03.webp` |
| intentional-scroll-indicator-dismissed | `/contact` | 360 / JS on / reduced | 725 | 11 | `.scroll-ind span` | Existing scroll cue is initially visible and is intentionally faded after scrollY exceeds 80px; it remains dismissed when returning to the top. JavaScript-off pages do not run that dismissal. It is a cue, not revealed page content. | `contact.php:331`; CSS `contact.php:247` | `reports/screenshots/phase-31b-scan/contact__360__js-on__motion-reduced-hidden-04.webp` |
| unused-min-height-tail | `/contact` | 768 / JS on / normal | 559 | 233 | `#miniHero` | Computed min-height creates a tail beyond the last visible text/media block after the declared bottom padding. Retain: the 88vh first-fold hero intentionally leaves room for its existing bottom scroll cue; no content or layout change authorized here. | `contact.php:325` | `reports/screenshots/phase-31b-scan/contact__768__js-on__motion-normal-dom-02.webp` |
| intentional-scroll-indicator-dismissed | `/contact` | 768 / JS on / normal | 725 | 11 | `.scroll-ind span` | Existing scroll cue is initially visible and is intentionally faded after scrollY exceeds 80px; it remains dismissed when returning to the top. JavaScript-off pages do not run that dismissal. It is a cue, not revealed page content. | `contact.php:331`; CSS `contact.php:247` | `reports/screenshots/phase-31b-scan/contact__768__js-on__motion-normal-hidden-03.webp` |
| unused-min-height-tail | `/contact` | 768 / JS on / reduced | 559 | 233 | `#miniHero` | Computed min-height creates a tail beyond the last visible text/media block after the declared bottom padding. Retain: the 88vh first-fold hero intentionally leaves room for its existing bottom scroll cue; no content or layout change authorized here. | `contact.php:325` | `reports/screenshots/phase-31b-scan/contact__768__js-on__motion-reduced-dom-02.webp` |
| intentional-scroll-indicator-dismissed | `/contact` | 768 / JS on / reduced | 725 | 11 | `.scroll-ind span` | Existing scroll cue is initially visible and is intentionally faded after scrollY exceeds 80px; it remains dismissed when returning to the top. JavaScript-off pages do not run that dismissal. It is a cue, not revealed page content. | `contact.php:331`; CSS `contact.php:247` | `reports/screenshots/phase-31b-scan/contact__768__js-on__motion-reduced-hidden-03.webp` |
| intentional-scroll-indicator-dismissed | `/contact` | 1280 / JS on / normal | 725 | 11 | `.scroll-ind span` | Existing scroll cue is initially visible and is intentionally faded after scrollY exceeds 80px; it remains dismissed when returning to the top. JavaScript-off pages do not run that dismissal. It is a cue, not revealed page content. | `contact.php:331`; CSS `contact.php:247` | `reports/screenshots/phase-31b-scan/contact__1280__js-on__motion-normal-hidden-02.webp` |
| intentional-scroll-indicator-dismissed | `/contact` | 1280 / JS on / reduced | 725 | 11 | `.scroll-ind span` | Existing scroll cue is initially visible and is intentionally faded after scrollY exceeds 80px; it remains dismissed when returning to the top. JavaScript-off pages do not run that dismissal. It is a cue, not revealed page content. | `contact.php:331`; CSS `contact.php:247` | `reports/screenshots/phase-31b-scan/contact__1280__js-on__motion-reduced-hidden-02.webp` |
| intentional-scroll-indicator-dismissed | `/services` | 360 / JS on / normal | 439 | 11 | `.scroll-ind span` | Existing scroll cue is initially visible and is intentionally faded after scrollY exceeds 80px; it remains dismissed when returning to the top. JavaScript-off pages do not run that dismissal. It is a cue, not revealed page content. | `services.php:386`; CSS `services.php:217` | `reports/screenshots/phase-31b-scan/services__360__js-on__motion-normal-hidden-15.webp` |
| intentional-scroll-indicator-dismissed | `/services` | 360 / JS on / reduced | 439 | 11 | `.scroll-ind span` | Existing scroll cue is initially visible and is intentionally faded after scrollY exceeds 80px; it remains dismissed when returning to the top. JavaScript-off pages do not run that dismissal. It is a cue, not revealed page content. | `services.php:386`; CSS `services.php:217` | `reports/screenshots/phase-31b-scan/services__360__js-on__motion-reduced-hidden-15.webp` |
| intentional-scroll-indicator-dismissed | `/services` | 768 / JS on / normal | 319 | 11 | `.scroll-ind span` | Existing scroll cue is initially visible and is intentionally faded after scrollY exceeds 80px; it remains dismissed when returning to the top. JavaScript-off pages do not run that dismissal. It is a cue, not revealed page content. | `services.php:386`; CSS `services.php:217` | `reports/screenshots/phase-31b-scan/services__768__js-on__motion-normal-hidden-15.webp` |
| intentional-scroll-indicator-dismissed | `/services` | 768 / JS on / reduced | 319 | 11 | `.scroll-ind span` | Existing scroll cue is initially visible and is intentionally faded after scrollY exceeds 80px; it remains dismissed when returning to the top. JavaScript-off pages do not run that dismissal. It is a cue, not revealed page content. | `services.php:386`; CSS `services.php:217` | `reports/screenshots/phase-31b-scan/services__768__js-on__motion-reduced-hidden-15.webp` |
| intentional-scroll-indicator-dismissed | `/services` | 1280 / JS on / normal | 579 | 11 | `.scroll-ind span` | Existing scroll cue is initially visible and is intentionally faded after scrollY exceeds 80px; it remains dismissed when returning to the top. JavaScript-off pages do not run that dismissal. It is a cue, not revealed page content. | `services.php:386`; CSS `services.php:217` | `reports/screenshots/phase-31b-scan/services__1280__js-on__motion-normal-hidden-11.webp` |
| intentional-scroll-indicator-dismissed | `/services` | 1280 / JS on / reduced | 579 | 11 | `.scroll-ind span` | Existing scroll cue is initially visible and is intentionally faded after scrollY exceeds 80px; it remains dismissed when returning to the top. JavaScript-off pages do not run that dismissal. It is a cue, not revealed page content. | `services.php:386`; CSS `services.php:217` | `reports/screenshots/phase-31b-scan/services__1280__js-on__motion-reduced-hidden-11.webp` |

## Pixel-band findings

Every band record includes route/state, y/height, selector, computed section context, neighboring visible text, source file/line, and crop in `reports/phase-31b-audit.json`. The appendix includes repeated bands in distinct states.

## Render baseline for no-content-change checks

The immutable local PHP-WASM render baseline contains all 43 frozen route entries at the pre-fix source. Exact rendered HTML, per-route byte count and SHA-256 are archived in `reports/phase-31-before-renders.json.gz`. The sitemap remains byte-identical with 38 entries. The other five routes are held/utility pages and remain in the audit because the explicit review inventory includes them.

## Disposition

Task2 fixes only the source-confirmed Home and About `#team` responsive min-height tails. Other pixel bands remain review candidates, not authorized savings. The Contact `#miniHero` 88vh first-fold tail is retained because its existing bottom scroll cue occupies that space on initial load. Intentional Explore/Reach Out cue dismissals remain unchanged. No user-facing copy, images, links, FAQ, schema, canonical, status, sitemap, or team-card text changed.
