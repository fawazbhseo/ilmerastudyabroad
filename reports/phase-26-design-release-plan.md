# Phase26: later design release, separate from content

2026-10-24. This note stays on arena/48320ee5-ilmerastudyabroad. It is not part of the117-file content payload or the proposed content branch. No design file changed. Content baseline remains164d6de plus the exact short-card exception; current live site is owner-reported Phase13, not changed here.

## Release sequencing and performance limit

First create/review/release the content-only branch in a separately authorized session. Once that content version is live and stable, the owner measures it with PageSpeed Insights as the **before-design** baseline. Measure the same URLs/device categories again after an independently approved design release. Do not compare Phase13-before with design-plus-content-after and attribute the whole difference to design.

The local Phase25c lab controls were unreliable in all three permitted sessions despite identical reference A/B HTML. No fourth local retry, score chasing, baseline relabelling or budget relaxation. Preserve all raw failures. Existing local numbers are not live-host or field proof. The owner will collect PageSpeed Insights before/after results, dates, URLs, mobile/desktop settings and any available field data, retaining every run. If CrUX field data is unavailable, record unavailable, not invented. Do not equate Lighthouse lab TBT with field INP or immediate deployment measurements with a full field-data window.

Keep the existing budgets for review: added transfer<150000B, no new external blocking request, CLS<=baseline and<0.1, LCP<=1.10baseline, TBT<=baseline+50ms. A later approval needs actual comparable evidence, not the current unreliable-control passes.

## Choosing-consultant article

Recheck https://ilmerastudyabroad.com/blog/how-to-choose-study-abroad-consultant-karnataka before and after design. Final local raw LCP was1031.3ms to2280.9ms (2.2117x), an unresolved FAIL, not waived by unreliable controls. Added transfer was97691B. Inspect actual LCP element, font readiness, blocking chain and layout rather than assuming the hero image caused it. The common FontFaceSet gate is a plausible cost centre, not a proven uniquely German fault or validated repair. No speculative font/source change was made in Phase26.

## Template tier decision

Current later-design policy is plain reference navy plus two matching inline variable faces for all9 destination pages, including held pages. All17 places and8 articles, including held pages, use the reference-palette gradient and selfhosted matching fonts; blog/legal/directory/error use that same gradient/selfhost method. This visual inconsistency across templates needs explicit owner review. One hero tier and font method must remain uniform across each entire template, never a country/page-specific exception. Plain/inline necessity was not re-certified by the unreliable lab sessions. Do not silently restore gradients or change fonts without comparable evidence. Stills remain disabled/unreferenced and the global scene switch remains available. Four reference sources stay unchanged except the approved card work.

## Reference accessibility: report only

Retain the24 reference contrast finding groups,387 original affected-node observations plus4 fresh observations (391 total). Full selectors/foreground/background/ratio vs4.5 and palette-only suggestions are in reports/phase-25-reference-a11y.md. No suggestion is applied by this plan or content release.

Retain all5 JS-on numerical layout-overflow cases: Home360 and768 legacy probes report40px extra from hidden testimonial reveal translateX60; About360/768 reports33px extra from hidden stats reveal translateX55; Contact360 reports36px extra from hidden info reveal translateX60, with a35px frame-dependent sample in final QA. Historical exact Phase25 probes use360, not the Phase24b375 verification width. Effective opacity0, clipping and horizontal-wheel scrollX0 were observed in the dedicated probes; do not claim all-frame harmlessness or a fixed issue. These are offscreen reveal-layout effects, not compositor noise. No reference redesign is authorized by this note.

## Future live font/cache URLs

These seven URLs belong to the LATER design release, not the content payload. Do not upload fonts as part of content or claim they are live now.

- https://ilmerastudyabroad.com/assets/fonts/outfit-reference-300.woff2
- https://ilmerastudyabroad.com/assets/fonts/outfit-reference-400.woff2
- https://ilmerastudyabroad.com/assets/fonts/outfit-reference-500.woff2
- https://ilmerastudyabroad.com/assets/fonts/outfit-reference-600.woff2
- https://ilmerastudyabroad.com/assets/fonts/outfit-reference-700.woff2
- https://ilmerastudyabroad.com/assets/fonts/cormorant-garamond-reference-400.woff2
- https://ilmerastudyabroad.com/assets/fonts/cormorant-garamond-reference-700.woff2

After an approved design upload, test GET and HEAD on the real origin:200/no unwanted redirects, Content-Type font/woff2, correct bytes and intended Cache-Control public, max-age=31536000, immutable. Check actual native font-directory IfModule rules are active, not merely present in source. Confirm native CSP permits required selfhost font requests and the deliberately inline data faces where used, without adding broad unsafe exceptions. Test cold/warm load and blocked-font fallback/body visibility. The local adapter did not prove native cache/CSP/MIME headers. Keep originals/licences and root .htaccess rules intact; no design code edit in this phase.

## Other unchanged go-live blockers

Native Apache/LiteSpeed rewrite/404 invocation, ACL/private-runtime layout, MIME/cache/CSP, contact delivery and a full backup/restore remain owner checks. Actual certificate and prior fees/payment/refund/reviews/scope/source approvals remain unresolved. Reports/tools/Git/caches are never website payload. Do not merge PR1, push main or deploy as part of this plan.
