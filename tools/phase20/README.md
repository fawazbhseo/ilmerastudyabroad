# Phase 20 local verification

This adapter is a local verification aid, not a native Apache or live-source
transport test. It binds to 0.0.0.0:8080 and accepts preview hosts. It serializes
fresh PHP requests and rotates the WASM runtime to avoid accumulated state.
No production credentials, account creation, form submission or deployment.

Runtime dependencies used outside the repository: Node 22.22.3,
@php-wasm/cli and @php-wasm/node 3.1.58, Playwright 1.58.2 and
@sparticuz/chromium 143.0.4. The WASM packages warn that their preferred
Node/npm versions are newer; these exact local checks nevertheless ran.
On this minimal Debian image, Chromium's bundled al2023 library archive
was expanded into a runtime directory and its lib folder supplied through
LD_LIBRARY_PATH. No generated binary or node_modules folder is committed.

Provide `php` on PATH (here a wrapper around the installed WASM CLI),
NODE_PATH pointing at the runtime's node_modules, and the library path.
Run the server from the repository root:

```sh
node tools/phase20/server.cjs
python3 tools/phase20/run.py --task 1 --evidence /path/outside/repo/task1
```

The runner always lints every PHP file, executes the maintained unit and
publication checks, freshly captures all 43 routes, compares FAQ questions
and answers with schema, checks default wording/presence/schema policies,
uses Chromium at 375/768/1280 with JavaScript off/on, exercises every FAQ,
and measures all 136 rendered location pairs below 15 percent. Browser
requests to external hosts are aborted. Scroll-triggered content is brought
into view before final-layout inspection; no live performance claim follows.

Each completed task result is written into reports/phase-20-checks.json.
The evidence directory contains HTML, detailed logs and the route manifest.
A successful run is not proof of live rankings, external raw HTTP status,
contact delivery, Google eligibility, official rule currency or Apache
rewrite/access-control behavior. The repository's existing strict defaults
and publication gates are not waived.

Harness setup corrections before Task 1 sign-off: the restored workspace
had no runtime/cache, so dependencies and browser libraries were rebuilt.
The independent FAQ parser was corrected to support both existing custom
accordion markups and inline-anchor text without adding whitespace. Browser
configuration removed single-process mode, and scroll checks explicitly
exercise the Contact reveal. An attempted animation-duration shortcut was
removed after a JavaScript-off stylesheet-load hang. Those are setup/debug
runs, not clean release cycles. The final complete Task 1 run passed.
