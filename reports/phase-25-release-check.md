# Phase25c current release check

**NOT READY FOR LIVE DEPLOYMENT.** Local verification/reporting tasks are checkpointed; required performance gates and native/proof readiness still FAIL. No merge, main push, deployment, submission or outreach. No public presentation/source changes in Phase25c.

Date2026-10-23. PR: https://github.com/fawazbhseo/ilmerastudyabroad/pull/1 . Session branch `arena/48320ee5-ilmerastudyabroad`. One final full verification cycle used of the permitted two. No fourth performance reliability session. The structural/noise gate, strict sub0.1px chrome tolerance,404 short-footer acceptance and report-only reference a11y instructions supersede the older Stage2 criteria retained below.

## Current acceptance matrix

| Check | Result | Evidence / limits |
|---|---|---|
| PHP lints, units,43 renders, strict wording/discovery/sitemap/schema/source/LLM/overlap | PASS | 35 check groups; existing guards not weakened |
| 43-route text/order/links/image-content/JSON-LD invariants | PASS | Exact Phase24b except approved team bios; prior five header loading=eager timing attributes disclosed |
| Browser JSon/off360/768/1280 | PASS | 258 cases, 1278 FAQ interactions, 36 photo checks, 54 derivative loads |
| Reference source and rendered HTML immutable | PASS | Four source files byte-exact Stage1; fresh HTML SHA values unchanged since Task1 |
| Reference structural and calibrated pixel gate | PASS | 12/12 PASS,0 structural diffs; all current maxdelta0/SSIM1; no source change |
| Header/footer geometry | PASS | 120/120 PASS, max tolerated0.016px strictly below0.1px;404 abbreviated footer accepted |
| Rebuilt palette/contrast/a11y | PASS | 42 rebuilt axe cases0 violations;9 explicit palette/state pairs>=4.5 |
| Light reading areas, no fully-dark rebuilt pages or overflow | PASS | 117 region/width cases; first posthero and longform light, at most one dark accent |
| Font failure-condition body/glyph visibility | PASS | 14 local HTTP-font-blocked JSon/off conditions; inline destination has no HTTP font dependency, not font-decode-failure proof |
| Reference report-only a11y/overflow inventory | PASS | All24 groups/387 original+4 fresh node instances (391 total),5 reproduced layout-overflow cases reported; not fixed |
| One hero tier/font method per whole template | PASS | 9 destination/17 place/8 article plus other rebuilt templates, held members included |
| Task2 performance reliability and unchanged budgets | FAIL | FAIL: all3 sessions unreliable; final14 routes7A/7B; nine of ten rebuilt raw passes, Choosing LCP FAIL; reference Services LCP/TBT and Contact/About TBT FAIL |
| Reliable proof of fallback necessity/validated font-gate repair | FAIL | Not established by unreliable controls; current whole-template conservative policy retained without speculative source edit |
| Native Apache/LiteSpeed and live deployment readiness | FAIL | No native rewrite/ACL/cache/MIME/CSP/runtime-layout/contact-delivery/backup-restore or actual certificate proof; prior blockers retained |

## All12 reference results

| Reference |360|768|1280|
|---|---|---|---|
| home | PASS:0 structural diffs, delta0, SSIM1 | PASS:0 structural diffs, delta0, SSIM1 | PASS:0 structural diffs, delta0, SSIM1 |
| services | PASS:0 structural diffs, delta0, SSIM1 | PASS:0 structural diffs, delta0, SSIM1 | PASS:0 structural diffs, delta0, SSIM1 |
| about | PASS:0 structural diffs, delta0, SSIM1 | PASS:0 structural diffs, delta0, SSIM1 | PASS:0 structural diffs, delta0, SSIM1 |
| contact | PASS:0 structural diffs, delta0, SSIM1 | PASS:0 structural diffs, delta0, SSIM1 | PASS:0 structural diffs, delta0, SSIM1 |

About360 baseline self-noise: maxdelta3, up to505576 differing pixels, minimum SSIM0.999324385. Current is exact. Full3-pair per-case floors and structures: phase-25c-reference-gate.md/JSON and phase-25c-structures/. This is calibrated capture noise, not a shared-CSS defect or a waiver of any real structural difference.

## New seven-by-seven performance table

### Method and complete results

**Local simulated Lighthouse data only. Not field data, actual CDN timing or native/live hosting proof.**

Immutable Stage1 HTML is A for the four references; immutable Phase24b HTML is A elsewhere. Independently frozen current HTML is B. Both use the same HTTP document/static fixture server and exact npm CDN mirrors. Each sample uses a fresh isolated-profile Chromium process, standard Lighthouse mobile simulated Slow4G/4x CPU, storage reset, serial execution. Seven A and seven B per completed route. Round0 A/B, round1 B/A, alternating through round6. No other browser/capture/QA benchmark runs overlap. Shared-host scheduling and software GPU remain limitations.

