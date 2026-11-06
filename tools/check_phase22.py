#!/usr/bin/env python3
"""Independently verify owner scope, exact founder biography and immutable facts."""
import argparse,collections,html,json,pathlib,re,subprocess
from check_discovery import routes,fetch,PublishedContent,validate_llm_text

def validate(root,base):
 scope=json.loads((root/'data/service-scope.json').read_text());entity=json.loads((root/'data/entity.json').read_text())
 assert scope['reviewed_on']=='2026-10-22'
 assert list(scope['services'])==['admissions','finance','scholarships','budgets','visa','documents','aps','medicine']
 assert entity['services']==list(scope['services'].values())
 assert scope['not_offered']=='ILMERA does not provide advice on working during study or staying after study.'
 bio='Jabir KJ is the founder of ILMERA Study Abroad, focused on helping students explore affordable international education opportunities.'
 assert scope['founder_bio']==bio and scope['not_offered'] in entity['description']
 for file in ['data/seo-map.json','.htaccess','includes/posts.php','data/proof.php']:
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
  assert not any(k in org[0] for k in ['makesOffer','aggregateRating','review','identifier','price']),route
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
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--root',type=pathlib.Path,default=pathlib.Path(__file__).resolve().parents[1]);p.add_argument('--base-url',required=True);a=p.parse_args();print('PASS',json.dumps(validate(a.root,a.base_url)))
