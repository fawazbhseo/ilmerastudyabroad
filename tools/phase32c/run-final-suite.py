#!/usr/bin/env python3
"""Run the Phase32c final verification suite once, serially, without resume."""
from __future__ import annotations
import datetime
import hashlib
import json
import os
import pathlib
import subprocess
import sys
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).resolve().parents[2]
OUT = ROOT / 'reports/phase-32c-final-suite-run-01.json'
RUNTIME = pathlib.Path(os.environ.get('PHASE32C_RUNTIME', '/home/user/phase32c-runtime'))
EVIDENCE = pathlib.Path(os.environ.get('PHASE32C_SUITE_EVIDENCE', str(RUNTIME / 'phase32c-final-suite-run-01')))
BASE = os.environ.get('PHASE31_BASE_URL', 'http://127.0.0.1:8094').rstrip('/')
NODE_MODULES = pathlib.Path(os.environ.get('PHASE31_RUNTIME', str(RUNTIME / 'node_modules')))
PHP_WASM = pathlib.Path(os.environ.get('PHP_WASM_CLI', str(NODE_MODULES / '.bin/php-wasm-cli')))
LOCK = EVIDENCE / 'phase32c-full-suite-started.json'


def utc_now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT, text=True).strip()


def save(report):
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def environment():
    env = dict(os.environ)
    env.update({
        'NODE_PATH': str(NODE_MODULES),
        'PHASE31_RUNTIME': str(NODE_MODULES),
        'PHASE31_EVIDENCE': str(EVIDENCE),
        'PHASE31_BASE_URL': BASE,
        'PHASE32C_RUNTIME': str(RUNTIME),
        'PHASE32C_SUITE_EVIDENCE': str(EVIDENCE),
        'PHP_WASM_CLI': str(PHP_WASM),
        'PHASE32A_PALETTE_OUT': str(EVIDENCE / 'palette.json'),
    })
    env['PATH'] = str(NODE_MODULES / '.bin') + os.pathsep + env.get('PATH', '')
    return env


def log_path(name):
    slug = ''.join(char.lower() if char.isalnum() else '-' for char in name).strip('-')
    return EVIDENCE / 'logs' / (slug + '.log')


def record(report, name, status, started, duration, details=None):
    row = {
        'name': name,
        'status': status,
        'started_at': started,
        'duration_seconds': round(duration, 2),
    }
    if details:
        row.update(details)
    report['groups'].append(row)
    save(report)
    print(f"{status} {name}", flush=True)
    return row


def execute_stream(command, env, log, label):
    log.parent.mkdir(parents=True, exist_ok=True)
    started = time.time()
    with log.open('w', encoding='utf-8', errors='replace') as handle:
        process = subprocess.Popen(
            [str(value) for value in command],
            cwd=ROOT,
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
            errors='replace',
        )
        assert process.stdout is not None
        for line in process.stdout:
            handle.write(line)
            handle.flush()
            print(f'[{label}] {line.rstrip()}', flush=True)
        code = process.wait()
    output = log.read_text(encoding='utf-8', errors='replace')
    return code, time.time() - started, output[-5000:], str(log)


def run_command(report, name, command, env, expected_json=None, validator=None):
    started_at = utc_now()
    log = log_path(name)
    code, duration, tail, logfile = execute_stream(command, env, log, name)
    status = 'PASS' if code == 0 else 'FAIL'
    details = {'command': [str(x) for x in command], 'exit_code': code, 'log': str(log), 'tail': tail}
    if expected_json:
        details['output_json'] = str(expected_json)
        if pathlib.Path(expected_json).is_file():
            try:
                data = json.loads(pathlib.Path(expected_json).read_text(encoding='utf-8'))
                if validator and not validator(data):
                    status = 'FAIL'
                    details['validation_error'] = 'Output JSON did not satisfy the expected result contract'
                details['output_status'] = data.get('status', data.get('passed'))
            except Exception as exc:
                status = 'FAIL'
                details['validation_error'] = f'{type(exc).__name__}: {exc}'
        elif code == 0:
            status = 'FAIL'
            details['validation_error'] = 'Expected JSON output is missing'
    return record(report, name, status, started_at, duration, details)


