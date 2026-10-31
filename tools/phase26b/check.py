"""Stage2 exact semantic invariants. Styling is never a content waiver."""
import json,pathlib,re,sys,subprocess,hashlib
ROOT=pathlib.Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'tools'))
from check_phase25 import Words,cards_only
from phase30.duplicates import expected_delta
from phase26b.expected import upgrade,PUBLIC_FILES
from team_bio_policy import validate_bio_contexts,validate_zaheer_llm
from check_discovery import routes,fetch
from check_cycle_consistency import Graphs
font_config=json.loads(subprocess.check_output(['php','-r',"require 'includes/visual-config.php'; echo json_encode([ILMERA_VISUAL_INLINE_FONT_TEMPLATES,ILMERA_VISUAL_PLAIN_HERO_TEMPLATES]);"],cwd=ROOT));
baseline=json.loads((ROOT/'reports/phase-25-baseline-renders.json').read_text())['routes'];rows=[]
for route,info in routes(ROOT).items():
 status,headers,body=fetch('http://127.0.0.1:8080',route);assert status==200,(route,status)
 text=body.decode();old=upgrade(baseline[route]['html']);expected=expected_delta(cards_only(old,route) if route in ['/','/about'] else old,route)
 validate_bio_contexts(text,route,info['status']=='published' and route!='/404')
 a,b=Words(text),Words(expected)
 assert a.words==b.words,(route,'text/order');assert a.links==b.links,(route,'link attributes');image_timing_only=False
 if a.images!=b.images:
  # DecisionD literal reference markup adds ONLY loading=eager to the first
  # header logo on five previously unprocessed pages. Image bytes/URLs/alt/
  # dimensions/styles and every other image attribute remain strictly exact.
  import copy
  ai,bi=copy.deepcopy(a.images),copy.deepcopy(b.images)
  assert ai[0][1].get('src')=='https://ilmerastudyabroad.com/assets/images/ilmera.logo.png' and ai[0][1].get('width')=='38'
  assert bi[0][1].get('loading') is None and ai[0][1].pop('loading')=='eager'
  assert ai==bi,(route,'image content/attributes beyond header timing');image_timing_only=True
 assert Graphs(text).graphs==Graphs(old).graphs,(route,'JSON-LD')
 for pat in [r'<link[^>]*rel="canonical"[^>]*>',r'<meta[^>]*name="robots"[^>]*>']:
  assert re.findall(pat,text)==re.findall(pat,old),(route,'discovery metadata')
 assert '/assets/js/hero-still.js' not in text and '/assets/images/hero-still-' not in text,route
 template = 'directory' if route=='/all-pages' else 'error' if route=='/404' else (re.search(r'class="p25 p25-([^"]+)',text)[1] if 'class="p25 p25-' in text else None)
 if template:
  assert text.count('data:font/woff2;base64,')==(2 if template in font_config[0] else 0),(route,'font tier')
  assert text.count('rel="preload" href="/assets/fonts/')==(0 if template in font_config[0] else 2),(route,'abovefold font preloads')
  if template in font_config[1]:assert '\nbody.p25 :is(.mini-hero' in text,(route,'plain tier')
 normalized=lambda v:re.sub(r'\bactive\b','',v)
 nav=lambda s:re.search(r'<nav id="il-nav">.*?</nav>',s,re.S)[0]
 footer=lambda s:re.search(r'<footer\b.*?</footer>',s,re.S)[0]
 reference=baseline['/']['html'];chrome={'header':normalized(nav(text))==normalized(nav(reference)),'footer':footer(text)==footer(reference)}
 rows.append({'route':route,'kind':info['kind'],'status':info['status'],'shared_visual':'class="p25 p25-' in text,'exact_text_links_images_schema':True,'font_tier':'inline measured fallback' if template in font_config[0] else 'selfhost' if template else 'unchanged reference','hero_tier':'plain measured fallback' if template in font_config[1] else 'gradient' if template else 'unchanged reference','header_loading_timing_aligned':image_timing_only,'chrome':chrome,'sha256':hashlib.sha256(body).hexdigest()})
