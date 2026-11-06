"""Report the unrelaxed Stage 1 gate. --require-pass fails on ANY remaining blocker."""
import argparse,hashlib,json,pathlib,re,subprocess,sys,urllib.request
ROOT=pathlib.Path(__file__).resolve().parents[2]
BASE='164d6de41159385e151ecefec54763eab59141a5'
PILOTS=['/study-in-germany','/study-abroad-counselling-mysuru','/blog/how-to-choose-study-abroad-consultant-karnataka','/blog/']
def read(name):return json.loads((ROOT/'reports'/name).read_text())
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
before=read('phase-25-before-metrics.json');after=read('phase-25-after-metrics.json')
b={r['route']:r for r in before['results']};a={r['route']:r for r in after['results']}
matched_order=[r['route'] for r in before['results']]==[r['route'] for r in after['results']]
rows=[]
for route in PILOTS:
 old,new=b[route],a[route];x,y=old['median'],new['median']
 blocking_old=set(u for s in old['samples'] for u in s['render_blocking']);blocking_new=set(u for s in new['samples'] for u in s['render_blocking'])
 html=urllib.request.urlopen('http://127.0.0.1:8080'+route).read().decode()
 # Font subset bytes are inside existing inline CSS, not new font HTTP requests.
 assert 'data:font/woff2;base64,' in html and 'href="/assets/fonts/' not in html
 assert not re.search(r'<link\b[^>]*rel="stylesheet"',html)
 checks={'added_transfer_under_150000_bytes':y['transfer_bytes']-x['transfer_bytes']<150000,'no_new_render_blocking_resource':not (blocking_new-blocking_old),'cls_no_worse_and_under_0_1':y['cls']<=x['cls'] and y['cls']<.1,'lcp_within_110_percent':y['lcp_ms']<=1.1*x['lcp_ms'],'tbt_within_baseline_plus_50_ms':y['tbt_ms']<=x['tbt_ms']+50,'lcp_is_text_or_container':all(re.match(r'<(?:h[1-6]|p|div|section|span)\b',s['lcp_element'] or '') for s in new['samples'])}
 rows.append({'route':route,'before':x,'after':y,'added_transfer_bytes':y['transfer_bytes']-x['transfer_bytes'],'lcp_limit_ms':1.1*x['lcp_ms'],'tbt_limit_ms':x['tbt_ms']+50,'new_render_blocking':sorted(blocking_new-blocking_old),'lcp_elements':[s['lcp_element'] for s in new['samples']],'checks':checks,'passed':all(checks.values())})
refs=['index.php','services.php','about.php','contact.php','includes/header.php','includes/footer.php']
def historical(f):return subprocess.check_output(['git','show',BASE+':'+f],cwd=ROOT,text=True)
def expand(h):return '#'+''.join(c*2 for c in h[1:]) if len(h)==4 else h
hexes=lambda s:{expand(h.lower()) for h in re.findall(r'#[\da-fA-F]{3,8}\b',s)}
def rgba_bases(text):
 return {tuple(int(float(n.strip())) for n in v.split(',')[:3]) for v in re.findall(r'rgba?\(([^)]*)\)',text) if len(v.split(',')) in [3,4]}
reference_text='\n'.join(historical(f) for f in refs)
palette=hexes(reference_text)|{'#%02x%02x%02x'%rgb for rgb in rgba_bases(reference_text)};rgb_palette=rgba_bases(reference_text)|{tuple(int(h[i:i+2],16) for i in (1,3,5)) for h in palette if len(h)==7};shared=['assets/css/visual-system.css','includes/visual-system.php']
colour_rows=[{'file':f,'outside_reference_palette':sorted(hexes((ROOT/f).read_text())-palette),'outside_reference_rgb_bases':sorted(rgba_bases((ROOT/f).read_text())-rgb_palette)} for f in shared]
# Every pre-existing PHP template/include is checked for newly introduced colours;
# unchanged legacy declarations are not misrepresented as a new design palette.
for f in subprocess.check_output(['git','ls-tree','-r','--name-only',BASE],cwd=ROOT,text=True).splitlines():
 if f.endswith('.php') and (ROOT/f).exists():
  added=hexes((ROOT/f).read_text())-hexes(historical(f));bad=added-palette
  colour_rows.append({'file':f,'new_colours':sorted(added),'outside_reference_palette':sorted(bad),'outside_reference_rgb_bases':sorted((rgba_bases((ROOT/f).read_text())-rgba_bases(historical(f)))-rgb_palette)})
colours_ok=all(not r['outside_reference_palette'] and not r['outside_reference_rgb_bases'] for r in colour_rows)
pixels=read('phase-25-reference-pixels.json');pixels_ok=all(r['changed_pixels_outside_team']==0 for r in pixels['comparisons'])
checks=read('phase-25-checks.json')['tasks'].get('task6');technical_ok=bool(checks) and all(c['status']=='PASS' for c in checks['checks'].values())
performance_ok=matched_order and all(r['passed'] for r in rows)
runtime=['includes/visual-config.php','includes/visual-system.php','includes/site-presentation.php','assets/css/visual-system.css','assets/fonts/outfit-latin.woff2','assets/fonts/cormorant-garamond-latin.woff2','assets/js/hero-still.js']
result={'stage':1,'rollout_authorized':False,'stage_2_started':False,'baseline_unchanged_sha256':sha(ROOT/'reports/phase-25-before-metrics.json'),'after_metrics_sha256':sha(ROOT/'reports/phase-25-after-metrics.json'),'matched_measurement_order':matched_order,'measurement_order':after.get('measurement_order'),'measurement_note':'Three storage-reset navigations per route, same ordered reference prefix as baseline; browser process reused, not a cold process for each sample. Local simulated medians, not field or native-hosting evidence. Unchanged reference controls show substantial run-to-run variation. All earlier candidate failures retained. No threshold widened.','limits':{'added_transfer_bytes_strictly_under':150000,'cls_strictly_under':.1,'cls_no_worse_than_baseline':True,'lcp_multiplier':1.1,'tbt_added_ms':50},'pilots':rows,'performance_passed':performance_ok,'colour_allowlist':{'passed':colours_ok,'palette':sorted(palette),'files':colour_rows},'technical_suite_passed':technical_ok,'strict_reference_pixels_passed':pixels_ok,'strict_reference_pixel_comparisons':pixels['comparisons'],'runtime_sha256':{f:sha(ROOT/f) for f in runtime},'gate_passed':performance_ok and colours_ok and technical_ok and pixels_ok,'status':'BLOCKED' if not (performance_ok and colours_ok and technical_ok and pixels_ok) else 'AWAITING OWNER APPROVAL','release_sentence':'Pilot complete. Waiting for owner approval before rollout.'}
(ROOT/'reports/phase-25-pilot-gate.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['status','performance_passed','technical_suite_passed','strict_reference_pixels_passed','gate_passed','rollout_authorized']},indent=2))
if '--require-pass' in sys.argv and not result['gate_passed']:sys.exit(1)
