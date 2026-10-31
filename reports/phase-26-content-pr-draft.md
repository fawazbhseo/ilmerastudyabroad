# Draft only: separate content release PR

**NOT OPENED.** The fixed session branch restriction prevents creating/pushing release/content-phase-24b or opening the requested PR from it. Do not open a replacement from arena into main: that includes the design history. PR1 metadata/comments/state were not edited; documentation pushes to its fixed source branch update its diff.

Requested title: **Release: content phases 14 to 24b (no design change)**
Requested head: `release/content-phase-24b`
Requested base: `main`
New PR URL: none.
New content-release commit hash: none. No candidate commit was fabricated.
Content boundary: `164d6de41159385e151ecefec54763eab59141a5`.
Narrow team patch SHA256: `b6bf61943ca1abd8e6235aadcec1b23ad70539717cd17aa0e32b7c7b6124a2bf` (artifact identity, NOT a Git commit).

## Description ready for an authorized release-branch session

Release content phases14 to24b independently of Phase25 design. Start exactly at the boundary above, apply only phase-26-team-only.patch and copy the content-release documentation. Do not cherry-pick the full4844f3f commit or arena Phase26 checkpoint commits: their ancestry/doc context belongs to the design branch. Commit the narrow changes on the separately authorized content branch, record its REAL final hash here, rerun checks, push that branch and open the title above. Do not merge/deploy.

Verification already performed on the isolated equivalent candidate:

- Original Phase24b stage5 runner/browser, PHP8.5 WASM CLI, all lint/unit/render/discovery/strict wording/structured-data/source/exposure/portrait/LLM checks PASS in545.13s.
-43 routes;38 published; exact38 sitemap URLs. No status/canonical/schema/image/FAQ/link changes.
- Six team card bios only, with one inline equal-row rule per page. Full canonical bios/About FAQs/LLMs unchanged. No Phase25 design stylesheet, shared visual PHP, font/still asset or report exists in the candidate.
-12 relative reference comparisons PASS. Approved team height changes shift later sections; no pixel-identical/absolute-footer-position claim.
- Exact117-file payload served from a clean folder alone: all43 outputs byte-match,38 published,38 sitemap URLs and12 first-party assets. Include the three protected root review journals and six protected data JSON runtime inputs despite general internal-JSON exclusions.
- Full evidence: phase-26-verification.md/JSON, phase-26-reference-comparison.json, phase-26-payload-checks.json; exact upload paths and SHA256 values in deploy-payload.md / phase-26-payload-manifest.json.
- Local tests ONLY. No native Apache/LiteSpeed AllowOverride/Require/rewrite/404/cache/MIME/CSP/private-layout proof, contact delivery or live-host proof. Original CDN/contact dependencies unchanged. No deployment, main push, merge or contact submission performed. Backup/restore and all existing owner/proof/business/source approvals remain required.

Raw inherited browser result:

```text
study-abroad-counselling-mysuru","js":true,"width":1280}
PASS case {"route":"/study-abroad-counselling-ponnampet","js":true,"width":1280}
PASS case {"route":"/study-abroad-counselling-shivamogga","js":true,"width":1280}
PASS case {"route":"/study-abroad-counselling-siddapura","js":true,"width":1280}
PASS case {"route":"/study-abroad-counselling-somwarpet","js":true,"width":1280}
PASS case {"route":"/study-abroad-counselling-udupi-manipal","js":true,"width":1280}
PASS case {"route":"/study-abroad-counselling-virajpet","js":true,"width":1280}
PASS case {"route":"/study-in-czech-republic","js":true,"width":1280}
PASS case {"route":"/study-in-gcc","js":true,"width":1280}
PASS case {"route":"/study-in-germany","js":true,"width":1280}
PASS case {"route":"/study-in-italy","js":true,"width":1280}
PASS case {"route":"/study-in-latvia","js":true,"width":1280}
PASS case {"route":"/study-in-lithuania","js":true,"width":1280}
PASS case {"route":"/study-in-russia","js":true,"width":1280}
PASS case {"route":"/study-in-slovakia","js":true,"width":1280}
PASS case {"route":"/study-in-uk","js":true,"width":1280}
PASS case {"route":"/terms","js":true,"width":1280}
{"status":"PASS","cases":258,"faq_expansions":1278,"team_photo_checks":36,"fawaz_derivative_load_checks":54,"viewports":[375,768,1280],"javascript":[false,true],"external_requests":"aborted; no live font/performance/delivery assertion"}
```