IQR is Q3 minus Q1, with linear-interpolated sample quartiles. JSON retains quartiles, every raw sample, passive LCP DOM/font/gate events, and failed or incomplete sessions. Disabling the oversized **post-trace report screenshot** in reruns does not disable page animations or alter the A/B throttling or metric budgets. Each arm within a session uses identical settings.

Reliability: every reference must have max(A/B,B/A) median LCP ratio<=1.10, a conservative symmetric reading. No tolerance added to the actual route budgets: added transfer<150000B, no new external blocking request, CLS<=A AND<0.1, LCP<=1.10A, TBT<=A+50ms. A control failure invalidates certification of that session, including otherwise numerically passing routes.

## Retained sessions

| Session | Completeness | Control symmetric ratios | Reliable |
|---|---|---|---|
| 1 | 24 samples, 1 complete routes | /=4.9769 | NO |
| 2 | 56 samples, 4 complete routes | /=1.0095, /services=1.0038, /contact=5.4517, /about=1.0164 | NO |
| 3 | 196 samples, 14 complete routes | /=5.0419, /services=4.8435, /contact=1.0200, /about=1.0089 | NO |

## Session3 table: UNRELIABLE, NOT CERTIFIED

Cells show **median [IQR]**. Bytes are raw local transfer totals; added bytes are B minus A. Ratios and tests use unrounded values. No baseline relabelled or failed sample deleted.

| Route | LCP A ms [IQR] | LCP B ms [IQR] | B/A | Transfer A/B [IQR] B | Added B | CLS A/B [IQR] | TBT A/B ms [IQR] | New blocking | Verdict |
|---|---:|---:|---:|---|---:|---|---|---:|---|
| `/` | 9292.3 [7723.8] | 1843.0 [3716.6] | 0.1983 | 1068515 [0] / 1068515 [0] | 0 | 0.000769 [0.000005] / 0.000769 [0.000015] | 1761.0 [586.0] / 1773.0 [237.0] | 0 | NOT CERTIFIED (raw PASS) |
| `/services` | 1997.1 [7635.6] | 9672.8 [7846.7] | 4.8435 | 1093114 [0] / 1093114 [0] | 0 | 0.000000 [0.003797] / 0.000000 [0.000000] | 1946.0 [334.3] / 2209.0 [345.8] | 0 | FAIL: lcp,tbt |
| `/contact` | 10786.9 [975.1] | 11002.5 [4752.7] | 1.0200 | 1049851 [0] / 1049851 [0] | 0 | 0.000000 [0.000000] / 0.000000 [0.000000] | 3399.5 [967.5] / 3621.5 [616.8] | 0 | FAIL: tbt |
| `/about` | 9147.1 [179.5] | 9228.7 [171.9] | 1.0089 | 1047496 [0] / 1047496 [0] | 0 | 0.007303 [0.001027] / 0.006758 [0.003311] | 1661.0 [238.0] / 1826.0 [222.5] | 0 | FAIL: tbt |
| `/study-in-germany` | 3037.7 [195.3] | 1147.4 [53.4] | 0.3777 | 230530 [0] / 199991 [0] | -30539 | 0.053536 [0.025454] / 0.000000 [0.000000] | 0.0 [0.0] / 0.0 [0.0] | 0 | NOT CERTIFIED (raw PASS) |
| `/study-in-italy` | 2919.3 [120.2] | 1172.6 [50.0] | 0.4017 | 228478 [0] / 197938 [0] | -30540 | 0.055367 [0.018332] / 0.000000 [0.000000] | 0.0 [0.0] / 8.5 [39.5] | 0 | NOT CERTIFIED (raw PASS) |
| `/study-in-gcc` | 3068.7 [135.0] | 1313.2 [88.6] | 0.4280 | 239266 [0] / 208727 [0] | -30539 | 0.042830 [0.014711] / 0.000000 [0.000000] | 0.0 [0.0] / 0.0 [12.8] | 0 | NOT CERTIFIED (raw PASS) |
| `/study-abroad-counselling-mysuru` | 2918.7 [1.5] | 1652.4 [315.7] | 0.5662 | 226483 [0] / 233615 [0] | 7132 | 0.045560 [0.020526] / 0.000000 [0.000000] | 0.0 [0.0] / 0.0 [0.0] | 0 | NOT CERTIFIED (raw PASS) |
| `/study-abroad-counselling-bengaluru` | 2918.5 [63.2] | 1652.4 [314.8] | 0.5662 | 226586 [0] / 233718 [0] | 7132 | 0.073798 [0.053247] / 0.000000 [0.000000] | 0.0 [0.0] / 0.0 [0.0] | 0 | NOT CERTIFIED (raw PASS) |
| `/blog/how-to-choose-study-abroad-consultant-karnataka` | 1031.3 [64.3] | 2280.9 [314.3] | 2.2117 | 143493 [0] / 241184 [0] | 97691 | 0.000000 [0.000000] / 0.000000 [0.000000] | 0.0 [11.5] / 0.0 [3.0] | 0 | FAIL: lcp |
| `/blog/documents-needed-to-study-abroad-from-india` | 3187.3 [121.0] | 1802.9 [628.7] | 0.5657 | 233830 [0] / 255209 [0] | 21379 | 0.032218 [0.010288] / 0.000000 [0.000000] | 0.0 [0.0] / 0.0 [0.0] | 0 | NOT CERTIFIED (raw PASS) |
| `/blog/` | 2771.1 [270.4] | 1654.1 [628.6] | 0.5969 | 211288 [0] / 232579 [0] | 21291 | 0.102867 [0.031043] / 0.000000 [0.000000] | 0.0 [0.0] / 0.0 [0.0] | 0 | NOT CERTIFIED (raw PASS) |
| `/privacy-policy` | 2993.3 [161.9] | 1652.5 [351.8] | 0.5521 | 231468 [0] / 229212 [0] | -2256 | 0.058473 [0.029236] / 0.000000 [0.000000] | 0.0 [0.0] / 0.0 [0.0] | 0 | NOT CERTIFIED (raw PASS) |
| `/all-pages` | 2769.5 [140.2] | 1652.3 [389.8] | 0.5966 | 203636 [0] / 224963 [0] | 21327 | 0.022408 [0.000000] / 0.000000 [0.000000] | 0.0 [0.0] / 0.0 [11.0] | 0 | NOT CERTIFIED (raw PASS) |

