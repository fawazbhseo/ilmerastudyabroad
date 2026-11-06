# Phase25c chrome tolerance

PASS: all120 route/viewport rows (Home reference plus39 rebuilt pages, each360/768/1280). Every visible header/footer node bounding rect, DOM order/tag/direct text, plus selected canonical computed typography/colour/spacing styles is compared. Footer y is relative to its own top, not document length.

Geometry differences strictly below0.1px are tolerated; none at or above0.1px. 1318 individual values differ below tolerance; maximum0.016000px. All non-geometric values must match exactly after active-link normalization. Full per-row tolerated values and differences are in phase-25c-chrome.json.

The404 footer remains deliberately abbreviated, an owner-accepted deviation preserving its words/links. Its header is still compared. No source CSS or page edits.

## Harness normalization diagnosis

The first run removed active classes but immediately sampled a still-running0.3s colour transition, retaining Home's old active white while rebuilt pages had the normal silver. That produced39 desktop colour-only mismatches, not geometry defects. Original result retained externally at /home/user/phase25c-evidence/chrome-before-active-transition-normalization.json. Disable the nav-link transition in the test DOM before clearing active state; the corrected full comparison has zero mismatches. This is active-link state normalization only, not a reference/source change or a relaxed colour threshold.
