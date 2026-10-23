# Phase 25 Stage 1 pilot gate

**Status: BLOCKED. No rollout authorized.**

PR: https://github.com/fawazbhseo/ilmerastudyabroad/pull/1

Stage 1 tasks 1-6 only. Germany, Mysuru, choosing-consultant article and blog index are the only opted-in pilots. Stage 2 has not started. No merge or deployment.

## Gate summary

- Local performance gate: **PASS**, all original budgets retained.
- Final full technical suite: **PASS** in 581.55s.
- Reference palette/template colour allowlist: **PASS**.
- Strict reference raster: **11/12 PASS, NOT fully cleared**. Home1280 has9 different anti-aliased corner pixels on the existing consultation CTA, one colour level per affected channel. Zero tolerance is retained. There is no broad mask, copied image content or accepted waiver. This remains a blocker, not an approved deviation.

## Local before/after medians

| Pilot | LCP before / after / limit (ms) | CLS before / after | TBT before / after (ms) | Added transfer | CDP requests before / after |
| --- | --- | --- | --- | --- | --- |
| Germany | 1592 / 1176 / 1751 | 0.053536 / 0.000000 | 0.0 / 2.0 | -41,093 B | 8 / 4 |
| Mysuru | 1588 / 1193 / 1747 | 0.045560 / 0.000000 | 0.0 / 0.0 | -41,140 B | 8 / 4 |
| Choosing-consultant article | 2182 / 1174 / 2400 | 0.000000 / 0.000000 | 50.0 / 0.0 | +49,290 B | 2 / 4 |
| Blog index | 2183 / 1159 / 2401 | 0.102867 / 0.000000 | 0.0 / 0.0 | -26,981 B | 7 / 4 |

Budget: added transfer strictly below150,000B; no new render-blocking resource; CLS no worse than baseline and strictly below0.1; LCP at most110% of original baseline; TBT at most baseline+50ms. Each final pilot meets every performance criterion. Every LCP sample is text/container, never a scene background. No new script transfer or blocking stylesheet; the reference fonts are embedded in existing inline CSS. CDP request counts include two data-font entries, not two extra font HTTP downloads.

Environment: local PHP8.5 WASM, Chromium143, Lighthouse12.8.2 simulated mobile Slow4G/4x CPU, npm-mirrored exact script/font inputs. Three storage-reset navigations per route, medians. Browser process is reused, not restarted per sample. Final before/after use the same seven-route order: Home, Services, Contact, then the four pilots. Original baseline values and thresholds are unchanged. The earlier after-harness incorrectly omitted that reference prefix; the corrected matched-order run and all four prior candidate failures are retained. Reference controls exhibit substantial run-to-run variance, so these are local navigation observations, not field/live-hosting improvement claims.

[Final raw medians and all samples](phase-25-after-metrics.json) | [Immutable before medians](phase-25-before-metrics.json) | [Machine-readable gate, budgets and source hashes](phase-25-pilot-gate.json)

Failed candidate records: [1](phase-25-failed-tier-1-metrics.json), [2](phase-25-failed-tier-2-metrics.json), [3](phase-25-failed-tier-3-metrics.json), [4](phase-25-failed-tier-4-metrics.json). No failures or limits were deleted/replaced to assert clearance.

## Design tokens and skeletons

- Existing reference families only: Outfit and Cormorant Garamond; actual custom font usage is asserted through Chromium platform-font APIs on all24 pilot JS-on/off viewport cases. Licensed subsets preserve source-family glyphs/metrics; Outfit retains its axis, Cormorant uses the700 role.
- Reference-derived1200px container,60px desktop/22px mobile gutters, left-aligned modular hierarchy and70ch CSS reading measure. Actual character count varies with proportional glyphs. Only3px/12px new component radii.
- Reference dark hero, then light reading surface, restrained sources/FAQ/table/callout/card patterns, at most one dark accent plus footer. No reference redesign, extra words, invented palette, icon filler, badges, reviews or stats.
- Exhaustive actual hex/RGB/type/spacing/button/container/breakpoint declarations and each reference skeleton/section sequence: [audit](phase-25-audit.md), [token inventory](phase-25-reference-tokens.json).
- Colour checker now normalizes existing reference RGB bases to their equivalent hex spelling; for example original rgba(13,27,62,.97) supplies#0d1b3e. This is a representation equivalence, not permission to invent colours. Shared CSS/includes and all existing PHP templates are checked for newly introduced colours.

