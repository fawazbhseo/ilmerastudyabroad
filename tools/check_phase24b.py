#!/usr/bin/env python3
"""Phase 24b: exact authorized bios/portraits/denies, inherited scope guards."""
import argparse,collections,copy,hashlib,html,json,pathlib,re,subprocess
from urllib.parse import urlsplit
from check_discovery import routes,fetch,PublishedContent,validate_llm_text,blocked_name_matches,blocked_names
from check_cycle_consistency import Graphs
from team_bio_policy import ZAHEER,FAWAZ,FAWAZ_SAME_AS
from phase24b.approved import BASELINE,DENY,ROOT_DENY,old,expected_source

def norm(s):return ' '.join(html.unescape(re.sub('<[^>]+>',' ',s)).split())
def walk(v):
 if isinstance(v,dict):
  yield v
  for x in v.values():yield from walk(x)
 elif isinstance(v,list):
  for x in v:yield from walk(x)

def validate_scope(root,base):
 scope=json.loads((root/'data/service-scope.json').read_text());entity=json.loads((root/'data/entity.json').read_text())
 assert scope['reviewed_on']=='2026-10-22'
 assert list(scope['services'])==['admissions','finance','scholarships','budgets','visa','documents','aps','medicine']
 assert entity['services']==list(scope['services'].values())
 assert scope['not_offered']=='ILMERA does not provide advice on working during study or staying after study.'
 bio='Jabir KJ is the founder of ILMERA Study Abroad, focused on helping students explore affordable international education opportunities.'
 assert scope['founder_bio']==bio and scope['not_offered'] in entity['description']
 for file in ['data/seo-map.json','includes/posts.php']:
  assert (root/file).read_bytes()==subprocess.check_output(['git','show','95ab613:'+file],cwd=root),('Protected source',file)
 original=json.loads(subprocess.check_output(['git','show','95ab613:data/answer-map.json'],cwd=root));answers=json.loads((root/'data/answer-map.json').read_text())
 for route,old in original.items():
  for key in ['question','answer','basis','reviewed_on','phase20_basis']:
   assert answers[route].get(key)==old.get(key),(route,'original official/direct answer',key)
 for file in ['index.php','about.php','.htaccess']:
  current=(root/file).read_bytes();old=subprocess.check_output(['git','show','95ab613:'+file],cwd=root)
  assert current.count(b'\n')-current.count(b'\r\n')==old.count(b'\n')-old.count(b'\r\n'),('Newline pattern',file)
 seen=0;services=[]
 for route,info in routes(root).items():
  if info['status']!='published' or route=='/404':continue
  text=fetch(base,route)[2].decode();nodes=[]
  def walk(v):
   if isinstance(v,dict):
    if '@type'in v:nodes.append(v)
    for x in v.values():walk(x)
   elif isinstance(v,list):
    for x in v:walk(x)
  for raw in re.findall(r'<script type="application/ld\+json">(.*?)</script>',text,re.S):walk(json.loads(raw))
  org=[x for x in nodes if x.get('@type')=='Organization' and (x.get('@id')=='https://ilmerastudyabroad.com/#organization' or x.get('name')=='ILMERA Study Abroad')];assert len(org)==1,(route,'Organization count')
  assert org[0]['description']==entity['description'] and org[0]['knowsAbout']==entity['services'],route
  assert not any(k in org[0] for k in ['makesOffer','aggregateRating','review','price']),route
  people=[x for x in nodes if x.get('@type')=='Person' and x.get('name')=='Jabir KJ'];assert len(people)==1,(route,'Existing Person count')
  assert people[0]['description']==bio and people[0]['jobTitle']=='Founder',route
  assert not any(x.get('@type') in ['Offer','Review','AggregateRating','LocalBusiness'] for x in nodes),route
  visible=' '.join(PublishedContent(re.sub(r'<script\b.*?</script>','',text,flags=re.S),include_government_citations=True).parts)
  assert not re.search(r'no[ -]charge|at no cost|non.refundable',visible,re.I),(route,'Unprovided business pricing/refund assertion')
  assert not re.search(r'only travel the process requires|CFO Zaheer KJ verifies|Manages admissions, visa documentation|realistically admit you',visible,re.I),(route,'Legacy business/outcome promise')
  if route=='/about':
   assert visible.count(bio)==1 and 'financial consultant' not in visible
   assert not any(x.get('name')=='Zaheer KJ' and 'knowsAbout' in x for x in nodes),'Unconfirmed additional team duties'
  if route=='/services':
   assert 'What ILMERA helps with' in visible and 'What ILMERA does not do' in visible
   assert scope['not_offered'] in visible
   services=[x for x in nodes if x.get('@type')=='Service']
   assert [x['description'] for x in services]==entity['services'],'Service records must match actual approved topics, not generic page metadata'
   assert len([x for x in nodes if x.get('@type')=='Question'])>=11
  seen+=1
 for name in ['llms.txt','llms-full.txt']:
  t=(root/name).read_text();validate_llm_text(root,name,t)
  assert entity['description'] in t and scope['not_offered'] in t and scope['disclosure'] in t and scope['founder_role'] in t
  assert not re.search(r'no[ -]charge|pre-departure|post-arrival|Sets the strategic|overall strategic direction',t,re.I),name
  # Exact first-party service exemption must not exempt an appended rule or URL.
  for extra in ['\nAPS decisions take a fixed time.','\nDSU awards are promised.','\nRussia safety is assured.','\nhttps://ilmerastudyabroad.com/study-in-russia']:
   rejected=False
   try:validate_llm_text(root,name,t+extra)
   except AssertionError:rejected=True
   assert rejected,(name,'Held guard regression',extra)
 return dict(published_pages=seen,owner_services=len(services),exact_founder_bio=True,one_organization=True,official_data_protected=True,unprovided_prices_absent=True,held_llm_guards=True)

