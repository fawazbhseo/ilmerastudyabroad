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

Task 3 commit: `4844f3f`, pushed with PR #1 checkpoint.

## Task 4: static hero tiers and single global switch

Generated text-free mobile/desktop WebP stills directly from the unchanged Home scene (720x900 and 1440x900, each <120,000 bytes). Capture-only preserveDrawingBuffer/seed/frozen first frame do not alter the website's reference scene. Sizes and hashes: phase-25-hero-assets.json. No stock imagery, new scene library, WebGL runtime or parallax added to pilots.

Decorative aria-hidden canvases draw the responsive still after two content frames plus idle scheduling. Canvas is not an LCP image candidate. Position is absolute with no content size dependency. No recurring RAF/animation exists; reduced-motion remains static. Save-Data makes no image request; hidden tabs defer scheduling/drawing and resume on visibility. JS-off/error fallback is the same reference-palette gradient. One `ILMERA_SCENES_ENABLED` constant turns off reference WebGL loading/visible overlays and pilot stills sitewide, yielding a plain palette hero. Default true leaves reference output unchanged. Article role has shorter padding and a quieter static still; future legal/404 roles are not applied in Stage 1.

Pilot enable switch remains OFF until task 5. Four opt-in/exclusion tests plus explicit scene ON/OFF tests PASS. Full lint/unit/render/browser/discovery/strict suite PASS in 536.86s. The two stills are 24,574 and 37,226 bytes. Default-off pilot application still produces no pilot render changes.

Task 4 commit: `5453480`, pushed with PR #1 checkpoint.

## Task 5: four pilots only and visual self-review

Enabled the existing hardcoded four-route allowlist only. The pure visual pass now runs after existing content overlays, so long introductions move into the first light reading container without changing a single word, heading order, link/image attribute or JSON-LD value. Global scene policy stays before early returns so its explicit OFF switch also covers utilities/held routes. No destination/place/article source or publication journal was edited.

Self-review corrections: dark opaque fixed pilot nav remains legible while scrolling over light sections, inline token-based gold links become reference navy on light, all interactive hit areas are at least44px, table wrapping stays inside the viewport, FAQ/keyboard focus states use high-contrast palette pairs. No static text/card hover movement. Footer/nav keep reference content, fonts/palette/grid; their pilot hit areas are deliberately larger for accessibility. Gradient fallback and faint static scene keep gold labels >=4.5 even over a hypothetical white scene pixel (worst-case5.11).

Initial QA exposed narrow footer/nav links and a test incorrectly checking pointer-mode focus-visible. Widened real hit areas; keyboard-mode focus now explicitly tested. Final pilot QA:24 JS-on/off cases at360/768/1280,126 FAQ expansions,12 axe WCAG A/AA runs with zero violations, zero targets below44px and tested menu Escape/focus. Save-Data zero still requests; hidden state zero before resume/one after; reduced motion/static normal each one responsive still. Hidden branch is document.hidden emulation, not OS throttling evidence.

Reference footprint correction: shorter/equal team cards initially moved following sections. Added exact team-only section minima and a Home768 bottom-padding adjustment, preserving original team section bounds at all three requested viewports. Card widths/photos/name/title styles and grid gaps are unchanged; all six fixed team rectangles equal baseline. This resolves the earlier flagged downstream-flow concern at the approval screenshot sizes. Source guard permits only exact generated team-only CSS, not arbitrary reference styling.

Capture correction: complete all finite GSAP/custom reveal classes and use original immutable baseline HTML replay for before images; allow only the static pilot loader's two RAFs while reference motion stays frozen. Original before captures remain in earlier task commits; final before/after use an identical corrected capture technique. No baseline performance values or source snapshot bytes are rebased. Full screenshots, strict outside-team pixel checks and full suite outcome below.

Task 6 pending. Stage 2 not started.

### Task 5 late self-review corrections

Raw fresh-context reference screenshots initially differed by tiny compositor rounding values (mostly one colour-channel level), even for byte-identical Services/Contact. A same-source repeat calibration demonstrated the harness issue. Use deterministic software compositing, sRGB and capture-only disabled WebGL dithering; do not add a pixel tolerance or hide outside-team differences. Re-shoot both sides with identical flags, then rerun the zero-tolerance reference test. No website scene source changes.

Font-bound inspection also caught a real visual issue: font-display optional could report fonts loaded while still rendering system fallback. Replaced that approach with small licensed same-family Unicode subsets embedded in the existing inline stylesheet. Outfit keeps its original variable weights; Cormorant is instantiated at700, its only pilot heading/brand weight, with original glyph metrics. Coverage is derived from all four immutable pilot texts; absent original emoji/non-Latin glyphs retain normal system fallback. No third design family or blocking request. Chromium platform-font checks now require actual custom Cormorant/Outfit glyphs in all24 pilot JS-on/off cases. Re-shoot pilots after this correction. Font subset generation is deterministic and preserves original OFL notices. Full suite PASS707.31s plus final font/syntax/all43-route strict and24-case font-bound checks; the final task6 run will repeat the full suite on the final gate state.

### Task 5 checkpoint result

Full suite PASS707.31s, followed by corrected-font all24-case checks, all43-route strict comparison, deterministic font regeneration check and final screenshot self-review. Forty-eight before/after images are provided with links/embeds in phase-25-pilot-review.md. Exact reference pixels:11/12 PASS; Home1280 has9 one-level navigation-CTA corner pixels remaining. That strict criterion is NOT waived and is NOT reported as passed; retain it as a pilot-gate blocker for owner review. No source/style change outside the authorized team area explains an intentional reference redesign. No Stage2 rollout.

## Task 6: final pilot gate (no rollout)

Retained four failed candidate measurement files. Dropped all four pilot scenes to a reference-palette gradient and zero scene fetch/script. Font subsets remain inline; block display plus atomic first-text paint removes partial-font shifts, with3s/error failsafe and visible JS-off. Local font HTTP preloads were tried and discarded; no extra critical font request remains.

Corrected measurement order to match the unchanged baseline: Home/Services/Contact reference prefix, then the four pilots, three storage-reset navigations each, same persistent browser process. Original budgets/medians are not weakened. Final pilot medians all PASS: Germany LCP1175.705ms/CLS0/TBT2ms; Mysuru1192.811/0/0; article1173.507/0/0; blog1158.922/0/0. Added transfer:-41093/-41140/+49290/-26981B, all<150000B. No new render-blocking resource. Reference controls vary substantially between local runs; no field/live-hosting improvement claims.

First task6 full run stopped at a colour-check extraction bug: original reference rgba(13,27,62,.97) had not been normalized to equivalent#0d1b3e. Fixed the reference-token extractor, not application colours or palette restrictions; same actual immutable RGB base only. Final full suite is being repeated with strengthened no-blank-body/zero-scene checks. All48 screenshots retained; final12 pilot after-images reshot/losslessly recompressed. Strict reference raster remains11/12 PASS,9 one-level Home1280 CTA-corner pixels unresolved. Gate stays BLOCKED; no Stage2.

Task6 final full syntax/unit/render/browser/discovery/strict suite PASS in581.55s (35 check groups), including strengthened actual-font/no-blank-body/zero-scene assertions. All24 pilot cases,126 FAQ expansions,12 axe runs pass. Final gate.py --require-pass intentionally exits1: performance/colour/technical PASS, strict reference raster FAIL on the9 Home1280 corner pixels. Baseline budgets and zero pixel tolerance remain unchanged. No Stage2, merge or deployment.
