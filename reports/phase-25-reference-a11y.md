# Reference accessibility: report only

No changes applied to Home, Services, About or Contact. Their source remains byte-exact to Stage1. This report retains all24 historical contrast finding groups, including every affected node, and investigates the five recorded JS-on layout-overflow cases. Rebuilt-page accessibility is tested separately.

## Contrast method

Foreground/background and observed ratio are taken verbatim from axe failure summaries in the committed Stage2 evidence. The target here is4.5:1, including larger text. Suggested fixes change one foreground declaration to the nearest passing existing-reference palette colour by squared sRGB distance, holding the measured background fixed. This is a minimal single-property palette suggestion, not a proposed palette redesign or an applied fix. Parent opacity/compositing must be remeasured if any suggestion is later approved.

### Finding01: `/`, 360px, JSon

| Selector | Foreground | Background | Observed / required | Smallest palette-only suggestion |
|---|---|---|---|---|
| `#coorg-kodagu > .container > div:nth-child(1) > .sec-label` | `#c9a84c` | `#e9edf8` | 1.95 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `div:nth-child(2) > p:nth-child(3)` | `#8a98b8` | `#e9edf8` | 2.46 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `.why-sec:nth-child(6) > .container > .why-hdr > .sec-label` | `#c9a84c` | `#e9edf8` | 1.95 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `.s-wrap:nth-child(8) > .container > div:nth-child(1) > .sec-label` | `#c9a84c` | `#e9edf8` | 1.95 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#faq > .container > .why-hdr > .sec-label` | `#c9a84c` | `#e9edf8` | 1.95 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `.source-review > p > a:nth-child(1)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `p > a:nth-child(2)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `p > a:nth-child(3)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |

### Finding02: `/services`, 360px, JSon

| Selector | Foreground | Background | Observed / required | Smallest palette-only suggestion |
|---|---|---|---|---|
| `#germany > .svc-num[aria-hidden="true"]` | `#17202b` | `#0a1628` | 1.10 /4.5 | foreground `#888888`, predicted 5.11:1 |
| `#italy > .svc-num[aria-hidden="true"]` | `#d9dee9` | `#e9edf8` | 1.15 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#italy > .rev.svc-grid > .on-light.svc-text.anim-fade-right > h2 > em` | `#c9a94e` | `#e9edf8` | 1.93 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `.highlight-box.on-light:nth-child(6) > .highlight-title` | `#c9a94e` | `#dfe3ee` | 1.76 /4.5 | foreground `#4a5568`, predicted 5.86:1 |
| `.highlight-box.on-light:nth-child(7) > .highlight-title` | `#c9a94e` | `#dfe3ee` | 1.76 /4.5 | foreground `#4a5568`, predicted 5.86:1 |
| `#italy > .rev.svc-grid > .on-light.svc-text.anim-fade-right > .svc-cta[href$="contact"]` | `#c9a94e` | `#e9edf8` | 1.93 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#italy > .rev.svc-grid > .on-light.svc-text.anim-fade-right > .related-guides[aria-label="Planning guides"] > h3` | `#ffffff` | `#e9edf8` | 1.17 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#italy > .rev.svc-grid > .on-light.svc-text.anim-fade-right > .related-guides[aria-label="Planning guides"] > ul > li:nth-child(1) > a` | `#ffffff` | `#e9edf8` | 1.17 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#italy > .rev.svc-grid > .on-light.svc-text.anim-fade-right > .related-guides[aria-label="Planning guides"] > ul > li:nth-child(2) > a` | `#ffffff` | `#e9edf8` | 1.17 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#uk > .svc-num[aria-hidden="true"]` | `#121113` | `#04060f` | 1.07 /4.5 | foreground `#888888`, predicted 5.71:1 |
| `#czech-republic > .svc-num[aria-hidden="true"]` | `#d9dee9` | `#e9edf8` | 1.15 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#czech-republic > .rev.svc-grid > .on-light.svc-text.anim-fade-right > h2 > em` | `#c9a94e` | `#e9edf8` | 1.93 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#czech-republic > .rev.svc-grid > .on-light.svc-text.anim-fade-right > .highlight-box.on-light > .highlight-title` | `#c9a94e` | `#dfe3ee` | 1.76 /4.5 | foreground `#4a5568`, predicted 5.86:1 |
| `#czech-republic > .rev.svc-grid > .on-light.svc-text.anim-fade-right > .svc-cta[href$="contact"]` | `#c9a94e` | `#e9edf8` | 1.93 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#czech-republic > .rev.svc-grid > .on-light.svc-text.anim-fade-right > .related-guides[aria-label="Planning guides"] > h3` | `#ffffff` | `#e9edf8` | 1.17 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#czech-republic > .rev.svc-grid > .on-light.svc-text.anim-fade-right > .related-guides[aria-label="Planning guides"] > ul > li:nth-child(1) > a` | `#ffffff` | `#e9edf8` | 1.17 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#czech-republic > .rev.svc-grid > .on-light.svc-text.anim-fade-right > .related-guides[aria-label="Planning guides"] > ul > li:nth-child(2) > a` | `#ffffff` | `#e9edf8` | 1.17 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#lithuania > .svc-num[aria-hidden="true"]` | `#17202b` | `#0a1628` | 1.10 /4.5 | foreground `#888888`, predicted 5.11:1 |
| `#latvia > .svc-num[aria-hidden="true"]` | `#d9dee9` | `#e9edf8` | 1.15 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#latvia > .rev.svc-grid > .on-light.svc-text.anim-fade-right > h2 > em` | `#c9a94e` | `#e9edf8` | 1.93 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#latvia > .rev.svc-grid > .on-light.svc-text.anim-fade-right > .svc-cta[href$="contact"]` | `#c9a94e` | `#e9edf8` | 1.93 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#latvia > .rev.svc-grid > .on-light.svc-text.anim-fade-right > .related-guides[aria-label="Planning guides"] > h3` | `#ffffff` | `#e9edf8` | 1.17 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#latvia > .rev.svc-grid > .on-light.svc-text.anim-fade-right > .related-guides[aria-label="Planning guides"] > ul > li:nth-child(1) > a` | `#ffffff` | `#e9edf8` | 1.17 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#latvia > .rev.svc-grid > .on-light.svc-text.anim-fade-right > .related-guides[aria-label="Planning guides"] > ul > li:nth-child(2) > a` | `#ffffff` | `#e9edf8` | 1.17 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#slovakia > .svc-num[aria-hidden="true"]` | `#121113` | `#04060f` | 1.07 /4.5 | foreground `#888888`, predicted 5.71:1 |
| `#russia > .svc-num[aria-hidden="true"]` | `#17202b` | `#0a1628` | 1.10 /4.5 | foreground `#888888`, predicted 5.11:1 |
| `#gcc > .svc-num[aria-hidden="true"]` | `#d9dee9` | `#e9edf8` | 1.15 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#gcc > .rev.svc-grid > .on-light.svc-text.anim-fade-right > h2 > em` | `#c9a94e` | `#e9edf8` | 1.93 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#gcc > .rev.svc-grid > .on-light.svc-text.anim-fade-right > .svc-cta[href$="contact"]` | `#c9a94e` | `#e9edf8` | 1.93 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#gcc > .rev.svc-grid > .on-light.svc-text.anim-fade-right > .related-guides[aria-label="Planning guides"] > h3` | `#ffffff` | `#e9edf8` | 1.17 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#gcc > .rev.svc-grid > .on-light.svc-text.anim-fade-right > .related-guides[aria-label="Planning guides"] > ul > li:nth-child(1) > a` | `#ffffff` | `#e9edf8` | 1.17 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#gcc > .rev.svc-grid > .on-light.svc-text.anim-fade-right > .related-guides[aria-label="Planning guides"] > ul > li:nth-child(2) > a` | `#ffffff` | `#e9edf8` | 1.17 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `p:nth-child(5) > a[href$="study-in-germany"]` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `p:nth-child(5) > a[href$="study-in-italy"]` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `p:nth-child(5) > a[href$="study-in-uk"]` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `p:nth-child(5) > a[href$="study-in-lithuania"]` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `p:nth-child(5) > a[href$="study-in-gcc"]` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `p:nth-child(5) > a:nth-child(6)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `p:nth-child(5) > a:nth-child(7)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `p:nth-child(5) > a:nth-child(8)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `.source-review > p > a:nth-child(1)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `.source-review > p > a:nth-child(2)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `.source-review > p > a:nth-child(3)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `a[href$="about#team"]` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |

