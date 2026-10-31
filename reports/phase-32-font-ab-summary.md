# Phase32 local font-chain diagnosis and A/B

## Scope

This diagnostic covers the place, article and blog-index templates on the local PHP-WASM adapter. It is not live-host or field performance evidence. A separate 42-sample candidate experiment compared the current font policy (A) with a narrowly transformed page (B). Each arm had seven serial samples per route, one fresh Chromium 143 process per sample, and alternating A/B order. Lighthouse used simulated Slow4G and 4x CPU. No sample was retried.

The B document changed only seven `font-display:block` rules to `font-display:swap` and removed the `.p25-font-pending body.p25{visibility:hidden;}` rule. Preloads, font files, text, styles other than that gate, images, scripts and route content were unchanged. Transform hashes and every raw sample are in `reports/phase-32-font-ab-results.json`.

## Existing request chain

The page builds one inline visual-system stylesheet, with no separate blocking visual-system CSS request. There are seven local webfont faces, all declared `font-display:block`, plus two local metric fallback faces. The document head preloads Outfit 300 and Cormorant Garamond 700, matching the primary body and heading weights. The font-gate script calls `document.fonts.load` for those same two faces and hides the page body until `document.fonts.ready` or its 3,000ms fail-open timer.

| Template | Viewport | Font responses | Body bytes | Requested weights |
|---|---:|---:|---:|---|
| Place | 360px | 4 | 72,784 | Outfit 300/500; Cormorant 400/700 |
| Place | 1280px | 5 | 86,816 | Outfit 300/400/500; Cormorant 400/700 |
| Article | 360px | 4 | 72,784 | Outfit 300/500; Cormorant 400/700 |
| Article | 1280px | 5 | 86,816 | Outfit 300/400/500; Cormorant 400/700 |
| Blog | 360px | 4 | 72,784 | Outfit 300/500; Cormorant 400/700 |
| Blog | 1280px | 5 | 86,816 | Outfit 300/400/500; Cormorant 400/700 |

The two preloads account for 36,348 response bytes. Other requested weights are not preloaded. Browser request bodies were measured from local responses; Resource Timing transferSize was not treated as byte evidence.

## Candidate comparison

| Route | A LCP median / IQR (ms) | B LCP median / IQR (ms) | B/A | CLS median A / B | TBT median A / B (ms) | Decision |
|---|---:|---:|---:|---:|---:|---|
| `/study-abroad-counselling-mysuru` | 1,727.26 / 314.65 | 2,355.79 / 629.17 | 1.3639 | 0 / 0 | 0 / 0 | Keep A |
| `/blog/how-to-choose-study-abroad-consultant-karnataka` | 1,727.07 / 0.41 | 1,726.62 / 0.37 | 0.9997 | 0 / 0 | 0 / 0 | Keep A |
| `/blog/` | 1,727.10 / 0.48 | 2,355.77 / 628.05 | 1.3640 | 0 / 0 | 0 / 0 | Keep A |

B did not produce a coherent LCP improvement across all three routes. Place and blog had a substantially higher B median and broad IQR; the article's 0.45ms median difference is negligible. CLS medians were unchanged at zero. The experiment does not authorize the change.

## Decision

**No font source change.** Keep the existing self-hosted font faces, preloads, `font-display:block`, font gate and inline stylesheet. This is the conservative result required by the owner rule: adopt a font change only if A/B demonstrates LCP improvement without worse CLS. The high IQRs on two routes limit interpretation further. The complete diagnostic and raw evidence are preserved in `reports/phase-32-font-audit.json` and `reports/phase-32-font-ab-results.json`.