def run_batch(report, name, commands, env):
    started_at = utc_now()
    start = time.time()
    failures = []
    logs = []
    for index, command in enumerate(commands, 1):
        command_name = pathlib.Path(str(command[-1])).name
        log = log_path(f'{name}-{index:02}-{command_name}')
        code, _, tail, logfile = execute_stream(command, env, log, f'{name} {index}/{len(commands)}')
        logs.append(str(log))
        if code:
            failures.append({'command': [str(x) for x in command], 'exit_code': code, 'log': str(log), 'tail': tail})
    status = 'PASS' if not failures else 'FAIL'
    return record(report, name, status, started_at, time.time() - start, {
        'command_count': len(commands),
        'failures': failures,
        'logs': logs,
    })


def run_php_lint(report, env):
    started_at = utc_now()
    start = time.time()
    files = [name for name in git('ls-files', '-z').split('\0') if name.endswith('.php')]
    files.sort()
    failures = []
    log = log_path('PHP-WASM lint all tracked PHP')
    log.parent.mkdir(parents=True, exist_ok=True)
    with log.open('w', encoding='utf-8', errors='replace') as handle:
        for index, rel in enumerate(files, 1):
            process = subprocess.run(
                [str(PHP_WASM), '-l', str(ROOT / rel)],
                cwd=ROOT,
                env=env,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
            )
            message = process.stdout or ''
            if process.returncode or 'No syntax errors detected' not in message:
                failures.append({'file': rel, 'exit_code': process.returncode, 'output': message[-1000:]})
            if index % 25 == 0 or index == len(files):
                print(f'PHP-WASM lint {index}/{len(files)}', flush=True)
            if process.returncode or 'No syntax errors detected' not in message:
                handle.write(f'FAIL {rel}\n{message}\n')
    lint_report = {'status': 'PASS' if not failures else 'FAIL', 'runtime': 'PHP 8.5.8 WASM CLI via @php-wasm/cli 3.1.50', 'file_count': len(files), 'failures': failures}
    (EVIDENCE / 'php-lint.json').write_text(json.dumps(lint_report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    status = 'PASS' if not failures and len(files) > 0 else 'FAIL'
    return record(report, 'PHP-WASM lint all tracked PHP', status, started_at, time.time() - start, {
        'php_file_count': len(files),
        'failures': failures,
        'runtime': lint_report['runtime'],
        'log': str(log),
        'raw_results': str(EVIDENCE / 'php-lint.json'),
    })


def route_render_check(report, suite_head):
    name = '43 current route renders and adapter integrity'
    started_at = utc_now()
    start = time.time()
    details = {}
    status = 'PASS'
    errors = []
    try:
        index_path = EVIDENCE / 'routes.json'
        render_dir = EVIDENCE / 'render-before'
        index = json.loads(index_path.read_text(encoding='utf-8'))
        entries = index.get('routes', [])
        baseline = json.loads((ROOT / 'reports/phase-32-before-render-index.json').read_text(encoding='utf-8'))
        archive = json.loads(__import__('gzip').decompress((ROOT / 'reports/phase-32-before-renders.json.gz').read_bytes()).decode('utf-8'))
        if index.get('source_head') != suite_head:
            errors.append(f"render source head {index.get('source_head')} does not match suite head {suite_head}")
        if baseline.get('source_commit') != '796879d7b3d5ca0fa1e398562e937e9f364a5f62':
            errors.append('Phase31b baseline index is not from 796879d')
        by_route = {entry.get('url'): entry for entry in entries}
        if len(by_route) != 43 or set(by_route) != set(archive.get('routes', {})):
            errors.append(f'route inventory mismatch: {len(by_route)} current versus {len(archive.get("routes", {}))} frozen')
        render_bytes = 0
        http_count = 0
        status_mismatches = []
        for route in sorted(set(by_route) & set(archive.get('routes', {}))):
            entry = by_route[route]
            base = archive['routes'][route]
            file_path = render_dir / entry.get('evidence', '')
            if not file_path.is_file():
                errors.append(f'missing route render: {route}')
                continue
            body = file_path.read_bytes()
            render_bytes += len(body)
            if len(body) != entry.get('bytes') or sha(body) != entry.get('sha256'):
                errors.append(f'current render index integrity mismatch: {route}')
            if entry.get('status') != base.get('status'):
                status_mismatches.append({'route': route, 'current': entry.get('status'), 'phase31b': base.get('status')})
            try:
                with urllib.request.urlopen(BASE + route, timeout=30) as response:
                    response_body = response.read()
                    http_status = response.status
            except urllib.error.HTTPError as exc:
                response_body = exc.read()
                http_status = exc.code
            except Exception as exc:
                errors.append(f'HTTP render fetch failed for {route}: {type(exc).__name__}: {exc}')
                continue
            if http_status != 200:
                errors.append(f'local adapter HTTP {http_status} for {route}')
            elif response_body != body:
                errors.append(f'local adapter body differs from saved render: {route}')
            else:
                http_count += 1
        if status_mismatches:
            errors.append(f'route status mismatches versus Phase31b: {status_mismatches}')
        if len(entries) != 43:
            errors.append(f'expected 43 route entries, got {len(entries)}')
        details = {
            'render_source_head': index.get('source_head'),
            'suite_head': suite_head,
            'phase31b_source_commit': baseline.get('source_commit'),
            'routes': len(entries),
            'adapter_http_body_matches': http_count,
            'render_bytes': render_bytes,
            'status_mismatches': status_mismatches,
            'render_index_sha256': sha(index_path.read_bytes()),
            'errors': errors,
        }
    except Exception as exc:
        status = 'FAIL'
        details = {'errors': [f'{type(exc).__name__}: {exc}']}
    if errors:
        status = 'FAIL'
    return record(report, name, status, started_at, time.time() - start, details)


def sitemap_check(report):
    name = 'Sitemap exactness and 38 unique URLs'
    started_at = utc_now()
    start = time.time()
    errors = []
    details = {}
    try:
        baseline = (ROOT / 'reports/phase-32-before-sitemap.xml').read_bytes()
        current_path = EVIDENCE / 'sitemap.xml'
        current = current_path.read_bytes()
        root = ET.fromstring(current)
        urls = [node.text or '' for node in root.iter() if node.tag.endswith('loc')]
        if current != baseline:
            errors.append('current sitemap bytes differ from the frozen Phase31b sitemap')
        if len(urls) != 38 or len(set(urls)) != 38:
            errors.append(f'expected 38 unique sitemap URLs, found {len(urls)} entries and {len(set(urls))} unique')
        details = {
            'baseline_sha256': sha(baseline),
            'current_sha256': sha(current),
            'byte_identical_to_phase31b': current == baseline,
            'url_count': len(urls),
            'unique_url_count': len(set(urls)),
            'errors': errors,
        }
    except Exception as exc:
        errors.append(f'{type(exc).__name__}: {exc}')
        details = {'errors': errors}
    return record(report, name, 'PASS' if not errors else 'FAIL', started_at, time.time() - start, details)


def content_report_check(report, name, result_path, required_categories):
    started_at = utc_now()
    start = time.time()
    errors = []
    try:
        data = json.loads(pathlib.Path(result_path).read_text(encoding='utf-8'))
        if data.get('route_count') != 43:
            errors.append(f"route_count is {data.get('route_count')}, expected 43")
        if data.get('status') != 'PASS':
            errors.append(f"comparator status is {data.get('status')}")
        for category in required_categories:
            count = data.get('category_route_counts', {}).get(category)
            if count != 43:
                errors.append(f'{category} parity is {count}/43')
        for category, routes in data.get('category_mismatches', {}).items():
            if routes:
                errors.append(f'{category} mismatches: {routes}')
        details = {
            'report': str(result_path),
            'route_count': data.get('route_count'),
            'category_route_counts': data.get('category_route_counts'),
            'category_mismatches': data.get('category_mismatches'),
            'errors': errors,
        }
    except Exception as exc:
        details = {'report': str(result_path), 'errors': [f'{type(exc).__name__}: {exc}']}
        errors.append(details['errors'][0])
    return record(report, name, 'PASS' if not errors else 'FAIL', started_at, time.time() - start, details)


def run_fresh_axe(report, env):
    name = 'Fresh-process axe A/AA on Home, Services, About and Contact'
    started_at = utc_now()
    start = time.time()
    routes = [('/', 'home'), ('/services', 'services'), ('/about', 'about'), ('/contact', 'contact')]
    results = []
    errors = []
    for route, slug in routes:
        output = EVIDENCE / 'axe' / f'{slug}.json'
        command = ['node', 'tools/phase32c/axe-fresh-route.cjs', '--route', route, '--out', str(output)]
        log = log_path(f'fresh-axe-{slug}')
        code, _, tail, logfile = execute_stream(command, env, log, f'axe {route}')
        row = {'route': route, 'exit_code': code, 'log': str(log), 'output': str(output), 'tail': tail}
        if output.is_file():
            try:
                data = json.loads(output.read_text(encoding='utf-8'))
                row.update({key: data.get(key) for key in ('status', 'browser', 'axe_version', 'violation_node_count', 'baseline_node_count', 'added_node_identities', 'removed_node_identities')})
                if data.get('status') != 'PASS_BASELINE_RELATIVE' or data.get('added_node_identities'):
                    errors.append({'route': route, 'added_node_identities': data.get('added_node_identities'), 'status': data.get('status')})
            except Exception as exc:
                errors.append({'route': route, 'error': f'{type(exc).__name__}: {exc}'})
        else:
            errors.append({'route': route, 'error': 'axe output JSON missing'})
        if code:
            errors.append({'route': route, 'exit_code': code, 'tail': tail})
        results.append(row)
    aggregate = {
        'status': 'PASS' if not errors and len(results) == 4 else 'FAIL',
        'axe_core': '4.11.0',
        'run_only': ['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa'],
        'fresh_chromium_process_per_route': True,
        'routes': results,
        'errors': errors,
        'interpretation': 'Baseline-relative only. Existing identities remain listed; no zero-violation or full-site certification is claimed.',
    }
    aggregate_path = EVIDENCE / 'axe' / 'aggregate.json'
    aggregate_path.parent.mkdir(parents=True, exist_ok=True)
    aggregate_path.write_text(json.dumps(aggregate, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return record(report, name, aggregate['status'], started_at, time.time() - start, {
        'aggregate_report': str(aggregate_path),
        'route_results': results,
        'errors': errors,
    })


def run_blank_space(report, env):
    name = 'Phase31 full blank-space scan and Contact tails'
    started_at = utc_now()
    start = time.time()
    scan_dir = EVIDENCE / 'blank-space-scan'
    summary_out = EVIDENCE / 'blank-space-summary.json'
    if scan_dir.exists() or summary_out.exists():
        return record(report, name, 'FAIL', started_at, time.time() - start, {'error': 'Refusing to reuse existing blank-space outputs'})
    command = [
        'node', 'tools/phase31/scan.cjs',
        '--out', str(scan_dir),
        '--crops', 'no',
        '--screenshot-dir', str(EVIDENCE / 'blank-space-crops'),
    ]
    scan_log = log_path('Phase31 516-case blank-space scan')
    code, scan_seconds, scan_tail, scan_log_name = execute_stream(command, env, scan_log, 'blank-space scan')
    scan_result = {'exit_code': code, 'duration_seconds': round(scan_seconds, 2), 'log': scan_log_name, 'tail': scan_tail}
    summary_code = None
    if (scan_dir / 'summary.json').is_file():
        summarize = [sys.executable, 'tools/phase32c/summarize-blank-space.py', '--scan-dir', str(scan_dir), '--out', str(summary_out)]
        summary_log = log_path('Phase31 blank-space summary')
        summary_code, _, summary_tail, summary_log_name = execute_stream(summarize, env, summary_log, 'blank-space summary')
        summary_result = {'exit_code': summary_code, 'log': summary_log_name, 'tail': summary_tail, 'output': str(summary_out)}
    else:
        summary_result = {'exit_code': None, 'error': 'scan summary.json is missing', 'output': str(summary_out)}
    errors = []
    if code:
        errors.append({'scan_exit_code': code, 'tail': scan_tail})
    if summary_code != 0:
        errors.append({'summary_exit_code': summary_code, 'detail': summary_result})
    if summary_out.is_file():
        try:
            summary = json.loads(summary_out.read_text(encoding='utf-8'))
            if summary.get('status') != 'PASS':
                errors.append({'summary_status': summary.get('status'), 'hidden_reveal_count': len(summary.get('hidden_reveal_text_findings', [])), 'case_failures': summary.get('case_completeness_failures')})
        except Exception as exc:
            errors.append({'summary_parse_error': f'{type(exc).__name__}: {exc}'})
    status = 'PASS' if not errors else 'FAIL'
    return record(report, name, status, started_at, time.time() - start, {
        'scan': scan_result,
        'summary': summary_result,
        'errors': errors,
    })


def run_target_audit(report, env, browser_json):
    name = '44px target rectangle audit'
    out = EVIDENCE / 'target-44px.json'
    return run_command(
        report,
        name,
        [sys.executable, 'tools/phase32c/check-44px-targets.py', '--browser-matrix', str(browser_json), '--out', str(out)],
        env,
        expected_json=out,
        validator=lambda data: data.get('status') == 'PASS',
    )


def main():
    if OUT.exists():
        raise SystemExit(f'Refusing to repeat or resume the one full suite: {OUT} already exists')
    if LOCK.exists():
        raise SystemExit(f'Refusing to repeat the one full suite: {LOCK} already exists')
    branch = git('branch', '--show-current')
    if branch != 'arena/48320ee5-ilmerastudyabroad':
        raise SystemExit(f'Wrong working branch: {branch}')
    suite_head = git('rev-parse', 'HEAD')
    if not (EVIDENCE / 'routes.json').is_file() or not (EVIDENCE / 'sitemap.xml').is_file():
        raise SystemExit('The one current PHP-WASM 43-route render capture is missing')
    if (EVIDENCE / 'browser-matrix.json').exists() or (EVIDENCE / 'blank-space-scan').exists():
        raise SystemExit('A final-suite output already exists; refusing to repeat any suite group')
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    (EVIDENCE / 'logs').mkdir(parents=True, exist_ok=True)
    LOCK.write_text(json.dumps({'suite_head': suite_head, 'branch': branch, 'started_at': utc_now(), 'single_run': True}, indent=2) + '\n', encoding='utf-8')

    report = {
        'phase': '32c',
        'task': 'one_final_full_suite',
        'status': 'RUNNING',
        'branch': branch,
        'suite_head': suite_head,
        'started_at': utc_now(),
        'local_only': True,
        'live_or_production_claim': False,
        'full_suite_run_count': 1,
        'no_resume_or_second_run': True,
        'render_source': {'adapter_evidence': str(EVIDENCE), 'baseline_source_commit': '796879d7b3d5ca0fa1e398562e937e9f364a5f62'},
        'requested_coverage': {
            'php_wasm_lint': True,
            'route_renders': 43,
            'phase31b_comparisons': ['rendered text', 'titles/headings', 'links', 'images', 'picture sources', 'JSON-LD'],
            'normal_browser_cases': 258,
            'reduced_motion_cases': 48,
            'axe_fresh_process_routes': ['/', '/services', '/about', '/contact'],
            'blank_space_scan_cases': 516,
            'target_rectangle_minimum_css_px': 44,
        },
        'evidence_directory_external': str(EVIDENCE),
        'groups': [],
        'runner_error': None,
    }
    save(report)
    env = environment()
    start = time.time()
    try:
        route_render_check(report, suite_head)
        run_php_lint(report, env)

        content_out = EVIDENCE / 'phase31b-content-comparison.json'
        run_command(
            report,
            '43-route text, link, image and picture-source parity to Phase31b',
            [sys.executable, 'tools/phase32c/compare-43-renders.py', '--current', str(EVIDENCE), '--out', str(content_out)],
            env,
            expected_json=content_out,
            validator=lambda data: data.get('status') == 'PASS' and data.get('route_count') == 43 and all(data.get('category_route_counts', {}).get(k) == 43 for k in ('text', 'title', 'headings', 'links', 'images', 'picture_sources')),
        )
        content_report_check(report, '43-route JSON-LD parity to Phase31b', content_out, ['json_ld'])
        sitemap_check(report)

        static_commands = [
            [sys.executable, 'tools/test_discovery.py'],
            [sys.executable, 'tools/test_wording.py'],
            [sys.executable, 'tools/test_citations.py'],
            [sys.executable, 'tools/test_italy_claims.py'],
            [sys.executable, 'tools/test_llm_directory.py'],
            [sys.executable, 'tools/test_llm_policy.py'],
            [sys.executable, 'tools/test_presence.py'],
            [sys.executable, 'tools/test_duplicate_answers.py'],
            [sys.executable, 'tools/test_team_bio_policy.py'],
            [sys.executable, 'tools/test_public_exposure.py'],
        ]
        run_batch(report, 'Static discovery and wording policy fixtures', static_commands, env)
        run_command(report, 'Rendered discovery, robots and inbound-link checks', [sys.executable, 'tools/check_discovery.py', '--base-url', BASE], env)
        run_command(report, 'Rendered publication wording and protected-copy review', [sys.executable, 'tools/check_publication_review.py', '--base-url', BASE], env)
        run_command(report, 'Technical SEO and structured-data validation', [sys.executable, 'tools/check_technical_seo.py', '--base-url', BASE], env)
        run_command(report, 'Phase20 published-route inventory', [sys.executable, 'tools/check_phase20.py', '--base-url', BASE], env)

        palette_out = EVIDENCE / 'palette.json'
        run_command(
            report,
            'Palette and measured fallback scope',
            ['node', 'tools/phase32a/palette_check.cjs'],
            env,
            expected_json=palette_out,
            validator=lambda data: data.get('status') == 'PASS' and len(data.get('cases', [])) == 12 and data.get('reduced_motion', {}).get('transition') == '0s',
        )

        browser_json = EVIDENCE / 'browser-matrix.json'
        browser_row = run_command(
            report,
            '258-case browser matrix, overflow and target-baseline shrink checks',
            ['node', 'tools/phase31/browser-suite.cjs', '--out', str(browser_json), '--require-visible', '--target-baseline', 'reports/phase-31-target-baseline.json'],
            env,
            expected_json=browser_json,
            validator=lambda data: data.get('normal_cases') == 258 and data.get('reduced_motion_cases') == 48 and data.get('total_cases') == 306 and len(data.get('cases', [])) == 306 and not data.get('target_size_baseline_comparison', {}).get('failures'),
        )
        if browser_row['status'] == 'PASS':
            try:
                browser = json.loads(browser_json.read_text(encoding='utf-8'))
                overflow = [case for case in browser['cases'] if case['scroll_width'] > case['width'] + 1 or case.get('body_scroll_width', case['width']) > case['width'] + 1]
                if overflow:
                    browser_row['status'] = 'FAIL'
                    browser_row['overflow_cases'] = overflow
                browser_row['normal_cases'] = browser.get('normal_cases')
                browser_row['reduced_motion_cases'] = browser.get('reduced_motion_cases')
                browser_row['total_cases'] = browser.get('total_cases')
                browser_row['overflow_case_count'] = len(overflow)
                browser_row['baseline_target_comparison'] = browser.get('target_size_baseline_comparison')
                save(report)
            except Exception as exc:
                browser_row['status'] = 'FAIL'
                browser_row['validation_error'] = f'{type(exc).__name__}: {exc}'
                save(report)
            run_target_audit(report, env, browser_json)
        else:
            record(report, '44px target rectangle audit', 'FAIL', utc_now(), 0, {'error': 'Required browser matrix did not complete; the 44px audit was not run.'})

        run_fresh_axe(report, env)
        run_blank_space(report, env)

        diff_check = run_command(report, 'Git whitespace and CRLF-aware diff check', ['git', '-c', 'core.whitespace=cr-at-eol', 'diff', '--check'], env)
        report['git_diff_check_status'] = diff_check['status']
    except Exception as exc:
        report['runner_error'] = f'{type(exc).__name__}: {exc}'
        save(report)
    report['finished_at'] = utc_now()
    report['suite_seconds'] = round(time.time() - start, 2)
    report['completed_group_count'] = len(report['groups'])
    report['failed_groups'] = [group['name'] for group in report['groups'] if group['status'] != 'PASS']
    report['planned_group_count'] = 16
    report['status'] = 'PASS' if not report['runner_error'] and not report['failed_groups'] and len(report['groups']) == 16 else 'FAIL'
    report['complete_no_skip_or_resume'] = not report['runner_error'] and len(report['groups']) == 16
    save(report)
    print(f"PHASE32C FINAL SUITE {report['status']}: {len(report['groups'])} groups, failed={len(report['failed_groups'])}, {report['suite_seconds']} seconds", flush=True)
    if report['failed_groups'] or report['runner_error']:
        sys.exit(1)


if __name__ == '__main__':
    main()