## Decision

All permitted reliability attempts exhausted. No further performance retry or baseline/budget relaxation.
**Performance acceptance: FAIL / not certified.** Reference HTML A/B hashes are byte-identical, yet the reference medians can show large simulated variance. This is not proof of a reference design/source regression or a measured live improvement. It does prevent a release performance sign-off. Required native hosting, backup/restore, contact delivery, certificate/source and deployment blockers remain open.


## Final whole-template tiers

| Template | Count | Hero | Fonts |
|---|---:|---|---|
| Destination, including held |9| Plain reference navy | Inline two matching variable faces, retained; necessity not re-certified |
| Place |17| Reference-palette gradient | Selfhost seven static reference weights, two abovefold preloads |
| Article, including held |8| Reference-palette gradient | Same selfhost method across all articles |
| Blog index |1| Reference-palette gradient | Selfhost |
| Legal |2| Reference-palette gradient | Selfhost |
| Directory |1| Reference-palette gradient | Selfhost |
|404/error |1| Reference-palette gradient | Selfhost |
| References |4| Original unchanged | Original unchanged |

Global scene switch retained; generated stills disabled/unreferenced. Full route membership, actual LCP nodes/fonts and gate analysis: phase-25c-template-diagnosis.md/JSON. No reliable necessity proof or validated new font-gate repair is claimed.

## Every remaining deviation, exception and blocker

1. **Performance not certified:** all3 allowed control sessions unreliable. Final Home symmetric ratio5.0419 and Services4.8435 exceed1.10. Choosing article raw LCP2280.9ms vs1031.3ms (2.2117x) also fails; Services raw LCP/TBT, Contact/About raw TBT fail. All results remain failures, not noise-waived budget passes. Nine rebuilt raw passes cannot certify the session.
2. **Fallback necessity/repair unproven:** all9 destinations retain plain/inline conservatively. Shared all-font-set paint gate is a plausible cost centre; no unique German markup defect proved and no speculative gate change committed. A heavier default tier was not newly certified.
3. **Reference contrast report-only:**24 original finding groups/387 original+4 fresh node instances (391 total) remain, with selector, foreground/background, ratio vs4.5 and minimal existing-palette suggestions. None applied.
4. **Reference numerical layout overflow:** Home360/768 hidden team reveal translateX60 yields+40px, About360/768 hidden stats reveal translateX55 yields+33px, Contact360 hidden info reveal translateX60 yields+36px. Effective opacity0, body clipping and wheel scrollX0 observed; start-state scrollWidth excess persists after returning to top. Not a scene/pixel-noise issue and not claimed fixed or harmless in every possible animation frame. Fresh AA Contact360 width395px versus396px in the dedicated probe is a1px frame variation of the same case.
5. **404 abbreviated footer accepted:** original words/links retained; not full reference footer. Header still matches.
6. **Subpixel chrome accepted:**1318 individual values differ strictly below0.1px, max0.016px. No>=0.1px or non-geometric mismatch after active-state normalization. Initial colour-transition normalization artifact retained externally and corrected in the harness, not source.
7. **Reference gutter differences retained:** rebuilt chrome follows canonical Home20px mobile gutter; About/Contact references retain22/24px and are compared with their own immutable baselines.
8. **44px reference-pitch constraint:** stacked footer links/contact rows retain legacy pitch below44px to avoid overlapping invisible hit areas; other invisible extensions preserve reference paint. Existing reference small targets are not redesigned.
9. **Five existing header timing-only attributes:** first logo loading=eager on404 and four held pages is the prior accepted presentation timing delta from Phase24b. Image bytes/URLs/alt/dimensions/styles unchanged. No Phase25c image changes.
10. **Representative/local performance only:**14 requested-plus-About routes, not field/live proof or every one of43 pages.404 has no separate performance navigation; all-pages is its utility-family representative. Exact npm CDN mirrors and equal HTTP fixture delivery do not model real CDN/native cache/MIME/CSP/HTTP transport. Shared-host/software GPU scheduling remains a limitation.
11. **JSoff instrumentation scope:** primary browser disables application JS; axe uses its serialized app-script-stripped DOM in a separate instrumentation-only context. Functional browser blocks external requests and finishes finite animations before geometry. No native/live claim from this method.
12. **Font failure scope:**14 HTTP-font-blocked JSon/off conditions show visible body/glyphs. Inline destination has no HTTP font dependency, so this is not corrupt/decode/CSP-font failure proof. Seven future native font/cache URLs remain below in historical evidence; local adapter cannot prove native headers.
13. **Native/proof go-live blockers:** no native Apache/LiteSpeed rewrite/404 invocation/ACL/cache/MIME/CSP/private-runtime-layout/contact-delivery proof or full backup/restore test. Actual registration certificate remains unavailable. All earlier registration, fees/payment/refund, reviews, scope, source/fact-verification and held-publication blockers stay open; no private certificate/contact/address/NIC details exposed.
14. **Deployment exclusions:** tools/reports/Git/runtime caches and test fixtures are not website upload material. Private-runtime/deny enforcement and deployment layout remain unverified. No merge/main push/deploy or account/submission/outreach action.

