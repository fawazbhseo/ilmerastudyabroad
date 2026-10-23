"""Unchanged hard budgets. Additional-page baselines are labelled, never invented."""
import json,pathlib,subprocess,sys
ROOT=pathlib.Path(__file__).resolve().parents[3]
original=json.loads(subprocess.check_output(['git','show','3f0e141:reports/phase-25-before-metrics.json'],cwd=ROOT))
additional=json.loads((ROOT/'reports/phase-25-stage-2-before-extra-metrics.json').read_text())
after=json.loads((ROOT/f'reports/phase-25-stage-2-{sys.argv[1]}-metrics.json').read_text())
originals={r['route']:r for r in original['results']};extra={r['route']:r for r in additional['results']}
assert after['measurement_order'][:7]==['/','/services','/contact','/study-in-germany','/study-abroad-counselling-mysuru','/blog/how-to-choose-study-abroad-consultant-karnataka','/blog/']
assert after['storage_reset_each_navigation'] and additional['storage_reset_each_navigation']
rows=[]
for a in after['results']:
 route=a['route'];b=originals.get(route,extra[route]);x,y=b['median'],a['median'];added=set(u for s in a['samples'] for u in s['render_blocking'])-set(u for s in b['samples'] for u in s['render_blocking'])
 tests={'added_transfer_under_150000':y['transfer_bytes']-x['transfer_bytes']<150000,'no_new_render_blocking':not added,'cls_not_above_baseline_and_under_point_one':y['cls']<=x['cls'] and y['cls']<.1,'lcp_at_most_110_percent':y['lcp_ms']<=x['lcp_ms']*1.1,'tbt_at_most_baseline_plus_50':y['tbt_ms']<=x['tbt_ms']+50}
 rows.append({'route':route,'baseline_source':'immutable Stage1 measurement' if route in originals else 'new local immutable-HTML replay, not a Stage1 measurement','before':x,'after':y,'added_transfer_bytes':y['transfer_bytes']-x['transfer_bytes'],'new_render_blocking':sorted(added),'tests':tests,'passed':all(tests.values())})
report={'candidate':sys.argv[1],'passed':all(r['passed'] for r in rows),'rows':rows,'method':'Original seven-route prefix retained including three reference controls. Three storage-reset navigations per route; medians; same Lighthouse mobile simulation and offline npm mirrors. Three added pages had no Stage1 measurements: immutable pre-rollout HTML is replayed for their before samples. Main-document delivery differs and makes this supplemental comparison local-only, not field/hosting proof. Original seven budgets are never replaced by replay results.'}
(ROOT/f'reports/phase-25-stage-2-{sys.argv[1]}-performance.json').write_text(json.dumps(report,indent=2)+'\n')
for r in rows:print(r['route'],r['passed'],[k for k,v in r['tests'].items() if not v],r['before'],r['after'])
sys.exit(0 if report['passed'] else 1)