def validate(root,base,stage=5,baseline_captures=None):
 validate_scope(root,base)
 # Every website/source byte is immutable except the exact approved transforms.
 existing=subprocess.check_output(['git','ls-tree','-r','--name-only',BASELINE],cwd=root,text=True).splitlines()
 current=set(subprocess.check_output(['git','ls-files'],cwd=root,text=True).splitlines())|set(subprocess.check_output(['git','ls-files','--others','--exclude-standard'],cwd=root,text=True).splitlines())
 for file in existing:
  if file.startswith(('reports/','tools/')) or file in ['llms.txt','llms-full.txt']:continue
  if file in ['CHANGELOG.md','flagged-items-for-verification.md']:
   assert (root/file).read_bytes().startswith(old(root,file)),('Append-only',file)
  else:assert (root/file).read_bytes()==expected_source(root,file,stage),('Unapproved source/asset/contact/fact change',file)
 extras={f for f in current-set(existing) if not f.startswith(('reports/','tools/'))}
 assert extras <= ({'data/.htaccess','includes/.htaccess'} if stage>=3 else set()),('Unexpected public file',extras)
 for file in ['index.php','about.php','.htaccess']:
  data=(root/file).read_bytes();previous=old(root,file)
  assert data.count(b'\n')-data.count(b'\r\n')==previous.count(b'\n')-previous.count(b'\r\n'),('Line-ending type',file)
 assert (root/'tools/blocked-names.txt').read_bytes()==old(root,'tools/blocked-names.txt')
 team=json.loads((root/'data/team.json').read_text())['members'];assert team[1]['description']==FAWAZ and team[2]['description']==ZAHEER and team[1]['sameAs']==FAWAZ_SAME_AS
 assert team[0]==json.loads(old(root,'data/team.json'))['members'][0]
 original_members=json.loads(old(root,'data/team.json'))['members']
 public=0;original_uses=[];portrait_count=0;bios_on=[]
 assert baseline_captures,'Independent baseline render capture required'
 manifest=json.loads((baseline_captures/'snapshots.json').read_text())
 for route,info in routes(root).items():
  status,headers,body=fetch(base,route);assert status==200
  text=body.decode();before=(baseline_captures/manifest[route]['file']).read_text()
  graphs=Graphs(text).graphs;expected_graphs=Graphs(before).graphs
  # All other schema, including fees/registration/official facts, stays exact.
  for graph in expected_graphs:
   for n in walk(graph):
    if n.get('@type')=='Person' and 'description' in n:
     if n.get('name')=='Fawaz BH':n['description']=FAWAZ;n['sameAs']=FAWAZ_SAME_AS
     elif n.get('name')=='Zaheer KJ':n['description']=ZAHEER
    if n.get('@type')=='Question':
     if n.get('name')=='Who is Fawaz BH?':n['acceptedAnswer']['text']=FAWAZ
     elif n.get('name')=='Who is Zaheer KJ?':n['acceptedAnswer']['text']=ZAHEER
  assert graphs==expected_graphs,(route,'Unexpected structured-data change')
  visible=norm(re.sub(r'<(?:script|style)\b.*?</(?:script|style)>','',text,flags=re.S))
  old_visible=norm(re.sub(r'<(?:script|style)\b.*?</(?:script|style)>','',before,flags=re.S))
  if route not in ['/about','/']:assert visible==old_visible,(route,'Visible facts changed')
  for tag in re.findall(r'<(?:img|source|meta|link)\b[^>]*>',text):
   if '/assets/images/fawazbh.webp' in tag:original_uses.append(route)
  imgs=re.findall(r'<img\b[^>]*>',text);previous_imgs=re.findall(r'<img\b[^>]*>',before)
  assert len(imgs)==len(previous_imgs)
  for tag,previous in zip(imgs,previous_imgs):
   if stage>=2 and '/assets/images/fawazbh.webp' in previous:previous=previous.replace('/assets/images/fawazbh.webp','/assets/images/fawazbh-192.webp')
   assert tag==previous,(route,'Portrait attribute or other image change')
   if 'fawazbh-' in tag:portrait_count+=1
  if info['status']!='published' or route=='/404':continue
  nodes=[n for g in graphs for n in walk(g)]
  for member in team:
   people=[n for n in nodes if n.get('@type')=='Person' and n.get('name')==member['name']]
   assert len(people)==1 and people[0]==member,(route,member['name'],'Canonical Person mismatch')
  for bio in [FAWAZ,ZAHEER]:assert visible.count(bio)==(2 if route=='/about' else 1 if route=='/' else 0),(route,'Visible bio context/count')
  remaining=visible.replace(FAWAZ,'').replace(ZAHEER,'');assert 'Adrex Media School' not in remaining,(route,'Training institute outside bios')
  for n in nodes:
   for key,v in n.items():
    if isinstance(v,str) and 'Adrex Media School' in v:
     assert v in [FAWAZ,ZAHEER] and ((n.get('@type')=='Person' and key=='description') or (n.get('@type')=='Answer' and key=='text')),(route,'Institution in unintended schema')
  assert not blocked_name_matches(' '.join(PublishedContent(text).parts),blocked_names(root))
  for member in original_members[1:]:assert member['description'] not in text,(route,'Old canonical bio')
  assert not re.search(r'Fawaz BH is CMO|Ask ILMERA to identify|Ask which person is responsible for any further',text,re.I),(route,'Old bio variant')
  assert not re.search(r'co[\s\-\u2010-\u2015]?found(?:er|ed)',text,re.I)
  bios_on.append(route);public+=1
 if stage>=2:assert not original_uses,('Remaining original portrait',original_uses)
 for f in ['llms.txt','llms-full.txt']:
  t=(root/f).read_text();assert t.count(FAWAZ)==t.count(ZAHEER)==1
  assert t.replace(FAWAZ,'').replace(ZAHEER,'').count('Adrex Media School')==0
  for m in original_members[1:]:assert m['description'] not in t
 if stage>=3:
  for folder in ['reports','tools','includes','data']:assert (root/folder/'.htaccess').read_bytes()==DENY
  assert (root/'.htaccess').read_bytes()==old(root,'.htaccess')+ROOT_DENY
  from phase24b.exposure import check_local
  exposure=check_local(root,base)
 else:exposure='pending task 3'
 return dict(published_pages=public,canonical_bios_on=bios_on,visible_bio_pages=['/','/about'],about_bio_faqs=2,exact_bios=True,jabir_unchanged=True,university_blocklist_unchanged=True,original_rendered_uses=sorted(set(original_uses)),fawaz_derivative_portrait_instances=portrait_count,exposure=exposure,registration_and_other_schema_unchanged=True)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--root',type=pathlib.Path,default=pathlib.Path(__file__).resolve().parents[1]);p.add_argument('--base-url',required=True);p.add_argument('--stage',type=int,required=True);p.add_argument('--baseline-captures',type=pathlib.Path,required=True);a=p.parse_args();print('PASS',json.dumps(validate(a.root,a.base_url,a.stage,a.baseline_captures)))
