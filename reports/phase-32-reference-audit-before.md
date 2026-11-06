# Phase32 reference resource audit before scene deferral

## Scope and limits

This local PHP-WASM/Chromium audit ran once per reference route at 360px and 1280px, using pinned local mirrors for external fonts and scripts. Resource bytes are response-body sizes, not compressed transfer measurements or live CDN data. The unthrottled browser LCP and long-task observations below are not comparable to the Lighthouse simulated Slow4G/4x CPU release budgets. The frozen-A Phase32 lab will provide the final budget comparison.

The useful pre-scene measure here is the sum of all successful response bodies other than Three.js, GSAP and ScrollTrigger. It represents the ordinary page payload before those deferred scene dependencies. The currently eager scene bundle is 717,632 bytes per reference page: Three.js 603,445 bytes, GSAP 71,520 bytes, and ScrollTrigger 42,667 bytes.

## Routes

| Route | Viewport | Total response bytes | Non-scene/pre-scene bytes | Image bytes | Unused JS source bytes | Unused CSS source bytes | Raw LCP ms | Long tasks |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `/` | 360 | 1,067,227 | 349,595 | 98,340 | 464,002 | 10,249 | 56 | 2 |
| `/` | 1280 | 1,081,259 | 363,627 | 98,340 | 460,960 | 10,859 | 36 | 2 |
| `/services` | 360 | 1,091,786 | 374,154 | 98,340 | 468,333 | 10,042 | 36 | 2 |
| `/services` | 1280 | 1,105,818 | 388,186 | 98,340 | 464,791 | 10,979 | 56 | 2 |
| `/about` | 360 | 1,045,989 | 328,357 | 98,340 | 460,272 | 11,636 | 380 | 2 |
| `/about` | 1280 | 1,045,989 | 328,357 | 98,340 | 458,022 | 12,179 | 460 | 2 |
| `/contact` | 360 | 1,034,492 | 316,860 | 98,340 | 468,876 | 8,195 | 56 | 1 |
| `/contact` | 1280 | 1,048,524 | 330,892 | 98,340 | 469,027 | 8,017 | 468 | 2 |

The sole image response in this fixture was `assets/images/ilmera.logo.png` at 98,340 bytes. It is displayed at approximately 38px in the header. The asset remains unchanged because image identity and page visuals are protected; review its current dimensions and any safe lossless optimization only if a separate pixel/hash check supports it.

Across these eight local cases, non-scene payload body bytes are below the 400,000-byte reference limit, with Services at 1280px closest to the boundary at 388,186 bytes. Removing or delaying the three scene dependencies avoids 717,632 response-body bytes before scene start. The full eager response totals are 1.03MB to 1.11MB. Native transfer compression and cache behavior remain unverified.

V8 block-coverage estimates show 458,022 to 469,027 uncompressed JavaScript source bytes unused on this single route path, mostly in Three.js and the GSAP packages. CSS coverage shows 8,017 to 12,179 uncompressed source bytes unused. These are one-path coverage estimates, not Lighthouse wasted-transfer bytes. Exact dependency/resource/coverage rows and raw long-task records are in `reports/phase-32-reference-audit-before.json`.

Raw local LCP is 36ms to 468ms. Observed long-task counts are one to two per case; the longest task is 662ms. The summed long-task TBT proxy is not Lighthouse TBT. Use the seven-sample simulated lab for final LCP/TBT/CLS comparisons and report any missed reference thresholds without qualification.

Contact `#miniHero` is not changed: Phase31's retained tails remain 138px at 360px and 233px at 768px, preserving the existing bottom scroll cue.