# Publication data, graph sources, original images and every original runtime file
# outside the named pure presentation integration points remain byte exact.
base='3f0e1417845291097c22e0fd02e0641752a48dd7'
allowed={'assets/css/visual-system.css','includes/visual-system.php','includes/visual-config.php','includes/site-presentation.php','includes/destination-page.php','includes/place-page.php','includes/links.php','blog/italy-dsu-scholarship-eligibility.php','blog/study-in-germany-free-aps-certificate.php','404.php'}
for f in subprocess.check_output(['git','ls-tree','-r','--name-only',base],cwd=ROOT,text=True).splitlines():
 if f.startswith(('tools/','reports/')) or f in allowed:continue
 old=subprocess.check_output(['git','show',base+':'+f],cwd=ROOT)
 if f in PUBLIC_FILES:old=upgrade(old.decode()).encode()
 if f in ['CHANGELOG.md','flagged-items-for-verification.md']:assert (ROOT/f).read_bytes().startswith(old),f
 else:assert (ROOT/f).read_bytes()==old,('protected file',f)
old_links=subprocess.check_output(['git','show',base+':includes/links.php'],cwd=ROOT);assert (ROOT/'includes/links.php').read_bytes().split(b'\n/* Phase25 held-article visual startup;')[0]==old_links
# Strict full source content guard for templates: only presentation buffer startup
# can be added, never arbitrary edits hidden by a rendered sample.
for f in ['includes/destination-page.php','includes/place-page.php','blog/italy-dsu-scholarship-eligibility.php','blog/study-in-germany-free-aps-certificate.php','404.php']:
 old=subprocess.check_output(['git','show',base+':'+f],cwd=ROOT);now=(ROOT/f).read_bytes()
 now=re.sub(rb"<\?php require_once __DIR__ \. '/(?:\.\./)?(?:includes/)?visual-system\.php'; ilmera_visual_start\((?:'error')?\); \?>\r?\n",b'',now,count=1)
 assert now==old,('template changed beyond startup',f)
# Every new visible colour must derive from actual immutable reference values.
refs='\n'.join(baseline[p]['html'] for p in ['/','/services','/about','/contact'])
hexes=lambda s:{h.lower() if len(h)!=4 else '#'+''.join(c*2 for c in h[1:].lower()) for h in re.findall(r'#[\da-fA-F]{3,8}\b',s)}
rgb=lambda s:{tuple(map(int,m)) for m in re.findall(r'rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)(?:\s*,[^)]*)?\)',s)}
palette=hexes(refs)|{'#%02x%02x%02x'%m for m in rgb(refs)};rgb_palette=rgb(refs)|{tuple(int(h[i:i+2],16) for i in (1,3,5)) for h in palette if len(h)==7}
for f in ['assets/css/visual-system.css','includes/visual-system.php']:
 text=(ROOT/f).read_text();assert hexes(text)<=palette,(f,hexes(text)-palette);assert rgb(text)<=rgb_palette,(f,rgb(text)-rgb_palette)
result={'routes':rows,'passed':True,'palette_passed':True,'reference_exclusions':['/','/services','/about','/contact'],'footer_exception':'404 baseline has an abbreviated footer. Preserving every word/link/image prevents adding the full reference footer. Kept its contents and recorded the unavoidable structural deviation.'}
(ROOT/'reports/phase-26b-invariants.json').write_text(json.dumps(result,indent=2)+'\n');print('PASS43 exact semantic/source/palette invariants; shared routes',sum(r['shared_visual'] for r in rows));print('Chrome structural differences:',[(r['route'],r['chrome']) for r in rows if not all(r['chrome'].values())])

for file in ['llms.txt','llms-full.txt']:validate_zaheer_llm((ROOT/file).read_text())
