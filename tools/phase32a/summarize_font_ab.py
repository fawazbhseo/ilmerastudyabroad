#!/usr/bin/env python3
"""Analyze the already-pushed Phase32a two-route font candidate capture."""
from __future__ import annotations
import collections,hashlib,json,math,pathlib,statistics
ROOT=pathlib.Path(__file__).resolve().parents[2]
RAW=ROOT/'reports/phase-32a-font-ab-run-01-raw.json'
FIXTURE=ROOT/'reports/phase-32a-font-ab-run-01-fixtures.json'
OUT_JSON=ROOT/'reports/phase-32a-font-ab-run-01-summary.json'
OUT_MD=ROOT/'reports/phase-32a-font-ab-run-01-summary.md'
ROUTES=['/study-abroad-counselling-mysuru','/blog/how-to-choose-study-abroad-consultant-karnataka']
METRICS=['lcp_ms','cls','tbt_ms','transfer_bytes','requests']
def quantile(vals,p):
 xs=sorted(float(v) for v in vals);i=(len(xs)-1)*p;lo=math.floor(i);hi=math.ceil(i)
 return xs[lo] if lo==hi else xs[lo]+(xs[hi]-xs[lo])*(i-lo)
def stats(vals):
 x=[float(v) for v in vals];q1=quantile(x,.25);q3=quantile(x,.75)
 return {'n':len(x),'median':statistics.median(x),'q1':q1,'q3':q3,'iqr':q3-q1,'min':min(x),'max':max(x)}
