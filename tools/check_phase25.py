#!/usr/bin/env python3
"""Phase 25 semantic invariants against the independently captured Phase 24b site.

Historical Phase24b exact-transform checker remains unchanged for its historical
scope. This phase compares all rendered words, links, schema and immutable blobs.
"""
import argparse,hashlib,json,pathlib,re,subprocess,sys
from html.parser import HTMLParser
from check_discovery import routes,fetch
from check_cycle_consistency import Graphs
from check_phase24b import validate_scope
from phase24b.exposure import check_local
BASE='164d6de41159385e151ecefec54763eab59141a5'
PILOTS={'/study-in-germany','/study-abroad-counselling-mysuru','/blog/how-to-choose-study-abroad-consultant-karnataka','/blog/'}
class Words(HTMLParser):
 def __init__(self,s):
  super().__init__(convert_charrefs=True);self.depth=0;self.words=[];self.links=[];self.images=[];self.feed(s)
 def handle_starttag(self,tag,attrs):
  d=dict(attrs)
  if tag in ['script','style']:self.depth+=1
  if tag=='a':self.links.append(d)
  if tag in ['img','source']:self.images.append((tag,d))
 def handle_endtag(self,tag):
  if tag in ['script','style']:self.depth-=1
 def handle_data(self,s):
  if not self.depth:self.words.extend(s.split())
def cards_only(text,route):
 from team_bio_policy import SHORT_CARD_BIOS
 assert route in ['/','/about']
 pattern=r'(<p\b[^>]*class="'+('testi-text' if route=='/' else 'team-bio')+r'"[^>]*>)(.*?)(</p>)'
 def replace(m):
  for name,bio in SHORT_CARD_BIOS.items():
   if m[2].startswith(name+' '):return m[1]+bio+m[3]
  return m[0]
 text=re.sub(pattern,replace,text,flags=re.S)
 if route=='/about':
  text=re.sub(r'^        <p>Jabir KJ is the Founder, responsible for university research, admissions and application guidance\.</p>\r?\n','',text,count=1,flags=re.M)
 return text
