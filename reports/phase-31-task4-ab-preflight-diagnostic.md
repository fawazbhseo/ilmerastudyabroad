# Task4 A/B browser startup diagnostic

The first runner invocation stopped at round 0, route `/`, arm A because the Chromium process could not load `libnspr4.so`. The browser did not start, no page was navigated, and Lighthouse produced no performance sample or metric. The partial startup record is preserved in `reports/phase-31-task4-ab-preflight-failure.json` and is not counted as A/B performance evidence.

The runner now inflates the pinned Chromium runtime libraries before launch. Its `--preflight-only` mode successfully started Chromium `143.0.7499.0`, connected over CDP, and closed without navigating to a page or invoking Lighthouse. The authorized measurement remains pending and will use a new output path. Once a valid Lighthouse sample begins, the protocol permits no retry or resume.
