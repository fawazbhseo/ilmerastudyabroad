#!/usr/bin/env python3
"""Freeze the immutable Phase31 baseline and current Phase32 11-route renders."""
from __future__ import annotations
import gzip, hashlib, json, os, pathlib, subprocess

ROOT = pathlib.Path(__file__).resolve().parents[2]
EVIDENCE = pathlib.Path(os.environ.get("PHASE32_AB_EVIDENCE", "/home/user/phase32-runtime/phase32-ab"))
B_RENDER = pathlib.Path(os.environ.get("PHASE32_B_RENDER_DIR", "/home/user/phase32-runtime/phase32-b/render-before"))
A_ARCHIVE = ROOT / "reports/phase-32-before-renders.json.gz"
A_INDEX = ROOT / "reports/phase-32-before-render-index.json"
MANIFEST = ROOT / "reports/phase-32-11-route-ab-fixtures.json"
FIXTURE = EVIDENCE / "fixtures.json"
A_COMMIT = "796879d7b3d5ca0fa1e398562e937e9f364a5f62"
ROUTES = [
    "/", "/services", "/about", "/contact",
    "/study-in-germany", "/study-in-italy",
    "/study-abroad-counselling-mysuru", "/study-abroad-counselling-bengaluru",
    "/blog/how-to-choose-study-abroad-consultant-karnataka",
    "/blog/cost-of-studying-abroad-for-indian-students", "/blog/",
]
CONTROLS = ROUTES[:4]
ROLES = {
    "/": "reference control",
    "/services": "reference control",
    "/about": "reference control",
    "/contact": "reference control",
    "/study-in-germany": "destination template",
    "/study-in-italy": "destination variant",
    "/study-abroad-counselling-mysuru": "place template and font-chain sample",
    "/study-abroad-counselling-bengaluru": "place variant",
    "/blog/how-to-choose-study-abroad-consultant-karnataka": "article template and font-chain sample",
    "/blog/cost-of-studying-abroad-for-indian-students": "article variant",
    "/blog/": "blog-index template and font-chain sample",
}
SHA = lambda data: hashlib.sha256(data).hexdigest()

def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()

