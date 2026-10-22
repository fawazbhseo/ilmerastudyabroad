#!/usr/bin/env python3
"""Validate the real document inventory, actual rendered placements and protected data."""
import argparse,collections,html,json,pathlib,re,subprocess
from check_discovery import routes,fetch

def validate(root,base=None):
 map_path=next(root/name for name in ['reports/phase-23-map.json','reports/phase-22-map.json','reports/phase-20-map.json'] if (root/name).exists())
 d=json.loads(map_path.read_text());source=json.loads((root/'reports/strategy-doc-research.json').read_text());seo=json.loads((root/'data/seo-map.json').read_text())
 assert len(source['keywords'])==17 and len(source['prompts'])==50
 assert all(k['volume'] is None and k['difficulty'] is None for k in source['keywords'])
 published={p for p,i in routes(root).items() if i['status']=='published' and p!='/404'}
 assert {k['page'] for k in d['keywords']}==published==set(seo) and len(published)==38
 assert len({k['primary'].casefold() for k in d['keywords']})==38
 for k in d['keywords']:
  assert k['primary']==seo[k['page']]['primary'] and 2<=len(k['secondary'])<=3
  assert k['primary']==k['phase19_primary'] and not k['changed'] and k['reason'] and k['document_basis']
 assert [p['id'] for p in d['prompts']]==list(range(1,51))
 counts=collections.Counter()
 for p,s in zip(d['prompts'],source['prompts']):
  assert (p['text'],p['section'])==(s['text'],s['section'])
  assert p['page'] in published and p['heading'] and p['basis']
  assert p['status'] in ['answered','partly answered','gap']
  assert bool(p['missing_fact'])==(p['status']!='answered'),p['id']
  counts[p['status']]+=1
  if base:
   status,_,body=fetch(base,p['page']);assert status==200
   headings=[' '.join(html.unescape(re.sub('<[^>]+>','',v)).split()) for _,v in re.findall(r'<(h[1-6]|summary)\b[^>]*>(.*?)</\1>',body.decode(),re.S)]
   assert p['heading'] in headings,(p['id'],p['heading'],headings)
 text=' '.join((root/'reports/prompt-map.md').read_text().split())
 assert f"{counts['answered']} answered, {counts['partly answered']} partly answered, {counts['gap']} gap" in text
 assert '38/38' in (root/'reports/keyword-map.md').read_text()
 if base:
  for path,entry in seo.items():
   body=fetch(base,path)[2].decode()
   for tag in re.findall(r'<meta\b[^>]*>',body):
    attrs=dict(re.findall(r'([\w:-]+)="([^"]*)"',tag))
    key=attrs.get('property',attrs.get('name',''))
    if key in ['og:title','twitter:title']:assert html.unescape(attrs['content'])==entry['title'],(path,key)
    if key in ['og:description','twitter:description']:assert html.unescape(attrs['content'])==entry['description'],(path,key)
   for raw in re.findall(r'<script type="application/ld\+json">(.*?)</script>',body,re.S):
    graph=json.loads(raw)
    for node in graph.get('@graph',[graph]):
     if node.get('@type') not in ['WebPage','Article','BlogPosting','Service']:continue
     if 'description' in node:assert node['description']==entry['description'],(path,'schema description')
     if 'name' in node:assert node['name']==entry['title'],(path,'schema name')
     if 'headline' in node:assert node['headline']==entry['h1'],(path,'schema headline')
 if base:
  body=fetch(base,'/study-abroad-consultants-in-karnataka')[2].decode()
  visible=re.search(r'<h2>Related place guides</h2>\s*<ul>(.*?)</ul>',body,re.S)[1]
  links=[(u,html.unescape(re.sub('<[^>]+>','',n)).strip()) for u,n in re.findall(r'<a\b[^>]*href="([^"]+)"[^>]*>(.*?)</a>',visible,re.S)]
  graphs=[json.loads(raw) for raw in re.findall(r'<script type="application/ld\+json">(.*?)</script>',body,re.S)]
  lists=[g for g in graphs if g.get('@type')=='ItemList'];assert len(lists)==1
  graph=lists[0];assert graph['numberOfItems']==len(links) and graph['itemListOrder'].endswith('ItemListUnordered')
  for position,(item,(url,label)) in enumerate(zip(graph['itemListElement'],links),1):
   assert item['position']==position and item['item']['name']==label
   assert item['item']['url']=='https://ilmerastudyabroad.com'+url and url in published
 # Destination/place/proof/journal bytes remain protected. Only the explicit
 # Phase 22 owner-approved entity description/service fields may differ.
 protected=list((root/'destinations').glob('*.php'))+list((root/'places').glob('*.php'))+[root/p for p in ['phase14-source-review.json','phase14-location-review.json','phase14-article-review.json','phase14-publication-report.md','includes/posts.php','data/proof.php']]
 for path in protected:
  expected_bytes=subprocess.check_output(['git','show','ad09f84:'+path.relative_to(root).as_posix()],cwd=root)
  if path.relative_to(root).as_posix()=='data/proof.php' and (root/'reports/phase-24-progress.md').exists():
   from check_phase24 import proof_source
   expected_bytes=proof_source(root)
  assert path.read_bytes()==expected_bytes,('Protected data',path)
 # Narrow current-phase exception, not a blanket entity/proof exemption.
 entity_path=root/'data/entity.json'
 original=json.loads(subprocess.check_output(['git','show','ad09f84:data/entity.json'],cwd=root))
 expected=dict(original)
 if (root/'reports/phase-22-map.json').exists():
  scope=json.loads((root/'data/service-scope.json').read_text())
  assert scope['reviewed_on']=='2026-10-22' and len(scope['services'])==8
  expected['description']+=' Services include academic and English-evidence review, admissions/application guidance, financial information, study-cost comparison, scholarship and supporting-document guidance, visa-document, appointment-procedure and refusal-related guidance, Germany APS guidance and Russia medicine counselling. ILMERA does not provide advice on working during study or staying after study. Responsible bodies make their own decisions; ILMERA does not promise outcomes.'
  expected['services']=list(scope['services'].values())
 if (root/'reports/phase-23-map.json').exists():
  # Final owner A/B allow only this nonnumeric payment-description addition.
  expected['description']+=' '+"ILMERA charges the student a service charge on top of the university's own fee. ILMERA also receives payments from some partner universities."
 assert json.loads(entity_path.read_text())==expected,('Only explicitly approved entity scope fields may change',entity_path)
 protected.append(entity_path)
 return dict(published_pages=38,unique_primaries=38,changed_primaries=0,document_fragments=17,prompts=50,prompt_statuses=dict(counts),protected_files=len(protected),destination_and_location_data_unchanged=True)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--base-url');p.add_argument('--root',type=pathlib.Path,default=pathlib.Path(__file__).resolve().parents[1]);a=p.parse_args();print('PASS',json.dumps(validate(a.root,a.base_url)))
