#!/usr/bin/env python3
"""Validate and summarize the completed Phase31 Task4 local A/B report."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_INPUT = ROOT / "reports/phase-31-task4-ab-results.json"
DEFAULT_OUTPUT = ROOT / "reports/phase-31-task4-ab-summary.md"
ROUTES = [
    "/",
    "/services",
    "/about",
    "/contact",
    "/study-in-germany",
    "/study-abroad-counselling-mysuru",
    "/blog/how-to-choose-study-abroad-consultant-karnataka",
    "/blog/",
]
CONTROLS = ROUTES[:4]
TARGETS = ROUTES[4:]
METRICS = ("lcp_ms", "cls", "tbt_ms", "transfer_bytes", "requests")
QUANTILES = {"q1": 0.25, "median": 0.5, "q3": 0.75}
BUDGETS = {
    "added_transfer": 150_000,
    "lcp_ratio": 1.10,
    "tbt_delta_ms": 50,
    "cls_limit": 0.1,
    "control_symmetric_lcp_ratio": 1.10,
}


def percentile(values: list[float], q: float) -> float:
    """Match the runner's linear interpolation at (n - 1) * q."""
    ordered = sorted(float(value) for value in values)
    if not ordered:
        raise ValueError("Cannot summarize an empty sample")
    position = (len(ordered) - 1) * q
    lower = math.floor(position)
    upper = math.ceil(position)
    return ordered[lower] + (ordered[upper] - ordered[lower]) * (position - lower)


def summarize(samples: list[dict[str, Any]]) -> dict[str, dict[str, float]]:
    result: dict[str, dict[str, float]] = {}
    for metric in METRICS:
        values = [float(sample[metric]) for sample in samples]
        q = {name: percentile(values, p) for name, p in QUANTILES.items()}
        q["iqr"] = q["q3"] - q["q1"]
        result[metric] = q
    return result


def close(actual: float, expected: float) -> bool:
    return math.isclose(float(actual), float(expected), rel_tol=1e-12, abs_tol=1e-12)


def assert_summary_matches(actual: dict[str, Any], expected: dict[str, Any], where: str) -> None:
    for metric in METRICS:
        for statistic in (*QUANTILES.keys(), "iqr"):
            if not close(actual[metric][statistic], expected[metric][statistic]):
                raise ValueError(
                    f"Embedded summary mismatch at {where} {metric}.{statistic}: "
                    f"{actual[metric][statistic]} != {expected[metric][statistic]}"
                )


def calculate_tests(row: dict[str, Any], summary: dict[str, Any]) -> tuple[dict[str, bool], float, float, float]:
    a, b = summary["A"], summary["B"]
    ratio = b["lcp_ms"]["median"] / a["lcp_ms"]["median"]
    symmetric_ratio = max(ratio, 1 / ratio)
    added_bytes = b["transfer_bytes"]["median"] - a["transfer_bytes"]["median"]
    blocking_a = {url for sample in row["A"] for url in sample.get("render_blocking", [])}
    new_blocking: list[str] = []
    seen_blocking: set[str] = set()
    for sample in row["B"]:
        for url in sample.get("render_blocking", []):
            if url not in blocking_a and url not in seen_blocking:
                new_blocking.append(url)
                seen_blocking.add(url)
    tests = {
        "added_transfer": added_bytes < BUDGETS["added_transfer"],
        "lcp": ratio <= BUDGETS["lcp_ratio"],
        "tbt": b["tbt_ms"]["median"] <= a["tbt_ms"]["median"] + BUDGETS["tbt_delta_ms"],
        "cls": (
            b["cls"]["median"] <= a["cls"]["median"]
            and b["cls"]["median"] < BUDGETS["cls_limit"]
        ),
        "no_new_render_blocking": not new_blocking,
    }
    if row.get("new_render_blocking") != new_blocking:
        raise ValueError(f"Embedded render-blocking comparison mismatch for {row['route']}")
    return tests, ratio, symmetric_ratio, added_bytes


def fmt(value: float, digits: int = 2) -> str:
    return f"{value:.{digits}f}"


def metric_cell(stats: dict[str, float], digits: int) -> str:
    return f"{fmt(stats['median'], digits)} / {fmt(stats['iqr'], digits)}"


