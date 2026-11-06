# Phase32 Contact `#miniHero` tail inspection

## Method

The current candidate was served locally at `/contact` from the frozen B render adapter, not the public site. Chromium 143.0.7499.0 / Playwright 1.58.2 inspected 360, 768 and 1280px widths, JavaScript on/off and normal/reduced motion (12 cases each). Two raw captures are retained:

- First-load: `phase-32-contact-minihero-audit.json`, SHA-256 `2354aab7f4de1ccb4f3ef612dfa5c4c5748ef40a2844ba4fbc2901da5d825ba5`.
- After full-page slow wheel scroll, 3-second settle and return to top: `phase-32-contact-minihero-postscroll-audit.json`, SHA-256 `c336cbf834146cdc998c693df7faf91227194809972f5248d1fa75bdda8cbd24`.

The first attempt at the Phase31 pixel scanner could not start because `sharp` is not installed in the Phase32 runtime. The focused post-scroll inspector mirrors the scanner's scroll/settle/return behavior and measures only this hero and its cue; it is not a replacement for the 43-route pixel scan.

## Current candidate measurements

| Width | `#miniHero` height / min-height | Last visible flow-text bottom | Flow-text tail to section bottom | `#scrollInd` state after scroll (JS on/off) | Cue bottom gap |
|---:|---:|---:|---:|---|---:|
| 360px | 792px / 792px | 607.47px | 184.53px | opacity 0 / 1 | 30px |
| 768px | 792px / 792px | 547.06px | 244.94px | opacity 0 / 1 | 30px |
| 1280px | 792px / 792px | 599.66px | 192.34px | opacity 0 / 1 | 30px |

The values are identical across reduced-motion modes and JS states. The cue is a visible, absolutely positioned 39px element at initial load, bottom `30px`, with “Reach Out” text. After the full scroll, its existing JS handler sets opacity to 0 when JavaScript is on; with JavaScript off it remains visible. Every case returned to scroll position 0. No spacing source was changed.

## Prior result comparison and disposition

The Phase31 scan had retained post-scroll Contact tails of 138px at 360px and 233px at 768px. Current Phase32 B measures 184.53px and 244.94px in the same scroll state, increases of 46.53px and 11.94px. The source/runtime snapshots differ, so this inspection does not attribute that delta to one specific font or style change. The 1280px current tail is 192.34px, below the scanner's 200px desktop candidate threshold.

Conservative disposition: retain the existing 792px hero and bottom cue. Do not count the tail as savings or change hero spacing without an approved visual review; the overall desktop presentation is explicitly protected. This focused audit neither clears nor re-runs the full 43-route blank-space scan.
