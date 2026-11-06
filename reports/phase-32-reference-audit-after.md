# Phase32 reference scene deferral and post-change resource audit

## Method and limits

Home, Services, About and Contact were audited at 360px and 1280px through the local PHP-WASM adapter, pinned resource mirrors and Chromium 143. Response byte values are uncompressed response-body sizes, not native-host or compressed transfer measurements. The resource audit ran JavaScript/CSS coverage and browser observers for 3.2 seconds after load. Its LCP, CLS and summed long-task values are local diagnostics, not Lighthouse results and not the release-budget measurements. See the exact rows in `reports/phase-32-reference-audit-after.json` and the unmodified pre-change readings in `reports/phase-32-reference-audit-before.json`.

## Response-body bytes

| Route | Before total, 360 / 1280 | After total, 360 / 1280 | After non-scene body bytes, 360 / 1280 | Deferred scene libraries on eligible desktop |
|---|---:|---:|---:|---:|
| `/` | 1,067,227 / 1,081,259 | 351,606 / 1,083,270 | 351,606 / 365,638 | 717,632 |
| `/services` | 1,091,786 / 1,105,818 | 376,165 / 1,107,829 | 376,165 / 390,197 | 717,632 |
| `/about` | 1,045,989 / 1,045,989 | 330,327 / 1,047,959 | 330,327 / 330,327 | 717,632 |
| `/contact` | 1,034,492 / 1,048,524 | 318,871 / 1,050,535 | 318,871 / 332,903 | 717,632 |

The three scene-library bodies remain 603,445 bytes for Three.js, 71,520 for GSAP and 42,667 for ScrollTrigger. On 360px and other excluded cases, none of these libraries is requested. On eligible desktop, they are requested after load and idle, so the complete post-load response sum still contains the libraries. All eight post-change non-scene body totals are numerically under the 400,000-byte reference cap. Services at 1280px is closest, with 9,803 bytes of headroom. This is not proof of compressed transfer on the deployment host.

The inline policy and reserved-canvas CSS increased the HTML document body by 1,970 to 2,011 bytes compared with the pre-change render. No external stylesheet or render-blocking script was added. The three external scene script tags were removed from their eager markup; eligible pages add them dynamically only after `load` plus idle. No page image was changed or added. The existing logo response remains 98,340 bytes.

## Post-change local paint, layout and long-task observations

| Route | Raw LCP ms, 360 / 1280 | CLS sum, 360 / 1280 | Observed long-task TBT proxy ms, 360 / 1280 |
|---|---:|---:|---:|
| `/` | 76 / 36 | 0.0007 / 0 | 6 / 177 |
| `/services` | 40 / 728 | 0 / 0.0475 | 2 / 866 |
| `/about` | 352 / 464 | 0.0245 / 0.0167 | 5 / 2,963 |
| `/contact` | 36 / 36 | 0.0192 / 0.0019 | 0 / 3,902 |

These raw LCP values are 36ms to 728ms on this unthrottled local run. Observer CLS sums are under 0.1 in all eight cases, but are not Lighthouse CLS. The long-task proxy is the sum of each observed task's duration over 50ms; it is not Lighthouse TBT. The 866ms to 3,902ms desktop proxy readings are red flags, not budget passes. A separate one-sample browser check without coverage also observed approximately 1,827ms on About and 3,682ms on Contact during deferred Three.js scene startup. The heavy scene initialization may jeopardize the 600ms reference TBT cap and the unchanged TBT budget. The final seven-sample frozen-A Lighthouse lab must decide this; do not treat this resource audit as release certification.

## Safeguard verification

`reports/phase-32-reference-scene-smoke.json` contains 36 browser cases across all four routes. Twenty-eight excluded cases made no Three.js, GSAP or ScrollTrigger requests: 360px mobile, 768px tablet, 1280px coarse pointer, reduced motion, Save-Data, 2G and downlink below 1.1 Mbps. The canvas retains viewport CSS geometry, and the static CSS background layers remain visible. All eight eligible fine-pointer desktop runs, four using idle callbacks and four using the timer fallback, initialized the existing WebGL scene exactly once with no page errors. First eligible script insertion occurred 3 to 476ms after `load`; when `requestIdleCallback` was disabled, the 1,500ms timer fallback began at 1,501ms on all four routes. The PHP-WASM policy fixtures also passed all four reference routes plus the four still templates with `ILMERA_SCENES_ENABLED=false`.

Contact `#miniHero` remains unchanged. Its retained 138px mobile and 233px tablet scroll-cue tails are documented in the Phase31 audit. No reference wording, heading, link, image, FAQ, schema, canonical, status or desktop layout was intentionally changed.
