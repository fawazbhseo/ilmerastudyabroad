#!/usr/bin/env python3
"""Analyze the already-committed Phase32c Task 3 raw Lighthouse samples."""
from __future__ import annotations
import datetime
import hashlib
import json
import pathlib
import subprocess

ROOT=pathlib.Path(__file__).resolve().parents[2]
RAW=ROOT/'reports/phase-32c-hero-ab-raw.json'
FIXTURE_MANIFEST=ROOT/'reports/phase-32c-hero-ab-fixtures.json'
OUT_JSON=ROOT/'reports/phase-32c-hero-ab-analysis.json'
OUT_MD=ROOT/'reports/phase-32c-hero-ab-analysis.md'
RAW_SHA_EXPECTED='039eb45d973b00844df525665d1ce6d6ebfb7a592c2db93dc0758aadd4e8351b'
RAW_COMMIT_EXPECTED='9ad242e'
ROUTES=[
    '/study-abroad-counselling-mysuru',
    '/blog/how-to-choose-study-abroad-consultant-karnataka',
]
PRIMARY_ARMS=['A','B-still','B-plain']
BUDGETS={
    'added_transfer_bytes_strictly_less_than':150000,
    'no_new_render_blocking_resource':True,
    'CLS_no_worse_than_A_and_below':0.1,
    'LCP_B_over_A_at_most':1.10,
    'TBT_increase_ms_at_most':50,
}

def sha(data:bytes)->str:
    return hashlib.sha256(data).hexdigest()

def git(*args:str)->str:
    return subprocess.check_output(['git',*args],cwd=ROOT,text=True).strip()

def quantile(values:list[float],q:float)->float:
    ordered=sorted(values)
    position=(len(ordered)-1)*q
    lower=int(position)
    upper=min(lower+1,len(ordered)-1)
    return ordered[lower]+(ordered[upper]-ordered[lower])*(position-lower)

def stats(values:list[float])->dict:
    if not values:raise SystemExit('Cannot summarize an empty metric set')
    q1=quantile(values,.25)
    median=quantile(values,.5)
    q3=quantile(values,.75)
    return {'median':median,'q1':q1,'q3':q3,'iqr':q3-q1,'min':min(values),'max':max(values),'n':len(values)}

def expected_plan()->list[dict]:
    orders=[
        ['A','B-still','B-plain'],
        ['A','B-plain','B-still'],
        ['B-still','A','B-plain'],
        ['B-still','B-plain','A'],
        ['B-plain','A','B-still'],
        ['B-plain','B-still','A'],
        ['A','B-still','B-plain'],
        ['B-still','B-plain','A'],
        ['B-plain','A','B-still'],
    ]
    plan=[]
    for round_number in range(9):
        route_order=ROUTES if round_number%2==0 else list(reversed(ROUTES))
        for route in route_order:
            arms=list(orders[round_number])
            if route==ROUTES[0]:
                index=arms.index('A')
                arms.insert(index+(1 if round_number%2==0 else 0),'A-repeat')
            for position,arm in enumerate(arms,1):
                plan.append({'round':round_number,'route':route,'arm':arm,'order':'>'.join(arms),'order_position':position})
    return plan