### Finding03: `/about`, 360px, JSon

| Selector | Foreground | Background | Observed / required | Smallest palette-only suggestion |
|---|---|---|---|---|
| `.container:nth-child(8) > p > a[href$="services"]` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `.source-review > p > a:nth-child(1)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `.source-review > p > a:nth-child(2)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `.source-review > p > a:nth-child(3)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `.team-disclosure > a[href$="about#team"]` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |

### Finding04: `/contact`, 360px, JSon

| Selector | Foreground | Background | Observed / required | Smallest palette-only suggestion |
|---|---|---|---|---|
| `.form-card > p > a[href$="services"]` | `#485366` | `#0e1019` | 2.44 /4.5 | foreground `#888888`, predicted 5.35:1 |
| `p > a[href$="blog/"]` | `#485366` | `#0e1019` | 2.44 /4.5 | foreground `#888888`, predicted 5.35:1 |
| `.container > p > a[href$="services"]` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `.team-disclosure > a[href$="about#team"]` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |

### Finding05: `/`, 768px, JSon

| Selector | Foreground | Background | Observed / required | Smallest palette-only suggestion |
|---|---|---|---|---|
| `#coorg-kodagu > .container > div:nth-child(1) > .sec-label` | `#c9a84c` | `#e9edf8` | 1.95 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `div:nth-child(2) > p:nth-child(3)` | `#8a98b8` | `#e9edf8` | 2.46 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `.why-sec:nth-child(6) > .container > .why-hdr > .sec-label` | `#c9a84c` | `#e9edf8` | 1.95 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `.s-wrap:nth-child(8) > .container > div:nth-child(1) > .sec-label` | `#c9a84c` | `#e9edf8` | 1.95 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#faq > .container > .why-hdr > .sec-label` | `#c9a84c` | `#e9edf8` | 1.95 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `.source-review > p > a:nth-child(1)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `p > a:nth-child(2)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `p > a:nth-child(3)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |

### Finding06: `/services`, 768px, JSon

| Selector | Foreground | Background | Observed / required | Smallest palette-only suggestion |
|---|---|---|---|---|
| `#italy > .svc-num[aria-hidden="true"]` | `#d9dee9` | `#e9edf8` | 1.15 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#italy > .rev.svc-grid > .on-light.svc-text.anim-fade-right > h2 > em` | `#c9a94e` | `#e9edf8` | 1.93 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `.highlight-box.on-light:nth-child(6) > .highlight-title` | `#c9a94e` | `#dfe3ee` | 1.76 /4.5 | foreground `#4a5568`, predicted 5.86:1 |
| `.highlight-box.on-light:nth-child(7) > .highlight-title` | `#c9a94e` | `#dfe3ee` | 1.76 /4.5 | foreground `#4a5568`, predicted 5.86:1 |
| `#italy > .rev.svc-grid > .on-light.svc-text.anim-fade-right > .svc-cta[href$="contact"]` | `#c9a94e` | `#e9edf8` | 1.93 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#italy > .rev.svc-grid > .on-light.svc-text.anim-fade-right > .related-guides[aria-label="Planning guides"] > h3` | `#ffffff` | `#e9edf8` | 1.17 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#italy > .rev.svc-grid > .on-light.svc-text.anim-fade-right > .related-guides[aria-label="Planning guides"] > ul > li:nth-child(1) > a` | `#ffffff` | `#e9edf8` | 1.17 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#italy > .rev.svc-grid > .on-light.svc-text.anim-fade-right > .related-guides[aria-label="Planning guides"] > ul > li:nth-child(2) > a` | `#ffffff` | `#e9edf8` | 1.17 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#uk > .svc-num[aria-hidden="true"]` | `#121113` | `#04060f` | 1.07 /4.5 | foreground `#888888`, predicted 5.71:1 |
| `#czech-republic > .svc-num[aria-hidden="true"]` | `#d9dee9` | `#e9edf8` | 1.15 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#czech-republic > .rev.svc-grid > .on-light.svc-text.anim-fade-right > h2 > em` | `#c9a94e` | `#e9edf8` | 1.93 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#czech-republic > .rev.svc-grid > .on-light.svc-text.anim-fade-right > .highlight-box.on-light > .highlight-title` | `#c9a94e` | `#dfe3ee` | 1.76 /4.5 | foreground `#4a5568`, predicted 5.86:1 |
| `#czech-republic > .rev.svc-grid > .on-light.svc-text.anim-fade-right > .svc-cta[href$="contact"]` | `#c9a94e` | `#e9edf8` | 1.93 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#czech-republic > .rev.svc-grid > .on-light.svc-text.anim-fade-right > .related-guides[aria-label="Planning guides"] > h3` | `#ffffff` | `#e9edf8` | 1.17 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#czech-republic > .rev.svc-grid > .on-light.svc-text.anim-fade-right > .related-guides[aria-label="Planning guides"] > ul > li:nth-child(1) > a` | `#ffffff` | `#e9edf8` | 1.17 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#czech-republic > .rev.svc-grid > .on-light.svc-text.anim-fade-right > .related-guides[aria-label="Planning guides"] > ul > li:nth-child(2) > a` | `#ffffff` | `#e9edf8` | 1.17 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#lithuania > .svc-num[aria-hidden="true"]` | `#17202b` | `#0a1628` | 1.10 /4.5 | foreground `#888888`, predicted 5.11:1 |
| `#latvia > .svc-num[aria-hidden="true"]` | `#d9dee9` | `#e9edf8` | 1.15 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#latvia > .rev.svc-grid > .on-light.svc-text.anim-fade-right > h2 > em` | `#c9a94e` | `#e9edf8` | 1.93 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#latvia > .rev.svc-grid > .on-light.svc-text.anim-fade-right > .svc-cta[href$="contact"]` | `#c9a94e` | `#e9edf8` | 1.93 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#latvia > .rev.svc-grid > .on-light.svc-text.anim-fade-right > .related-guides[aria-label="Planning guides"] > h3` | `#ffffff` | `#e9edf8` | 1.17 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#latvia > .rev.svc-grid > .on-light.svc-text.anim-fade-right > .related-guides[aria-label="Planning guides"] > ul > li:nth-child(1) > a` | `#ffffff` | `#e9edf8` | 1.17 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#latvia > .rev.svc-grid > .on-light.svc-text.anim-fade-right > .related-guides[aria-label="Planning guides"] > ul > li:nth-child(2) > a` | `#ffffff` | `#e9edf8` | 1.17 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#slovakia > .svc-num[aria-hidden="true"]` | `#121113` | `#04060f` | 1.07 /4.5 | foreground `#888888`, predicted 5.71:1 |
| `#russia > .svc-num[aria-hidden="true"]` | `#17202b` | `#0a1628` | 1.10 /4.5 | foreground `#888888`, predicted 5.11:1 |
| `#gcc > .svc-num[aria-hidden="true"]` | `#d9dee9` | `#e9edf8` | 1.15 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#gcc > .rev.svc-grid > .on-light.svc-text.anim-fade-right > h2 > em` | `#c9a94e` | `#e9edf8` | 1.93 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#gcc > .rev.svc-grid > .on-light.svc-text.anim-fade-right > .svc-cta[href$="contact"]` | `#c9a94e` | `#e9edf8` | 1.93 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#gcc > .rev.svc-grid > .on-light.svc-text.anim-fade-right > .related-guides[aria-label="Planning guides"] > h3` | `#ffffff` | `#e9edf8` | 1.17 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#gcc > .rev.svc-grid > .on-light.svc-text.anim-fade-right > .related-guides[aria-label="Planning guides"] > ul > li:nth-child(1) > a` | `#ffffff` | `#e9edf8` | 1.17 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#gcc > .rev.svc-grid > .on-light.svc-text.anim-fade-right > .related-guides[aria-label="Planning guides"] > ul > li:nth-child(2) > a` | `#ffffff` | `#e9edf8` | 1.17 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `p:nth-child(5) > a[href$="study-in-germany"]` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `p:nth-child(5) > a[href$="study-in-italy"]` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `p:nth-child(5) > a[href$="study-in-uk"]` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `p:nth-child(5) > a[href$="study-in-lithuania"]` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `p:nth-child(5) > a[href$="study-in-gcc"]` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `p:nth-child(5) > a:nth-child(6)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `p:nth-child(5) > a:nth-child(7)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `p:nth-child(5) > a:nth-child(8)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `.source-review > p > a:nth-child(1)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `.source-review > p > a:nth-child(2)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `.source-review > p > a:nth-child(3)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `a[href$="about#team"]` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |

