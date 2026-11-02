#!/usr/bin/env python3
"""Analyze the already-pushed Phase32a six-route raw Lighthouse capture."""
from __future__ import annotations
import collections,hashlib,json,math,pathlib,statistics
ROOT=pathlib.Path(__file__).resolve().parents[2]
RAW=ROOT/'reports/phase-32a-6-route-ab-run-01-raw.json'
FIXTURE_MANIFEST=ROOT/'reports/phase-32a-six-route-fixtures.json'
OUT_JSON=ROOT/'reports/phase-32a-6-route-ab-run-01-summary.json'
OUT_MD=ROOT/'reports/phase-32a-6-route-ab-run-01-summary.md'
ROUTES=['/study-in-germany','/study-abroad-counselling-mysuru','/blog/how-to-choose-study-abroad-consultant-karnataka','/blog/','/services','/contact']
TARGETS=set(ROUTES[:4]);CONTROLS=set(ROUTES[4:])
BUDGETS={'added_transfer_bytes_strictly_below':150000,'LCP_B_over_A_at_most':1.10,'TBT_delta_ms_at_most':50,'CLS_B_no_greater_than_A':True,'CLS_B_strictly_below':0.1,'no_new_render_blocking_url':True}

def q(values,p):
 xs=sorted(float(v) for v in values);pos=(len(xs)-1)*p;lo=math.floor(pos);hi=math.ceil(pos)
 return xs[lo] if lo==hi else xs[lo]+(xs[hi]-xs[lo])*(pos-lo)
def stats(values):
 vals=[float(v) for v in values];q1=q(vals,.25);q3=q(vals,.75)
 return {'n':len(vals),'median':statistics.median(vals),'q1':q1,'q3':q3,'iqr':q3-q1,'min':min(vals),'max':max(vals)}
def ratio(n,d):return None if d==0 else n/d
def fmt(x,places=2):return 'n/a' if x is None else f'{x:.{places}f}'
def med_iqr(s,places=2):return f"{fmt(s['median'],places)} / {fmt(s['iqr'],places)}"
def url_summary(samples,field):
 counts=collections.Counter();bytes_by=collections.defaultdict(list);timings=collections.defaultdict(list);statuses=collections.Counter()
 for sample in samples:
  for item in sample.get(field,[]):
   url=item.get('url','');key='data:font/woff2 (embedded)' if field=='font_network' and url.startswith('data:font/woff2') else url
   counts[key]+=1
   size=item.get('transferSize')
   if isinstance(size,(int,float)):bytes_by[key].append(size)
   if item.get('startTime') is not None and item.get('endTime') is not None:timings[key].append(float(item['endTime'])-float(item['startTime']))
   statuses[str(item.get('statusCode'))]+=1
 return {'occurrences':dict(counts),'transfer_size_bytes':{k:stats(v) for k,v in bytes_by.items() if v},'duration_ms':{k:stats(v) for k,v in timings.items() if v},'status_codes':dict(statuses)}