def validate(raw:dict,raw_bytes:bytes,fixture:dict)->tuple[dict,list[dict]]:
    if sha(raw_bytes)!=RAW_SHA_EXPECTED:raise SystemExit('Raw evidence hash differs from the committed pre-analysis checkpoint')
    if raw.get('status')!='COMPLETE' or raw.get('analysis_status')!='NOT_STARTED':raise SystemExit('Raw evidence is not a complete unanalysed session')
    if raw.get('environment',{}).get('A_source_commit')!=fixture['source_commits']['A'] or raw.get('environment',{}).get('B_source_commit')!=fixture['source_commits']['B_current']:
        raise SystemExit('Raw A/B source commits do not match the committed fixture manifest')
    if raw.get('fixture_manifest_sha256')!=sha(FIXTURE_MANIFEST.read_bytes()):raise SystemExit('Raw fixture-manifest hash mismatch')
    raw_commit=git('log','-1','--format=%H','--',str(RAW.relative_to(ROOT)))
    if not raw_commit.startswith(RAW_COMMIT_EXPECTED):raise SystemExit(f'Raw file was not committed at the expected checkpoint: {raw_commit}')
    if git('status','--porcelain','--',str(RAW.relative_to(ROOT))):raise SystemExit('Raw evidence is modified after its commit')
    samples=raw.get('samples',[])
    if len(samples)!=63 or len(raw.get('planned_order',[]))!=63:raise SystemExit(f'Expected 63 samples, got {len(samples)}')
    plan=expected_plan()
    if len(raw.get('planned_order',[]))!=len(plan):raise SystemExit('Recorded plan length mismatch')
    for planned_raw,planned in zip(raw['planned_order'],plan):
        if any(planned_raw.get(key)!=value for key,value in planned.items()):raise SystemExit('Top-level planned order differs from the fixed schedule')
    for index,(sample,planned) in enumerate(zip(samples,plan),1):
        for key,value in planned.items():
            if sample.get(key)!=value:raise SystemExit(f'Sample order mismatch at index {index}, field {key}')
        if sample.get('sample_index')!=index or sample.get('status')!='PASS' or sample.get('fresh_browser_process') is not True:
            raise SystemExit(f'Invalid raw sample status/index at {index}')
        if not str(sample.get('browser_version','')).startswith('143.'):
            raise SystemExit(f'Unexpected browser version at sample {index}')
        for key in ['lcp_ms','cls','tbt_ms','transfer_bytes','requests']:
            if not isinstance(sample.get(key),(int,float)):
                raise SystemExit(f'Missing raw metric {key} at sample {index}')
        settings=sample.get('lighthouse_settings',{})
        if settings.get('form_factor')!='mobile' or settings.get('throttling_method')!='simulate':
            raise SystemExit(f'Unexpected Lighthouse model at sample {index}: {settings}')
    counts={route:{'A':0,'B-still':0,'B-plain':0,'A-repeat':0} for route in ROUTES}
    for sample in samples:counts[sample['route']][sample['arm']]+=1
    expected_counts={
        ROUTES[0]:{'A':9,'B-still':9,'B-plain':9,'A-repeat':9},
        ROUTES[1]:{'A':9,'B-still':9,'B-plain':9,'A-repeat':0},
    }
    if counts!=expected_counts:raise SystemExit(f'Arm counts mismatch: {counts}')
    return counts,plan