def validate(root,base,stage,baseline):
 scope=validate_scope(root,base,short_cards=stage>=3);manifest=json.loads((baseline/'snapshots.json').read_text());changed=[]
 source_exceptions={'includes/site-presentation.php'} if stage>=2 else set()
 if stage>=3:source_exceptions|={'index.php','about.php'}
 for f in subprocess.check_output(['git','ls-tree','-r','--name-only',BASE],cwd=root,text=True).splitlines():
  if f.startswith(('reports/','tools/')):continue
  old=subprocess.check_output(['git','show',BASE+':'+f],cwd=root);now=(root/f).read_bytes()
  if f in ['CHANGELOG.md','flagged-items-for-verification.md']:assert now.startswith(old),('Append-only',f)
  elif f in ['index.php','about.php'] and stage>=3:
   # Only exact card paragraphs and team-area equal-height CSS may change.
   expected=cards_only(old.decode(), '/' if f=='index.php' else '/about').encode()
   now=re.sub(rb'/\* Phase 25 team-only equal heights \*/#team \.(?:testi|team)-grid\{grid-auto-rows:1fr;\}',b'',now)
   assert now==expected,('Reference source outside card exception',f)
  elif f not in source_exceptions:assert now==old,('Protected source/facts/status/assets',f)
 if stage>=2:
  data=(root/'includes/site-presentation.php').read_bytes();old=subprocess.check_output(['git','show',BASE+':includes/site-presentation.php'],cwd=root)
  data=data.replace(b"require_once __DIR__ . '/visual-system.php';\n",b'',1).replace(b"    $html = ilmera_visual_present($html);\n",b'',1)
  assert data==old,'Presentation logic other than isolated visual hook changed'
 for route,info in routes(root).items():
  status,headers,body=fetch(base,route);assert status==200
  text=body.decode();before=(baseline/manifest[route]['file']).read_text();expected=cards_only(before,route) if stage>=3 and route in ['/','/about'] else before
  a,b=Words(text),Words(expected)
  assert a.words==b.words,(route,'Rendered text/order changed')
  assert a.links==b.links,(route,'Links or attributes changed')
  assert a.images==b.images,(route,'Photos/alt/crop/source changes')
  assert Graphs(text).graphs==Graphs(before).graphs,(route,'JSON-LD changed')
  for pattern in [r'<link[^>]*rel="canonical"[^>]*>',r'<meta[^>]*name="robots"[^>]*>']:
   assert re.findall(pattern,text)==re.findall(pattern,before),(route,'Discovery metadata changed')
  if text!=before:changed.append(route)
  if stage<5 and route not in ['/','/about']:assert body==(baseline/manifest[route]['file']).read_bytes(),(route,'Premature rollout')
  if route not in PILOTS|{'/','/about'}:assert body==(baseline/manifest[route]['file']).read_bytes(),(route,'Non-pilot changed')
  if stage>=3:
   from team_bio_policy import validate_bio_contexts
   validate_bio_contexts(text,route,info['status']=='published' and route!='/404')
 assert set(changed)<=PILOTS|{'/','/about'},changed
 if stage>=5:assert set(changed)==PILOTS|{'/','/about'},changed
 existing=set(subprocess.check_output(['git','ls-tree','-r','--name-only',BASE],cwd=root,text=True).splitlines())
 current=set(subprocess.check_output(['git','ls-files'],cwd=root,text=True).splitlines())|set(subprocess.check_output(['git','ls-files','--others','--exclude-standard'],cwd=root,text=True).splitlines())
 allowed={'includes/visual-system.php','includes/visual-config.php','assets/css/visual-system.css','assets/fonts/outfit-latin.woff2','assets/fonts/cormorant-garamond-latin.woff2','assets/fonts/outfit-OFL.txt','assets/fonts/cormorant-garamond-OFL.txt'} if stage>=2 else set()
 if stage>=4:allowed|={'assets/js/hero-still.js','assets/images/hero-still-720.webp','assets/images/hero-still-1440.webp'}
 extras={f for f in current-existing if not f.startswith(('reports/','tools/'))}
 assert extras<=allowed,('Unexpected public source/asset',extras-allowed)
 for f in ['llms.txt','llms-full.txt','data/team.json','phase14-article-review.json','.htaccess']:
  assert (root/f).read_bytes()==subprocess.check_output(['git','show',BASE+':'+f],cwd=root),f
 if stage>=2:
  palette=set()
  for filename in ['index.php','services.php','about.php','contact.php','includes/header.php','includes/footer.php']:
   palette|={h.lower() for h in re.findall(r'#[\da-fA-F]{3,8}\b',subprocess.check_output(['git','show',BASE+':'+filename],cwd=root,text=True))}
  def expand(h):return '#'+''.join(c*2 for c in h[1:]) if len(h)==4 else h
  palette={expand(h) for h in palette}
  css=(root/'assets/css/visual-system.css').read_text()
  assert {expand(h.lower()) for h in re.findall(r'#[\da-fA-F]{3,8}\b',css)}<=palette,'New colour outside reference palette'
  assert set(re.findall(r'border-radius:([^;}]+)',css))<={'3px','12px','0','inherit'},'More than two new component radii'
  assert set(re.findall(r"font-family:([^;}]+)",css))<={"'Outfit',sans-serif","'Cormorant Garamond',serif","'Outfit'","'Cormorant Garamond'"}
 return {'scope':scope,'routes':43,'changed_routes':changed,'exact_words_links_schema_images':True,'protected_sources':True,'local_exposure':check_local(root,base)}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--base-url',required=True);p.add_argument('--stage',type=int,required=True);p.add_argument('--baseline-captures',type=pathlib.Path,required=True);a=p.parse_args();print('PASS',json.dumps(validate(pathlib.Path(__file__).resolve().parents[1],a.base_url,a.stage,a.baseline_captures)))
