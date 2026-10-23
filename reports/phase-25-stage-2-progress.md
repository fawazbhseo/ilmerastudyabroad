# Phase 25 Stage 2 progress

Owner authorization: 2026-10-23, decisions A-F. Session branch only; PR1. No deployment or merge.

Resume safety: clean checkout fetched and aligned with remote session branch at3f0e1417845291097c22e0fd02e0641752a48dd7. Stage1 report, progress, audit, complete token inventory and git history reviewed. No prior Stage2 checkpoint exists. Baseline renders reconstructed byte-for-byte from the immutable Phase24b capture, not current pages.

## Task status

- Task1 header/footer/fonts: complete.
- Task2A destinations: complete.
- Task2B places: complete.
- Task2C articles/index: complete.
- Task2D legal/utility: complete.
- Task3 verification: completed with declared immutable-reference/404/target deviations; two cycles plus scoped recovery, no all-green release claim. One final cycle remains within the maximum3 if performance changes a template.
- Task4 performance: complete. All seven rebuilt samples PASS after destination-only plain/inline fallback; unchanged Services control FAILS LCP. Overall performance gate remains FAIL, no waiver.
- Task5 owner review sheet: not started.
- Task6 release sign-off: not started.

RuleC replaces the prior zero-tolerance rule by explicit owner authorization, not an automatic test relaxation. First measure two unchanged baseline captures. Exact reference chrome wins over minimum hit size when an invisible extension cannot avoid overlapping adjacent targets. References remain excluded from font and template rollout. Generated stills remain unreferenced.

## Task1 checkpoint

Four pilots re-shot at360/768/1280. Exact visible chrome property comparison with Home passes all12 pilot/width cases (active link colour excluded; unpainted zero-width border colour is not a visible difference). Removed pilot opaque nav, footer gaps, transformed typography and visible hit-size overrides. Original include markup is untouched. Invisible hit extensions apply only where targets cannot overlap. Stacked footer links/contact lines remain at reference pitch, a declared44px exception under decisionD.

Seven self-hosted Latin files supply the exact reference mirror weights: Outfit300/400/500/600/700 and Cormorant400/700. Only Outfit300 and Cormorant700 preload. Metric aliases use system fallback x-height/vertical overrides, not additional design families. Atomic text-paint gate and3s/error failsafe remain; JS-off never receives the hidden class. Font directory has additive IfModule-guarded MIME/cache directives; root.htaccess bytes unchanged. Native caching is not proven locally.

Before runtime edits, two original baseline passes were recorded. About had a larger transient background difference. A controlled repeated calibration (fixed clocks and suppressed repeating decorative timers, harness only) also reproduces9 one-level CTA-corner pixels at exactly the Home Stage1 locations on unchanged About1280, within0.01percent. Home emits no shared stylesheet, so new shared CSS cannot cause its9 corner pixels. Treat those9 within-rule pixels as accepted anti-aliasing noise under decisionC, not a waiver for larger differences. About768 self-noise remains above the rule and will not be claimed accepted. Both raw and controlled noise reports retained.

All43 semantic/source/palette comparisons PASS. Four pilots only remain opted in. Full rollout and bounded verification follow.

## Task2A checkpoint

Destination role now applies at template level to all9 routes (7 published,2 held). Shared held-template startup runs only the visual buffer, not publication/SEO presentation. Held statuses/robots/discovery remain exact. All43 text/order/link/image/JSON-LD/source/palette checks PASS.12 routes currently styled:9 destinations plus the other3 existing pilots. No still URLs or loader emitted.

## Task2B checkpoint

Place role now applies to the shared template: all17 published locations and any held instance without a publication-status condition. Current inventory has no held place route. All43 semantic/source/palette comparisons PASS.28 routes styled; no facts, scope/contact data, internal links or metadata changed.

## Task2C checkpoint