### Finding07: `/about`, 768px, JSon

| Selector | Foreground | Background | Observed / required | Smallest palette-only suggestion |
|---|---|---|---|---|
| `.container:nth-child(8) > p > a[href$="services"]` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `.source-review > p > a:nth-child(1)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `.source-review > p > a:nth-child(2)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `.source-review > p > a:nth-child(3)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `.team-disclosure > a[href$="about#team"]` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |

### Finding08: `/contact`, 768px, JSon

| Selector | Foreground | Background | Observed / required | Smallest palette-only suggestion |
|---|---|---|---|---|
| `.form-card > p > a[href$="about#team"]` | `#465062` | `#0e1018` | 2.33 /4.5 | foreground `#888888`, predicted 5.36:1 |
| `.container > p > a[href$="services"]` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `.team-disclosure > a[href$="about#team"]` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |

### Finding09: `/`, 1280px, JSon

| Selector | Foreground | Background | Observed / required | Smallest palette-only suggestion |
|---|---|---|---|---|
| `#coorg-kodagu > .container > div:nth-child(1) > .sec-label` | `#c9a84c` | `#e9edf8` | 1.95 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `div:nth-child(2) > p:nth-child(3)` | `#8a98b8` | `#e9edf8` | 2.46 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `.why-sec:nth-child(6) > .container > .why-hdr > .sec-label` | `#c9a84c` | `#e9edf8` | 1.95 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `.s-wrap:nth-child(8) > .container > div:nth-child(1) > .sec-label` | `#c9a84c` | `#e9edf8` | 1.95 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#faq > .container > .why-hdr > .sec-label` | `#c9a84c` | `#e9edf8` | 1.95 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `.source-review > p > a:nth-child(1)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `p > a:nth-child(2)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `p > a:nth-child(3)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |

### Finding10: `/services`, 1280px, JSon

| Selector | Foreground | Background | Observed / required | Smallest palette-only suggestion |
|---|---|---|---|---|
| `#germany > .svc-num[aria-hidden="true"]` | `#17202b` | `#0a1628` | 1.10 /4.5 | foreground `#888888`, predicted 5.11:1 |
| `#italy > .svc-num[aria-hidden="true"]` | `#d9dee9` | `#e9edf8` | 1.15 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#italy > .rev.svc-grid > .on-light.svc-text.anim-fade-right > h2 > em` | `#c9a94e` | `#e9edf8` | 1.93 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `.highlight-box.on-light:nth-child(6) > .highlight-title` | `#c9a94e` | `#dfe3ee` | 1.76 /4.5 | foreground `#4a5568`, predicted 5.86:1 |
| `.highlight-box.on-light:nth-child(7) > .highlight-title` | `#c9a94e` | `#dfe3ee` | 1.76 /4.5 | foreground `#4a5568`, predicted 5.86:1 |
| `#italy > .rev.svc-grid > .on-light.svc-text.anim-fade-right > .svc-cta[href$="contact"]` | `#c9a94e` | `#e9edf8` | 1.93 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#italy > .rev.svc-grid > .on-light.svc-text.anim-fade-right > .related-guides[aria-label="Planning guides"] > h3` | `#ffffff` | `#e9edf8` | 1.17 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#italy > .rev.svc-grid > .on-light.svc-text.anim-fade-right > .related-guides[aria-label="Planning guides"] > ul > li:nth-child(1) > a` | `#ffffff` | `#e9edf8` | 1.17 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#italy > .rev.svc-grid > .on-light.svc-text.anim-fade-right > .related-guides[aria-label="Planning guides"] > ul > li:nth-child(2) > a` | `#ffffff` | `#e9edf8` | 1.17 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#uk > .svc-num[aria-hidden="true"]` | `#121113` | `#04060f` | 1.07 /4.5 | foreground `#888888`, predicted 5.71:1 |
| `#czech-republic > .svc-num[aria-hidden="true"]` | `#d9dee9` | `#e9edf8` | 1.15 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#czech-republic > .rev.svc-grid > .on-light.svc-text.anim-fade-right > h2 > em` | `#caaa50` | `#e9edf8` | 1.91 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#czech-republic > .rev.svc-grid > .on-light.svc-text.anim-fade-right > .highlight-box.on-light > .highlight-title` | `#caaa50` | `#dfe3ee` | 1.74 /4.5 | foreground `#4a5568`, predicted 5.86:1 |
| `#czech-republic > .rev.svc-grid > .on-light.svc-text.anim-fade-right > .svc-cta[href$="contact"]` | `#caaa50` | `#e9edf8` | 1.91 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#czech-republic > .rev.svc-grid > .on-light.svc-text.anim-fade-right > .related-guides[aria-label="Planning guides"] > h3` | `#feffff` | `#e9edf8` | 1.16 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#czech-republic > .rev.svc-grid > .on-light.svc-text.anim-fade-right > .related-guides[aria-label="Planning guides"] > ul > li:nth-child(1) > a` | `#feffff` | `#e9edf8` | 1.16 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#czech-republic > .rev.svc-grid > .on-light.svc-text.anim-fade-right > .related-guides[aria-label="Planning guides"] > ul > li:nth-child(2) > a` | `#feffff` | `#e9edf8` | 1.16 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#lithuania > .svc-num[aria-hidden="true"]` | `#17202b` | `#0a1628` | 1.10 /4.5 | foreground `#888888`, predicted 5.11:1 |
| `#latvia > .svc-num[aria-hidden="true"]` | `#d9dee9` | `#e9edf8` | 1.15 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#latvia > .rev.svc-grid > .on-light.svc-text.anim-fade-right > h2 > em` | `#caaa50` | `#e9edf8` | 1.91 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#latvia > .rev.svc-grid > .on-light.svc-text.anim-fade-right > .svc-cta[href$="contact"]` | `#caaa50` | `#e9edf8` | 1.91 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#latvia > .rev.svc-grid > .on-light.svc-text.anim-fade-right > .related-guides[aria-label="Planning guides"] > h3` | `#feffff` | `#e9edf8` | 1.16 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#latvia > .rev.svc-grid > .on-light.svc-text.anim-fade-right > .related-guides[aria-label="Planning guides"] > ul > li:nth-child(1) > a` | `#feffff` | `#e9edf8` | 1.16 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#latvia > .rev.svc-grid > .on-light.svc-text.anim-fade-right > .related-guides[aria-label="Planning guides"] > ul > li:nth-child(2) > a` | `#feffff` | `#e9edf8` | 1.16 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#slovakia > .svc-num[aria-hidden="true"]` | `#121113` | `#04060f` | 1.07 /4.5 | foreground `#888888`, predicted 5.71:1 |
| `#russia > .svc-num[aria-hidden="true"]` | `#17202b` | `#0a1628` | 1.10 /4.5 | foreground `#888888`, predicted 5.11:1 |
| `#gcc > .svc-num[aria-hidden="true"]` | `#d9dee9` | `#e9edf8` | 1.15 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#gcc > .rev.svc-grid > .on-light.svc-text.anim-fade-right > h2 > em` | `#caaa50` | `#e9edf8` | 1.91 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#gcc > .rev.svc-grid > .on-light.svc-text.anim-fade-right > .svc-cta[href$="contact"]` | `#caaa50` | `#e9edf8` | 1.91 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#gcc > .rev.svc-grid > .on-light.svc-text.anim-fade-right > .related-guides[aria-label="Planning guides"] > h3` | `#feffff` | `#e9edf8` | 1.16 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#gcc > .rev.svc-grid > .on-light.svc-text.anim-fade-right > .related-guides[aria-label="Planning guides"] > ul > li:nth-child(1) > a` | `#feffff` | `#e9edf8` | 1.16 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#gcc > .rev.svc-grid > .on-light.svc-text.anim-fade-right > .related-guides[aria-label="Planning guides"] > ul > li:nth-child(2) > a` | `#feffff` | `#e9edf8` | 1.16 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `p:nth-child(5) > a[href$="study-in-germany"]` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `p:nth-child(5) > a[href$="study-in-italy"]` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `p:nth-child(5) > a[href$="study-in-uk"]` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `p:nth-child(5) > a[href$="study-in-lithuania"]` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `p:nth-child(5) > a[href$="study-in-gcc"]` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `p:nth-child(5) > a:nth-child(6)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `p:nth-child(5) > a:nth-child(7)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `p:nth-child(5) > a:nth-child(8)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `.source-review > p > a:nth-child(1)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `.source-review > p > a:nth-child(2)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `.source-review > p > a:nth-child(3)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `a[href$="about#team"]` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |

