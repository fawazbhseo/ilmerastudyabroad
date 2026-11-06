# Phase32 Blog-index desktop A/B

## Scope and method

A supplemental desktop-only 14-sample Lighthouse A/B was run for `/blog/` against the frozen run02 fixture. Each arm has seven fresh Chromium processes, serially interleaved A/B and B/A. Chromium 143.0.7499.0, Playwright 1.58.2 and Lighthouse 12.8.2. Lighthouse's pinned `desktop-config` was used with desktopDense4G throttling and desktop screen emulation. Requests used the local fixture/assets and pinned local resource mirrors. This is local desktop-simulated evidence, not field or production-host proof.

| Metric | A median / IQR | B median / IQR | B minus A / ratio |
|---|---:|---:|---:|
| LCP | 590.63ms / 129.11ms | 590.81ms / 0.14ms | +0.18ms / 1.0003 |
| TBT | 0ms / 0ms | 0ms / 0ms | 0ms |
| CLS | 0 / 0 | 0 / 0 | 0 |
| Total transfer | 284,903 bytes / 0 | 287,586 bytes / 0 | +2,683 bytes |
| Requests | 8 / 0 | 8 / 0 | 0 |

The desktop Blog TBT delta is within the unchanged +50ms allowance in this local test. B has no new render-blocking URL. Both arms made one request for the 1440 WebP still per sample, 37,226 resource bytes and 37,403 reported transfer bytes, HTTP 200. In B, the still remains a post-load decorative asset and the LCP candidate is text (`p.sub`); A's LCP candidate is the `section.blog-hero`. B does not request a larger still than the current 40KB desktop file budget.

## Limits

This result covers only Blog index desktop behavior. It does not clear the three mobile run02 LCP-ratio failures, the reference-page desktop scene TBT issue, the local 400KB pre-scene body cap on other pages, or any live-host behavior. Raw samples and request records are in `phase-32-blog-desktop-ab-results.json` (SHA-256 `0b579dbbf4582b2f3a8158b9462f087decd4beb7bf134fc4f8aa14ef6a193635`). `performance_release_certified` remains false.