## Every changed file

Exact Phase25c manifest (all paths, no omissions): [phase-25c-changed-files.md](phase-25c-changed-files.md). Historical Stage2 manifest is preserved below.

**Plain-language readiness:** the reference layout and chrome gates now pass under the authorized rules, but performance cannot be signed off and the article LCP failure remains unresolved. Do not deploy this branch. Further reliable performance evidence/validated whole-template repair and all native/backup/proof approvals are required.

<!-- PHASE25C_HISTORY -->

# Phase25 Stage2 release check

**Decision: NOT READY FOR DEPLOYMENT.** Local rollout and owner review package completed; acceptance failures below remain failures. No merge, main push, deployment, submission, account action or outreach. PR: https://github.com/fawazbhseo/ilmerastudyabroad/pull/1 . Session branch: `arena/48320ee5-ilmerastudyabroad`.

Date:2026-10-23. Stage1 boundary:`3f0e1417845291097c22e0fd02e0641752a48dd7`. Existing Stage1 evidence and prior blockers retained.

## Acceptance matrix

| Criterion | Result | Evidence / limits |
|---|---|---|
| Template rollout | PASS |39 non-reference routes;9 destinations,17 places,8 articles,index,privacy,terms,directory,404. Four references excluded. |
| Text/headings/order/links/images/schema | PASS with timing disclosure |43 exact Phase24b semantic comparisons, except previously approved six card bios. Image bytes/URLs/alt/dimensions/style exact; only first-header-logo loading=eager added on5 formerly unprocessed pages. |
| Protected business/publication/proof data | PASS | Original held article hashes, post metadata and33 protected records exact. Link-helper original prefix exact; presentation-only held integration appended. |
| Lint/renders/policy/discovery/SEO | PASS local | PHP lint;43 renders/126 schema FAQ pairs; publication/robots/self-canonicals/sitemap/no held discovery/broken-link/schema/strict wording/LLM parity; source hashes and overlap guards. |
| Browser functionality | PASS stated method |258 JS-on/off browser cases at360/768/1280;1278 FAQ interactions,36 team image and54 derivative-load checks. External requests aborted in this inherited geometry runner; finite animations finished before geometry assertions. |
| Approved team work | PASS source scope | Six exact card paragraphs; lengths127/130/126 characters, spread4. Photos/names/titles/alt/full bios/schema/About FAQ/LLMs unchanged. Raw team-region deltas retained and attributable to the already approved bio/card work, not a general mask waiver. |
| Palette/light-dark/readability | PASS rebuilt |117 region/width cases: first posthero light, longform light, not fully dark, at most1 dark accent; no overflow. Two design families; main radius tokens3px/12px. Original chrome circles preserved. No generated still referenced. |
| Header markup | PASS |43/43 after active-state normalization. |
| Full footer markup/height | FAIL404 |42/43 full footers match.404 keeps its original abbreviated content; adding full footer would violate immutable words/links/images. |
| Visible chrome property equality | FAIL declared subpixel case | Final destination inline fallback yields Germany1280 nav-links auto-margin222.750px versus Home222.734px, about0.016px. Other full-footer route comparisons match;404 shortened-footer differences retained. No tolerance quietly added. |
|44px controls | EXCEPTION under decisionD | Invisible extensions preserve painted chrome where non-overlapping. Stacked footer links/contact rows keep reference pitch below44px. Reference legacy targets remain unchanged. |
| Axe A/AA | PASS rebuilt samples; FAIL immutable references |42 rebuilt template/width/scripting cases0 violations; final destination fallback6 cases0.24 reference cases each retain a contrast finding. JS-off method disclosed below. |
| Motion-on reference overflow | FAIL legacy cases | Five sampled transient reference overflow cases;0 rebuilt cases. References not redesigned to conceal them. |
| RuleC reference raster | FAIL | About360 exceeds both limits; exact figures below. No waiver for larger unchanged-source noise. |
| Performance | PASS7 rebuilt samples; FAIL overall | Strict budgets unchanged. Final Services control fails LCP. Initial Contact failure retained. All rebuilt CLS0; no new blocking resource. |
| Font failsafe | PASS local |14 blocked-HTTP-font JS-on/off samples show visible body and painted heading glyphs. Destination now has measured inline fallback with no HTTP font dependency. |
| Cache/MIME policy source | PASS source only | Additive font-directory IfModule rules; root.htaccess byte-exact. Local adapter7 font HEADs200/font/woff2, no native cache header proof. |
| Native hosting / backup / live delivery | UNVERIFIED, BLOCKED | No native Apache/LiteSpeed rewrite/ACL/cache/MIME/CSP proof, contact-delivery proof, production runtime-layout enforcement or full backup/restore test. Actual registration certificate unavailable; all earlier proof/fees/review/scope/source blockers preserved. |

