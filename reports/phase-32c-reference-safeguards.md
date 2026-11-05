# Phase32c Task 2: reference scene safeguards

## Disposition

Task 2 is complete as an evidence and classification checkpoint. The 60-case matrix has 49 literal geometry passes at the requested 0.1 CSS-pixel tolerance. The other 11 cases are all Contact and remain recorded as raw geometry differences. Same-source A/A controls reproduce the Contact select-height variation, so those differences are classified as **MEASUREMENT ARTEFACT**. This classification does not convert the 11 raw geometry failures into passes. No reference-page source change was made for them.

## Method and scope

- Compared Phase31b source `796879d` with the runtime candidate source `091442f` on Home, Services, About and Contact, at 360, 768 and 1280 CSS pixels, in scene, still, reduced-motion, disabled-scene-switch and JavaScript-off states. The disabled-switch cases use isolated PHP-WASM adapter copies with the switch set off.
- Ran 60 baseline/current pairs, or 120 source renders. Each pair used one fresh Chromium browser/context and a shared page navigated baseline then current. Visible DOM geometry excludes the scene layers and pointer-following cursor overlay. The tolerance remained 0.1 CSS pixels.
- Scrolled by wheel in 55%-viewport increments with 220ms dwell per step. The harness recorded each scroll position, checked full-page reach after fonts settled, waited three seconds at the bottom, and recorded reveal targets still pending. No End-key jump was used.
- Exact parity checks cover rendered text, headings, links, image sets, picture sources, JSON-LD and canonicals. The same-source A/A controls used the same current adapter/source twice. The raw matrix and A/A evidence are `reports/phase-32c-reference-safeguards.json` and `reports/phase-32c-reference-safeguards-aa.json`. DOM text is represented by parity booleans and hashes; geometry strings are hashed to keep the evidence focused on layout.

## Matrix results

| Reference route | Literal 0.1px passes | Raw geometry differences | Disposition |
| --- | ---: | ---: | --- |
| Home | 15/15 | 0 | PASS |
| Services | 15/15 | 0 | PASS |
| About | 15/15 | 0 | PASS |
| Contact | 4/15 | 11 | Raw differences retained; classified MEASUREMENT ARTEFACT by A/A evidence |

Across all 60 cases:

- Rendered text, heading order/text, links, images, picture sources, JSON-LD and canonicals were exact in 60/60.
- All 120 baseline/current renders reached the page end. All JavaScript-enabled reveal targets were settled, with zero cases having pending reveals. There were zero runtime errors and zero incomplete-scroll cases.
- Header and About team landmark geometry matched in 60/60. Team-card boxes and text matched in 60/60. Footer geometry matched in 49/60; in the 11 Contact cases it starts 4px lower after the form controls.
- The four previously authorized contrast restorations are the recorded color-only style differences: Home note `#888888` to the existing `--grey-dark`, About FAQ heading to the existing light heading color, and the About team and Kodagu labels to the existing navy. These changes do not alter text, links, imagery or geometry.
- Scene expectations matched in all 60 cases. The Phase31b source created WebGL in 24 cases, including phone-width and reduced-motion states. The current source created WebGL only in the four 1280px normal scene cases. No hero-still node or still-image request appeared on any of the four reference pages in any state.

### Contact geometry detail

Every one of the 11 Contact cases has the two native select controls at 46px in the Phase31b render and 48px in the current render. Each select differs by 2px and the resulting accumulated page/footer displacement is 4px. Maximum absolute element delta is 4px. The reported affected-box counts are 317 at 360px for still and disabled-switch states, 326 for JavaScript-off; the same counts apply at 768px. At 1280px the counts are 265 for scene, still and reduced-motion, 293 for disabled-switch, and 274 for JavaScript-off. Text and semantic content remain exact in every case.

The current/current A/A controls show this is not a stable source delta. Contact 360px disabled-switch A/A has the same 317 affected boxes, with the direction reversed between renders. Contact 1280px disabled-switch A/A has 265 affected boxes, also with the direction reversed. Contact 768px disabled-switch A/A and JavaScript-off A/A at all three widths are exact. About and Services A/A at 360px disabled-switch are exact; the current render settles all 14 About and 41 Services reveal targets. No select CSS change is authorized or justified by these results.

## Phase32 source changes reaching these pages

- The shared output filter now replaces remote reference font CSS with local WOFF2 faces and preloads on `/`, `/services`, `/about` and `/contact`. The injected local-font style was observed in all 60 current renders.
- The shared reference-scene policy defers the existing scene libraries until after load and idle, and prevents scene startup for narrow/coarse-pointer, reduced-motion, slow-connection and disabled-switch states. Current WebGL starts were limited to the eligible 1280px normal scene cases. Static page content and fallback layers remain present.
- The four contrast restorations listed above were also present in the current reference renders and are expected Task 1 styling changes.

The earlier hero-still feature remains scoped to destination, place, article and blog-index heroes. It was not applied to Home, Services, About or Contact: there were zero still nodes and zero still requests in all 60 reference-page cases. Under the Phase32 reference-resource guardrails, no new reference still/image was added, the existing logo was not optimized, and Contact `#miniHero` was not altered. The current Phase32c Task 3 three-arm hero-still A/B has not started, and no Task 3 still decision or implementation has been applied.

## Next step

Start Phase32c Task 3 on Mysuru and the selected article. Use frozen A at `7d1bb9e`, current B-still and current B-plain, nine fresh-browser samples per arm per route with alternating order, plus the requested A/A repeat. Commit raw samples before analysis. Do not start the final full suite until Tasks 1-3 are complete.
