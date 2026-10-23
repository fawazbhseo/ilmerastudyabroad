# Phase 25 progress

Stage 1 tasks 1-6 only. Session branch `arena/48320ee5-ilmerastudyabroad`; PR #1 remains open. No merge, deployment or Stage 2 rollout is authorized.

## Resume safety

Fetched the session branch and compared every tracked remote blob to the restored disk files. All matched Phase 24b HEAD `164d6de41159385e151ecefec54763eab59141a5`. Only then aligned the stale local pointer/index using a mixed reset; no worktree content was discarded. Fresh runtime dependencies and evidence are outside the checkout. PHP WASM is not native hosting verification.

## Task 1: report-only audit

Reference source and all 43 route renders captured before public edits. Audit, exhaustive tokens, baseline team dimensions, 24 baseline screenshots and local Lighthouse samples are provided. Owner card counts: Jabir 127, Zaheer 130, Fawaz 126; spread 4 (PASS <=6). References are not uniformly light in the actual source; preserve them and apply the requested light reading-area rule only to pilot opt-ins. Full lint/unit/render/browser/discovery/strict suite PASS in 662.30s: 43 route renders, 258 browser cases, original portrait integrity and all held/status/schema/FAQ guards retained. Corrected the capture harness before checkpoint to complete finite GSAP reveals and stitch real viewport rasters, avoiding a SwiftShader >8192px full-page repeat artifact. PNGs recompressed losslessly; no site changes.

Task 1 commit: `cee3bf4`, pushed with PR #1 checkpoint.

## Task 2: isolated shared design system

Added a pure visual overlay, shared inline stylesheet and four-route allowlist. Default opt-in remains OFF until task 5; all 43 renders must still be byte-identical. New components reuse reference palette, serif/sans families, 1200px grid and 60/22px gutters. Light reading sections, restrained cards/FAQ/tables/forms, sources/callouts, breadcrumbs, CTA/header/footer and team primitives are provided. The pilot stylesheet has only 3px and 12px component radii; it does not impose those radii on immutable reference cards/photos.

Same existing font families are locally bundled with OFL notices: Fontsource variable Outfit 5.2.8 and Cormorant Garamond 5.2.6. Inline @font-face with optional display avoids adding a blocking stylesheet and prevents late font-swap layout shifts. Only opted-in pilots remove the old external font CSS. The article's missing font load is addressed without changing its protected source/hash. No reference request changes.

Verification harness now finishes finite CSS transitions programmatically before asserting final geometry, rather than waiting wall-clock time for each of 1,278 FAQ interactions. Same 258 JS-on/off cases, assertions, photo loads and FAQ interactions are retained; historical runner is unchanged. This is a test-speed change, not a website animation change. Full-check suite PASS in 556.79s, including exact 43-route byte parity while opt-in is OFF, palette/radii/font guards, four opt-in/eleven exclusion tests and all inherited business/discovery/browser checks.

Task 2 commit: `0ed812e`, pushed with PR #1 checkpoint.

## Task 3: exact owner card bios

Replaced only Home/About card biographies with the three exact supplied texts. Character lengths 127/130/126, spread 4 PASS. Photos, widths/crops, names, titles, alt text and existing styling are intact. Team-only grid auto rows make cards equal-height, including one-column mobile grids. No other reference styles change.

Closer source inspection correction to Task 1: About's Jabir card contained both the full canonical founder description and a separate duplicate role paragraph. The new exact owner card replaces that card biography and removes its redundant old role paragraph; the identical existing About FAQ answer is untouched. There is no separate long-form biography section. Jabir's full canonical Person description and both LLM files are byte-identical; Fawaz/Zaheer full About FAQ answers remain intact. The Phase24b scope helper now takes an explicit short-card flag with a strict expected visible-founder count of zero in Phase25, retaining its historical default of one. All other schema, FAQ and business assertions remain active.

Short texts are allowed only in the six actual card paragraphs. Regression tests reject shortened schema/FAQ/prose/other-route usage and extra claims; the full-bio training-institute exception is unchanged. Full lint/unit/render/browser/discovery/strict suite PASS in 542.04s. Eight bio-policy regressions pass; all 43 renders preserve exact text/order except the explicit card replacement/removal, identical links/images/JSON-LD and protected source/status data. All 38 published canonical team records and both LLM files remain unchanged.

Tasks 4-6 pending. Stage 2 not started.
