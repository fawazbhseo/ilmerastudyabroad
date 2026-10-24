# Phase27 pack and proof (no deployment)

Source runtime is a3d696f7942b2df5c76d660c2b9f3252881ce314. Later Phase27 commits contain only reports/tools/logs. The manifest exports this exact entire branch runtime, including design, not the obsolete117-file content candidate. Never use older Phase26 export instructions for the current release.

## Offline owner export

`python3 tools/phase27/export.py --out /new/temporary/pack --zip /new/artifact.zip`

Requires Git history containing the pinned commit and the current Phase27 manifest. Reads exact Git blobs, verifies size/SHA256, refuses an existing output folder/ZIP. It never deploys, submits, changes site files or calls a server. All130 ZIP entries sit at the root, with no wrapper directory. reports/tools contain only their two deny-only .htaccess files. Keep the manifest outside public hosting. No Node/PHP runtime is needed for this export.

## Agent proof reproduction

Use a new external /home/user/phase27/source archive of the pinned commit; do not switch/create a branch/worktree. The running repo adapter on8080 is the existing tools/phase25/server.cjs. All public repo bytes must match the source archive. Use an external dependency environment, not production node_modules:

- PHP8.5 WASM CLI/node/universal3.1.58, Playwright1.58.2/Chromium143 with al2023 libraries, Pillow13 and axe-core4.10.3 from Phase26b infrastructure.
- marked15.0.12 is used only for printing the owner checklist. No new production dependency, external network or site JS is introduced.
- NODE_PATH/PATH/LD_LIBRARY_PATH/PYTHONPATH point to the external runtime. Do not inherit the archive Git environment when committing/pushing.

`python3 tools/phase27/payload.py build` freezes all43 repo HTTP renders, walks first-party HTML/CSS assets and records external dependencies, then copies only the130-file allowlist into a NEW payload folder. Build refuses a previous folder. It includes the9 mandatory runtime JSON files, all8 denies/font policies, PHP-read CSS/two variable faces,7 static faces, licences and default favicon. No still is referenced, and unused original/alternate images are not copied. No file is rewritten to repair an omission.

`node tools/phase27/server.cjs /home/user/phase27/payload 8084` starts a fresh PHP memory filesystem with only the payload at /site, no host filesystem mount. A startup probe proves the original checkout is inaccessible. Static delivery is rooted in the clean folder. Server binds0.0.0.0, accepts preview hosts and never contacts production. Route/access/MIME behavior is an explicit local adapter, not .htaccess execution.

`python3 tools/phase27/payload.py check` compares all43 outputs against current repo and frozen renders, fetches all20 first-party/runtime/licence asset paths plus discovery/verification endpoints with GET/HEAD, checks38 sitemap URLs/held exclusion, hashes and private HTTP probes. It cannot prove native Apache/LiteSpeed/ACL/rewrite/ErrorDocument/cache/MIME/CSP, external CDN/gstatic/provider delivery or backup restore. Those remain owner checks. Asset URLs in the four immutable references still depend on their original outside fonts/scripts.

`python3 tools/phase27/verify.py` runs the EXISTING full tools/phase26b/run.py with no skips in the source archive. An external index supplies Git lookups; child tools write historical reports only in the archive, not in Git. Fresh lints/units/43 renders/discovery/strict wording/schema/source/258 browser cases/contrast/66 accessibility cases are run. It is not a new performance-lab session. Original known reference findings are reported, never repaired or pruned. Read phase-27-verification.json for exact results, not a deployment certification.

`node tools/phase27/checklist.cjs` renders current Markdown offline into the excluded reports/post-deploy-checklist.pdf. There must be exactly2 A4 pages. The hidden page-break marker is documentation-only. The checklist's PSI tables are blank owner records; choosing guide may have no Phase13 baseline.

Source tracked exclusions are394 of524 files at the pinned commit. Phase27's additional internal files are also excluded; final combined counts and exact changed paths are recorded in the handoff. Git metadata/untracked caches/node_modules are unbounded exclusions, not misleadingly counted as source tracked files.