## Final tiers and switches

| Template | Routes | Final hero | Font method |
|---|---:|---|---|
| Destination |9| Plain reference navy | Measured inline escape hatch only for this failing template |
| Place |17| Reference-palette gradient | Self-hosted exact Latin reference weights |
| Article, including2 held |8| Reference-palette gradient | Self-hosted |
| Blog index |1| Reference-palette gradient | Self-hosted |
| Legal |2| Reference-palette gradient | Self-hosted |
| Directory |1| Reference-palette gradient | Self-hosted |
|404/error |1| Reference-palette gradient | Self-hosted |
| Four references |4| Original heroes unchanged | Original font loading unchanged |

`ILMERA_SCENES_ENABLED=true` is the normal sitewide setting. False hides existing scene/decorative layers, removes the external Three.js dependency and applies plain reference-navy heroes, including references, while leaving all text/links/images/schema/statuses unchanged. Default ON does not inject shared CSS/fonts into references. Generated stills remain disabled/unreferenced in either state. No per-page inline font data by default: only destination is in the measured fallback lists. Directory/error have separate fallback keys; no blanket utility fallback.

Self-hosted pages preload only Outfit300 and Cormorant700. Seven exact static Latin weights are available on demand. Metric fallback aliases are system fallback adjustments, not extra design families. FontFaceSet-ready text paint has an error/3s failsafe; script-disabled pages never acquire the hidden class. Destination fallback embeds the existing two variable Latin faces, no font preload URLs. Idempotence, switch on/off, fallback and arbitrary ErrorDocument-URI fixtures pass. Native ErrorDocument invocation itself is not proved.

## Performance before / final after

Local PHP8.5 WASM, Chromium143, Lighthouse12.8.2 mobile Slow4G/4x CPU simulation; exact-version npm mirrors, not live CDN/native hosting. Three storage-reset navigations per route; medians. Original seven-route prefix retained: Home,Services,Contact,Germany,Mysuru,choosing article,blog; then documents article,privacy,all-pages. Original seven Stage1 values are immutable. The three added-page before samples replay immutable pre-rollout HTML, clearly supplemental rather than invented Stage1 measurements. Main-document delivery differs; comparison remains local-only.

Budgets: added transfer<150000bytes; no added render-blocking URL; CLS<=baseline and<0.1; LCP<=110% baseline; TBT<=baseline+50ms. No weakened threshold.