### Finding11: `/about`, 1280px, JSon

| Selector | Foreground | Background | Observed / required | Smallest palette-only suggestion |
|---|---|---|---|---|
| `.container:nth-child(8) > p > a[href$="services"]` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `.source-review > p > a:nth-child(1)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `.source-review > p > a:nth-child(2)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `.source-review > p > a:nth-child(3)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `.team-disclosure > a[href$="about#team"]` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |

### Finding12: `/contact`, 1280px, JSon

| Selector | Foreground | Background | Observed / required | Smallest palette-only suggestion |
|---|---|---|---|---|
| `.form-card > p` | `#495467` | `#0e1019` | 2.48 /4.5 | foreground `#888888`, predicted 5.35:1 |
| `.form-card > p > a[href$="services"]` | `#495467` | `#0e1019` | 2.48 /4.5 | foreground `#888888`, predicted 5.35:1 |
| `p > a[href$="blog/"]` | `#495467` | `#0e1019` | 2.48 /4.5 | foreground `#888888`, predicted 5.35:1 |
| `.form-card > p > a[href$="about#team"]` | `#495467` | `#0e1019` | 2.48 /4.5 | foreground `#888888`, predicted 5.35:1 |
| `.container > p > a[href$="services"]` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `.team-disclosure > a[href$="about#team"]` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |

### Finding13: `/`, 360px, JSoff