def main():
 for p in [OUT_JSON,OUT_MD]:
  if p.exists():raise SystemExit(f'Refusing to overwrite existing analysis: {p}')
 raw_bytes=RAW.read_bytes();raw=json.loads(raw_bytes);fixture=json.loads(FIXTURE_MANIFEST.read_text())
 if raw.get('status')!='COMPLETE' or len(raw.get('samples',[]))!=84 or any(s.get('status')!='PASS' for s in raw['samples']):raise SystemExit('Raw capture is incomplete or contains a failed sample')
 if raw['environment'].get('fixture_sha256')!=fixture['fixture_json_sha256']:raise SystemExit('Raw run and frozen six-route fixture do not match')
 if hashlib.sha256(raw_bytes).hexdigest()!='73884a1e3b306dfb9ae5323c23eee22173cc466c32af396eae05ac4e89099875':raise SystemExit('Raw SHA-256 differs from the pushed checkpoint')
 by=collections.defaultdict(list)
 for s in raw['samples']:by[(s['route'],s['arm'])].append(s)
 for route in ROUTES:
  for arm in 'AB':
   rows=by[(route,arm)]
   if len(rows)!=7:raise SystemExit(f'Expected exactly seven {arm} samples for {route}')
   if len({s['round'] for s in rows})!=7:raise SystemExit(f'Duplicate or missing rounds for {route} {arm}')
 routes=[]
 metric_names=['lcp_ms','tbt_ms','cls','transfer_bytes','requests']
 for route in ROUTES:
  a,b=by[(route,'A')],by[(route,'B')]
  arms={arm:{name:stats([s[name] for s in samples]) for name in metric_names} for arm,samples in [('A',a),('B',b)]}
  paired={}
  for name in ['lcp_ms','tbt_ms','cls','transfer_bytes']:
   am={s['round']:s[name] for s in a};bm={s['round']:s[name] for s in b}
   deltas=[bm[i]-am[i] for i in range(7)];ratios=[bm[i]/am[i] for i in range(7) if am[i]!=0]
   paired[name]={'B_minus_A':stats(deltas),'B_over_A':stats(ratios) if ratios else None}
  lcp_ratio=ratio(arms['B']['lcp_ms']['median'],arms['A']['lcp_ms']['median'])
  transfer_delta=arms['B']['transfer_bytes']['median']-arms['A']['transfer_bytes']['median']
  tbt_delta=arms['B']['tbt_ms']['median']-arms['A']['tbt_ms']['median']
  cls_delta=arms['B']['cls']['median']-arms['A']['cls']['median']
  block_a=set(u for s in a for u in s.get('render_blocking',[]));block_b=set(u for s in b for u in s.get('render_blocking',[]));new_block=sorted(block_b-block_a)
  still_a=[s for s in a for _ in s.get('still_requests',[])];still_b=[s for s in b for _ in s.get('still_requests',[])]
  failures=[]
  checks={'added_transfer':transfer_delta<150000,'LCP_ratio':lcp_ratio is not None and lcp_ratio<=1.10,'TBT_delta':tbt_delta<=50,'CLS':arms['B']['cls']['median']<=arms['A']['cls']['median'] and arms['B']['cls']['median']<0.1,'no_new_render_blocking':not new_block}
  if route in TARGETS:
   if not checks['added_transfer']:failures.append(f"added transfer {transfer_delta:.0f} bytes is not below 150000")
   if not checks['LCP_ratio']:failures.append(f"median LCP B/A {lcp_ratio:.4f} exceeds 1.10" if lcp_ratio is not None else 'median LCP ratio undefined')
   if not checks['TBT_delta']:failures.append(f'median TBT delta {tbt_delta:.2f} ms exceeds 50 ms')
   if not checks['CLS']:failures.append(f"median CLS {arms['B']['cls']['median']:.6f} is worse than A {arms['A']['cls']['median']:.6f} or not below 0.1")
   if not checks['no_new_render_blocking']:failures.append('new render-blocking URL(s): '+', '.join(new_block))
  else:
   for key,value in checks.items():
    if not value:failures.append('control-only observation: '+key+' failed')
  sym=max(lcp_ratio,1/lcp_ratio) if lcp_ratio and lcp_ratio>0 else None
  routes.append({'route':route,'role':'treatment target' if route in TARGETS else 'measurement control, not byte-identical to A','arms':arms,'paired_round_metrics':paired,'ratios':{'LCP_B_over_A_medians':lcp_ratio,'LCP_paired_B_over_A':paired['lcp_ms']['B_over_A'],'symmetric_LCP_control_ratio':sym,'transfer_B_over_A_medians':ratio(arms['B']['transfer_bytes']['median'],arms['A']['transfer_bytes']['median']),'TBT_B_over_A_medians':ratio(arms['B']['tbt_ms']['median'],arms['A']['tbt_ms']['median']),'CLS_B_over_A_medians':ratio(arms['B']['cls']['median'],arms['A']['cls']['median'])},'median_deltas':{'transfer_bytes_B_minus_A':transfer_delta,'tbt_ms_B_minus_A':tbt_delta,'cls_B_minus_A':cls_delta},'checks':checks,'new_render_blocking_urls':new_block,'all_render_blocking_urls':{'A':sorted(block_a),'B':sorted(block_b)},'still_request_occurrences':{'A':len(still_a),'B':len(still_b)},'still_resource_bytes':{'A':[item.get('transferSize') for s in a for item in s.get('still_requests',[])],'B':[item.get('transferSize') for s in b for item in s.get('still_requests',[])]},'font_network':{'A':url_summary(a,'font_network'),'B':url_summary(b,'font_network')},'warning_count':sum(len(s.get('warnings',[])) for s in a+b),'budget_failures':failures,'route_budget':'PASS' if route in TARGETS and not failures else ('FAIL' if route in TARGETS else 'CONTROL ONLY')})
 controls=[x for x in routes if x['route'] in CONTROLS]
 result={'phase':'32a','task':'six_route_local_lighthouse_ab_analysis','raw_path':'reports/phase-32a-6-route-ab-run-01-raw.json','raw_sha256':hashlib.sha256(raw_bytes).hexdigest(),'raw_bytes':len(raw_bytes),'fixture_sha256':raw['environment']['fixture_sha256'],'A_source_commit':raw['environment']['A_source_commit'],'B_rendered_source_head':raw['environment']['B_rendered_source_head'],'browser':raw['environment']['chromium'],'playwright':raw['environment']['playwright'],'lighthouse':raw['environment']['lighthouse'],'run_started_at':raw['started_at'],'run_finished_at':raw['finished_at'],'local_simulation_only':True,'field_data':False,'sample_count':len(raw['samples']),'samples_per_arm_per_route':7,'total_lighthouse_warnings':sum(len(s.get('warnings',[])) for s in raw['samples']),'budgets':BUDGETS,'routes':routes,'target_pass_count':sum(x['route_budget']=='PASS' for x in routes if x['route'] in TARGETS),'target_route_count':len(TARGETS),'control_symmetric_lcp_gate':'PASS' if all(x['ratios']['symmetric_LCP_control_ratio'] is not None and x['ratios']['symmetric_LCP_control_ratio']<=1.10 for x in controls) else 'FAIL','performance_release_certified':False,'target_fallback_routes':[x['route'] for x in routes if x['route'] in TARGETS and x['route_budget']=='FAIL'],'interpretation':'Single-session local simulated mobile Lighthouse data only. B/A compares pushed B renders with frozen Task4 A and includes prior shared Phase32 presentation differences. Services and Contact are controls, not byte-identical no-op controls. Do not describe these results as field performance.','ratio_note':'Paired ratios with a zero A denominator are omitted; those cells are descriptive only and not used by the fixed budget gates. The LCP budget uses ratio of arm medians.','still_observation':'The Blog index mobile guard intentionally skips the hero still at viewport widths at or below 768px; the mobile B samples therefore made no still request on /blog/.'}
 OUT_JSON.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
 md=['# Phase32a six-route local A/B summary','','## Protocol and scope','',f"- Raw capture: [`phase-32a-6-route-ab-run-01-raw.json`](phase-32a-6-route-ab-run-01-raw.json), SHA-256 `{result['raw_sha256']}`. Raw was committed and pushed before this analysis.",f"- A: frozen Task4 source `{result['A_source_commit']}`. B rendered source: `{result['B_rendered_source_head']}`. Frozen fixture SHA-256 `{result['fixture_sha256']}`.",f"- {result['sample_count']} completed samples, seven per arm on each of six routes, alternating order, one fresh Chromium process per sample. Chromium `{result['browser']}`, Playwright `{result['playwright']}`, Lighthouse `{result['lighthouse']}`.",'- Local simulated mobile Lighthouse only, using the pinned local fixture and resource mirrors. This is not live-site or field data.',f"- Lighthouse warnings: {result['total_lighthouse_warnings']}.",'', '## Median and IQR results','', 'IQR is Q3 minus Q1, with quartiles linearly interpolated at `(n - 1) * p`. Arm cells show `median / IQR`. The paired LCP ratio uses seven within-round B/A pairs. The budget LCP ratio is B median divided by A median.',result['ratio_note'],'', '| Route | LCP A ms med/IQR | LCP B ms med/IQR | LCP B/A medians | Paired LCP B/A med/IQR | TBT A ms med/IQR | TBT B ms med/IQR | TBT delta ms | CLS A med/IQR | CLS B med/IQR | CLS delta |','|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|']
 for x in routes:
  a,b=x['arms']['A'],x['arms']['B'];pr=x['paired_round_metrics']['lcp_ms']['B_over_A'];md.append(f"| `{x['route']}` | {med_iqr(a['lcp_ms'])} | {med_iqr(b['lcp_ms'])} | {fmt(x['ratios']['LCP_B_over_A_medians'],4)} | {med_iqr(pr,4) if pr else 'n/a'} | {med_iqr(a['tbt_ms'])} | {med_iqr(b['tbt_ms'])} | {fmt(x['median_deltas']['tbt_ms_B_minus_A'])} | {med_iqr(a['cls'],6)} | {med_iqr(b['cls'],6)} | {fmt(x['median_deltas']['cls_B_minus_A'],6)} |")
 md+=['','Paired per-round changes are included because local timings are variable. Each cell below is the median / IQR of seven round-level B minus A differences.','', '| Route | LCP delta ms med/IQR | TBT delta ms med/IQR | CLS delta med/IQR | Transfer delta bytes med/IQR | Transfer paired B/A med/IQR | TBT paired B/A med/IQR | CLS paired B/A med/IQR |','|---|---:|---:|---:|---:|---:|---:|---:|']
 for x in routes:
  p=x['paired_round_metrics'];md.append(f"| `{x['route']}` | {med_iqr(p['lcp_ms']['B_minus_A'])} | {med_iqr(p['tbt_ms']['B_minus_A'])} | {med_iqr(p['cls']['B_minus_A'],6)} | {med_iqr(p['transfer_bytes']['B_minus_A'],0)} | {med_iqr(p['transfer_bytes']['B_over_A'],4) if p['transfer_bytes']['B_over_A'] else 'n/a'} | {med_iqr(p['tbt_ms']['B_over_A'],4) if p['tbt_ms']['B_over_A'] else 'n/a'} | {med_iqr(p['cls']['B_over_A'],4) if p['cls']['B_over_A'] else 'n/a'} |")
 md+=['','| Route | Transfer A bytes med/IQR | Transfer B bytes med/IQR | Added median bytes | Transfer B/A medians | Requests A med/IQR | Requests B med/IQR | Still requests A/B | New render-blocking URLs | Budget/fallback decision |','|---|---:|---:|---:|---:|---:|---:|---:|---|---|']
 for x in routes:
  a,b=x['arms']['A'],x['arms']['B'];blocking=', '.join(x['new_render_blocking_urls']) if x['new_render_blocking_urls'] else 'none';decision=x['route_budget']+('; fallback to palette required' if x['route'] in TARGETS and x['route_budget']=='FAIL' else '')
  md.append(f"| `{x['route']}` | {med_iqr(a['transfer_bytes'],0)} | {med_iqr(b['transfer_bytes'],0)} | {fmt(x['median_deltas']['transfer_bytes_B_minus_A'],0)} | {fmt(x['ratios']['transfer_B_over_A_medians'],4)} | {med_iqr(a['requests'],0)} | {med_iqr(b['requests'],0)} | {x['still_request_occurrences']['A']}/{x['still_request_occurrences']['B']} | {blocking} | {decision} |")
 md+=['','## Budget outcome','',f"- Treatment targets meeting all unchanged budgets: **{result['target_pass_count']}/{result['target_route_count']}**.",f"- Target fallback routes: {', '.join('`'+r+'`' for r in result['target_fallback_routes']) if result['target_fallback_routes'] else 'none'}.",f"- Services and Contact symmetric median-LCP control gate: **{result['control_symmetric_lcp_gate']}**. They are measurement controls with pre-existing shared Phase32 presentation differences and cannot be changed in this phase.",'- `performance_release_certified=false` remains unchanged.', '- Fixed budgets: added transfer strictly below 150,000 bytes; median LCP B/A at most 1.10; median TBT increase at most 50 ms; median CLS no worse than A and below 0.1; no new render-blocking URL. No budget was relaxed.','', '| Control route | B/A median LCP | Symmetric ratio | Control gate |', '|---|---:|---:|---|']
 for x in controls:md.append(f"| `{x['route']}` | {fmt(x['ratios']['LCP_B_over_A_medians'],4)} | {fmt(x['ratios']['symmetric_LCP_control_ratio'],4)} | {'PASS' if x['ratios']['symmetric_LCP_control_ratio'] is not None and x['ratios']['symmetric_LCP_control_ratio']<=1.10 else 'FAIL'} |")
 md.append('')
 for x in routes:
  md.append(f"### `{x['route']}`: {x['route_budget']}")
  if x['budget_failures']:md.extend('- '+reason for reason in x['budget_failures'])
  else:md.append('- No median-based budget failure.')
  md.append(f"- Median deltas: transfer {x['median_deltas']['transfer_bytes_B_minus_A']:.0f} bytes; TBT {x['median_deltas']['tbt_ms_B_minus_A']:.2f} ms; CLS {x['median_deltas']['cls_B_minus_A']:.6f}; median LCP ratio {fmt(x['ratios']['LCP_B_over_A_medians'],4)}.")
  if x['route'] in TARGETS:md.append('- Required palette fallback: '+('yes' if x['route_budget']=='FAIL' else 'no'))
 md+=['','## Interpretation limits','',result['interpretation'],result['still_observation'],'','Font request, still request, render-blocking URL and warning details are preserved in the raw JSON and the companion summary JSON. No font change has been made based on this report.']
 OUT_MD.write_text('\n'.join(md)+'\n',encoding='utf-8')
 print(json.dumps({'status':'PASS','target_pass_count':result['target_pass_count'],'target_count':result['target_route_count'],'fallback_routes':result['target_fallback_routes'],'control_gate':result['control_symmetric_lcp_gate'],'summary':str(OUT_MD),'summary_json':str(OUT_JSON),'raw_sha256':result['raw_sha256']},indent=2))
if __name__=='__main__':main()