| Route | LCP ms before / after | CLS before / after | TBT ms before / after | Bytes before / after | Added bytes | Requests before / after | Result |
|---|---:|---:|---:|---:|---:|---:|---|
| Home | 9500.889 / 1922.652 | 0.000779459 / 0.000759213 | 2075.0 / 581.0 | 1068530 / 1068534 | +4 | 15 / 15 | PASS |
| Services | 2105.098 / 8941.540 | 0.000000000 / 0.000000000 | 2440.0 / 1376.0 | 1093133 / 1093133 | +0 | 15 / 15 | FAIL |
| Contact | 1939.857 / 1893.258 | 0.000000000 / 0.000000000 | 3541.5 / 1480.0 | 1049871 / 1049871 | +0 | 15 / 15 | PASS |
| Germany | 1592.006 / 1181.228 | 0.053536100 / 0.000000000 | 0.0 / 3.0 | 230549 / 200010 | -30539 | 8 / 4 | PASS |
| Mysuru | 1588.466 / 1652.165 | 0.045559560 / 0.000000000 | 0.0 / 0.0 | 226502 / 233606 | +7104 | 8 / 6 | PASS |
| Choosing article | 2182.251 / 2280.590 | 0.000000000 / 0.000000000 | 50.0 / 0.0 | 143512 / 241176 | +97664 | 2 / 6 | PASS |
| Blog index | 2182.743 / 2280.591 | 0.102866511 / 0.000000000 | 0.0 / 0.0 | 211307 / 232570 | +21263 | 7 / 6 | PASS |
| Documents article* | 2310.000 / 1801.618 | 0.002173099 / 0.000000000 | 0.0 / 0.0 | 233700 / 255194 | +21494 | 8 / 7 | PASS |
| Privacy* | 2160.000 / 2280.625 | 0.058472851 / 0.000000000 | 0.0 / 0.0 | 231338 / 229203 | -2135 | 8 / 6 | PASS |
| All pages* | 2160.000 / 1651.540 | 0.019660750 / 0.000000000 | 0.0 / 0.0 | 203506 / 224954 | +21448 | 7 / 6 | PASS |

*Supplemental before baseline; no Stage1 measurement existed for these three pages. No separate404 performance navigation was requested/measured; all-pages is the utility sample, not proof of every page.

Initial default selfhost/gradient Germany LCP2430.752ms failed1751.207ms cap. Only destination dropped to plain navy plus authorized inline fonts; final1181.228ms, CLS0, TBT3ms,200010bytes passes every budget. Other rebuilt templates retain gradient/selfhost. Initial Contact control8786.532ms/.004813818 failed; final Contact passes, while final unchanged Services8941.540ms fails2315.607ms cap. These swings are local variance, not a source-driven reference speedup or accepted budget waiver. Both candidates and all90 navigation samples retained. No unchanged-control retry to pursue green. Reference tier drop would violate decisionB, so that failed control stays failed.

Raw: `phase-25-stage-2-before-extra-metrics.json`, `phase-25-stage-2-after-metrics.json`, `phase-25-stage-2-after-performance.json`, `phase-25-stage-2-fallback-metrics.json`, `phase-25-stage-2-fallback-performance.json`. All seven rebuilt final samples have no new blocking resource; greatest added transfer is97664bytes on choosing article.

## Four-reference raster results

Outside the approved team region: max channel delta2 AND changed pixels<=0.01% of page. Inside: only previously approved bios/equal-height card work; exact approved source/content/assets checked independently. Control captures precede those approved bios; raw team-region differences retained in `phase-25-stage-2-team-region-raster.json`.

| Reference |360|768|1280|
|---|---|---|---|
| Home | PASS: 0px, max0 | PASS: 0px, max0 | PASS: 0px, max0 |
| Services | PASS: 0px, max0 | PASS: 0px, max0 | PASS: 9px, max1 |
| About | FAIL: 501067px, max3 | PASS: 0px, max0 | PASS: 0px, max0 |
| Contact | PASS: 0px, max0 | PASS: 0px, max0 | PASS: 9px, max1 |

About360:501067 changed pixels,9.9439364%, max3. Not accepted. Controlled unchanged-source repeat also failed About768:687822pixels,9.7210633%,max4. Initial/noise-corrected reports preserved. Nine1-level CTA-corner pixels reproduced on unchanged source and appear on final Services/Contact1280; they meet the owner rule and are not attributed to shared CSS, which references never receive. Home final is0 at all widths. Larger About noise remains an acceptance failure even though source/HTML is unchanged; no shared-style deviation has been demonstrated or hidden by a relaxed threshold.

## Accessibility, cycles and deviations

Three bounded cycles used; cycle2 resumes only its repaired guard/tail, not a reset allowance. Original held-source and protected-metadata guard failures were corrected without changing review records or relaxing their hashes. Directory DIV target was corrected in the visual intro matcher and region probe. Legal links gained underlines; dark-region focus gains palette contrast. Final cycle3 retests changed destination AA/chrome plus fresh43-route/protected-data/discovery/SEO guards. No further cycles or repeated immutable-reference pursuit. See `phase-25-stage-2-cycles.md`.

True JS-off primary contexts supply layout/visibility/keyboard evidence. Axe cannot complete asynchronously with scripting disabled, so it audits that serialized DOM in a separate instrumentation-only context with all application scripts removed and noscript children retained. This is not a claim that application JS was enabled. Menu open/Escape tested JS-on; JS-off retains original navigation behavior and reachable links. Reduced motion tested; browser geometry runner finishes finite animations, while the expanded reference audit records motion-related transient overflow rather than hiding it.

Complete deviations/limitations:

1. RuleC fails larger About360 renderer differences; unchanged-repeat noise is not a blanket waiver.
2.404 full footer markup/height cannot match without forbidden added words/links/image. Original shortened contents retained and reference bottom-row styling applied.
3. Destination inline-font fallback produces approximately0.016px desktop nav auto-margin difference at1280; all other full-footer comparisons match. This is a recorded exactness failure, not rounded into PASS.
4. Canonical rebuilt footer gutters follow Home20px mobile; references themselves vary20/22/24px and remain unchanged.
5. Stacked reference footer links/contact targets remain below44px to avoid overlapping invisible hit areas; exact reference pitch wins under decisionD.
6. First header logo gets loading=eager on404 and four held pages only. This is fetch-timing metadata, no image content/URL/alt/dimension/style change.
7. Destination-only plain/inline tier is the measured conditional budget fallback, not the default or an unmeasured global inline-font revert.
8. Immutable references retain24 sampled axe contrast findings and five motion-on transient overflow cases. No redesign authorized under A/C.
9. Services final control fails performance; Contact initial failure retained. References not modified to chase simulated timing variance; thresholds unchanged.
10. Three supplemental before baselines use immutable-HTML replay;404 is not separately performance-sampled. All figures are local simulated medians, not field/hosting data.
11. Native Apache/LiteSpeed cache/MIME/CSP/ACL/rewrite, private runtime layout, delivery, backup/restore and certificate proof remain unverified. Existing registration/fees/reviews/scope/source blockers stay open.

## Exact live font/cache test URLs

URLs to verify only after a separately approved deployment, not claims that these branch files are live. Expected native status200, Content-Type font/woff2, Cache-Control public,max-age=31536000,immutable; verify CSP permits self fonts and the authorized data fallback. Local adapter HEAD results200/font/woff2 only; cache headers absent because it does not execute.htaccess. Root.htaccess unchanged; font-child mod_mime/mod_headers directives guarded and additive.

| URL | Weight / family | Bytes | SHA256 |
|---|---|---:|---|
| https://ilmerastudyabroad.com/assets/fonts/outfit-reference-300.woff2 | 300 Outfit | 13956 | `ef88e74f63ce75b54cce4d5a4087c6f180750b9ebae6ab6e5bf2a9939bf6958f` |
| https://ilmerastudyabroad.com/assets/fonts/outfit-reference-400.woff2 | 400 Outfit | 14032 | `71f028fd2349990b3f8aa643abe767e82e0f596be407ae66f0004ff164121bdb` |
| https://ilmerastudyabroad.com/assets/fonts/outfit-reference-500.woff2 | 500 Outfit | 13528 | `fc9bff941def6d924a71632bd8a93190528872eae6414844f3c367ff948d92fd` |
| https://ilmerastudyabroad.com/assets/fonts/outfit-reference-600.woff2 | 600 Outfit | 14140 | `8cfe15c2c6de6ef8efff3eedbd52a383ac9ef23d6c23f6cd9f9b838f5f37dc36` |
| https://ilmerastudyabroad.com/assets/fonts/outfit-reference-700.woff2 | 700 Outfit | 14060 | `5d5e3734089a74707292ce8a3e186def34cd63e33879f9ac3689a8d8da9d0706` |
| https://ilmerastudyabroad.com/assets/fonts/cormorant-garamond-reference-400.woff2 | 400 Cormorant Garamond | 22908 | `727acdbfd81848bcc9a5c2a6c64ba1b97ba93c69515382785483ce0cc068be08` |
| https://ilmerastudyabroad.com/assets/fonts/cormorant-garamond-reference-700.woff2 | 700 Cormorant Garamond | 22392 | `949a2a601dd37c9aeb888b1ce6ce17383173aaea128af4a16df45e77e6fcd903` |

Font policy file:`assets/fonts/.htaccess`. Before live: full production backup AND restore test, native access-denial/runtime-folder enforcement, rewrite/status/canonical/robots checks, HTTP/cache/MIME/CSP checks, contact-delivery proof and owner acceptance of every unresolved criterion. Do not upload reports/tools/caches/Git/internal evidence. No deploy readiness certification is issued.

## Owner review and task checkpoints

[Contact sheet](phase-25-contact-sheet.md):16 raw-branch full-page1280/360 images, requested order; final destination pilot3 widths refreshed. Lossless decoded RGB checks pass. No new website images.

PR checkpoints: Task1 comment6363879187;2A6363894681;2B6363899664;2C6363912338;2D6363950920;3=6364618908;4=6364917737;5=6365013641. Final Task6 checkpoint follows this report.

Final cycle3 core checks PASS in83.83seconds; PHP files:97. This does not override failed release criteria.

## Every changed file in Stage2

Delta from the fixed Stage1 boundary3f0e141, including report/tool/evidence files. No business-data/image/reference-source rewrite is hidden behind this list.

