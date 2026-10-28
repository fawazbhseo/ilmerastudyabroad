# Phase31 Task4 local A/B protocol

## Purpose and variants

This is a local simulated comparison of the approved static hero still, not a field or live-site speed test.

- **A:** the verified Task2 source before the Task3 static-still CSS, commit `7d1bb9ec0522bcbc7953262920fafb50bf04ab72`.
- **B:** the verified Task3 source with the static still, commit `806769a0d379e2059f654ba96be1561484d64598`.
- The four reference controls are `/`, `/services`, `/about` and `/contact`. Their Task2 and Task3 rendered HTML is byte-identical.
- The four treatment routes are `/study-in-germany`, `/study-abroad-counselling-mysuru`, `/blog/how-to-choose-study-abroad-consultant-karnataka` and `/blog/`. For each, removing the exact Task3 CSS heredoc from B makes the complete rendered HTML byte-identical to A. No copy, image, metadata, link, status or other style changes are part of this candidate.

The frozen route HTML and SHA-256 manifest are in `reports/phase-31-task4-ab-fixtures.json`. The raw A/B fixture JSON is preserved in `reports/phase-31-task4-ab-fixtures.tar.gz`.

## Delivery and sampling

A test-only HTTP fixture host serves both arms at the same local origin and page paths. Static files use the same current repository assets for both arms. Third-party scripts and fonts are mirrored from the pinned npm packages or aborted. No request is forwarded as live CDN evidence.

The planned single session contains seven A and seven B fresh Chromium processes for each of the eight routes, 112 samples total. For every route, round 0 runs A then B, round 1 runs B then A, alternating through round 6. Samples are serial. Each sample gets a fresh isolated browser process and Lighthouse storage reset. No other browser, screenshot, accessibility or QA benchmark may overlap. There is no resume, retry or selective deletion of a failed sample.

Pinned tooling: Chromium `143.0.7499.0`, Playwright `1.58.2`, Lighthouse `12.8.2`, PHP-WASM `8.5.10`, and the locally mirrored font/script packages listed in the runtime environment. Lighthouse runs its mobile simulated Slow4G and 4x CPU model. The oversized post-trace report screenshot is disabled consistently; page animations and metric collection remain active.

## Recorded measures and interpretation

Every sample retains LCP, CLS, TBT, total transfer bytes, request count, render-blocking request URLs, actual still-image requests, font requests, passive LCP/font/paint-gate observations, warnings, and failures. Reports include medians and linearly interpolated IQRs for both arms.

For diagnosis, the report also calculates the prior local comparison budgets: B adds under 150,000 transfer bytes, median LCP is no more than 1.10 times A, TBT is no more than A plus 50 ms, CLS does not increase and stays below 0.1, and there are no new render-blocking URLs. The four reference controls must have a symmetric median LCP ratio no greater than 1.10 for a reliable local session. A failure or unreliable control remains a failure or limitation; no budgets are relaxed and no retry is authorized in this protocol.

Even a complete numerical pass is **not** a live-speed gain, field Core Web Vitals result, native-hosting proof, release certification, deployment approval or permission to merge. Historical Phase25 and Phase25c benchmark files are not modified.
