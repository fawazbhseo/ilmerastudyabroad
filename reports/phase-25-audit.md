# Phase 25 reference audit

## Scope and evidence

Report-only audit, taken from unmodified Phase 24b HEAD `164d6de41159385e151ecefec54763eab59141a5`. No page source was changed for this task. Stage 1 only. The exhaustive selector/declaration/inline-style/context and colour-use inventory is [phase-25-reference-tokens.json](phase-25-reference-tokens.json). It includes every actual reference declaration, not an invented replacement palette.

The source does **not** implement a uniform light reference system: default heroes and navigation are dark, Home/Services contain multiple dark bands, About has both dark and light bands, Contact is predominantly dark. There is no active light-theme toggle; dormant `data-theme="light"` selectors are not the default. References remain immutable. Pilots will borrow actual light-section surfaces and typography while following the requested light reading-area rule; this is a deliberate synthesis of existing roles, not a claim that the whole reference sequence already satisfies that rule.

## Actual design tokens

### `/`

| Property | Actual unique values |
| --- | --- |
| font-family | `"Cormorant Garamond",serif`, `"Outfit",sans-serif`, `Outfit,sans-serif` |
| font-size | `10px`, `11px`, `12px`, `13px`, `14px`, `15px`, `16px`, `17px`, `18px`, `20px`, `22px`, `24px`, `30px`, `32px`, `34px`, `36px`, `38px`, `48px`, `54px`, `76px`, `90px` |
| font-weight | `300`, `400`, `500`, `600`, `700` |
| line-height | `1`, `1.06`, `1.15`, `1.4`, `1.5`, `1.6`, `1.65`, `1.7`, `1.75`, `1.8` |
| letter-spacing | `.02em`, `.05em`, `.08em`, `.14em`, `.18em`, `.1em`, `.22em`, `.25em`, `.3em`, `.4em` |
| max-width | `1100px`, `1200px`, `220px`, `300px`, `580px`, `720px`, `760px`, `820px`, `900px` |
| padding | `0`, `0 20px`, `0 20px 20px`, `0 22px`, `0 26px 24px`, `0 32px`, `0 60px`, `100px 20px 60px`, `10px 20px`, `110px 0`, `120px 24px 80px`, `130px 0`, `16px 0`, `16px 36px`, `16px 8px`, `18px 20px`, `18px 48px`, `22px 26px`, `24px 20px`, `28px 24px`, `32px 0`, `32px 26px`, `36px 28px`, `40px`, `48px 36px`, `4px`, `5px 14px`, `60px 0`, `60px 0 70px`, `6px 16px`, `80px 0`, `80px 0 100px`, `80px 0 40px`, `8px 16px` |
| padding-top | `110px`, `28px` |
| padding-bottom | `110px`, `4px` |
| margin | `0`, `0 auto`, `0 auto 30px`, `0 auto 38px`, `18px auto`, `20px 0` |
| margin-bottom | `0`, `10px`, `12px`, `14px`, `16px`, `18px`, `20px`, `22px`, `24px`, `26px`, `30px`, `36px`, `40px`, `4px`, `52px`, `56px`, `64px`, `7px`, `8px` |
| gap | `0`, `10px`, `12px`, `16px`, `20px`, `24px`, `28px`, `32px`, `36px`, `40px`, `5px`, `8px` |
| border-radius | `12px`, `14px`, `16px`, `20px`, `2px`, `3px`, `50%`, `inherit` |
| box-shadow | `0 0 40px var(--gold-glow)`, `0 16px 50px rgba(10,22,40,0.13)`, `0 20px 60px rgba(10,22,40,0.15)`, `0 4px 30px rgba(10,22,40,0.06)`, `0 4px 30px rgba(10,22,40,0.07)`, `0 4px 40px rgba(10,22,40,0.08)` |

Breakpoints: `all / @keyframes beamSw`, `all / @keyframes bounce`, `all / @keyframes floatUp`, `all / @keyframes marquee`, `all / @keyframes nebulaD`, `all / @keyframes shimmerPulse`, `all / @media (max-width:1024px)`, `all / @media (max-width:480px)`, `all / @media (max-width:768px)`, `all / @media (min-width:1440px)`, `all / @media (min-width:769px) and (max-width:1024px)`

Exact colour values and each selector/property use are in the inventory, including scene-only colours.