Article role now covers all8 articles, including2 held, and the blog index. Four-route allowlisting and still-tier code are removed; template classification now controls application. Held articles get only visual startup, preserving their original robots/status/schema/copy. All43 exact semantic/source/palette comparisons PASS.35 routes styled.

## Task2D checkpoint

Privacy, terms, all-pages and404 now use shared legal/utility roles. All39 non-reference routes are styled, four references excluded. Legal/directory introductions move to the first light section without changing any token or order.404 splits after its original H1 into hero/light content; its abbreviated footer keeps every original word/link and gains reference bottom-row structure, not invented full-footer content.

Literal header markup now matches the reference after active-link normalization on all43 pages. On five previously unprocessed pages only loading=eager was added to the existing first header logo. Fetch timing is not image content; the strict checker explicitly records this single timing attribute and still requires every image byte/URL/alt/dimension/style and all other attributes unchanged. Footer markup matches on42/43;404 remains the documented content-preservation exception. All43 semantic/source/palette comparisons PASS.

## Task3 checkpoint

Cycle1/2 guard findings were fixed without changing any protected metadata or loosening original hash checks. Both held articles AND includes/posts.php are byte-exact; pure held visual startup is appended to the unchanged link-helper module. Recovery passed43 fresh renders/126 FAQ pairs,258 browser cases360/768/1280 JS-on/off, discovery/sitemap/canonicals/robots/structured data/strict wording/broken-link policies and location overlap. Earlier cycle2 unit/lint logs retained, recovery syntax repeated.

Expanded chrome120 cases: all38 full-footer rebuilt routes match Home, header matches all39;404 shortened-footer differences remain explicit.117 rebuilt region/width probes PASS: first posthero light, readable light longform, not fully dark, at most1 dark accent, no overflow, text visible.14 blocked-font JS-on/off probes show painted heading glyphs and visible body. All-template AA:42 rebuilt cases have0 axe violations;24 immutable-reference cases each retain a contrast violation. Five reference motion-on transient overflow cases are recorded; rebuilt samples have none. Header/footer stacked targets below44px remain at reference pitch under decisionD.

RuleC remains FAIL for About360, despite exact unchanged source/HTML and no shared CSS injection. No tolerance waiver, reference redesign, fabricated native proof or deployment. Bounded logs explain failures, repairs and scope conflicts; no retry loop for immutable reference findings.

### Task4 measured fallback

Candidate1 default gradient/self-hosted: all rebuilt samples except Germany pass; Germany LCP2430.752ms exceeds immutable1592.006ms baseline*1.1. All rebuilt CLS0, TBT0, added transfer below150000bytes and no new blocking resources. Only destination template drops to plain reference-navy hero plus the permitted Stage1 inline-font escape hatch, triggered by its measured budget failure. Other templates keep gradient/self-hosted fonts. Full original seven-route prefix plus three additional samples will be remeasured with three storage-reset navigation medians.

Unchanged Contact control also fails LCP/CLS (8786.532ms/.004813818 versus1939.857ms/0). Its reference hero/source cannot be tier-dropped under decisionB. This is retained as a failed control, not waived or redesigned. No source changes to the four references. Additional baselines are labelled immutable-HTML replay, not invented Stage1 measurements.

## Task4 checkpoint

Final destination fallback median: LCP1181.228ms, CLS0, TBT3ms, transfer200010bytes (minus30539), requests4. All other rebuilt samples retain gradient/self-hosted; all7 rebuilt samples PASS every unchanged budget. All have CLS0; no new blocking resource. Raw initial failure and full remeasurement retained.

Final unchanged Services control LCP8941.540ms exceeds2315.607ms cap; FAIL. Contact passes final but failed initial. Reference heroes stay unchanged; do not claim source-driven speedups or waive local control variance. Three added-page baselines are labelled supplemental immutable-HTML replay; original seven Stage1 per-route baseline values are untouched. No more unchanged-reference performance retries to pursue a pass.
