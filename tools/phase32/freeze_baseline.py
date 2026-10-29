#!/usr/bin/env python3
"""Freeze the pre-Phase32 PHP renders without changing the session branch."""
from __future__ import annotations
import gzip, hashlib, json, pathlib, subprocess, urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[2]
BASE_URL = "http://127.0.0.1:8080"
BASELINE_COMMIT = "796879d7b3d5ca0fa1e398562e937e9f364a5f62"
ROUTES_FILE = ROOT / "reports/phase-25-baseline-renders.json"
ARCHIVE = ROOT / "reports/phase-32-before-renders.json.gz"
INDEX = ROOT / "reports/phase-32-before-render-index.json"
SITEMAP = ROOT / "reports/phase-32-before-sitemap.xml"
SHA = lambda data: hashlib.sha256(data).hexdigest()

def fetch(route: str) -> tuple[int, bytes]:
    with urllib.request.urlopen(BASE_URL + route, timeout=90) as response:
        return response.status, response.read()

def main() -> None:
    runtime_changes = subprocess.check_output(
        ["git", "diff", "--name-only", BASELINE_COMMIT, "HEAD", "--",
         "*.php", "includes/**", "assets/**", "data/**", "destinations/**",
         "places/**", "blog/**", "robots.txt", "sitemap.xml", "llms.txt", "llms-full.txt"],
        cwd=ROOT, text=True,
    ).splitlines()
    if runtime_changes:
        raise SystemExit(f"Pre-Phase32 runtime differs from {BASELINE_COMMIT[:7]}: {runtime_changes}")
    route_info = json.loads(ROUTES_FILE.read_text(encoding="utf-8"))["routes"]
    routes = sorted(route_info)
    if len(routes) != 43 or len(set(routes)) != 43:
        raise SystemExit(f"Expected the frozen 43-route inventory, found {len(routes)}")
    rows = {}
    index_rows = []
    for route in routes:
        status, body = fetch(route)
        if status != 200:
            raise SystemExit(f"Expected HTTP 200 for {route}, got {status}")
        text = body.decode("utf-8", errors="strict")
        rows[route] = {"status": status, "bytes": len(body), "sha256": SHA(body), "html": text}
        index_rows.append({"route": route, "status": status, "bytes": len(body), "sha256": SHA(body)})
    sitemap_status, sitemap = fetch("/sitemap.xml")
    if sitemap_status != 200:
        raise SystemExit(f"Expected sitemap HTTP 200, got {sitemap_status}")
    import xml.etree.ElementTree as ET
    urls = [node.text for node in ET.fromstring(sitemap).iter() if node.tag.endswith("loc")]
    if len(urls) != 38 or len(set(urls)) != 38:
        raise SystemExit(f"Expected the exact 38 unique sitemap URLs, got {len(urls)}")
    payload = json.dumps({"source_commit": BASELINE_COMMIT, "rendered_at_head": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(), "routes": rows}, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    ARCHIVE.write_bytes(gzip.compress(payload, compresslevel=9, mtime=0))
    SITEMAP.write_bytes(sitemap)
    manifest = {
        "phase": 32,
        "purpose": "Immutable pre-Phase32 rendered comparison baseline",
        "source_commit": BASELINE_COMMIT,
        "rendered_at_head": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
        "rendered_runtime_diff_from_baseline_commit": runtime_changes,
        "route_count": len(routes),
        "routes": index_rows,
        "render_archive": ARCHIVE.relative_to(ROOT).as_posix(),
        "render_archive_sha256": SHA(ARCHIVE.read_bytes()),
        "render_archive_bytes": ARCHIVE.stat().st_size,
        "sitemap": {"path": SITEMAP.relative_to(ROOT).as_posix(), "status": sitemap_status, "bytes": len(sitemap), "sha256": SHA(sitemap), "entries": len(urls)},
        "live_or_native_hosting": False,
    }
    INDEX.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"PASS frozen {len(routes)} routes and {len(urls)} sitemap entries; archive {ARCHIVE.stat().st_size} bytes")

if __name__ == "__main__":
    main()