| Selector | Foreground | Background | Observed / required | Smallest palette-only suggestion |
|---|---|---|---|---|
| `#coorg-kodagu > .container > div:nth-child(1) > .sec-label` | `#c9a84c` | `#e9edf8` | 1.95 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `div:nth-child(2) > p:nth-child(3)` | `#8a98b8` | `#e9edf8` | 2.46 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `.why-sec:nth-child(6) > .container > .why-hdr > .sec-label` | `#c9a84c` | `#e9edf8` | 1.95 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `.s-wrap:nth-child(8) > .container > div:nth-child(1) > .sec-label` | `#c9a84c` | `#e9edf8` | 1.95 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `em` | `#888888` | `#ffffff` | 3.54 /4.5 | foreground `#5a6b8c`, predicted 5.36:1 |
| `#faq > .container > .why-hdr > .sec-label` | `#c9a84c` | `#e9edf8` | 1.95 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `.source-review > p > a:nth-child(1)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `p > a:nth-child(2)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `p > a:nth-child(3)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |

### Finding14: `/services`, 360px, JSoff

| Selector | Foreground | Background | Observed / required | Smallest palette-only suggestion |
|---|---|---|---|---|
| `#germany > .svc-num[aria-hidden="true"]` | `#17202b` | `#0a1628` | 1.10 /4.5 | foreground `#888888`, predicted 5.11:1 |
| `#italy > .svc-num[aria-hidden="true"]` | `#d9dee9` | `#e9edf8` | 1.15 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#italy > .rev.svc-grid > .on-light.svc-text > h2 > em` | `#c9a84c` | `#e9edf8` | 1.95 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `.highlight-box.on-light:nth-child(6) > .highlight-title` | `#c9a84c` | `#dfe3ed` | 1.77 /4.5 | foreground `#4a5568`, predicted 5.86:1 |
| `.highlight-box.on-light:nth-child(7) > .highlight-title` | `#c9a84c` | `#dfe3ed` | 1.77 /4.5 | foreground `#4a5568`, predicted 5.86:1 |
| `#italy > .rev.svc-grid > .on-light.svc-text > .svc-cta[href$="contact"]` | `#c9a84c` | `#e9edf8` | 1.95 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#italy > .rev.svc-grid > .on-light.svc-text > .related-guides[aria-label="Planning guides"] > h3` | `#ffffff` | `#e9edf8` | 1.17 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#italy > .rev.svc-grid > .on-light.svc-text > .related-guides[aria-label="Planning guides"] > ul > li:nth-child(1) > a` | `#ffffff` | `#e9edf8` | 1.17 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#italy > .rev.svc-grid > .on-light.svc-text > .related-guides[aria-label="Planning guides"] > ul > li:nth-child(2) > a` | `#ffffff` | `#e9edf8` | 1.17 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#uk > .svc-num[aria-hidden="true"]` | `#121113` | `#04060f` | 1.07 /4.5 | foreground `#888888`, predicted 5.71:1 |
| `#czech-republic > .svc-num[aria-hidden="true"]` | `#d9dee9` | `#e9edf8` | 1.15 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#czech-republic > .rev.svc-grid > .on-light.svc-text > h2 > em` | `#c9a84c` | `#e9edf8` | 1.95 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#czech-republic > .rev.svc-grid > .on-light.svc-text > .highlight-box.on-light > .highlight-title` | `#c9a84c` | `#dfe3ed` | 1.77 /4.5 | foreground `#4a5568`, predicted 5.86:1 |
| `#czech-republic > .rev.svc-grid > .on-light.svc-text > .svc-cta[href$="contact"]` | `#c9a84c` | `#e9edf8` | 1.95 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#czech-republic > .rev.svc-grid > .on-light.svc-text > .related-guides[aria-label="Planning guides"] > h3` | `#ffffff` | `#e9edf8` | 1.17 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#czech-republic > .rev.svc-grid > .on-light.svc-text > .related-guides[aria-label="Planning guides"] > ul > li:nth-child(1) > a` | `#ffffff` | `#e9edf8` | 1.17 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#czech-republic > .rev.svc-grid > .on-light.svc-text > .related-guides[aria-label="Planning guides"] > ul > li:nth-child(2) > a` | `#ffffff` | `#e9edf8` | 1.17 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#lithuania > .svc-num[aria-hidden="true"]` | `#17202b` | `#0a1628` | 1.10 /4.5 | foreground `#888888`, predicted 5.11:1 |
| `#latvia > .svc-num[aria-hidden="true"]` | `#d9dee9` | `#e9edf8` | 1.15 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#latvia > .rev.svc-grid > .on-light.svc-text > h2 > em` | `#c9a84c` | `#e9edf8` | 1.95 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#latvia > .rev.svc-grid > .on-light.svc-text > .svc-cta[href$="contact"]` | `#c9a84c` | `#e9edf8` | 1.95 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#latvia > .rev.svc-grid > .on-light.svc-text > .related-guides[aria-label="Planning guides"] > h3` | `#ffffff` | `#e9edf8` | 1.17 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#latvia > .rev.svc-grid > .on-light.svc-text > .related-guides[aria-label="Planning guides"] > ul > li:nth-child(1) > a` | `#ffffff` | `#e9edf8` | 1.17 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#latvia > .rev.svc-grid > .on-light.svc-text > .related-guides[aria-label="Planning guides"] > ul > li:nth-child(2) > a` | `#ffffff` | `#e9edf8` | 1.17 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#slovakia > .svc-num[aria-hidden="true"]` | `#121113` | `#04060f` | 1.07 /4.5 | foreground `#888888`, predicted 5.71:1 |
| `#russia > .svc-num[aria-hidden="true"]` | `#17202b` | `#0a1628` | 1.10 /4.5 | foreground `#888888`, predicted 5.11:1 |
| `#gcc > .svc-num[aria-hidden="true"]` | `#d9dee9` | `#e9edf8` | 1.15 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#gcc > .rev.svc-grid > .on-light.svc-text > h2 > em` | `#c9a84c` | `#e9edf8` | 1.95 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#gcc > .rev.svc-grid > .on-light.svc-text > .svc-cta[href$="contact"]` | `#c9a84c` | `#e9edf8` | 1.95 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#gcc > .rev.svc-grid > .on-light.svc-text > .related-guides[aria-label="Planning guides"] > h3` | `#ffffff` | `#e9edf8` | 1.17 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#gcc > .rev.svc-grid > .on-light.svc-text > .related-guides[aria-label="Planning guides"] > ul > li:nth-child(1) > a` | `#ffffff` | `#e9edf8` | 1.17 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#gcc > .rev.svc-grid > .on-light.svc-text > .related-guides[aria-label="Planning guides"] > ul > li:nth-child(2) > a` | `#ffffff` | `#e9edf8` | 1.17 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `p:nth-child(5) > a[href$="study-in-germany"]` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `p:nth-child(5) > a[href$="study-in-italy"]` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `p:nth-child(5) > a[href$="study-in-uk"]` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `p:nth-child(5) > a[href$="study-in-lithuania"]` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `p:nth-child(5) > a[href$="study-in-gcc"]` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `p:nth-child(5) > a:nth-child(6)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `p:nth-child(5) > a:nth-child(7)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `p:nth-child(5) > a:nth-child(8)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `.source-review > p > a:nth-child(1)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `.source-review > p > a:nth-child(2)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `.source-review > p > a:nth-child(3)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `a[href$="about#team"]` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |

### Finding15: `/about`, 360px, JSoff

| Selector | Foreground | Background | Observed / required | Smallest palette-only suggestion |
|---|---|---|---|---|
| `.container > .sec-label` | `#c9a84c` | `#e9edf8` | 1.95 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#team > .container > .team-hdr > .sec-label` | `#c9a84c` | `#e9edf8` | 1.95 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `article:nth-child(1) > .team-role` | `#c9a84c` | `#ffffff` | 2.28 /4.5 | foreground `#8a6a00`, predicted 5.07:1 |
| `article:nth-child(2) > .team-role` | `#c9a84c` | `#ffffff` | 2.28 /4.5 | foreground `#8a6a00`, predicted 5.07:1 |
| `article:nth-child(3) > .team-role` | `#c9a84c` | `#ffffff` | 2.28 /4.5 | foreground `#8a6a00`, predicted 5.07:1 |
| `#faq-h2` | `#0a1628` | `#04060f` | 1.11 /4.5 | foreground `#888888`, predicted 5.71:1 |
| `.container:nth-child(8) > p > a[href$="services"]` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `.source-review > p > a:nth-child(1)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `.source-review > p > a:nth-child(2)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `.source-review > p > a:nth-child(3)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `.team-disclosure > a[href$="about#team"]` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |

### Finding16: `/contact`, 360px, JSoff

| Selector | Foreground | Background | Observed / required | Smallest palette-only suggestion |
|---|---|---|---|---|
| `.form-card > p > a[href$="services"]` | `#4a5568` | `#0e1019` | 2.52 /4.5 | foreground `#888888`, predicted 5.35:1 |
| `p > a[href$="blog/"]` | `#4a5568` | `#0e1019` | 2.52 /4.5 | foreground `#888888`, predicted 5.35:1 |
| `.container > p > a[href$="services"]` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `.team-disclosure > a[href$="about#team"]` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |

### Finding17: `/`, 768px, JSoff

