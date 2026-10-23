# Phase 25 local verification

All runtime dependencies are installed outside the checkout, not deployable. Use
Node 22.22.3; `@php-wasm/cli@3.1.58`, `playwright@1.58.2`,
`@sparticuz/chromium@143.0.4`, `three@0.128.0`, `gsap@3.12.2`,
`@fontsource/outfit@5.2.8`, `@fontsource/cormorant-garamond@5.2.8`,
`lighthouse@12.8.2`; Python Pillow 13.0.0 and tinycss2. The PHP wrapper executes
`@php-wasm/cli/php-wasm.js`. Extract Sparticuz's al2023.tar.br libraries to
`$PHASE25_RUNTIME/libs`. Source `tools/phase25/env.sh`.

Serve `NODE_PATH=... node tools/phase24b/server.cjs` on 0.0.0.0:8080. This is a
manual PHP/rewrite/access mirror, NOT a native .htaccess engine. All existing
native hosting/backup/layout/contact-delivery blockers stand.

`capture.py <external-dir>` captures all 43 routes. Preserve the pre-edit baseline;
`reports/phase-25-baseline-renders.json` records exact UTF-8 render bytes, including
CRLF, for reconstructing this baseline if the external runtime is lost. Never
rebaseline against edited pages. `audit.py <baseline-dir>` inventories references.
`screenshots.cjs before|after` produces all references and pilots at 360/768/1280.
Motion is deliberately frozen, seeded, with reference scripts mirrored from npm.
`metrics.cjs before|after` runs three independent Lighthouse mobile navigations
per route, simulated Slow 4G / CPU 4x, writing all samples and medians. Run it
without concurrent test/screenshot workloads. Mirrors are not live CDN, font
service, production compression or field performance evidence.

`run.py --task task-N --stage N --baseline-captures <external-dir> --evidence
<external-dir>` runs syntax, units, fresh full rendering/schema/FAQ parity, strict
business/discovery/status/claim invariants, all-route responsive JS-on/off browser
checks, portrait integrity, access-policy patterns and manual deny probes. The
Phase25 guard replaces historical Phase24b source-transform expectations with
immutable Phase24b blob checks, exact authorized card transforms, all-43-route
word/link/image/JSON-LD parity, and strict pilot route allowlisting. Historical
Phase24b tools/evidence remain intact. No tests are silently skipped.

Bundled pilot font assets: `@fontsource-variable/outfit@5.2.8` and
`@fontsource-variable/cormorant-garamond@5.2.6`, Latin normal variable woff2,
original OFL license notices alongside. No new font family or blocking stylesheet.
`pngjs@7.0.0` stitches screenshots; lossless RGB PNG recompression preserves pixels.
Phase25 browser checks programmatically finish finite transitions before checking
end-state geometry. The same route/viewport/JS/FAQ/photo assertions are retained;
this avoids spending wall-clock time on every closing FAQ transition.

`build_still.cjs` captures only the actual WebGL canvas (not a screenshot of its
page rectangle), avoiding embedded headings/navigation. Capture-only preserved
drawing buffer does not modify source. Pillow WebP quality78/method6 encodes
720x900 and1440x900, recorded hashes/sizes in phase-25-hero-assets.json.
Single sitewide switch: includes/visual-config.php, ILMERA_SCENES_ENABLED.
Default ON does not change reference HTML; OFF hides overlays, removes reference
Three.js loading and omits pilot canvases/loader, yielding plain palette heroes.

For final pilots serve tools/phase25/server.cjs, the same local manual adapter plus
explicit font/woff2 MIME. This is not production MIME/native-server evidence.
`pilot.cjs` adds360/768/1280 JS-on/off, all FAQs, axe-core4.11.0 WCAG A/AA,
44px bounds, menu/Escape, keyboard focus, Save-Data/reduced-motion/hidden branches.
Hidden state is document.hidden emulation, not OS scheduler proof.
`contrast.py` checks default/hover/focus palette pairs and a conservative white
scene pixel at0.15 opacity over navy: worst ratio5.11, required4.5.
`footprint.py` emits only audited team section minima/padding, preserving reference
section bounds at the three screenshot widths while equalizing short cards.
`screenshots.cjs before --baseline` replays the immutable original HTML, never
the edited page, to apply identical capture-harness corrections to both sides.

Final font correction supersedes optional-display notes above: subset_fonts.py
uses fontTools/Brotli with recalcTimestamp=False. Original licensed Outfit keeps
variable weights; Cormorant is instantiated at700 (the only pilot role weight).
All available original glyphs used by the four immutable pilot texts are kept,
with original metrics. PHP embeds their base64 bytes in existing inline CSS; no
new font request or design family. CDP platform-font checks cover all24 cases.
Capture pre-paint no-motion/GSAP-end styles and software/sRGB/dither flags are
harness-only. Do not relax pixels.py: its remaining9 one-level Home1280
nav-CTA-corner pixels are an explicit failing pilot gate, not a claimed PASS.