### `/services`

| Property | Actual unique values |
| --- | --- |
| font-family | `"Cormorant Garamond",serif`, `"Outfit",sans-serif`, `Outfit,sans-serif` |
| font-size | `0.7em`, `10px`, `11px`, `12px`, `13px`, `14px`, `15px`, `16px`, `17px`, `18px`, `20px`, `22px`, `24px`, `26px`, `28px`, `30px`, `32px`, `34px`, `36px`, `42px`, `46px`, `48px`, `60px`, `64px`, `96px` |
| font-weight | `300`, `400`, `500`, `600`, `700` |
| line-height | `1`, `1.08`, `1.15`, `1.18`, `1.3`, `1.4`, `1.5`, `1.55`, `1.6`, `1.7`, `1.75`, `1.8` |
| letter-spacing | `.02em`, `.05em`, `.06em`, `.07em`, `.14em`, `.18em`, `.1em`, `.22em`, `.25em`, `.3em` |
| max-width | `1000px`, `1100px`, `1200px`, `220px`, `600px`, `760px`, `820px`, `960px` |
| padding | `0`, `0 20px`, `0 22px`, `0 4px 24px`, `0 60px`, `0 8px`, `10px 18px`, `10px 20px`, `110px 0`, `120px 22px 50px`, `130px 0`, `130px 24px 60px`, `16px 0`, `16px 24px`, `16px 36px`, `18px 12px`, `18px 20px`, `20px 44px 20px 4px`, `22px 16px`, `24px 18px`, `24px 50px 24px 4px`, `32px 0`, `32px 24px`, `4px`, `4px 12px`, `50px 0`, `65px 0`, `6px 14px`, `70px 0`, `80px 0 40px`, `8px 0 8px 30px`, `8px 16px` |
| padding-top | `28px` |
| padding-bottom | `22px`, `4px` |
| margin | `0`, `0 auto`, `18px auto`, `20px 0`, `20px auto 0`, `auto` |
| margin-bottom | `0`, `10px`, `12px`, `16px`, `18px`, `20px`, `22px`, `26px`, `3px`, `40px`, `4px`, `50px`, `64px`, `6px`, `8px`, `90px` |
| gap | `10px`, `12px`, `16px`, `18px`, `20px`, `24px`, `28px`, `32px`, `36px`, `40px`, `5px`, `6px`, `80px`, `8px` |
| border-radius | `10px`, `12px`, `14px`, `20px`, `2px`, `3px`, `50%`, `8px`, `inherit` |
| box-shadow | `0 0 0 0 rgba(201,168,76,0)`, `0 0 0 0 var(--gold-glow)`, `0 0 0 18px rgba(201,168,76,0)`, `0 0 20px var(--gold-glow)`, `0 0 40px var(--gold-glow)`, `0 16px 40px rgba(0,0,0,0.3)`, `inset 0 0 50px rgba(201,168,76,0.08),0 0 50px rgba(201,168,76,0.08)` |

Breakpoints: `all / @keyframes bounce`, `all / @keyframes floatUp`, `all / @keyframes gP`, `all / @keyframes nA`, `all / @keyframes ringPulse`, `all / @keyframes sHex`, `all / @keyframes sPulse`, `all / @keyframes sSpin`, `all / @keyframes sSpinR`, `all / @media (max-width:380px)`, `all / @media (max-width:480px)`, `all / @media (max-width:600px)`, `all / @media (max-width:768px)`, `all / @media (max-width:980px)`

Exact colour values and each selector/property use are in the inventory, including scene-only colours.

### `/about`