| Selector | Foreground | Background | Observed / required | Smallest palette-only suggestion |
|---|---|---|---|---|
| `#coorg-kodagu > .container > div:nth-child(1) > .sec-label` | `#c9a84c` | `#e9edf8` | 1.95 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `div:nth-child(2) > p:nth-child(3)` | `#8a98b8` | `#e9edf8` | 2.46 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `.why-sec:nth-child(6) > .container > .why-hdr > .sec-label` | `#c9a84c` | `#e9edf8` | 1.95 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `.s-wrap:nth-child(8) > .container > div:nth-child(1) > .sec-label` | `#c9a84c` | `#e9edf8` | 1.95 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `em` | `#888888` | `#ffffff` | 3.54 /4.5 | foreground `#5a6b8c`, predicted 5.36:1 |
| `#faq > .container > .why-hdr > .sec-label` | `#c9a84c` | `#e9edf8` | 1.95 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `.source-review > p > a:nth-child(1)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `p > a:nth-child(2)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `p > a:nth-child(3)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |

### Finding18: `/services`, 768px, JSoff

| Selector | Foreground | Background | Observed / required | Smallest palette-only suggestion |
|---|---|---|---|---|
| `#italy > .svc-num[aria-hidden="true"]` | `#d9dee9` | `#e9edf8` | 1.15 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#italy > .rev.svc-grid > .on-light.svc-text > h2 > em` | `#c9a84c` | `#e9edf8` | 1.95 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `.highlight-box.on-light:nth-child(6) > .highlight-title` | `#c9a84c` | `#dfe3ed` | 1.77 /4.5 | foreground `#4a5568`, predicted 5.86:1 |
| `.highlight-box.on-light:nth-child(7) > .highlight-title` | `#c9a84c` | `#dfe3ed` | 1.77 /4.5 | foreground `#4a5568`, predicted 5.86:1 |
| `#italy > .rev.svc-grid > .on-light.svc-text > .svc-cta[href$="contact"]` | `#c9a84c` | `#e9edf8` | 1.95 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#italy > .rev.svc-grid > .on-light.svc-text > .related-guides[aria-label="Planning guides"] > h3` | `#ffffff` | `#e9edf8` | 1.17 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#italy > .rev.svc-grid > .on-light.svc-text > .related-guides[aria-label="Planning guides"] > ul > li:nth-child(1) > a` | `#ffffff` | `#e9edf8` | 1.17 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#italy > .rev.svc-grid > .on-light.svc-text > .related-guides[aria-label="Planning guides"] > ul > li:nth-child(2) > a` | `#ffffff` | `#e9edf8` | 1.17 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#uk > .svc-num[aria-hidden="true"]` | `#121113` | `#04060f` | 1.07 /4.5 | foreground `#888888`, predicted 5.71:1 |
| `#czech-republic > .svc-num[aria-hidden="true"]` | `#d9dee9` | `#e9edf8` | 1.15 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#czech-republic > .rev.svc-grid > .on-light.svc-text > h2 > em` | `#c9a84c` | `#e9edf8` | 1.95 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#czech-republic > .rev.svc-grid > .on-light.svc-text > .highlight-box.on-light > .highlight-title` | `#c9a84c` | `#dfe3ed` | 1.77 /4.5 | foreground `#4a5568`, predicted 5.86:1 |
| `#czech-republic > .rev.svc-grid > .on-light.svc-text > .svc-cta[href$="contact"]` | `#c9a84c` | `#e9edf8` | 1.95 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#czech-republic > .rev.svc-grid > .on-light.svc-text > .related-guides[aria-label="Planning guides"] > h3` | `#ffffff` | `#e9edf8` | 1.17 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#czech-republic > .rev.svc-grid > .on-light.svc-text > .related-guides[aria-label="Planning guides"] > ul > li:nth-child(1) > a` | `#ffffff` | `#e9edf8` | 1.17 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#czech-republic > .rev.svc-grid > .on-light.svc-text > .related-guides[aria-label="Planning guides"] > ul > li:nth-child(2) > a` | `#ffffff` | `#e9edf8` | 1.17 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#lithuania > .svc-num[aria-hidden="true"]` | `#17202b` | `#0a1628` | 1.10 /4.5 | foreground `#888888`, predicted 5.11:1 |
| `#latvia > .svc-num[aria-hidden="true"]` | `#d9dee9` | `#e9edf8` | 1.15 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#latvia > .rev.svc-grid > .on-light.svc-text > h2 > em` | `#c9a84c` | `#e9edf8` | 1.95 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#latvia > .rev.svc-grid > .on-light.svc-text > .svc-cta[href$="contact"]` | `#c9a84c` | `#e9edf8` | 1.95 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#latvia > .rev.svc-grid > .on-light.svc-text > .related-guides[aria-label="Planning guides"] > h3` | `#ffffff` | `#e9edf8` | 1.17 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#latvia > .rev.svc-grid > .on-light.svc-text > .related-guides[aria-label="Planning guides"] > ul > li:nth-child(1) > a` | `#ffffff` | `#e9edf8` | 1.17 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#latvia > .rev.svc-grid > .on-light.svc-text > .related-guides[aria-label="Planning guides"] > ul > li:nth-child(2) > a` | `#ffffff` | `#e9edf8` | 1.17 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#slovakia > .svc-num[aria-hidden="true"]` | `#121113` | `#04060f` | 1.07 /4.5 | foreground `#888888`, predicted 5.71:1 |
| `#russia > .svc-num[aria-hidden="true"]` | `#17202b` | `#0a1628` | 1.10 /4.5 | foreground `#888888`, predicted 5.11:1 |
| `#gcc > .svc-num[aria-hidden="true"]` | `#d9dee9` | `#e9edf8` | 1.15 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#gcc > .rev.svc-grid > .on-light.svc-text > h2 > em` | `#c9a84c` | `#e9edf8` | 1.95 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#gcc > .rev.svc-grid > .on-light.svc-text > .svc-cta[href$="contact"]` | `#c9a84c` | `#e9edf8` | 1.95 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#gcc > .rev.svc-grid > .on-light.svc-text > .related-guides[aria-label="Planning guides"] > h3` | `#ffffff` | `#e9edf8` | 1.17 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#gcc > .rev.svc-grid > .on-light.svc-text > .related-guides[aria-label="Planning guides"] > ul > li:nth-child(1) > a` | `#ffffff` | `#e9edf8` | 1.17 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#gcc > .rev.svc-grid > .on-light.svc-text > .related-guides[aria-label="Planning guides"] > ul > li:nth-child(2) > a` | `#ffffff` | `#e9edf8` | 1.17 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `p:nth-child(5) > a[href$="study-in-germany"]` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `p:nth-child(5) > a[href$="study-in-italy"]` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `p:nth-child(5) > a[href$="study-in-uk"]` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `p:nth-child(5) > a[href$="study-in-lithuania"]` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `p:nth-child(5) > a[href$="study-in-gcc"]` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `p:nth-child(5) > a:nth-child(6)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `p:nth-child(5) > a:nth-child(7)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `p:nth-child(5) > a:nth-child(8)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `.source-review > p > a:nth-child(1)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `.source-review > p > a:nth-child(2)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `.source-review > p > a:nth-child(3)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `a[href$="about#team"]` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |

### Finding19: `/about`, 768px, JSoff

| Selector | Foreground | Background | Observed / required | Smallest palette-only suggestion |
|---|---|---|---|---|
| `.container > .sec-label` | `#c9a84c` | `#e9edf8` | 1.95 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#team > .container > .team-hdr > .sec-label` | `#c9a84c` | `#e9edf8` | 1.95 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `article:nth-child(1) > .team-role` | `#c9a84c` | `#ffffff` | 2.28 /4.5 | foreground `#8a6a00`, predicted 5.07:1 |
| `article:nth-child(2) > .team-role` | `#c9a84c` | `#ffffff` | 2.28 /4.5 | foreground `#8a6a00`, predicted 5.07:1 |
| `article:nth-child(3) > .team-role` | `#c9a84c` | `#ffffff` | 2.28 /4.5 | foreground `#8a6a00`, predicted 5.07:1 |
| `#faq-h2` | `#0a1628` | `#04060f` | 1.11 /4.5 | foreground `#888888`, predicted 5.71:1 |
| `.container:nth-child(8) > p > a[href$="services"]` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `.source-review > p > a:nth-child(1)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `.source-review > p > a:nth-child(2)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `.source-review > p > a:nth-child(3)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `.team-disclosure > a[href$="about#team"]` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |

### Finding20: `/contact`, 768px, JSoff

| Selector | Foreground | Background | Observed / required | Smallest palette-only suggestion |
|---|---|---|---|---|
| `.form-card > p > a[href$="about#team"]` | `#4a5568` | `#0e1019` | 2.52 /4.5 | foreground `#888888`, predicted 5.35:1 |
| `.container > p > a[href$="services"]` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `.team-disclosure > a[href$="about#team"]` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |

### Finding21: `/`, 1280px, JSoff