- `404.php`
- `CHANGELOG.md`
- `assets/css/visual-system.css`
- `assets/fonts/.htaccess`
- `assets/fonts/cormorant-garamond-reference-400.woff2`
- `assets/fonts/cormorant-garamond-reference-700.woff2`
- `assets/fonts/outfit-reference-300.woff2`
- `assets/fonts/outfit-reference-400.woff2`
- `assets/fonts/outfit-reference-500.woff2`
- `assets/fonts/outfit-reference-600.woff2`
- `assets/fonts/outfit-reference-700.woff2`
- `flagged-items-for-verification.md`
- `includes/destination-page.php`
- `includes/links.php`
- `includes/place-page.php`
- `includes/site-presentation.php`
- `includes/visual-config.php`
- `includes/visual-system.php`
- `reports/phase-25-contact-sheet.md`
- `reports/phase-25-release-check.md`
- `reports/phase-25-stage-2-accessibility.json`
- `reports/phase-25-stage-2-after-metrics.json`
- `reports/phase-25-stage-2-after-performance.json`
- `reports/phase-25-stage-2-baseline-noise.json`
- `reports/phase-25-stage-2-before-extra-metrics.json`
- `reports/phase-25-stage-2-checks.json`
- `reports/phase-25-stage-2-chrome.json`
- `reports/phase-25-stage-2-contact-assets.json`
- `reports/phase-25-stage-2-controlled-noise.json`
- `reports/phase-25-stage-2-cycles.md`
- `reports/phase-25-stage-2-fallback-metrics.json`
- `reports/phase-25-stage-2-fallback-performance.json`
- `reports/phase-25-stage-2-final-checks.json`
- `reports/phase-25-stage-2-final-destination-axe.json`
- `reports/phase-25-stage-2-font-assets.json`
- `reports/phase-25-stage-2-font-http-local.json`
- `reports/phase-25-stage-2-initial-privacy-axe.json`
- `reports/phase-25-stage-2-invariants.json`
- `reports/phase-25-stage-2-progress.md`
- `reports/phase-25-stage-2-reference-raster.json`
- `reports/phase-25-stage-2-regions-fonts.json`
- `reports/phase-25-stage-2-team-region-raster.json`
- `reports/screenshots/phase-25-stage-2/after-article-1280.png`
- `reports/screenshots/phase-25-stage-2/after-article-360.png`
- `reports/screenshots/phase-25-stage-2/after-article-768.png`
- `reports/screenshots/phase-25-stage-2/after-blog-1280.png`
- `reports/screenshots/phase-25-stage-2/after-blog-360.png`
- `reports/screenshots/phase-25-stage-2/after-blog-768.png`
- `reports/screenshots/phase-25-stage-2/after-germany-1280.png`
- `reports/screenshots/phase-25-stage-2/after-germany-360.png`
- `reports/screenshots/phase-25-stage-2/after-germany-768.png`
- `reports/screenshots/phase-25-stage-2/after-layout.json`
- `reports/screenshots/phase-25-stage-2/after-mysuru-1280.png`
- `reports/screenshots/phase-25-stage-2/after-mysuru-360.png`
- `reports/screenshots/phase-25-stage-2/after-mysuru-768.png`
- `reports/screenshots/phase-25-stage-2/review-404-1280.webp`
- `reports/screenshots/phase-25-stage-2/review-404-360.webp`
- `reports/screenshots/phase-25-stage-2/review-all-pages-1280.webp`
- `reports/screenshots/phase-25-stage-2/review-all-pages-360.webp`
- `reports/screenshots/phase-25-stage-2/review-article-1280.webp`
- `reports/screenshots/phase-25-stage-2/review-article-360.webp`
- `reports/screenshots/phase-25-stage-2/review-blog-1280.webp`
- `reports/screenshots/phase-25-stage-2/review-blog-360.webp`
- `reports/screenshots/phase-25-stage-2/review-germany-1280.webp`
- `reports/screenshots/phase-25-stage-2/review-germany-360.webp`
- `reports/screenshots/phase-25-stage-2/review-mysuru-1280.webp`
- `reports/screenshots/phase-25-stage-2/review-mysuru-360.webp`
- `reports/screenshots/phase-25-stage-2/review-privacy-1280.webp`
- `reports/screenshots/phase-25-stage-2/review-privacy-360.webp`
- `reports/screenshots/phase-25-stage-2/review-services-1280.png`
- `reports/screenshots/phase-25-stage-2/review-services-360.png`
- `tools/phase25/stage2/accessibility.cjs`
- `tools/phase25/stage2/browser.cjs`
- `tools/phase25/stage2/check.py`
- `tools/phase25/stage2/chrome.cjs`
- `tools/phase25/stage2/contact.cjs`
- `tools/phase25/stage2/contact_assets.py`
- `tools/phase25/stage2/final.py`
- `tools/phase25/stage2/metrics.cjs`
- `tools/phase25/stage2/performance.py`
- `tools/phase25/stage2/policy.php`
- `tools/phase25/stage2/raster.py`
- `tools/phase25/stage2/regions.cjs`
- `tools/phase25/stage2/release.py`
- `tools/phase25/stage2/run.py`
- `tools/phase25/stage2/screenshots.cjs`