def fmt(x,d=2):return 'n/a' if x is None else f'{x:.{d}f}'
def display(s,d=2):return f"{fmt(s['median'],d)} / {fmt(s['iqr'],d)}"
def main():
 for out in [OUT_JSON,OUT_MD]:
  if out.exists():raise SystemExit(f'Refusing to overwrite existing font analysis {out}')
 raw_bytes=RAW.read_bytes();raw=json.loads(raw_bytes);fixture=json.loads(FIXTURE.read_text())
 if raw.get('status')!='COMPLETE' or len(raw.get('samples',[]))!=28 or any(s.get('status')!='PASS' for s in raw['samples']):raise SystemExit('Font A/B raw run is incomplete or contains failed samples')
 raw_sha=hashlib.sha256(raw_bytes).hexdigest()
 if raw_sha!='23c8b48d8eb06051fd98b08c3910cc66787d4f2af68fce4826582e1048bb9769':raise SystemExit('Raw font SHA-256 differs from pushed checkpoint')
 if raw['environment'].get('fixture_sha256')!=fixture['fixture_json_sha256']:raise SystemExit('Raw and candidate fixture hashes do not match')
 by=collections.defaultdict(list)
 for s in raw['samples']:by[(s['route'],s['arm'])].append(s)
 routes=[]
 for route in ROUTES:
  aa,bb=by[(route,'A')],by[(route,'B')]
  if len(aa)!=7 or len(bb)!=7:raise SystemExit(f'Expected exactly seven samples per arm: {route}')
  a={m:stats([s[m] for s in aa]) for m in METRICS};b={m:stats([s[m] for s in bb]) for m in METRICS}
  am={s['round']:s for s in aa};bm={s['round']:s for s in bb}
  lcp_delta=stats([bm[i]['lcp_ms']-am[i]['lcp_ms'] for i in range(7)])
  lcp_pair_ratio=stats([bm[i]['lcp_ms']/am[i]['lcp_ms'] for i in range(7) if am[i]['lcp_ms']])
  cls_delta=stats([bm[i]['cls']-am[i]['cls'] for i in range(7)])
  tbt_delta=stats([bm[i]['tbt_ms']-am[i]['tbt_ms'] for i in range(7)])
  transfer_delta=stats([bm[i]['transfer_bytes']-am[i]['transfer_bytes'] for i in range(7)])
  lcp_gain=b['lcp_ms']['median']<a['lcp_ms']['median'];cls_no_worse=b['cls']['median']<=a['cls']['median']
  routes.append({'route':route,'A_current_font_policy':a,'B_swap_candidate':b,'B_over_A_median_ratios':{m:(b[m]['median']/a[m]['median'] if a[m]['median'] else None) for m in METRICS},'paired_round':{'LCP_B_minus_A':lcp_delta,'LCP_B_over_A':lcp_pair_ratio,'CLS_B_minus_A':cls_delta,'TBT_B_minus_A':tbt_delta,'transfer_B_minus_A':transfer_delta},'decision_components':{'candidate_LCP_lower':lcp_gain,'candidate_CLS_median_no_worse':cls_no_worse},'font_candidate_qualifies':lcp_gain and cls_no_worse,'warnings':sum(len(s.get('warnings',[])) for s in aa+bb),'font_request_counts':{'A':[len(s.get('font_network',[])) for s in aa],'B':[len(s.get('font_network',[])) for s in bb]},'render_blocking_urls':{'A':sorted(set(u for s in aa for u in s.get('render_blocking',[]))),'B':sorted(set(u for s in bb for u in s.get('render_blocking',[])))}})
 decision=all(x['font_candidate_qualifies'] for x in routes)
 result={'phase':'32a','task':'fresh_font_candidate_ab_analysis','raw_path':'reports/phase-32a-font-ab-run-01-raw.json','raw_sha256':raw_sha,'raw_bytes':len(raw_bytes),'fixture_sha256':fixture['fixture_json_sha256'],'A_source_commit':raw['environment']['A_source_commit'],'candidate_description':raw['environment']['B_candidate'],'chromium':raw['environment']['chromium'],'playwright':raw['environment']['playwright'],'lighthouse':raw['environment']['lighthouse'],'local_simulation_only':True,'field_data':False,'sample_count':len(raw['samples']),'samples_per_arm_per_route':7,'rounds_interleaved':True,'warnings':sum(len(s.get('warnings',[])) for s in raw['samples']),'quartiles':'Linear interpolation at (n - 1) * p','routes':routes,'candidate_qualifies_both_routes':decision,'decision':'ADOPT_CANDIDATE' if decision else 'KEEP_CURRENT_FONT_POLICY','decision_rule':'Candidate median LCP must be lower on both routes and candidate median CLS no worse on either.','font_source_change':'none, unless the two-route decision passes','performance_release_certified':False}
 OUT_JSON.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
 md=['# Phase32a fresh font candidate A/B summary','','## Protocol','',f"- Raw capture was committed and pushed before analysis: [`phase-32a-font-ab-run-01-raw.json`](phase-32a-font-ab-run-01-raw.json), SHA-256 `{raw_sha}`.",f"- Frozen candidate fixture SHA-256 `{result['fixture_sha256']}`; A is current post-fallback font policy from `{result['A_source_commit']}`. B changes only seven `font-display:block` declarations to `swap` and removes the single body-visibility gate rule.",f"- {result['sample_count']} passing samples, seven per arm per route, alternating order, fresh Chromium per sample. Chromium {result['chromium']}, Playwright {result['playwright']}, Lighthouse {result['lighthouse']}.",'- Local simulated mobile Lighthouse only. Not field data.',f"- Warnings: {result['warnings']}.",'','## Results','', 'Cells show `median / IQR`, with IQR based on linear interpolation at `(n - 1) * p`. Paired LCP deltas/ratios use the seven interleaved rounds.','', '| Route | LCP A ms med/IQR | LCP B ms med/IQR | B/A ratio of medians | Paired LCP B/A med/IQR | Paired LCP delta ms med/IQR | CLS A med/IQR | CLS B med/IQR | Paired CLS delta med/IQR | TBT A ms med/IQR | TBT B ms med/IQR |','|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|']
 for x in routes:
  a=x['A_current_font_policy'];b=x['B_swap_candidate'];p=x['paired_round'];md.append(f"| `{x['route']}` | {display(a['lcp_ms'])} | {display(b['lcp_ms'])} | {fmt(x['B_over_A_median_ratios']['lcp_ms'],4)} | {display(p['LCP_B_over_A'],4)} | {display(p['LCP_B_minus_A'])} | {display(a['cls'],6)} | {display(b['cls'],6)} | {display(p['CLS_B_minus_A'],6)} | {display(a['tbt_ms'])} | {display(b['tbt_ms'])} |")
 md+=['','| Route | Transfer A bytes med/IQR | Transfer B bytes med/IQR | Transfer B/A ratio | Requests A med/IQR | Requests B med/IQR | Fonts requested A/B per sample | Candidate LCP lower | CLS median no worse | Decision |','|---|---:|---:|---:|---:|---:|---:|---|---|---|']
 for x in routes:
  a=x['A_current_font_policy'];b=x['B_swap_candidate'];md.append(f"| `{x['route']}` | {display(a['transfer_bytes'],0)} | {display(b['transfer_bytes'],0)} | {fmt(x['B_over_A_median_ratios']['transfer_bytes'],4)} | {display(a['requests'],0)} | {display(b['requests'],0)} | {x['font_request_counts']['A']}/{x['font_request_counts']['B']} | {'yes' if x['decision_components']['candidate_LCP_lower'] else 'no'} | {'yes' if x['decision_components']['candidate_CLS_median_no_worse'] else 'no'} | {'route criteria met' if x['font_candidate_qualifies'] else 'route criteria fail'} |")
 md+=['','The route-level column is diagnostic only. Adoption requires both routes to pass.','', '## Decision','',f"**{ 'Candidate qualifies on both routes' if decision else 'Keep the current font policy; candidate does not qualify on both routes' }.** The rule requires lower candidate median LCP on both Mysuru and the article, with candidate median CLS no worse on either. Mysuru candidate median LCP is lower by 0.03 ms; the article candidate median LCP is higher by 1.66 ms. LCP IQRs are 628-703 ms, so the small Mysuru difference is not a coherent gain. CLS medians are unchanged at zero on both routes. `performance_release_certified=false` remains unchanged.",'','No changes are made to font families, files, weights, preloads, `font-display` or the font gate. All values are local simulated results, not live or field performance.']
 OUT_MD.write_text('\n'.join(md)+'\n',encoding='utf-8')
 print(json.dumps({'status':'PASS','raw_sha256':raw_sha,'candidate_qualifies_both_routes':decision,'decision':result['decision'],'routes':[{ 'route':x['route'],'A_LCP_median':x['A_current_font_policy']['lcp_ms']['median'],'B_LCP_median':x['B_swap_candidate']['lcp_ms']['median'],'LCP_ratio':x['B_over_A_median_ratios']['lcp_ms'],'A_CLS_median':x['A_current_font_policy']['cls']['median'],'B_CLS_median':x['B_swap_candidate']['cls']['median'],'qualifies':x['font_candidate_qualifies']} for x in routes],'summary':str(OUT_MD),'summary_json':str(OUT_JSON)},indent=2))
if __name__=='__main__':main()