| Selector | Foreground | Background | Observed / required | Smallest palette-only suggestion |
|---|---|---|---|---|
| `#coorg-kodagu > .container > div:nth-child(1) > .sec-label` | `#c9a84c` | `#e9edf8` | 1.95 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `div:nth-child(2) > p:nth-child(3)` | `#8a98b8` | `#e9edf8` | 2.46 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `.why-sec:nth-child(6) > .container > .why-hdr > .sec-label` | `#c9a84c` | `#e9edf8` | 1.95 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `.s-wrap:nth-child(8) > .container > div:nth-child(1) > .sec-label` | `#c9a84c` | `#e9edf8` | 1.95 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `em` | `#888888` | `#ffffff` | 3.54 /4.5 | foreground `#5a6b8c`, predicted 5.36:1 |
| `#faq > .container > .why-hdr > .sec-label` | `#c9a84c` | `#e9edf8` | 1.95 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `.source-review > p > a:nth-child(1)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `p > a:nth-child(2)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `p > a:nth-child(3)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |

### Finding22: `/services`, 1280px, JSoff

| Selector | Foreground | Background | Observed / required | Smallest palette-only suggestion |
|---|---|---|---|---|
| `#germany > .svc-num[aria-hidden="true"]` | `#17202b` | `#0a1628` | 1.10 /4.5 | foreground `#888888`, predicted 5.11:1 |
| `#italy > .svc-num[aria-hidden="true"]` | `#d9dee9` | `#e9edf8` | 1.15 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#italy > .rev.svc-grid > .on-light.svc-text > h2 > em` | `#c9a84c` | `#e9edf8` | 1.95 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `.highlight-box.on-light:nth-child(6) > .highlight-title` | `#c9a84c` | `#dfe3ed` | 1.77 /4.5 | foreground `#4a5568`, predicted 5.86:1 |
| `.highlight-box.on-light:nth-child(7) > .highlight-title` | `#c9a84c` | `#dfe3ed` | 1.77 /4.5 | foreground `#4a5568`, predicted 5.86:1 |
| `#italy > .rev.svc-grid > .on-light.svc-text > .svc-cta[href$="contact"]` | `#c9a84c` | `#e9edf8` | 1.95 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#italy > .rev.svc-grid > .on-light.svc-text > .related-guides[aria-label="Planning guides"] > h3` | `#ffffff` | `#e9edf8` | 1.17 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#italy > .rev.svc-grid > .on-light.svc-text > .related-guides[aria-label="Planning guides"] > ul > li:nth-child(1) > a` | `#ffffff` | `#e9edf8` | 1.17 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#italy > .rev.svc-grid > .on-light.svc-text > .related-guides[aria-label="Planning guides"] > ul > li:nth-child(2) > a` | `#ffffff` | `#e9edf8` | 1.17 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#uk > .svc-num[aria-hidden="true"]` | `#121113` | `#04060f` | 1.07 /4.5 | foreground `#888888`, predicted 5.71:1 |
| `#czech-republic > .svc-num[aria-hidden="true"]` | `#d9dee9` | `#e9edf8` | 1.15 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#czech-republic > .rev.svc-grid > .on-light.svc-text > h2 > em` | `#c9a84c` | `#e9edf8` | 1.95 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#czech-republic > .rev.svc-grid > .on-light.svc-text > .highlight-box.on-light > .highlight-title` | `#c9a84c` | `#dfe3ed` | 1.77 /4.5 | foreground `#4a5568`, predicted 5.86:1 |
| `#czech-republic > .rev.svc-grid > .on-light.svc-text > .svc-cta[href$="contact"]` | `#c9a84c` | `#e9edf8` | 1.95 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#czech-republic > .rev.svc-grid > .on-light.svc-text > .related-guides[aria-label="Planning guides"] > h3` | `#ffffff` | `#e9edf8` | 1.17 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#czech-republic > .rev.svc-grid > .on-light.svc-text > .related-guides[aria-label="Planning guides"] > ul > li:nth-child(1) > a` | `#ffffff` | `#e9edf8` | 1.17 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#czech-republic > .rev.svc-grid > .on-light.svc-text > .related-guides[aria-label="Planning guides"] > ul > li:nth-child(2) > a` | `#ffffff` | `#e9edf8` | 1.17 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#lithuania > .svc-num[aria-hidden="true"]` | `#17202b` | `#0a1628` | 1.10 /4.5 | foreground `#888888`, predicted 5.11:1 |
| `#latvia > .svc-num[aria-hidden="true"]` | `#d9dee9` | `#e9edf8` | 1.15 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#latvia > .rev.svc-grid > .on-light.svc-text > h2 > em` | `#c9a84c` | `#e9edf8` | 1.95 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#latvia > .rev.svc-grid > .on-light.svc-text > .svc-cta[href$="contact"]` | `#c9a84c` | `#e9edf8` | 1.95 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#latvia > .rev.svc-grid > .on-light.svc-text > .related-guides[aria-label="Planning guides"] > h3` | `#ffffff` | `#e9edf8` | 1.17 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#latvia > .rev.svc-grid > .on-light.svc-text > .related-guides[aria-label="Planning guides"] > ul > li:nth-child(1) > a` | `#ffffff` | `#e9edf8` | 1.17 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#latvia > .rev.svc-grid > .on-light.svc-text > .related-guides[aria-label="Planning guides"] > ul > li:nth-child(2) > a` | `#ffffff` | `#e9edf8` | 1.17 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#slovakia > .svc-num[aria-hidden="true"]` | `#121113` | `#04060f` | 1.07 /4.5 | foreground `#888888`, predicted 5.71:1 |
| `#russia > .svc-num[aria-hidden="true"]` | `#17202b` | `#0a1628` | 1.10 /4.5 | foreground `#888888`, predicted 5.11:1 |
| `#gcc > .svc-num[aria-hidden="true"]` | `#d9dee9` | `#e9edf8` | 1.15 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#gcc > .rev.svc-grid > .on-light.svc-text > h2 > em` | `#c9a84c` | `#e9edf8` | 1.95 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#gcc > .rev.svc-grid > .on-light.svc-text > .svc-cta[href$="contact"]` | `#c9a84c` | `#e9edf8` | 1.95 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#gcc > .rev.svc-grid > .on-light.svc-text > .related-guides[aria-label="Planning guides"] > h3` | `#ffffff` | `#e9edf8` | 1.17 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#gcc > .rev.svc-grid > .on-light.svc-text > .related-guides[aria-label="Planning guides"] > ul > li:nth-child(1) > a` | `#ffffff` | `#e9edf8` | 1.17 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#gcc > .rev.svc-grid > .on-light.svc-text > .related-guides[aria-label="Planning guides"] > ul > li:nth-child(2) > a` | `#ffffff` | `#e9edf8` | 1.17 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `p:nth-child(5) > a[href$="study-in-germany"]` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `p:nth-child(5) > a[href$="study-in-italy"]` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `p:nth-child(5) > a[href$="study-in-uk"]` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `p:nth-child(5) > a[href$="study-in-lithuania"]` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `p:nth-child(5) > a[href$="study-in-gcc"]` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `p:nth-child(5) > a:nth-child(6)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `p:nth-child(5) > a:nth-child(7)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `p:nth-child(5) > a:nth-child(8)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `.source-review > p > a:nth-child(1)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `.source-review > p > a:nth-child(2)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `.source-review > p > a:nth-child(3)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `a[href$="about#team"]` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |

### Finding23: `/about`, 1280px, JSoff

