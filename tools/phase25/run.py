#!/usr/bin/env python3
"""Phase 25 full syntax/unit/render/browser/discovery/strict verification; historical business checks retained. Never deploys or submits forms."""
import argparse,collections,hashlib,html,json,os,pathlib,re,subprocess,sys,time
ROOT=pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'tools'))
from check_discovery import routes,fetch,PublishedContent,blocked_name_matches,blocked_names,prohibited_wording_matches,physical_presence_matches
from check_cycle_consistency import Graphs,allowed_schema
p=argparse.ArgumentParser();p.add_argument('--task',required=True);p.add_argument('--stage',type=int,required=True);p.add_argument('--baseline-captures',type=pathlib.Path);p.add_argument('--evidence',type=pathlib.Path,required=True);a=p.parse_args()
a.evidence.mkdir(parents=True,exist_ok=True);start=time.time();checks={};base='http://127.0.0.1:8080'
def run(label,args):
 t=time.time();r=subprocess.run(args,cwd=ROOT,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
 (a.evidence/(re.sub(r'[^a-z0-9]+','-',label.lower())+'.log')).write_text(r.stdout)
 assert r.returncode==0,(label,r.returncode,r.stdout[-4000:])
 checks[label]={'status':'PASS','seconds':round(time.time()-t,2),'output_tail':r.stdout[-1400:]}
 print('PASS',label,flush=True)
files=sorted(ROOT.rglob('*.php'))
for f in files:
 r=subprocess.run(['php','-l',str(f)],cwd=ROOT,capture_output=True,text=True)
 assert r.returncode==0 and 'No syntax errors detected' in r.stdout,(f,r.stdout,r.stderr)
checks['PHP syntax']={'status':'PASS','files':len(files),'runtime':'PHP 8.5 WASM CLI'}
print('PASS PHP syntax',len(files),flush=True)
for name in ['test_discovery.py','test_citations.py','test_italy_claims.py','test_llm_directory.py','test_llm_policy.py','test_presence.py','test_wording.py','test_team_bio_policy.py']:
 run(name,[sys.executable,'tools/'+name])
if a.stage>=4:
 run('scene ON',['php','tools/phase25/test_scenes.php','on'])
 run('scene OFF',['php','tools/phase25/test_scenes.php','off'])
if a.stage>=2:run('visual opt-in and local-font policy',['php','tools/phase25/test_visual.php'])
for name in ['check_destination_sources.php','check_place_contact.php','check_place_publication.php','test_proof.php','test_strategy_schema.php']:
 run(name,['php','tools/'+name])
if a.stage>=1:run('access policy patterns, not native engine',[sys.executable,'tools/test_public_exposure.py'])
if a.stage>=1:run('portrait encoding and original integrity',[sys.executable,'tools/phase24/build_portraits.py'])
run('authored location overlap',[sys.executable,'tools/check_location_content.py'])
for name in ['check_discovery.py','check_publication_review.py','check_italy_claims.py','check_phase19.py','check_technical_seo.py','build_llms_directory.py','check_phase20.py','check_phase25.py']:
 run(name,[sys.executable,'tools/'+name,'--base-url',base]+(['--stage',str(a.stage),'--baseline-captures',str(a.baseline_captures)] if name=='check_phase25.py' else []))
manifest={};faq_count=0
norm=lambda s:' '.join(html.unescape(re.sub('<[^>]+>','',s)).split())
for i,(path,info) in enumerate(routes(ROOT).items()):
 status,headers,body=fetch(base,path);text=body.decode();assert status==200,(path,status)
 assert not re.search(r'(?:Fatal error|Parse error|Warning):',text),path
 graphs=Graphs(text).graphs
 allnodes=[]
 def walk(value):
  if isinstance(value,dict):
   if '@type' in value:allnodes.append(value)
   for v in value.values():walk(v)
  elif isinstance(value,list):
   for v in value:walk(v)
 for g in graphs:walk(g)
 if info['status']=='published' and path!='/404':
  content=' '.join(PublishedContent(text,include_government_citations=True).parts)
  assert not prohibited_wording_matches(content),(path,'cost wording')
  assert not blocked_name_matches(' '.join(PublishedContent(text).parts),blocked_names(ROOT)),(path,'names')
  assert not physical_presence_matches(content),(path,'physical presence')
  assert '\u2014' not in text,(path,'em dash')
  for g in graphs:allowed_schema(g)
 visible=[]
 for block in re.findall(r'<details\b[^>]*class="il-faq"[^>]*>(.*?)</details>',text,re.S):
  q=re.search(r'<summary[^>]*>(.*?)</summary>',block,re.S);answer=block[q.end():]
  visible.append((norm(q[1]),norm(answer)))
 for q,answer in re.findall(r'<span class="faq-q-text">(.*?)</span>.*?<div class="faq-ans">(.*?)</div>',text,re.S):
  visible.append((norm(q),norm(answer)))
 for q,answer in re.findall(r'<button class="faq-q">(.*?)</button>.*?<div class="faq-a">(.*?)</div>',text,re.S):
  visible.append((norm(q),norm(answer)))
 schema=[(norm(e['name']),norm(e['acceptedAnswer']['text'])) for g in allnodes if g.get('@type')=='FAQPage' for e in g.get('mainEntity',[])]
 assert collections.Counter(visible)==collections.Counter(schema),(path,'FAQ mismatch',visible,schema)
 faq_count+=len(visible)
 filename=f'{i:02}.html';(a.evidence/filename).write_bytes(body);manifest[path]={'file':filename,'info':info}
(a.evidence/'snapshots.json').write_text(json.dumps(manifest,indent=2)+'\n')
checks['render schema and strict policy']={'status':'PASS','routes':len(manifest),'faq_pairs':faq_count,'faq_exact_visible_schema_parity':True}
print('PASS fresh renders/schema/wording',len(manifest),flush=True)
run('independent cycle consistency',[sys.executable,'tools/check_cycle_consistency.py','--captures',str(a.evidence)])
run('browser',['node','tools/phase25/browser.cjs',str(a.evidence),'5'])
# Full rendered main overlap, matching the established five-token coverage method.
from check_location_content import inspect
raw=subprocess.check_output(['php','-r','$o=[];foreach(glob("places/*.php") as $f){$d=include $f;$o[$d["slug"]]=$d;}echo json_encode($o);'],cwd=ROOT)
places=json.loads(raw);names=sorted([v['name'] for v in places.values()],key=len,reverse=True);pattern=re.compile('|'.join(map(re.escape,names)),re.I);tokens={}
for path,item in manifest.items():
 if item['info']['kind']!='place':continue
 text=(a.evidence/item['file']).read_text();main=re.search(r'<main\b[^>]*>(.*?)</main>',text,re.S)[1]
 # Only sitewide header/footer and contact CTA boilerplate are excluded; authored FAQs remain.
 main=re.sub(r'<p class="conversion-cta".*?</p>','',main,flags=re.S)
 main=re.sub(r'<script\b.*?</script>','',main,flags=re.S)
 tokens[path]=re.findall(r"[a-z0-9]+(?:'[a-z]+)?",pattern.sub('LOCATION',norm(main)).lower())
maximum=0;pairs=0
import itertools
for x,y in itertools.combinations(tokens,2):
 ta,tb=tokens[x],tokens[y];sa=[tuple(ta[i:i+5]) for i in range(len(ta)-4)];sb=[tuple(tb[i:i+5]) for i in range(len(tb)-4)];common=set(sa)&set(sb)
 values=[len({j for i,s in enumerate(ss) if s in common for j in range(i,i+5)})/len(tt)*100 for ss,tt in [(sa,ta),(sb,tb)]]
 assert max(values)<15,(x,y,values)
 maximum=max(maximum,*values);pairs+=1
checks['rendered location overlap']={'status':'PASS','pairs':pairs,'maximum_percent':maximum}

run('whitespace',['git','-c','core.whitespace=cr-at-eol','diff','--check'])
result={'task':a.task,'checked_on':'2026-10-23','parent':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),'seconds':round(time.time()-start,2),'environment':'PHP 8.5 WASM adapter/CLI and Chromium; external browser requests aborted','live_deployment':False,'native_apache':False,'external_raw_http':False,'contact_delivery':False,'checks':checks}
(a.evidence/'result.json').write_text(json.dumps(result,indent=2)+'\n')
report=ROOT/'reports/phase-25-checks.json';data=json.loads(report.read_text()) if report.exists() else {'baseline':'164d6de41159385e151ecefec54763eab59141a5','tasks':{}}
data['tasks'][a.task]=result;report.write_text(json.dumps(data,indent=2)+'\n');print('ALL PASS',a.task,result['seconds'],flush=True)