| Property | Actual unique values |
| --- | --- |
| font-family | `"Cormorant Garamond",serif`, `"Outfit",sans-serif` |
| font-size | `10px`, `11px`, `12px`, `13px`, `14px`, `15px`, `16px`, `17px`, `18px`, `19px`, `20px`, `22px`, `24px`, `26px`, `30px`, `32px`, `36px`, `42px`, `48px`, `60px`, `66px`, `9px` |
| font-weight | `300`, `400`, `500`, `600`, `700` |
| line-height | `1`, `1.08`, `1.15`, `1.18`, `1.5`, `1.6`, `1.65`, `1.7`, `1.75`, `1.78`, `1.8` |
| letter-spacing | `.02em`, `.04em`, `.05em`, `.12em`, `.14em`, `.18em`, `.1em`, `.22em`, `.25em`, `.3em` |
| max-width | `100%`, `1000px`, `1200px`, `120px`, `220px`, `380px`, `560px`, `720px`, `760px`, `820px`, `none` |
| padding | `0`, `0 10px`, `0 20px`, `0 20px 20px`, `0 22px`, `0 26px 24px`, `0 60px`, `10px 20px`, `110px 0`, `120px 22px 30px`, `12px 20px`, `130px 0`, `130px 24px 60px`, `14px 8px`, `16px 24px`, `16px 36px`, `18px 20px`, `22px 14px`, `22px 26px`, `24px`, `28px`, `28px 0`, `32px 26px`, `40px 32px`, `44px`, `4px`, `6px 14px`, `70px 0`, `80px 0 40px`, `8px 16px` |
| padding-top | `28px` |
| padding-bottom | `4px` |
| margin | `0`, `0 auto`, `0 auto 22px`, `18px auto`, `18px auto 0`, `20px 0`, `20px auto 0`, `32px auto`, `34px auto 0`, `36px 0 14px` |
| margin-bottom | `0`, `10px`, `14px`, `16px`, `18px`, `20px`, `22px`, `24px`, `28px`, `40px`, `4px`, `56px`, `64px`, `72px`, `8px` |
| gap | `10px`, `12px`, `16px`, `18px`, `20px`, `24px`, `28px`, `32px`, `36px`, `40px`, `44px`, `5px`, `80px`, `8px` |
| border-radius | `10px`, `12px`, `14px`, `16px`, `20px`, `2px`, `3px`, `50%`, `8px` |
| box-shadow | `0 0 0 0 rgba(201,168,76,0)`, `0 0 0 0 var(--gold-glow)`, `0 0 0 18px rgba(201,168,76,0)`, `0 0 24px var(--gold-glow)`, `0 0 40px var(--gold-glow)`, `0 14px 45px rgba(10,22,40,0.13)`, `0 20px 50px rgba(0,0,0,0.3)`, `0 22px 60px rgba(10,22,40,0.14)`, `0 4px 30px rgba(10,22,40,0.07)`, `0 4px 40px rgba(10,22,40,0.07)` |

Breakpoints: `all / @keyframes bounce`, `all / @keyframes floatUp`, `all / @keyframes gP`, `all / @keyframes nA`, `all / @keyframes ringPulse`, `all / @media (max-width:1024px),(hover:none)`, `all / @media (max-width:480px)`, `all / @media (max-width:600px)`, `all / @media (max-width:700px)`, `all / @media (max-width:768px)`, `all / @media (max-width:900px)`, `all / @media (prefers-reduced-motion:reduce)`

Exact colour values and each selector/property use are in the inventory, including scene-only colours.

### `/contact`

| Property | Actual unique values |
| --- | --- |
| font-family | `"Cormorant Garamond",serif`, `"Outfit",sans-serif`, `Outfit,sans-serif` |
| font-size | `10px`, `11px`, `12px`, `13px`, `14px`, `15px`, `16px`, `18px`, `22px`, `24px`, `30px`, `32px`, `36px`, `38px`, `48px`, `66px`, `9px` |
| font-weight | `300`, `400`, `500`, `600`, `700` |
| line-height | `1`, `1.08`, `1.15`, `1.4`, `1.55`, `1.6`, `1.7`, `1.75`, `1.8` |
| letter-spacing | `.02em`, `.05em`, `.12em`, `.14em`, `.18em`, `.1em`, `.22em`, `.25em`, `.2em`, `.3em` |
| max-width | `1120px`, `1200px`, `220px`, `540px`, `760px`, `780px`, `820px`, `960px` |
| padding | `0`, `0 20px`, `0 24px`, `0 5px`, `0 60px`, `100px 24px 40px`, `10px 18px`, `10px 20px`, `10px 24px`, `110px 0`, `130px 24px 110px`, `14px 16px`, `16px 0`, `16px 24px`, `17px`, `24px`, `26px 0`, `28px`, `28px 0`, `28px 20px`, `32px 0`, `4px`, `52px`, `6px 14px`, `75px 0`, `80px 0`, `80px 0 40px`, `8px 16px` |
| padding-top | `28px` |
| padding-bottom | `22px`, `4px` |
| margin | `0`, `0 auto`, `18px auto`, `20px 0`, `20px auto 0`, `32px 0 28px`, `32px auto` |
| margin-bottom | `0`, `10px`, `14px`, `16px`, `18px`, `20px`, `24px`, `26px`, `28px`, `36px`, `3px`, `4px`, `5px`, `64px`, `68px`, `8px` |
| gap | `10px`, `12px`, `16px`, `18px`, `20px`, `32px`, `36px`, `40px`, `48px`, `5px`, `60px`, `8px` |
| border-radius | `10px`, `12px`, `14px`, `22px`, `2px`, `3px`, `50%`, `5px`, `8px` |
| box-shadow | `0 0 45px var(--gold-glow)` |