| Selector | Foreground | Background | Observed / required | Smallest palette-only suggestion |
|---|---|---|---|---|
| `.container > .sec-label` | `#c9a84c` | `#e9edf8` | 1.95 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `#team > .container > .team-hdr > .sec-label` | `#c9a84c` | `#e9edf8` | 1.95 /4.5 | foreground `#5a6b8c`, predicted 4.58:1 |
| `article:nth-child(1) > .team-role` | `#c9a84c` | `#ffffff` | 2.28 /4.5 | foreground `#8a6a00`, predicted 5.07:1 |
| `article:nth-child(2) > .team-role` | `#c9a84c` | `#ffffff` | 2.28 /4.5 | foreground `#8a6a00`, predicted 5.07:1 |
| `article:nth-child(3) > .team-role` | `#c9a84c` | `#ffffff` | 2.28 /4.5 | foreground `#8a6a00`, predicted 5.07:1 |
| `#faq-h2` | `#0a1628` | `#04060f` | 1.11 /4.5 | foreground `#888888`, predicted 5.71:1 |
| `.container:nth-child(8) > p > a[href$="services"]` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `.source-review > p > a:nth-child(1)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `.source-review > p > a:nth-child(2)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `.source-review > p > a:nth-child(3)` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `.team-disclosure > a[href$="about#team"]` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |

### Finding24: `/contact`, 1280px, JSoff

| Selector | Foreground | Background | Observed / required | Smallest palette-only suggestion |
|---|---|---|---|---|
| `.form-card > p` | `#4a5568` | `#0e1019` | 2.52 /4.5 | foreground `#888888`, predicted 5.35:1 |
| `.form-card > p > a[href$="services"]` | `#4a5568` | `#0e1019` | 2.52 /4.5 | foreground `#888888`, predicted 5.35:1 |
| `p > a[href$="blog/"]` | `#4a5568` | `#0e1019` | 2.52 /4.5 | foreground `#888888`, predicted 5.35:1 |
| `.form-card > p > a[href$="about#team"]` | `#4a5568` | `#0e1019` | 2.52 /4.5 | foreground `#888888`, predicted 5.35:1 |
| `.container > p > a[href$="services"]` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |
| `.team-disclosure > a[href$="about#team"]` | `#0000ee` | `#04060f` | 2.15 /4.5 | foreground `#4488ff`, predicted 5.98:1 |

## Five retained overflow cases

A larger scrollWidth alone is not proof that readable content is clipped or that a user can pan sideways. The new sampler observes original animations without changing reference CSS or disabling scenes. Early frames, naturally settled scroll/reveal state and a horizontal-wheel attempt are retained in phase-25c-reference-overflow.json. Invisible transformed nodes are included because they can affect layout overflow without painting. Fixed decorative layers are not assumed to be the scroll-container cause merely because their rectangles exceed the viewport.

### `/` at360px

Historical document width400px; sampled widths[360, 360, 360, 400, 400, 400]; settled width400px. Horizontal-wheel scrollX=0. Diagnosis: transformed layout-edge contributors observed.

- `article.testi-card.reveal-r` at4833ms: right=400.000px, top=11312.9px, transform `matrix(1, 0, 0, 1, 60, 0)`, effective opacity0.0000, visibility `visible`. Transform/clip chain: `article.testi-card.reveal-r` overflow=hidden, transform=matrix(1, 0, 0, 1, 60, 0); `body.` overflow=hidden, transform=none.

Visible-to-user assessment: the observed layout-edge contributors have zero effective opacity or hidden visibility, so they are not painted at those sampled frames. Their transforms still enlarge layout overflow.
After natural reveal scrolling, document scrollWidth remains enlarged by offscreen hidden reveal start states; this is a retained numerical layout deviation, not compositor noise. The horizontal wheel did not pan the page. No reference fix applied. The matching right-edge matrices identify reveal-layout start states, not a3D scene or floating decorative glyph, as the measured edge contributors.

### `/about` at360px

Historical document width393px; sampled widths[360, 393, 393, 393, 393, 393]; settled width393px. Horizontal-wheel scrollX=0. Diagnosis: transformed layout-edge contributors observed.

- `div.stats-block` at4654ms: right=393.000px, top=2122.5px, transform `matrix(1, 0, 0, 1, 55, 0)`, effective opacity0.0000, visibility `visible`. Transform/clip chain: `div.stats-block` overflow=visible, transform=matrix(1, 0, 0, 1, 55, 0); `body.` overflow=hidden, transform=none.

Visible-to-user assessment: the observed layout-edge contributors have zero effective opacity or hidden visibility, so they are not painted at those sampled frames. Their transforms still enlarge layout overflow.
After natural reveal scrolling, document scrollWidth remains enlarged by offscreen hidden reveal start states; this is a retained numerical layout deviation, not compositor noise. The horizontal wheel did not pan the page. No reference fix applied. The matching right-edge matrices identify reveal-layout start states, not a3D scene or floating decorative glyph, as the measured edge contributors.

### `/contact` at360px

Historical document width396px; sampled widths[360, 360, 360, 396, 396, 396]; settled width396px. Horizontal-wheel scrollX=0. Diagnosis: transformed layout-edge contributors observed.

- `div.contact-info.reveal-r.anim-fade-right` at4709ms: right=396.000px, top=1723.0px, transform `matrix(1, 0, 0, 1, 60, 0)`, effective opacity0.0000, visibility `visible`. Transform/clip chain: `div.contact-info.reveal-r.anim-fade-right` overflow=visible, transform=matrix(1, 0, 0, 1, 60, 0); `body.` overflow=hidden, transform=none.

Visible-to-user assessment: some edge contributors are painted during transition. Body/root clipping and the settled layout must be considered; this is not silently waived as an invisible scene artifact.
After natural reveal scrolling, document scrollWidth remains enlarged by offscreen hidden reveal start states; this is a retained numerical layout deviation, not compositor noise. The horizontal wheel did not pan the page. No reference fix applied. The matching right-edge matrices identify reveal-layout start states, not a3D scene or floating decorative glyph, as the measured edge contributors.

### `/` at768px

Historical document width808px; sampled widths[768, 768, 768, 808, 808, 808]; settled width808px. Horizontal-wheel scrollX=0. Diagnosis: transformed layout-edge contributors observed.

- `article.testi-card.reveal-r` at4457ms: right=808.000px, top=9312.4px, transform `matrix(1, 0, 0, 1, 60, 0)`, effective opacity0.0000, visibility `visible`. Transform/clip chain: `article.testi-card.reveal-r` overflow=hidden, transform=matrix(1, 0, 0, 1, 60, 0); `body.` overflow=hidden, transform=none.

Visible-to-user assessment: the observed layout-edge contributors have zero effective opacity or hidden visibility, so they are not painted at those sampled frames. Their transforms still enlarge layout overflow.
After natural reveal scrolling, document scrollWidth remains enlarged by offscreen hidden reveal start states; this is a retained numerical layout deviation, not compositor noise. The horizontal wheel did not pan the page. No reference fix applied. The matching right-edge matrices identify reveal-layout start states, not a3D scene or floating decorative glyph, as the measured edge contributors.

### `/about` at768px

Historical document width801px; sampled widths[768, 768, 768, 768, 801, 801]; settled width801px. Horizontal-wheel scrollX=0. Diagnosis: transformed layout-edge contributors observed.

- `div.stats-block` at4566ms: right=801.000px, top=1341.8px, transform `matrix(1, 0, 0, 1, 55, 0)`, effective opacity0.0000, visibility `visible`. Transform/clip chain: `div.stats-block` overflow=visible, transform=matrix(1, 0, 0, 1, 55, 0); `body.` overflow=hidden, transform=none.

Visible-to-user assessment: the observed layout-edge contributors have zero effective opacity or hidden visibility, so they are not painted at those sampled frames. Their transforms still enlarge layout overflow.
After natural reveal scrolling, document scrollWidth remains enlarged by offscreen hidden reveal start states; this is a retained numerical layout deviation, not compositor noise. The horizontal wheel did not pan the page. No reference fix applied. The matching right-edge matrices identify reveal-layout start states, not a3D scene or floating decorative glyph, as the measured edge contributors.

