# Phase29 read-only design diagnosis

No tool deploys, contacts production or mutates a public runtime file in the checkout. Disposable roots and installed dependencies live in /home/user/phase29. New report HTML extracts and screenshots remain under the HTTP-denied reports folder, outside the130-file manifest. No performance/reliability lab is run.

## Environment

Node22.22.3. Install outside the repository:

```sh
npm install --prefix /home/user/phase29/runtime --no-audit --no-fund \
  @php-wasm/node@3.1.58 @php-wasm/universal@3.1.58 \
  @sparticuz/chromium@143.0.4 playwright@1.58.2 marked@15.0.12
python3 -m pip install --target /home/user/phase29/pylibs \
  beautifulsoup4==4.14.2 Pillow==12.0.0 pypdf==6.1.1
```

Extract the npm Chromium package's bin/al2023.tar.br using Node zlib.brotliDecompressSync into an external tar, then unpack into /home/user/phase29/runtime/libs. Set NODE_PATH=/home/user/phase29/runtime/node_modules and LD_LIBRARY_PATH=/home/user/phase29/runtime/libs/lib for browser tools. PYTHONPATH=/home/user/phase29/pylibs is needed for duplicate/PDF/image checks. Packages and browser binaries are not Git deliverables. PHP WASM package includes the tested7.4/8.0/8.1/8.5 runtimes. These are functional version comparisons, not recommendations to host on unsupported old releases.

## Reproduction order in a fresh external workspace

1. `python3 tools/phase29/inventory.py` verifies all current/ZIP/manifest hashes and inventories include/read/constant source sites.
2. `python3 tools/phase29/prepare.py` extracts the exact130-file ZIP, actual end-Phase13 a643836 archive, predesign cached Germany HTML from the existing frozen baseline report, and the actual changed-PHP list. It refuses an existing payload destination. Do not delete evidence or a checkout just to bypass that guard; use a fresh disposable workspace if reproducing.
3. Start `node tools/phase29/server.cjs` with process tooling. Binds0.0.0.0:8090, serializes requests, loads only a copied memory filesystem into each PHP VM and explicitly emulates routing/private denies. It is NOT an Apache/LiteSpeed simulator. PHP display_errors=0, error_reporting=E_ALL, warnings/fatals retained in external diagnostics and fault-results JSON. A PHP library exception with a PHP response is captured, not mistaken for a generic adapter failure.
4. Fetch each of the four Task2 paths from the local server into /home/user/phase29/current-renders using its slash-to-underscore filename convention, then run `python3 tools/phase29/tags.py`. Exact link/style/script tags except non-design JSON-LD are copied without reformatting/base64 truncation. Canonical is retained because the classifier consumes it. Actual included PHP files are captured with a shutdown trace in the diagnostic wrapper, not injected into production source.
5. `node tools/phase29/capture.cjs` creates22 cases and24 PNGs at390x844, fresh contexts, no production/provider fetch. Production-origin first-party image requests are fulfilled from the selected local fixture; other external requests abort. Optional CASES=comma,list selects cases and merges with prior evidence, allowing failed-run plumbing to be corrected without changing runtime content. HTTP fault probes are separate from disk-read faults. Captures wait3300ms for the original font gate to settle and record real platform glyph fonts via CDP, not just CSS family declarations.
6. `python3 tools/phase29/compare.py` validates all screenshot hashes and the five-symptom comparison. The original owner screenshot was unavailable, so no pixel-exact claim. Explicit missing-assets/header combination is not mislabeled as a single fault.
7. `python3 tools/phase29/rules.py` inventories all8 payload .htaccess files and records static path reasoning. Available native commands are checked. No engine was installed and no native behavior is certified.
8. `node tools/phase29/owner_sheet.cjs` prints the owner Markdown offline into an external PDF. pypdf verified one A4 page; only Markdown and the proof JSON are committed.
9. `python3 tools/phase29/duplicates.py` freshly renders all38 published sitemap routes and compares first answers to following paragraphs under documented lexical thresholds, retaining all nonmatches and citations. It proposes but never applies a fix.
10. `python3 tools/phase29/scope.py` verifies every preexisting file except append-only root logs is byte-identical to56914f2, manifest/ZIP unchanged, all new paths restricted to reports/tools, original line endings/no new em dashes,22 cases/24 screenshot hashes and new tool syntax.

Only the Phase29 reports are regenerated. Historical Phase25-28 reports, source, runtime .htaccess files and release ZIP remain byte-identical. No native permissions, cache operation, response header, actual Hostinger behavior or live-host hash is established by these local tools. Actual owner/server checks remain required.