Breakpoints: `all / @keyframes bounce`, `all / @keyframes floatUp`, `all / @keyframes gP`, `all / @keyframes nA`, `all / @media (max-width:480px)`, `all / @media (max-width:768px)`

Exact colour values and each selector/property use are in the inventory, including scene-only colours.

## Reference skeleton and section sequence

- Shared header: fixed 70px, 60px desktop insets, serif brand and Outfit navigation, responsive hamburger/menu; shared footer: void surface, grid of brand/navigation/destinations/guides/online locations/contact, legal/review row. Existing phone glyphs, footer contents and links are preserved.
- Home: full-viewport centered dark animated hero; marquee and destinations/locations (dark); Kodagu (light); why (light); counselling disclosures (dark); special circumstances (light); FAQ (light); team (dark); latest guides (dark); conversion (dark); tuition sources; dark footer. Reference contains pre-existing glass, hover transforms, badges, glow and noise. Do not reproduce those embellishments in the new pilots, and do not redesign the reference to remove them.
- Services: 72vh dark mini hero; dark highlights and Germany; Italy light; UK dark; Czech light; Lithuania dark; Latvia light; Slovakia/Russia dark; GCC light; services/process/FAQ/source review; dark footer. Publication/status handling remains as-is.
- About: 72vh dark mini hero; story (light), mission (dark), values (navy), Kodagu (light), team (light), FAQ/source review, dark footer. Each section selector and exact declarations are captured in the inventory.
- Contact: 88vh dark mini hero; contact form/details and FAQ; dark footer. Fields and delivery are not altered or submitted.

## Template comparison

| Template | Baseline differences from reference | Stage 1 decision |
| --- | --- | --- |
| Destination | 800px container including 60px gutters; centered article hero; all-dark long body; outlined pill; dark FAQ/author blocks | Germany only: reference-width outer grid, 70ch light reading lane, restrained dark hero; remove pill shape without changing its text |
| Place | Same article-shell drift and dark long body, 800px container; authored editorial/process/FAQ blocks | Mysuru only, same shared system |
| Blog index | 1200px outer grid; dark two-column cards, 18px radius, transforms/glow and tag pills | Light reference-style card grid, normal text categories, stable cards |
| Article | Centered 44/30px hero, dark long body, smaller 28px h2, gold links and dark tables | Choosing-consultant article only; short static hero, light prose/tables and reference serif hierarchy |
| Privacy / terms | Dark article-like legal text | Audit only; unchanged until owner approval |
| 404 | Existing utility treatment and discovery rules | Audit only; unchanged |
| All pages | Existing directory shell and grouped links | Audit only; unchanged |

## Scene implementation and loading

Home, Services, About and Contact load Three.js r128, GSAP 3.12.2 and ScrollTrigger 3.12.2 using three deferred CDN scripts. Exact npm-mirror sizes: Three 603,113 bytes; GSAP 71,187 bytes; ScrollTrigger 42,334 bytes (CDP transfer accounting adds synthetic response overhead in the local lab). No scene image assets exist initially. The chosen consultant article declares the reference font families but does not load the font stylesheet; its baseline therefore uses fallback fonts. This must be corrected without adding a render-blocking resource on the pilot. Font CSS is render-blocking and requests Outfit and Cormorant Garamond with display=swap. Script URLs are exhaustive in the token inventory.

Home uses a fixed full-window WebGL canvas, 1600/500 far stars and 500/150 middle stars desktop/mobile, a wireframe globe/rings, orbiting caps, books and helix, with CSS vignette/nebula/grain and desktop floating SVGs. About/Services/Contact each have their own scene code. Existing reference render loops are requestAnimationFrame-driven; resize listeners update the renderer; mobile reduces object counts. Their source does not provide the new pilot Save-Data/hidden-tab guarantees. Do not silently rewrite these immutable reference scenes. The new global OFF switch may disable them explicitly; the default remains unchanged.