def main()->None:
    if OUT_JSON.exists() or OUT_MD.exists():raise SystemExit('Refusing to overwrite existing Task 3 analysis outputs')
    raw_bytes=RAW.read_bytes()
    raw=json.loads(raw_bytes)
    fixture=json.loads(FIXTURE_MANIFEST.read_text(encoding='utf-8'))
    counts,plan=validate(raw,raw_bytes,fixture)
    groups={(route,arm):[s for s in raw['samples'] if s['route']==route and s['arm']==arm] for route in ROUTES for arm in ['A','B-still','B-plain','A-repeat']}
    metric_keys=['lcp_ms','cls','tbt_ms','transfer_bytes','requests']
    summaries={}
    for route in ROUTES:
        summaries[route]={}
        for arm in PRIMARY_ARMS:
            samples=groups[(route,arm)]
            summaries[route][arm]={key:stats([float(sample[key]) for sample in samples]) for key in metric_keys}
    paired={}
    for route in ROUTES:
        paired[route]={arm:[] for arm in ['B-still','B-plain']}
        for round_number in range(9):
            a=next(s for s in groups[(route,'A')] if s['round']==round_number)
            for arm in ['B-still','B-plain']:
                b=next(s for s in groups[(route,arm)] if s['round']==round_number)
                paired[route][arm].append({
                    'round':round_number+1,
                    'lcp_ratio_B_over_A':float(b['lcp_ms'])/float(a['lcp_ms']),
                    'tbt_delta_ms_B_minus_A':float(b['tbt_ms'])-float(a['tbt_ms']),
                    'cls_delta_B_minus_A':float(b['cls'])-float(a['cls']),
                    'transfer_delta_bytes_B_minus_A':float(b['transfer_bytes'])-float(a['transfer_bytes']),
                })
    aa_pairs=[]
    for round_number in range(9):
        a=next(s for s in groups[(ROUTES[0],'A')] if s['round']==round_number)
        repeat=next(s for s in groups[(ROUTES[0],'A-repeat')] if s['round']==round_number)
        aa_pairs.append({
            'round':round_number+1,
            'lcp_A_ms':float(a['lcp_ms']),'lcp_A_repeat_ms':float(repeat['lcp_ms']),
            'lcp_repeat_over_A':float(repeat['lcp_ms'])/float(a['lcp_ms']),
            'lcp_abs_difference_ms':abs(float(repeat['lcp_ms'])-float(a['lcp_ms'])),
            'tbt_A_ms':float(a['tbt_ms']),'tbt_A_repeat_ms':float(repeat['tbt_ms']),
            'tbt_signed_difference_ms':float(repeat['tbt_ms'])-float(a['tbt_ms']),
            'tbt_abs_difference_ms':abs(float(repeat['tbt_ms'])-float(a['tbt_ms'])),
            'cls_abs_difference':abs(float(repeat['cls'])-float(a['cls'])),
            'transfer_abs_difference_bytes':abs(float(repeat['transfer_bytes'])-float(a['transfer_bytes'])),
        })
    noise={
        'route':ROUTES[0],
        'method':'Nine same-route A/A pairs. Report paired absolute differences and A-repeat/A ratios. The maximum observed absolute differences are used as a conservative margin check; this is a small-sample noise estimate, not a confidence interval.',
        'lcp_abs_difference_ms':stats([pair['lcp_abs_difference_ms'] for pair in aa_pairs]),
        'lcp_repeat_over_A':stats([pair['lcp_repeat_over_A'] for pair in aa_pairs]),
        'lcp_max_absolute_ratio_deviation_from_1':max(abs(pair['lcp_repeat_over_A']-1) for pair in aa_pairs),
        'tbt_abs_difference_ms':stats([pair['tbt_abs_difference_ms'] for pair in aa_pairs]),
        'tbt_signed_difference_ms':stats([pair['tbt_signed_difference_ms'] for pair in aa_pairs]),
        'cls_abs_difference':stats([pair['cls_abs_difference'] for pair in aa_pairs]),
        'transfer_abs_difference_bytes':stats([pair['transfer_abs_difference_bytes'] for pair in aa_pairs]),
        'pairs':aa_pairs,
    }
    blocking={}
    still_requests={}
    request_quality={}
    budget_results={}
    for route in ROUTES:
        a_samples=groups[(route,'A')]
        a_blocking={url for sample in a_samples for url in sample.get('render_blocking',[])}
        blocking[route]={'A_union':sorted(a_blocking),'candidates':{}}
        still_requests[route]={}
        request_quality[route]={}
        for arm in ['A','B-still','B-plain']:
            arm_samples=groups[(route,arm)]
            requests=[row for sample in arm_samples for row in sample.get('still_requests',[])]
            still_requests[route][arm]={
                'samples_with_still_request':sum(bool(sample.get('still_requests')) for sample in arm_samples),
                'request_count':len(requests),
                'urls':sorted({item['url'] for item in requests}),
                'median_transfer_bytes_per_still_request':stats([float(item['transferSize'] or 0) for item in requests]) if requests else None,
            }
            request_quality[route][arm]={
                'samples_with_warnings':sum(bool(sample.get('warnings')) for sample in arm_samples),
                'warning_count':sum(len(sample.get('warnings',[])) for sample in arm_samples),
                'request_failure_count':sum(len(sample.get('request_failures',[])) for sample in arm_samples),
                'distinct_request_failure_urls':sorted({item.get('url','') for sample in arm_samples for item in sample.get('request_failures',[])}),
            }
            if arm=='A':continue
            arm_blocking={url for sample in arm_samples for url in sample.get('render_blocking',[])}
            new_blocking=sorted(arm_blocking-a_blocking)
            blocking[route]['candidates'][arm]={'arm_union':sorted(arm_blocking),'new_urls_vs_A':new_blocking}
            a_summary=summaries[route]['A'];b_summary=summaries[route][arm]
            transfer_delta=b_summary['transfer_bytes']['median']-a_summary['transfer_bytes']['median']
            lcp_ratio=b_summary['lcp_ms']['median']/a_summary['lcp_ms']['median']
            tbt_delta=b_summary['tbt_ms']['median']-a_summary['tbt_ms']['median']
            cls_delta=b_summary['cls']['median']-a_summary['cls']['median']
            point={
                'added_transfer':{'delta_bytes':transfer_delta,'strict_threshold_bytes':150000,'pass':transfer_delta<150000},
                'no_new_render_blocking':{'new_urls':new_blocking,'pass':not new_blocking},
                'lcp':{'B_over_A':lcp_ratio,'maximum':1.10,'pass':lcp_ratio<=1.10},
                'tbt':{'B_minus_A_ms':tbt_delta,'maximum_increase_ms':50,'pass':tbt_delta<=50},
                'cls':{'A_median':a_summary['cls']['median'],'B_median':b_summary['cls']['median'],'B_minus_A':cls_delta,'B_must_be_less_than':0.1,'pass':b_summary['cls']['median']<=a_summary['cls']['median'] and b_summary['cls']['median']<0.1},
            }
            point['result']='PASS' if all(check['pass'] for check in point.values() if isinstance(check,dict) and 'pass' in check) else 'FAIL'
            budget_results.setdefault(route,{})[arm]={'point_estimate_budgets':point}
    lcp_noise=noise['lcp_max_absolute_ratio_deviation_from_1']
    tbt_noise=noise['tbt_abs_difference_ms']['max']
    cls_noise=noise['cls_abs_difference']['max']
    for route in ROUTES:
        for arm in ['B-still','B-plain']:
            point=budget_results[route][arm]['point_estimate_budgets']
            lcp_upper=point['lcp']['B_over_A']+lcp_noise
            tbt_upper=point['tbt']['B_minus_A_ms']+tbt_noise
            cls_upper=point['cls']['B_minus_A']+cls_noise
            margin={
                'lcp_noise_adjusted_upper_ratio':lcp_upper,
                'lcp_maximum':1.10,
                'lcp_margin_pass':lcp_upper<=1.10,
                'tbt_noise_adjusted_upper_delta_ms':tbt_upper,
                'tbt_maximum_increase_ms':50,
                'tbt_margin_pass':tbt_upper<=50,
                'cls_noise_adjusted_upper_delta':cls_upper,
                'cls_no_worse_maximum_delta':0,
                'cls_margin_pass':cls_upper<=0 and point['cls']['B_median']<0.1,
                'noise_floor_route':'/study-abroad-counselling-mysuru',
                'article_noise_note':'Mysuru A/A values are used as a conservative same-harness margin proxy. There is no separate article A/A block, so article uncertainty is not independently measured.',
            }
            margin['result']='PASS' if margin['lcp_margin_pass'] and margin['tbt_margin_pass'] and margin['cls_margin_pass'] else 'INCONCLUSIVE_OR_FAIL'
            budget_results[route][arm]['noise_adjusted_margin_check']=margin
            budget_results[route][arm]['conservative_still_eligible']=point['result']=='PASS' and margin['result']=='PASS'
    still_eligible=all(budget_results[route]['B-still']['conservative_still_eligible'] for route in ROUTES)
    decision='B-still' if still_eligible else 'B-plain'
    decision_text=('Select B-still only if it passes all five point-estimate budgets on both routes and its LCP, TBT and CLS remain inside those limits after adding the maximum observed Mysuru A/A absolute noise margin. Any failed point budget or unresolved noise-adjusted margin selects B-plain.'
                   ' The added noise margin is stricter than the owner limits and cannot relax them.')
    raw_commit=git('log','-1','--format=%H','--',str(RAW.relative_to(ROOT)))
    result={
        'phase':'32c','task':'3_hero_still_three_arm_ab_analysis','analysis_status':'COMPLETE',
        'generated_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'evidence_scope':'Local simulated Lighthouse data only. Not PageSpeed Insights, field data, production/CDN timing or a live-site performance claim.',
        'raw_evidence':{'path':str(RAW.relative_to(ROOT)),'bytes':len(raw_bytes),'sha256':sha(raw_bytes),'committed_before_analysis':True,'commit':raw_commit,'sample_count':len(raw['samples']),'all_sample_statuses_pass':True,'counts':counts},
        'fixture_manifest':{'path':str(FIXTURE_MANIFEST.relative_to(ROOT)),'sha256':sha(FIXTURE_MANIFEST.read_bytes()),'A_source_commit':fixture['source_commits']['A'],'B_source_commit':fixture['source_commits']['B_current'],'prior_fixture_provenance_audit':fixture['prior_phase31_fixture_audit']},
        'fixed_budgets':BUDGETS,
        'summary_method':'Linear interpolation quantiles using p=(n-1)q, matching the existing Phase32 A/B runner. For each route and primary arm, report median, Q1, Q3 and IQR for LCP, CLS, TBT, total-byte-weight transfer and request count. Budget comparisons use primary-arm and A medians.',
        'arm_summaries':summaries,
        'paired_rounds':paired,
        'A_A_noise_floor':noise,
        'render_blocking_comparison':blocking,
        'still_request_summary':still_requests,
        'sample_quality':request_quality,
        'budget_results':budget_results,
        'conservative_decision_rule':decision_text,
        'decision':{'selected_test_arm':decision,'all_route_B_still_conservative_eligibility':still_eligible,'rationale':'B-still is not selected unless every strict gate and each noise-adjusted safety margin pass on both routes. The existing plain palette is retained when any result is failed or inconclusive. No production source was changed by this local test decision.'},
        'owner_confirmation_required':'Owner confirmation via PageSpeed Insights remains required before any live-site performance conclusion or release decision.',
    }
    OUT_JSON.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    lines=[
        '# Phase32c Task 3 hero-still A/B analysis','',
        '## Scope and raw evidence','',
        f"This is a local simulated Lighthouse analysis, not PageSpeed Insights, field data, production/CDN timing or a live-site performance claim. The committed raw input is `{RAW.relative_to(ROOT)}` ({len(raw_bytes):,} bytes, SHA-256 `{sha(raw_bytes)}`), committed as `{raw_commit[:7]}` before analysis. All {len(raw['samples'])} planned fresh-browser sample rows passed collection QA.",'',
        f"Routes: `{ROUTES[0]}` and `{ROUTES[1]}`. A source: `{fixture['source_commits']['A']}`. Current B source: `{fixture['source_commits']['B_current']}`. Each primary arm has nine samples per route; Mysuru includes nine additional adjacent A/A pairs.",'',
        '## Median and IQR results','',
        '| Route | Arm | n | LCP median (ms) | LCP IQR | CLS median | CLS IQR | TBT median (ms) | TBT IQR | Transfer median (bytes) | Transfer IQR | Requests median | Requests IQR |','|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|',
    ]
    for route in ROUTES:
        for arm in PRIMARY_ARMS:
            values=summaries[route][arm]
            fmt=lambda key,field:f"{values[key][field]:.3f}"
            lines.append(f"| `{route}` | {arm} | {values['lcp_ms']['n']} | {fmt('lcp_ms','median')} | {fmt('lcp_ms','iqr')} | {fmt('cls','median')} | {fmt('cls','iqr')} | {fmt('tbt_ms','median')} | {fmt('tbt_ms','iqr')} | {fmt('transfer_bytes','median')} | {fmt('transfer_bytes','iqr')} | {fmt('requests','median')} | {fmt('requests','iqr')} |")
    lines+=['','## Paired-round ratios and deltas','','LCP ratios are candidate/A for the same route and round. TBT, CLS and transfer fields are B minus A. Values are listed for all nine rounds.','']
    for route in ROUTES:
        lines += [f"### `{route}`",'', '| Round | B-still/A LCP | B-still TBT delta (ms) | B-plain/A LCP | B-plain TBT delta (ms) |','|---:|---:|---:|---:|---:|']
        for index in range(9):
            still=paired[route]['B-still'][index]
            plain=paired[route]['B-plain'][index]
            lines.append(f"| {index+1} | {still['lcp_ratio_B_over_A']:.4f} | {still['tbt_delta_ms_B_minus_A']:.3f} | {plain['lcp_ratio_B_over_A']:.4f} | {plain['tbt_delta_ms_B_minus_A']:.3f} |")
    lines+=['','## A/A noise floor','','Nine paired fresh-browser repeats on Mysuru compare the primary A sample with its adjacent A-repeat sample. The maximum observed absolute differences are used only as a stricter decision margin, not as a confidence interval. The same-harness Mysuru noise proxy is applied to the article route because no separate article A/A block was collected.','',
        '| Metric | Median | IQR | Maximum observed |','|---|---:|---:|---:|',
        f"| Absolute LCP difference (ms) | {noise['lcp_abs_difference_ms']['median']:.3f} | {noise['lcp_abs_difference_ms']['iqr']:.3f} | {noise['lcp_abs_difference_ms']['max']:.3f} |",
        f"| A-repeat/A LCP ratio | {noise['lcp_repeat_over_A']['median']:.4f} | {noise['lcp_repeat_over_A']['iqr']:.4f} | max absolute deviation from 1 = {noise['lcp_max_absolute_ratio_deviation_from_1']:.4f} |",
        f"| Absolute TBT difference (ms) | {noise['tbt_abs_difference_ms']['median']:.3f} | {noise['tbt_abs_difference_ms']['iqr']:.3f} | {noise['tbt_abs_difference_ms']['max']:.3f} |",
        f"| Absolute CLS difference | {noise['cls_abs_difference']['median']:.6f} | {noise['cls_abs_difference']['iqr']:.6f} | {noise['cls_abs_difference']['max']:.6f} |",
        f"| Absolute transfer difference (bytes) | {noise['transfer_abs_difference_bytes']['median']:.3f} | {noise['transfer_abs_difference_bytes']['iqr']:.3f} | {noise['transfer_abs_difference_bytes']['max']:.3f} |",
        '',
        '## Fixed budget gates','',
        '| Route | Arm | Added transfer <150,000 B | No new render blocker | LCP ratio <=1.10 | TBT increase <=50 ms | CLS no worse and <0.1 | Point result | Noise-adjusted still margin |','|---|---|---|---|---|---|---|---|---|',
    ]
    for route in ROUTES:
        for arm in ['B-still','B-plain']:
            entry=budget_results[route][arm]
            point=entry['point_estimate_budgets']
            margin=entry['noise_adjusted_margin_check']
            show=lambda name:'PASS' if point[name]['pass'] else 'FAIL'
            lines.append(f"| `{route}` | {arm} | {point['added_transfer']['delta_bytes']:.3f} B, {show('added_transfer')} | {show('no_new_render_blocking')} | {point['lcp']['B_over_A']:.4f}, {show('lcp')} | {point['tbt']['B_minus_A_ms']:.3f} ms, {show('tbt')} | {point['cls']['B_median']:.6f}, {show('cls')} | {point['result']} | {margin['result']} |")
            if point['no_new_render_blocking']['new_urls']:
                lines.append(f"  New render-blocking URLs for {route} {arm}: `{', '.join(point['no_new_render_blocking']['new_urls'])}`.")
    lines += ['',f"New render-blocking URL sets are in `{OUT_JSON.relative_to(ROOT)}`. Hero-still network requests per arm are recorded there as well.",'','## Conservative decision','',decision_text,'',f"**Decision: retain `{decision}`.** {result['decision']['rationale']}",'','Owner confirmation via PageSpeed Insights remains required. No PageSpeed Insights result was supplied or inferred.','',
        '## Fixture provenance note','',
        'The prior Phase31 Task4 fixture archive was retained unchanged, but its claimed A source commit does not match its stored A HTML on protected content for these two routes. This analysis uses a fresh PHP-WASM render of the exact A commit, with content parity validated across all three arms. See `reports/phase-32c-hero-ab-fixtures.json` for the specific differing fields.','',
        '## Reproducibility','',
        f"Raw data hash: `{sha(raw_bytes)}`. Analysis script: `tools/phase32c/analyze-hero-ab.py`. Machine-readable results: `{OUT_JSON.relative_to(ROOT)}`. The run is simulated and local-only; it is not live-site verification.",
    ]
    OUT_MD.write_text('\n'.join(lines)+'\n',encoding='utf-8')
    print(json.dumps({'analysis_status':'COMPLETE','raw_sha256':sha(raw_bytes),'raw_commit':raw_commit,'routes':len(ROUTES),'samples':len(raw['samples']),'decision':decision,'point_budget_results':{route:{arm:budget_results[route][arm]['point_estimate_budgets']['result'] for arm in ['B-still','B-plain']} for route in ROUTES},'noise_adjusted_still_eligible':still_eligible,'json':str(OUT_JSON.relative_to(ROOT)),'markdown':str(OUT_MD.relative_to(ROOT))},indent=2))

if __name__=='__main__':main()
