# Phase32a measured palette fallback check

Date: 2026-11-02

## Decision

The frozen six-route local A/B analysis at `reports/phase-32a-6-route-ab-run-01-summary.md` required a plain-palette fallback for the `place` and `article` template groups. Mysuru exceeded the TBT budget by 16.24 ms, and the choosing-consultant article exceeded the LCP ratio budget (1.4243 versus 1.10) and TBT budget (+59 ms versus +50 ms). The summary and pushed raw run remain the measurement evidence; no post-fallback performance claim is made here.

`includes/visual-config.php` now lists `place` and `article` in `ILMERA_VISUAL_PLAIN_HERO_TEMPLATES`. The site-wide `ILMERA_SCENES_ENABLED` switch remains enabled and unchanged. Destination and Blog-index groups are not included in this fallback. No Home, Services, About or Contact source changed.

## Fast verification

- PHP-WASM 8.5.8 lint passed for `includes/visual-system.php`, `includes/visual-config.php`, `destinations/germany.php`, `places/mysuru.php`, `study-in-germany.php`, `study-abroad-counselling-mysuru.php`, `blog/how-to-choose-study-abroad-consultant-karnataka.php` and `blog/index.php`.
- PHP-WASM rendered `/study-abroad-counselling-mysuru` and `/blog/how-to-choose-study-abroad-consultant-karnataka` with HTTP 200 and non-empty HTML.
- Both fallback renders contain no `p32-hero-still` canvas markup, no `hero-still-640.webp` or `hero-still-1440.webp` URL, and no hero still loader script. Therefore there is no delayed still `Image` request or hero still in the noscript rule on these template groups.
- The six-route fixture content comparator passed on both pages: normalized text/order, title, headings, meta, robots, canonical, semantic links/order, image/picture-source attributes and JSON-LD match frozen A. No wording, headings, links, FAQs, schema or image content was changed.
- Rendered outputs were temporary under `/home/user/phase32a-runtime/phase32a-after-fallback/`; no generated HTML is retained in Git. The repository records are this check report, the small config change, progress and the verification flag.

This is an affected-template lint/render/content check only. The full suite remains reserved for its single final run. A post-fallback A/B measurement has not been run, and this report does not claim the fallback cures the measured TBT/LCP deltas.
