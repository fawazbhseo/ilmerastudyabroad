# Phase25c interleaved A/B performance

**Local simulated Lighthouse data only. Not field data, actual CDN timing or native/live hosting proof.**

Immutable Stage1 HTML is A for the four references; immutable Phase24b HTML is A elsewhere. Independently frozen current HTML is B. Both use the same HTTP document/static fixture server and exact npm CDN mirrors. Each sample uses a fresh isolated-profile Chromium process, standard Lighthouse mobile simulated Slow4G/4x CPU, storage reset, serial execution. Seven A and seven B per completed route. Round0 A/B, round1 B/A, alternating through round6. No other browser/capture/QA benchmark runs overlap. Shared-host scheduling and software GPU remain limitations.

IQR is Q3 minus Q1, with linear-interpolated sample quartiles. JSON retains quartiles, every raw sample, passive LCP DOM/font/gate events, and failed or incomplete sessions. Disabling the oversized **post-trace report screenshot** in reruns does not disable page animations or alter the A/B throttling or metric budgets. Each arm within a session uses identical settings.

Reliability: every reference must have max(A/B,B/A) median LCP ratio<=1.10, a conservative symmetric reading. No tolerance added to the actual route budgets: added transfer<150000B, no new external blocking request, CLS<=A AND<0.1, LCP<=1.10A, TBT<=A+50ms. A control failure invalidates certification of that session, including otherwise numerically passing routes.

## Retained sessions

| Session | Completeness | Control symmetric ratios | Reliable |
|---|---|---|---|
| 1 | 24 samples, 1 complete routes | /=4.9769 | NO |
| 2 | 56 samples, 4 complete routes | /=1.0095, /services=1.0038, /contact=5.4517, /about=1.0164 | NO |
| 3 | 196 samples, 14 complete routes | /=5.0419, /services=4.8435, /contact=1.0200, /about=1.0089 | NO |

## Session3 table: UNRELIABLE, NOT CERTIFIED

Cells show **median [IQR]**. Bytes are raw local transfer totals; added bytes are B minus A. Ratios and tests use unrounded values. No baseline relabelled or failed sample deleted.

| Route | LCP A ms [IQR] | LCP B ms [IQR] | B/A | Transfer A/B [IQR] B | Added B | CLS A/B [IQR] | TBT A/B ms [IQR] | New blocking | Verdict |
|---|---:|---:|---:|---|---:|---|---|---:|---|
| `/` | 9292.3 [7723.8] | 1843.0 [3716.6] | 0.1983 | 1068515 [0] / 1068515 [0] | 0 | 0.000769 [0.000005] / 0.000769 [0.000015] | 1761.0 [586.0] / 1773.0 [237.0] | 0 | NOT CERTIFIED (raw PASS) |
| `/services` | 1997.1 [7635.6] | 9672.8 [7846.7] | 4.8435 | 1093114 [0] / 1093114 [0] | 0 | 0.000000 [0.003797] / 0.000000 [0.000000] | 1946.0 [334.3] / 2209.0 [345.8] | 0 | FAIL: lcp,tbt |
| `/contact` | 10786.9 [975.1] | 11002.5 [4752.7] | 1.0200 | 1049851 [0] / 1049851 [0] | 0 | 0.000000 [0.000000] / 0.000000 [0.000000] | 3399.5 [967.5] / 3621.5 [616.8] | 0 | FAIL: tbt |
| `/about` | 9147.1 [179.5] | 9228.7 [171.9] | 1.0089 | 1047496 [0] / 1047496 [0] | 0 | 0.007303 [0.001027] / 0.006758 [0.003311] | 1661.0 [238.0] / 1826.0 [222.5] | 0 | FAIL: tbt |
| `/study-in-germany` | 3037.7 [195.3] | 1147.4 [53.4] | 0.3777 | 230530 [0] / 199991 [0] | -30539 | 0.053536 [0.025454] / 0.000000 [0.000000] | 0.0 [0.0] / 0.0 [0.0] | 0 | NOT CERTIFIED (raw PASS) |
| `/study-in-italy` | 2919.3 [120.2] | 1172.6 [50.0] | 0.4017 | 228478 [0] / 197938 [0] | -30540 | 0.055367 [0.018332] / 0.000000 [0.000000] | 0.0 [0.0] / 8.5 [39.5] | 0 | NOT CERTIFIED (raw PASS) |
| `/study-in-gcc` | 3068.7 [135.0] | 1313.2 [88.6] | 0.4280 | 239266 [0] / 208727 [0] | -30539 | 0.042830 [0.014711] / 0.000000 [0.000000] | 0.0 [0.0] / 0.0 [12.8] | 0 | NOT CERTIFIED (raw PASS) |
| `/study-abroad-counselling-mysuru` | 2918.7 [1.5] | 1652.4 [315.7] | 0.5662 | 226483 [0] / 233615 [0] | 7132 | 0.045560 [0.020526] / 0.000000 [0.000000] | 0.0 [0.0] / 0.0 [0.0] | 0 | NOT CERTIFIED (raw PASS) |
| `/study-abroad-counselling-bengaluru` | 2918.5 [63.2] | 1652.4 [314.8] | 0.5662 | 226586 [0] / 233718 [0] | 7132 | 0.073798 [0.053247] / 0.000000 [0.000000] | 0.0 [0.0] / 0.0 [0.0] | 0 | NOT CERTIFIED (raw PASS) |
| `/blog/how-to-choose-study-abroad-consultant-karnataka` | 1031.3 [64.3] | 2280.9 [314.3] | 2.2117 | 143493 [0] / 241184 [0] | 97691 | 0.000000 [0.000000] / 0.000000 [0.000000] | 0.0 [11.5] / 0.0 [3.0] | 0 | FAIL: lcp |
| `/blog/documents-needed-to-study-abroad-from-india` | 3187.3 [121.0] | 1802.9 [628.7] | 0.5657 | 233830 [0] / 255209 [0] | 21379 | 0.032218 [0.010288] / 0.000000 [0.000000] | 0.0 [0.0] / 0.0 [0.0] | 0 | NOT CERTIFIED (raw PASS) |
| `/blog/` | 2771.1 [270.4] | 1654.1 [628.6] | 0.5969 | 211288 [0] / 232579 [0] | 21291 | 0.102867 [0.031043] / 0.000000 [0.000000] | 0.0 [0.0] / 0.0 [0.0] | 0 | NOT CERTIFIED (raw PASS) |
| `/privacy-policy` | 2993.3 [161.9] | 1652.5 [351.8] | 0.5521 | 231468 [0] / 229212 [0] | -2256 | 0.058473 [0.029236] / 0.000000 [0.000000] | 0.0 [0.0] / 0.0 [0.0] | 0 | NOT CERTIFIED (raw PASS) |
| `/all-pages` | 2769.5 [140.2] | 1652.3 [389.8] | 0.5966 | 203636 [0] / 224963 [0] | 21327 | 0.022408 [0.000000] / 0.000000 [0.000000] | 0.0 [0.0] / 0.0 [11.0] | 0 | NOT CERTIFIED (raw PASS) |

## Decision

All permitted reliability attempts exhausted. No further performance retry or baseline/budget relaxation.
**Performance acceptance: FAIL / not certified.** Reference HTML A/B hashes are byte-identical, yet the reference medians can show large simulated variance. This is not proof of a reference design/source regression or a measured live improvement. It does prevent a release performance sign-off. Required native hosting, backup/restore, contact delivery, certificate/source and deployment blockers remain open.