Pilot tiers must add no WebGL or JS library. Use a static scene still only if it can stay decorative, below 120KB per size and outside LCP, with a zero-resource palette fallback for JS-off/Save-Data. No parallax is needed. Articles use a shorter static hero. Other routes remain unopted-in.

## Team inventory

Home: `#team .testi-grid` (three desktop columns, two at 769-1024px, one at <=768px), `.testi-card`, 40px desktop padding / 32px 26px mobile, original 16px radius and glass treatment. Photos are 96px circles. About: `.team-grid` three columns (two <=700px, one <=600px), 28px gap, 40px 32px padding, original 20px radius; photos 88px circles. About cards have centered names/titles and justified 14px bios; Home uses 15px bios. Preserve these layouts, photos, crops, names, titles and alt text. Grid auto rows currently make desktop cards equal within each row; one-column rows are content-sized, so equal-card-height treatment may be needed inside the authorized team area.

The full Jabir, Fawaz and Zaheer descriptions live in canonical Person data; About FAQ answers retain full bios, and both LLM files retain full descriptions. There is no separate long-form team biography section beyond those About FAQ answers; do not invent one or shorten those answers. The card paragraphs are the only replacement locations.

| Exact supplied card | Characters including spaces and punctuation |
| --- | ---: |
| Jabir KJ | 127 |
| Zaheer KJ | 130 |
| Fawaz BH | 126 |

Spread = 4, within the required maximum of 6. No wording changes needed.

Actual baseline card sizes at all requested widths: [phase-25-before-layout.json](phase-25-before-layout.json).

## Baseline local measurements

Three cold Lighthouse mobile simulated Slow 4G / 4x CPU navigations per route. PHP 8.5 WASM adapter, Chromium 143, Lighthouse 12.8.2. External hosts are unavailable in this sandbox: exact JS versions and same font families/weights are mirrored from npm; production-absolute images are served from this checkout. This is a reproducible **local lab**, not production transfer compression, field CWV, native Apache/LiteSpeed, real CDN availability or contact-delivery evidence. Resource transfer figures are CDP-reported under those synthetic responses. All sample values, script payloads, render-blockers, LCP element and medians: [phase-25-before-metrics.json](phase-25-before-metrics.json). Blog index is included additionally so every pilot has a baseline.

## Baseline screenshots

All four references and four future pilots were captured at 360, 768 and 1280px, height 900px, full-page. Motion is frozen and deterministic seeded scene geometry used solely by the capture harness, so frame timing cannot be mistaken for reference changes. Same-font npm mirrors are used; these are not actual Google Fonts network responses. Files: `reports/screenshots/phase-25/before-{home,services,about,contact,germany,mysuru,article,blog}-{360,768,1280}.png`. Screenshot completion and dimensions are recorded in the baseline layout JSON. No reference source was changed.

### Measured baseline medians

| Route | Transfer bytes | Requests | LCP ms | CLS | TBT ms |
| --- | ---: | ---: | ---: | ---: | ---: |
| `/` | 1068530 | 15 | 9500.89 | 0.000779 | 2075.0 |
| `/services` | 1093133 | 15 | 2105.1 | 0 | 2440 |
| `/contact` | 1049871 | 15 | 1939.86 | 0 | 3541.5 |
| `/study-in-germany` | 230549 | 8 | 1592.01 | 0.053536 | 0 |
| `/study-abroad-counselling-mysuru` | 226502 | 8 | 1588.47 | 0.04556 | 0 |
| `/blog/how-to-choose-study-abroad-consultant-karnataka` | 143512 | 2 | 2182.25 | 0 | 50 |
| `/blog/` | 211307 | 7 | 2182.74 | 0.102867 | 0 |

Screenshot harness correction before Task 1 checkpoint: complete the finite reference GSAP reveals before freezing motion. Chromium/SwiftShader can repeat full-page tiles above 8192px; screenshots are stitched from real 900px viewport rasters to prevent that artifact. Fixed navigation appears only in the top tile. This changes capture technique only, not site source. The identical technique will be used after edits.