## Team cards and content integrity

Exact supplied card counts: Jabir127, Zaheer130, Fawaz126 characters; spread4 passes the required<=6 check. Only six card biographies and the redundant founder-role paragraph inside the original About card are replaced/removed. Names, titles, image files, crop, alt text, card widths and full biographies outside cards remain protected. Full Person descriptions, both LLM files, existing About FAQs and Fawaz sameAs are unchanged. The actual baseline has no separate long-form About biography section; none was invented.

All43 route word/order/link/image/JSON-LD/status/source checks remain exact beyond the explicit team exception. All38 published canonical team records and discovery/held-page policies remain unchanged. Team section rectangles are exact at360/768/1280; equal-height cards do not move surrounding reference sections.

[Bio/footprint evidence](phase-25-team-footprints.json) | [Strict zero-tolerance reference pixels](phase-25-reference-pixels.json) | [Full suite evidence](phase-25-checks.json)

## Screenshots, accessibility and self-review

[Pilot review with before/after links and embeds](phase-25-pilot-review.md) contains all four pilots and four immutable references at360/768/1280. All48 required full-page PNGs are retained and losslessly recompressed. Final pilot after-images show the measured gradient-only tier, not the rejected still candidate.

Final checks cover24 pilot JS-on/off cases,126 FAQ expansions,12 axe A/AA runs,44px targets, keyboard focus, mobile menu/Escape, no horizontal overflow and actual custom fonts. Text/default/hover/focus palette contrast minimum5.11 against4.5. Body visibility and removal of the short font-pending state are explicitly asserted, including JS-off. No forms were submitted.

## Decisions, deviations and unresolved items

1. **Performance fallback:** all four pilots use a close reference-palette CSS gradient, no scene image/canvas/script fetch. The generated responsive stills remain available and below120KB each, but are not enabled on these pilots. The component fixture still tests ON/OFF; production mode tests assert zero scene fetches for normal/reduced-motion/Save-Data/hidden/resume. No new scene library, WebGL or parallax. Reference scenes remain unchanged; the single sitewide OFF constant still produces plain palette heroes.
2. **Font correction:** optional display was rejected because it painted fallback despite loaded-font status. Final same-family subsets are inline, use block display, and decode atomically before JS-on text visibility; a3s/error failsafe prevents a stranded blank body. JS-off never receives the pending class. No network font dependency is added. This is disclosed paint behavior, not a hidden metric workaround.
3. **Pilot chrome:** nav/footer/link hit boxes are enlarged to44px; the fixed pilot nav is opaque dark over light reading content. Reference chrome is untouched.
4. **Capture corrections:** seeded scene randomness/frozen clock/end-state animation, pre-paint no-motion, deterministic software/sRGB/dither controls and real viewport stitching are harness-only. The9 remaining Home1280 CTA-corner pixels are unresolved; no full pixel PASS or rollout readiness is claimed.
5. **Native limitations:** no native Apache/LiteSpeed/HTTP/MIME/CSP/contact-delivery/nonpublic-runtime-layout/backup-restore proof. Existing business/proof/held-page blockers remain. Internal reports/tooling/caches/Git must not be uploaded with public files. No live upload has occurred.

## Every changed Stage 1 file

[Complete file-by-file manifest](phase-25-stage-1-files.md), relative to the Phase24b checkpoint164d6de. Historical append-only logs remain intact. Task-specific commits/checkpoints are listed in [progress](phase-25-progress.md).

Pilot complete. Waiting for owner approval before rollout.
