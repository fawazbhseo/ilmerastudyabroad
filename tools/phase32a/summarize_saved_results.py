#!/usr/bin/env python3
"""Aggregate the saved Phase32a suite and targeted reruns without running tests."""
from __future__ import annotations
import datetime
import json
import pathlib

ROOT=pathlib.Path(__file__).resolve().parents[2]
SUITE=ROOT/'reports/phase-32a-full-suite-run-01.json'
RERUNS=ROOT/'reports/phase-32a-2-rerun-results.json'

def main():
    report=json.loads(SUITE.read_text(encoding='utf-8'))
    reruns=json.loads(RERUNS.read_text(encoding='utf-8'))
    checks=report.get('checks')
    if not isinstance(checks,list) or len(checks)!=24:
        raise ValueError(f'Expected 24 saved checks, found {len(checks) if isinstance(checks,list) else "invalid"}')
    by_name={row.get('name'):row for row in checks}
    if len(by_name)!=24 or None in by_name:
        raise ValueError('Saved suite check names are missing or duplicated')

    original_snapshot=report.get('original_run') or {
        'status':report.get('status'),
        'failed_checks':report.get('failed_checks',[]),
        'runner_error':report.get('runner_error'),
        'suite_exit_code':report.get('suite_exit_code'),
        'started_at':report.get('started_at'),
        'finished_at':report.get('finished_at'),
    }

    target_statuses={}
    details={}
    for row in reruns.get('groups',[]):
        if row.get('substep')=='a':
            name=row['name']
            if row.get('rerun_status') not in {'PASS','FAIL'}:
                raise ValueError(f'Invalid rendered check rerun status for {name}')
            target_statuses[name]=row['rerun_status']
            details[name]={k:row.get(k) for k in ['previous_status','rerun_status','attempts','command','runtime','adapter','summary','log_external']}

    browser=reruns.get('browser_rechecks')
    if not isinstance(browser,dict):
        raise ValueError('Saved isolated browser rerun details are missing')
    palette=browser.get('palette',{})
    palette_complete=(palette.get('routes')==10 and palette.get('passed_cases')==10 and not palette.get('failed_cases'))
    target_statuses['Final palette and fallback scope']='PASS' if palette_complete and palette.get('status')=='PASS' else 'FAIL'
    details['Final palette and fallback scope']={
        'previous_status':'FAIL',
        'rerun_status':target_statuses['Final palette and fallback scope'],
        'isolated_cases':palette.get('routes'),
        'passed_cases':palette.get('passed_cases'),
        'failed_cases':palette.get('failed_cases'),
        'crashed_process_attempts':browser.get('crashed_process_attempts',[]),
        'evidence':'reports/phase-32a-2-rerun-results.json#browser_rechecks.palette',
    }

    axe=browser.get('axe',{})
    axe_complete=(len(axe.get('routes',[]))==8 and all(r.get('process_result',{}).get('status')=='PASS' for r in axe.get('routes',[])))
    axe_status='PASS' if axe_complete and not axe.get('added_findings') else 'FAIL'
    target_statuses['Axe representative pages, one per template']=axe_status
    details['Axe representative pages, one per template']={
        'previous_status':'FAIL',
        'rerun_status':axe_status,
        'baseline':'reports/phase-31-accessibility-baseline.json',
        'baseline_nodes':axe.get('baseline_total_nodes'),
        'current_nodes':axe.get('current_total_nodes'),
        'added_count':len(axe.get('added_findings',[])),
        'resolved_count':len(axe.get('resolved_findings',[])),
        'added_findings':axe.get('added_findings',[]),
        'routes':[
            {'route':r.get('route'),'template':r.get('template'),'comparison':r.get('baseline_comparison')}
            for r in axe.get('routes',[])
        ],
        'evidence':'reports/phase-32a-2-rerun-results.json#browser_rechecks.axe',
    }

    for name,status in target_statuses.items():
        if name not in by_name:
            raise ValueError(f'Rerun result has no matching original check: {name}')
        row=by_name[name]
        previous=row.get('initial_status',row.get('status'))
        if details[name].get('previous_status') not in (None,previous):
            raise ValueError(f'Original status mismatch for {name}: {details[name].get("previous_status")} vs {previous}')
        row['initial_status']=previous
        row['status']=status
        row['targeted_rerun']=details[name]

    final_statuses=[r.get('status') for r in checks]
    if any(s not in {'PASS','FAIL'} for s in final_statuses):
        raise ValueError('A saved check has an unknown final status')
    failed=[r['name'] for r in checks if r['status']!='PASS']
    pass_count=len(checks)-len(failed)
    if len(target_statuses)!=4:
        raise ValueError(f'Expected four targeted rerun groups, found {len(target_statuses)}')

    report['original_run']=original_snapshot
    report['original_run_status']=original_snapshot.get('status')
    report['original_failed_checks']=original_snapshot.get('failed_checks',[])
    report['original_runner_error']=original_snapshot.get('runner_error')
    report['status']='PASS' if not failed else 'FAIL'
    report['completed_checks']=len(checks)
    report['failed_checks']=failed
    report['runner_error']=None
    report['summary_aggregation_error']=None
    report['summary_recomputed_from_saved_results']=True
    report['summary_recomputed_at']=datetime.datetime.now(datetime.timezone.utc).isoformat()
    report['summary_method']='tools/phase32a/summarize_saved_results.py'
    report['full_suite_rerun']=False
    report['final_summary']={
        'status':report['status'],
        'total_groups':len(checks),
        'pass_count':pass_count,
        'fail_count':len(failed),
        'failed_checks':failed,
        'targeted_groups_rechecked':sorted(target_statuses),
        'aggregation_error':None,
        'recomputed_without_keyerror':True,
        'full_suite_rerun':False,
        'scope':'original saved 24 checks with only the four requested targeted rerun outcomes overlaid',
    }
    SUITE.write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

    reruns['summary_aggregation']={
        'status':'PASS',
        'method':'tools/phase32a/summarize_saved_results.py',
        'total_groups':len(checks),
        'pass_count':pass_count,
        'fail_count':len(failed),
        'failed_checks':failed,
        'keyerror':None,
        'full_suite_rerun':False,
    }
    RERUNS.write_text(json.dumps(reruns,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(f"SUMMARY PASS: {len(checks)} groups aggregated without KeyError; {pass_count} PASS, {len(failed)} FAIL")
    if failed:
        print('Remaining failed group(s): '+', '.join(failed))
    else:
        print('All groups PASS')

if __name__=='__main__':
    main()
