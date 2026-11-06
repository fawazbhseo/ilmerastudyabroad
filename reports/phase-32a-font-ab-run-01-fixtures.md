# Phase32a fresh font candidate fixture

Status: **PASS**. Current font-policy source `4746142eaea674b66549d20d4352f720018adee7`; fixture-freeze HEAD `c95f3e49dd9224289c5842aadc86d7c14a84d313`. The runtime tree did not change after the post-fallback render.

Fixture SHA-256 `734b060d00486d788f4e50bc5eaa82187f18edc7aa1850a820fad649f5737231` (269509 bytes), stored externally at `/home/user/phase32a-runtime/phase32a-font-ab-run01/fixtures.json`.

| Route | A/B bytes | Display declarations changed | Visibility gate removed | Preloads/families/weights unchanged | Protected content |
|---|---:|---:|---:|---|---|
| `/study-abroad-counselling-mysuru` | 61808/61755 | 7 | 1 | yes | PASS |
| `/blog/how-to-choose-study-abroad-consultant-karnataka` | 69724/69671 | 7 | 1 | yes | PASS |

A is the current post-fallback page. B is a candidate-only HTML transform; no font source, preload or production setting has changed. It swaps `font-display` and removes the body-visibility gate. All protected content comparisons pass.

Seven A and seven B Lighthouse samples per route, alternating pair order; fresh Chromium per sample, serial, no retries.

This is a local fixture only. No browser measurement or metric analysis has run yet.