def failed_reasons(tests: dict[str, bool], row: dict[str, Any], summary: dict[str, Any], ratio: float) -> str:
    if all(tests.values()):
        return "None"
    a, b = summary["A"], summary["B"]
    reasons: list[str] = []
    if not tests["added_transfer"]:
        reasons.append(f"transfer (+{fmt(b['transfer_bytes']['median'] - a['transfer_bytes']['median'], 0)} B)")
    if not tests["lcp"]:
        reasons.append(f"LCP ({ratio:.4f} > 1.10)")
    if not tests["tbt"]:
        delta = b["tbt_ms"]["median"] - a["tbt_ms"]["median"]
        reasons.append(f"TBT (+{fmt(delta, 2)} ms > 50 ms)")
    if not tests["cls"]:
        if b["cls"]["median"] > a["cls"]["median"]:
            reasons.append(f"CLS ({b['cls']['median']:.6f} > {a['cls']['median']:.6f})")
        else:
            reasons.append(f"CLS ({b['cls']['median']:.6f} is not below 0.1)")
    if not tests["no_new_render_blocking"]:
        reasons.append("new render-blocking URL")
    return "; ".join(reasons)


def build_markdown(report: dict[str, Any], rows: list[dict[str, Any]], raw_sha: str) -> str:
    method = report["method"]
    env = report["environment"]
    session = report["session"]
    start = report["started_at"]
    finish = session["finished_at"]

    summaries: dict[str, dict[str, Any]] = {}
    calculated: dict[str, tuple[dict[str, bool], float, float, float]] = {}
    for row in rows:
        summary = {arm: summarize(row[arm]) for arm in ("A", "B")}
        for arm in ("A", "B"):
            assert_summary_matches(row["summary"][arm], summary[arm], f"{row['route']} {arm}")
        checks = calculate_tests(row, summary)
        summaries[row["route"]] = summary
        calculated[row["route"]] = checks
        tests, ratio, symmetric, added = checks
        if row.get("tests") != tests:
            raise ValueError(f"Embedded budget tests mismatch for {row['route']}")
        expected_result = "PASS" if all(tests.values()) else "FAIL"
        if row.get("local_budget_result") != expected_result:
            raise ValueError(f"Embedded route result mismatch for {row['route']}")
        if not close(row["ratio_b_over_a"], ratio):
            raise ValueError(f"Embedded LCP ratio mismatch for {row['route']}")
        if not close(row["symmetric_lcp_ratio"], symmetric):
            raise ValueError(f"Embedded symmetric LCP ratio mismatch for {row['route']}")
        if not close(row["added_transfer_bytes"], added):
            raise ValueError(f"Embedded transfer delta mismatch for {row['route']}")
        if row["route"] in CONTROLS:
            expected_control = symmetric <= BUDGETS["control_symmetric_lcp_ratio"]
            if row.get("control_reliability") is not expected_control:
                raise ValueError(f"Embedded control result mismatch for {row['route']}")
        elif row.get("control_reliability") is not None:
            raise ValueError(f"Treatment route has control result for {row['route']}")

    control_passes = all(
        calculated[route][2] <= BUDGETS["control_symmetric_lcp_ratio"]
        for route in CONTROLS
    )
    if session.get("control_reliable") is not control_passes:
        raise ValueError("Embedded control reliability result does not match recomputation")
    if session.get("performance_release_certified") is not False:
        raise ValueError("This local A/B report must not certify performance release")

    control_lines = []
    for route in CONTROLS:
        _, ratio, symmetric, _ = calculated[route]
        control_lines.append(
            f"| `{route}` | {ratio:.4f} | {symmetric:.4f} | "
            f"{'PASS' if symmetric <= BUDGETS['control_symmetric_lcp_ratio'] else 'FAIL'} |"
        )

    budget_lines = []
    for row in rows:
        route = row["route"]
        tests, ratio, _, added = calculated[route]
        reasons = failed_reasons(tests, row, summaries[route], ratio)
        budget_lines.append(
            f"| `{route}` | {fmt(added, 0)} | {ratio:.4f} | {reasons} | "
            f"{'PASS' if all(tests.values()) else 'FAIL'} |"
        )

    stats_lines = []
    for row in rows:
        route = row["route"]
        for arm in ("A", "B"):
            values = summaries[route][arm]
            stats_lines.append(
                f"| `{route}` | {arm} | {metric_cell(values['lcp_ms'], 2)} | "
                f"{metric_cell(values['cls'], 6)} | {metric_cell(values['tbt_ms'], 2)} | "
                f"{metric_cell(values['transfer_bytes'], 0)} | "
                f"{metric_cell(values['requests'], 0)} |"
            )

    route_passes = [row["route"] for row in rows if row["local_budget_result"] == "PASS"]
    failed_routes = [row["route"] for row in rows if row["local_budget_result"] == "FAIL"]
    target_ratios = [calculated[route][1] for route in TARGETS]
    target_still = {
        route: (sum(len(sample.get("still_requests", [])) for sample in next(r for r in rows if r["route"] == route)["A"]),
                sum(len(sample.get("still_requests", [])) for sample in next(r for r in rows if r["route"] == route)["B"]))
        for route in TARGETS
    }

    return f"""# Task4 local A/B result summary

## Scope and evidence

This is the single local-only comparison of the frozen Task2 source (A, `{env['A_source_commit'][:7]}`) against Task3 with the approved static still CSS (B, `{env['B_source_commit'][:7]}`). It uses the eight routes in the fixed protocol, with four byte-identical reference controls and four treatment routes. This is not a live-site, CDN, field Core Web Vitals, release, merge, or deployment result.

- Run: {start} to {finish}.
- Samples: {session['totals']['samples']} total, {session['totals']['A']} A and {session['totals']['B']} B. All {session['totals']['samples']} samples completed with `PASS`; the capture contains zero Lighthouse warnings. No sample was retried or resumed.
- Runtime: Chromium {env.get('chromium', '143.x')}, Playwright {env['playwright']}, Lighthouse {env['lighthouse']}; {method['performance_model']}.
- Fixture SHA-256: `{env['fixture_sha256']}`. Raw report: [`phase-31-task4-ab-results.json`](phase-31-task4-ab-results.json), SHA-256 `{raw_sha}`.
- The pre-navigation Chromium startup diagnostic is preserved separately in `phase-31-task4-ab-preflight-failure.json`; it did not navigate a page or contribute a sample.

## Findings

- **Median-LCP control gate: {'PASS' if control_passes else 'FAIL'} (4/4 controls).** The protocol compares the symmetric ratio `max(B/A, A/B)` with 1.10. This is a median-only gate, not proof that local variance is low. In particular, the measured LCP IQRs are broad on `/` A (4,137 ms), `/services` B (7,872 ms), and `/contact` A/B (4,980/8,906 ms).
- **Per-route local budget gate: {len(route_passes)}/8 PASS.** Passing routes: {', '.join(f'`{r}`' for r in route_passes)}. Failing routes: {', '.join(f'`{r}`' for r in failed_routes)}. These are diagnostic, one-session local results only.
- **Treatment-route still requests:** each target has A/B counts `{target_still[TARGETS[0]][0]}/{target_still[TARGETS[0]][1]}` for Germany, `{target_still[TARGETS[1]][0]}/{target_still[TARGETS[1]][1]}` for Mysuru, `{target_still[TARGETS[2]][0]}/{target_still[TARGETS[2]][1]}` for the article, and `{target_still[TARGETS[3]][0]}/{target_still[TARGETS[3]][1]}` for the blog index. Every B sample requested one 720px still (24,574 resource bytes, HTTP 200); A requested none. B's median total transfer was 25,541 bytes higher per target route, below the fixed 150,000-byte cap, with one additional request. No new render-blocking URLs were observed on any route.
- B's median LCP was higher than A on all four targets in this local simulator. B/A ratios were {', '.join(f'`{route}` {calculated[route][1]:.4f}' for route in TARGETS)}. Germany, the article, and the blog index fail the 1.10 LCP ratio budget; Mysuru stays within it and passes the other route budgets.
- `control_reliable` is true by the prespecified median-LCP rule, while `performance_release_certified` is false. The prescribed route budgets are not all met. Do not interpret any median as a live speed gain or make deployment or release claims from this capture.

## Control reliability calculation

| Control route | B/A median LCP | Symmetric ratio | Median control gate |
|---|---:|---:|---|
{chr(10).join(control_lines)}

## Per-route budget results

The fixed checks are: added transfer below 150,000 bytes; median LCP ratio B/A no greater than 1.10; median TBT no greater than A plus 50 ms; median CLS no greater than A and below 0.1; and no new render-blocking URL.

| Route | Added transfer (B) | B/A median LCP | Failed check(s) | Local route gate |
|---|---:|---:|---|---|
{chr(10).join(budget_lines)}

## Medians and IQRs

Each cell is `median / IQR` over seven samples for that route and arm. Quartiles use linear interpolation at `(n - 1) * p` for p = 0.25 and 0.75, matching the runner. Transfer is in bytes, requests are counts, and CLS is unitless. Full samples, Q1/Q3, render-blocking URLs, still requests, font records, passive observations, and warnings remain in the raw JSON.

| Route | Arm | LCP ms median / IQR | CLS median / IQR | TBT ms median / IQR | Transfer bytes median / IQR | Requests median / IQR |
|---|---:|---:|---:|---:|---:|---:|
{chr(10).join(stats_lines)}

## Interpretation limits

All browser requests were routed through the local fixture and the checked-in resource handler or fulfilled from pinned local mirrors; unsupported external requests are aborted. URL strings retained in the report identify resources, not remote measurements. This single Lighthouse mobile simulation has substantial control-route spread and is not a field test. The result changes no site behavior, historical benchmark, release status, or merge/deployment decision.
"""


