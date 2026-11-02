# Phase32a font-chain diagnosis

Date: 2026-11-02

## Scope and source continuity

This covers the place, article and Blog-index templates. The palette fallback commit changes only `ILMERA_VISUAL_PLAIN_HERO_TEMPLATES`; it does not change CSS, font files, font declarations, preloads or the font gate. The freshly pushed six-route A/B raw capture also confirms the same four local font URLs were requested in each A and B sample on Mysuru, the choosing-consultant article and Blog index, with HTTP 200 responses. The raw Lighthouse resource entries contain no per-resource start/end times, so the detailed Resource Timing values below are explicitly reused from the already-committed, matching-source diagnostic `reports/phase-32-font-audit.json`, not presented as new throttled timing samples.

## Current chain

- `includes/visual-system.php` emits one inline `<style id="ilmera-visual-system">`. The new visual system adds no external CSS request. The earlier six-case Playwright audit recorded zero stylesheet responses for Mysuru, the article and Blog index at 360px and 1280px. The Lighthouse raw run reported no render-blocking resource URLs on any of the six routes.
- Seven self-hosted WOFF2 faces are declared in `assets/css/visual-system.css`: Outfit 300, 400, 500, 600 and 700; Cormorant Garamond 400 and 700. All seven use `font-display:block`. Two local metric fallback faces use Arial and Times New Roman; these do not fetch a font file.
- The document preloads exactly Outfit 300 and Cormorant Garamond 700 as same-origin WOFF2 with `crossorigin="anonymous"`. They match the body and main heading weights. The font gate calls `document.fonts.load` for those same faces, adds `p25-font-pending`, and keeps `body.p25` hidden until `document.fonts.ready` or the 3,000ms fail-open timer. This is not an external CSS network block, but it can delay visible text and the text LCP while fonts resolve.
- The Google Fonts stylesheet and preconnect links are removed by the presentation layer. The sampled place/article/blog pages had no Google Fonts requests. Local font response status was 200.
- At 360px, the audit requested Outfit 300/500 and Cormorant Garamond 400/700. At 1280px, it also requested Outfit 400. Outfit 600/700 were declared but not requested in these cases. Two of the four/five requested font files are not preloaded: Outfit 500 and Cormorant Garamond 400, plus Outfit 400 at 1280px.

## Response weights and local timing observations

The following are response-body bytes and `PerformanceResourceTiming.responseEnd` values from the prior matching-source local diagnostic. They are not Slow4G timings or field data. All six rows recorded `fontPending=false` at the end of capture.

| Template | Viewport | Requested faces | Font response bytes | Max responseEnd among font responses | loadEventEnd |
|---|---:|---|---:|---:|---:|
| Place | 360px | Outfit 300/500; Cormorant 400/700 | 72,784 | 26.174 ms | 62.5 ms |
| Place | 1280px | Outfit 300/400/500; Cormorant 400/700 | 86,816 | 7.817 ms | 43.1 ms |
| Article | 360px | Outfit 300/500; Cormorant 400/700 | 72,784 | 12.535 ms | 51.2 ms |
| Article | 1280px | Outfit 300/400/500; Cormorant 400/700 | 86,816 | 9.246 ms | 52.1 ms |
| Blog index | 360px | Outfit 300/500; Cormorant 400/700 | 72,784 | 6.482 ms | 39.2 ms |
| Blog index | 1280px | Outfit 300/400/500; Cormorant 400/700 | 86,816 | 8.170 ms | 52.9 ms |

Preloaded response bytes total 36,348. For comparison, the fresh six-route Lighthouse raw capture records all four mobile font resources for Mysuru, article and Blog index in each arm, seven samples per arm, HTTP 200. Its local fixture transferSize values were 14,133 bytes (Outfit 300), 22,569 (Cormorant 700), 23,085 (Cormorant 400) and 13,705 (Outfit 500); those values include the simulated fixture response accounting and are not source file sizes.

## Diagnosis and next test

There is no external blocking stylesheet or Google Fonts dependency. The material risk is the combination of `font-display:block` and the body-visibility gate, not a slow third-party font chain. The existing Phase32 candidate changed the seven webfont faces to `font-display:swap` and removed the body-visibility rule while preserving families, files, weights, preloads and content. That earlier result was not adopted because it did not show a coherent gain across its routes.

A fresh interleaved A/B on the current post-fallback Mysuru and article pages is the next step. It will test only that same bounded candidate, with seven samples per arm per route and a fresh Chromium process per sample. No font change is authorized unless candidate LCP improves on both measured routes and CLS is no worse. Otherwise retain all existing font files, preloads, `font-display:block` declarations and the current gate, and report the non-change.