def main() -> None:
    if len(ROUTES) != 11 or len(set(ROUTES)) != 11 or set(ROUTES) != set(ROLES):
        raise SystemExit("The frozen 11-route selection is invalid")
    if not A_ARCHIVE.is_file() or not A_INDEX.is_file():
        raise SystemExit("The frozen Phase32 A render archive and index are required")
    archive_bytes = A_ARCHIVE.read_bytes()
    a_index = json.loads(A_INDEX.read_text(encoding="utf-8"))
    if a_index.get("source_commit") != A_COMMIT or a_index.get("route_count") != 43:
        raise SystemExit("The A render index is not the frozen Phase31 baseline")
    if a_index.get("render_archive_sha256") != SHA(archive_bytes):
        raise SystemExit("The A render archive hash does not match its frozen index")
    with gzip.open(A_ARCHIVE, "rt", encoding="utf-8") as stream:
        a_archive = json.load(stream)
    if a_archive.get("source_commit") != A_COMMIT or len(a_archive.get("routes", {})) != 43:
        raise SystemExit("The A render archive is not the exact 43-route frozen baseline")
    b_index_path = B_RENDER / "routes.json"
    if not b_index_path.is_file():
        raise SystemExit(f"Missing current-B route capture index: {b_index_path}")
    b_index_bytes = b_index_path.read_bytes()
    b_index = json.loads(b_index_bytes)
    b_commit = git("rev-parse", "HEAD")
    if b_index.get("source_head") != b_commit:
        raise SystemExit(f"Current-B route capture is from {b_index.get('source_head')}, expected current HEAD {b_commit}")
    b_rows = {row["url"]: row for row in b_index.get("routes", [])}
    if len(b_rows) != 43 or set(b_rows) != set(a_archive["routes"]):
        raise SystemExit("Current B must contain the exact same frozen 43-route inventory")
    fixtures: dict[str, dict[str, str]] = {}
    rows = []
    for route in ROUTES:
        a_row = a_archive["routes"][route]
        b_row = b_rows[route]
        if a_row.get("status") != 200 or b_row.get("status") != 200:
            raise SystemExit(f"Expected HTTP 200 in both frozen arms for {route}")
        a_html = a_row["html"]
        b_path = B_RENDER / b_row["evidence"]
        b_bytes = b_path.read_bytes()
        b_html = b_bytes.decode("utf-8", errors="strict")
        if len(a_html) == 0 or len(b_html) == 0:
            raise SystemExit(f"Empty HTML render for {route}")
        if len(a_html.encode("utf-8")) != a_row["bytes"] or SHA(a_html.encode("utf-8")) != a_row["sha256"]:
            raise SystemExit(f"A frozen HTML integrity check failed for {route}")
        if len(b_bytes) != b_row["bytes"]:
            raise SystemExit(f"B frozen HTML byte-count check failed for {route}")
        b_sha256 = SHA(b_bytes)
        fixtures[route] = {"A": a_html, "B": b_html}
        rows.append({
            "route": route,
            "role": ROLES[route],
            "is_reference_control": route in CONTROLS,
            "A_http_status": a_row["status"],
            "B_http_status": b_row["status"],
            "A_html_bytes": a_row["bytes"],
            "B_html_bytes": b_row["bytes"],
            "A_html_sha256": a_row["sha256"],
            "B_html_sha256": b_sha256,
        })
    FIXTURE.parent.mkdir(parents=True, exist_ok=True)
    fixture_bytes = (json.dumps(fixtures, ensure_ascii=False, separators=(",", ":")) + "\n").encode("utf-8")
    FIXTURE.write_bytes(fixture_bytes)
    assets = {}
    for asset in ["assets/images/hero-still-720.webp", "assets/images/hero-still-1440.webp"]:
        data = (ROOT / asset).read_bytes()
        assets[asset] = {"bytes": len(data), "sha256": SHA(data)}
    manifest = {
        "phase": 32,
        "purpose": "Frozen 11-route local A/B fixture manifest. A is the immutable pre-Phase32 render; B is the current committed Phase32 render.",
        "A_source_commit": A_COMMIT,
        "B_source_commit": b_commit,
        "A_render_archive": {"path": A_ARCHIVE.relative_to(ROOT).as_posix(), "sha256": SHA(archive_bytes), "bytes": len(archive_bytes)},
        "B_render_index_sha256": SHA(b_index_bytes),
        "B_render_index_path_outside_repository": str(b_index_path),
        "fixture_json_sha256": SHA(fixture_bytes),
        "fixture_json_bytes": len(fixture_bytes),
        "fixture_path_outside_repository": str(FIXTURE),
        "baseline_inventory_count": 43,
        "route_count": len(ROUTES),
        "control_routes": CONTROLS,
        "selection_reason": "Four reference controls, all four requested hero template groups, the three diagnosed font-chain pages, and second destination/place/article variants for 11 unique routes.",
        "order": "Seven rounds per route; A/B on even rounds and B/A on odd rounds; a fresh Chromium process per sample; serial with no retry or resume.",
        "performance_model": "Lighthouse mobile simulated Slow4G and 4x CPU.",
        "budgets": {
            "added_transfer_bytes_lt": 150000,
            "lcp_ratio_b_over_a_lte": 1.10,
            "tbt_delta_ms_lte": 50,
            "cls_b_no_greater_than_a": True,
            "cls_b_lt": 0.1,
            "no_new_render_blocking_resource": True,
            "reference_lcp_ms_lte": 4000,
            "reference_tbt_ms_lte": 600,
            "reference_cls_lt": 0.1,
            "reference_pre_scene_response_body_bytes_lt": 400000,
        },
        "still_assets": assets,
        "routes": rows,
        "local_or_native_hosting": "local only; no production hosting, CDN or field measurement",
    }
    MANIFEST.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"PASS frozen A/B fixture: {len(ROUTES)} unique routes, {len(CONTROLS)} reference controls")
    print(f"A source {A_COMMIT}; B source {b_commit}")
    print(f"Fixture {FIXTURE} ({len(fixture_bytes)} bytes, sha256 {SHA(fixture_bytes)})")
    print(f"Manifest {MANIFEST.relative_to(ROOT)}")

if __name__ == "__main__":
    main()