def validate(report: dict[str, Any]) -> list[dict[str, Any]]:
    if report.get("phase") != 31 or report.get("task") != 4:
        raise ValueError("Input is not a Phase31 Task4 report")
    if report.get("status") != "COMPLETE" or report.get("session", {}).get("status") != "COMPLETE":
        raise ValueError("Refusing to summarize an incomplete session")
    if report.get("route_order") != ROUTES:
        raise ValueError("Route order differs from the frozen Task4 protocol")
    rows = report["session"].get("routes", [])
    if [row.get("route") for row in rows] != ROUTES:
        raise ValueError("Session route rows differ from the frozen Task4 protocol")
    for row in rows:
        for arm in ("A", "B"):
            samples = row.get(arm, [])
            if len(samples) != 7:
                raise ValueError(f"Expected seven {arm} samples for {row['route']}")
            if any(sample.get("status") != "PASS" for sample in samples):
                raise ValueError(f"Non-PASS sample in {row['route']} {arm}")
            if any(sample.get("warnings") or sample.get("error") for sample in samples):
                raise ValueError(f"Warning or sample error in {row['route']} {arm}")
            for round_index, sample in enumerate(samples):
                expected_order = "AB" if round_index % 2 == 0 else "BA"
                if sample.get("round") != round_index or sample.get("order") != expected_order:
                    raise ValueError(f"Interleave order mismatch in {row['route']} {arm} round {round_index}")
        expected_control_result = True if row["route"] in CONTROLS else None
        if row.get("control_reliability") is not expected_control_result:
            raise ValueError(f"Unexpected control classification for {row['route']}")

    totals = report["session"].get("totals", {})
    if totals != {"samples": 112, "A": 56, "B": 56, "routes_passing_local_budgets": 2}:
        raise ValueError(f"Unexpected completed sample totals: {totals}")
    if report["session"].get("routes_complete") is not True:
        raise ValueError("Runner did not mark all routes complete")
    if report["session"].get("local_budgets_passed") is not False:
        raise ValueError("Unexpected all-routes budget result")
    for route in TARGETS:
        row = next(item for item in rows if item["route"] == route)
        if any(sample.get("still_requests") for sample in row["A"]):
            raise ValueError(f"Unexpected still-image request in A for {route}")
        for sample in row["B"]:
            requests = sample.get("still_requests", [])
            if len(requests) != 1:
                raise ValueError(f"Expected one still-image request in B for {route}")
            request = requests[0]
            if (
                not request.get("url", "").endswith("/assets/images/hero-still-720.webp")
                or request.get("resourceType") != "Image"
                or request.get("resourceSize") != 24_574
                or request.get("statusCode") != 200
            ):
                raise ValueError(f"Unexpected still-image response in B for {route}: {request}")
    for route in CONTROLS:
        row = next(item for item in rows if item["route"] == route)
        if any(sample.get("still_requests") for arm in ("A", "B") for sample in row[arm]):
            raise ValueError(f"Unexpected still-image request on control {route}")
    return rows


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT, help="completed raw A/B JSON")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT, help="Markdown summary path")
    args = parser.parse_args()

    raw_bytes = args.input.read_bytes()
    report = json.loads(raw_bytes)
    rows = validate(report)
    markdown = build_markdown(report, rows, hashlib.sha256(raw_bytes).hexdigest())
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(markdown, encoding="utf-8")
    print(f"PASS: validated 112 samples and wrote {args.output}")


if __name__ == "__main__":
    main()
