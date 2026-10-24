# Phase26 isolated content handoff

No release branch exists. All commits/pushes belong only to the fixed arena branch. PR1 is not repurposed or edited through GitHub. No main push, merge or deployment. Current arena production source is untouched. Do not upload this checkout, or cherry-pick its design ancestry into the content release.

## Reproduction and branch-safe constraints

Use a separately authorized release checkout for actual branch/PR work. The verified content source is the entire immutable164d6de tree plus reports/phase-26-team-only.patch (six files). Patch includes only two public pages, exact card policy/tests and two narrowly adjusted historical check expectations. It has no Phase25 shared design dependency. A new content commit/PR must get its own real hash/link; the patch SHA256 is not a commit.

Within this session, archives were created outside Git at /home/user/phase26/base (164d6de), pre24b (0c5c437), candidate (164 plus patch), and payload (allowlist only). No branch or worktree was created. prepare.py restores the six candidate files from base before applying the narrow transform, making it repeatable. It never modifies arena production files. git apply --check against an unmodified164 tree validates the standalone patch.

Runtime dependencies outside Git: PHP WASM CLI/node/universal3.1.58 (PHP8.5), Playwright1.58.2, Sparticuz Chromium143.0.4 with extracted al2023 shared libraries, three0.128.0, gsap3.12.2, fontsource Outfit/Cormorant5.2.8, Pillow13.0.0. See tools/phase25/README.md for the existing infrastructure recipe, not for design code to import. None of these tools belong in the payload. Original Phase24b runner/browser files stay byte-identical to164d6de.

The archive tools' git lookups used GIT_DIR pointing at this repository, GIT_WORK_TREE pointing at candidate and an EXTERNAL GIT_INDEX_FILE populated with git read-tree164d6de. That does not change the session index/branch or create a content commit. The inherited result's parent field is the lookup HEAD, NOT a candidate commit. Clear those environment variables before operating on the session repository.

Render pre24b with render.cjs for inherited Phase24b baseline guards and separately render164 for reference appearance. /home/user/phase26/evidence/routes.json is the unchanged routes() map from baseline tools/check_discovery.py. Run the unmodified candidate tools/phase24b/run.py with --stage5, --baseline-captures pointing at pre24b captures and evidence outside Git. All original checks are kept; only exact card exceptions in the policy/expected-source checks are updated. visual.cjs uses capture-only motion/font mirrors and reports explicit section-height reflow, not pixel identity. Its resource mirror lives in arena tooling and is not a candidate runtime dependency.

Serve the candidate with the original Phase24b server adapter on8080. payload.py build copies exactly the117 paths into a clean new folder, no symlinks. A separate copy of the SAME adapter with only its listen port changed to8083 serves that folder. payload.py check verifies every route against candidate bytes, every first-party asset, discovery text/XML and selected protected runtime probes. The engine itself is external infrastructure; there is no application include/symlink fallback to the candidate. Adapter manually mirrors denies, not native Apache.

The only runtime JSON exceptions to broad exclusions are the three root phase14 review journals and six data JSON inputs, all HTTP-denied but PHP-readable. No moving/rewriting them is authorized. All reports/tools/Markdown/CSV/Git/caches/fixtures remain excluded. Original external fonts/CDN scripts/contact service are unchanged and not rehosted or claimed live-tested.

## Deliverables

Exact paths/hashes: reports/phase-26-payload-manifest.json. Human allowlist: reports/deploy-payload.md. Owner checklist: reports/post-deploy-checklist.md (compact514-word checklist). Full public/denied URLs are separate TSV/TXT files. Copy only content documentation to a future content branch, not the later design plan. Test-generated temporary archives, caches, screenshots and runtimes are outside Git and not committed.
