#!/usr/bin/env python3
"""Phase 23 owner facts, exact existing bios/assets, fee-only FAQ and empty registration."""
import argparse,hashlib,html,json,pathlib,re,subprocess
from urllib.parse import urlsplit
from check_discovery import routes,fetch
BASELINE='6befa0f'
def old(root,file):return subprocess.check_output(['git','show',BASELINE+':'+file],cwd=root)
def plain(value):return ' '.join(html.unescape(re.sub('<[^>]+>',' ',value)).split())
def validate(root,base):
 payment=json.loads((root/'data/payment-disclosure.json').read_text());inventory=json.loads((root/'reports/phase-23-team-inventory.json').read_text())['team'];team=json.loads((root/'data/team.json').read_text())['members']
 assert payment['student_charge']=="ILMERA charges the student a service charge between ₹3 lakh and ₹15 lakh, depending on destination and university. This is on top of the university's own fee."
 assert payment['university_payments']=='ILMERA also receives payments from some partner universities.'
 assert payment['policy']=='ILMERA has a written service-fee and payment policy covering service inclusions and refund terms. The policy terms are not yet published on this site.'
 assert payment['no_feedback']=='ILMERA is a new consultancy and has no student feedback yet. There are no published student reviews.'
 assert payment['future_feedback']=='Future feedback will be published only with written permission and verified video.'
 assert [m['name'] for m in team]==['Jabir KJ','Fawaz BH','Zaheer KJ']
 assert [m['jobTitle'] for m in team]==['Founder','Chief Marketing Officer','Chief Financial Officer']
 asset_map={};oversized=[]
 for member,original in zip(team,inventory):
  assert member['description']==original['bio_text'],'No substitute or shortened bio'
  assert member['image']=='https://ilmerastudyabroad.com'+original['images'][0]['path']
  for url in member.get('sameAs',[]):assert url in old(root,'about.php').decode() or url in old(root,'index.php').decode(),'New profile URL'
  for asset in original['images']:
   path=root/asset['path'].lstrip('/');content=path.read_bytes();assert content==old(root,path.relative_to(root).as_posix()),('Changed portrait',path)
   assert hashlib.sha256(content).hexdigest()==asset['sha256']
   assert fetch(base,asset['path'])[2]==content,('Real photo HTTP bytes',path)
   assert not re.search(r'placeholder|avatar|default|team[-_]?[0-9]',path.name,re.I)
   asset_map[asset['path']]=member
   if len(content)>300000:oversized.append({'path':asset['path'],'bytes':len(content),'preserved_original':True})
 # Preserve ALL existing About biography variants, not merely the new canonical data.
 about=(root/'about.php').read_bytes().decode();original=old(root,'about.php').decode()
 for pattern in [r'<p class="team-bio">(.*?)</p>',r'<summary>Who is (?:Jabir KJ|Fawaz BH|Zaheer KJ)\?</summary>(.*?)</details>',r'"description": "((?:Jabir KJ|Fawaz BH|Zaheer KJ)[^\r\n]*)"']:
  assert re.findall(pattern,about,re.S)==re.findall(pattern,original,re.S),('Existing bio changed',pattern)
 home=(root/'index.php').read_bytes().decode();previous=old(root,'index.php').decode()
 def home_bios(s):return [re.findall(r'<p\b[^>]*>(.*?)</p>',x,re.S) for x in re.findall(r'<article class="testi-card[^>]*>(.*?)</article>',s,re.S)]
 assert home_bios(home)==home_bios(previous),'Existing Home bios changed'
 for file in ['data/proof.php','data/seo-map.json','includes/posts.php','.htaccess']:
  assert (root/file).read_bytes()==old(root,file),('Protected bytes',file)
 for file in ['index.php','about.php','.htaccess']:
  a=(root/file).read_bytes();b=old(root,file);assert a.count(b'\n')-a.count(b'\r\n')==b.count(b'\n')-b.count(b'\r\n'),('Line endings',file)
 expected_pages={'/services','/contact','/blog/how-to-choose-study-abroad-consultant-karnataka','/blog/cost-of-studying-abroad-for-indian-students'}
 expected_disclosure=' '.join(payment[k] for k in ['student_charge','university_payments','policy','before_paying'])
 pages=0;photo_instances=0
 for route,info in routes(root).items():
  if info['status']!='published' or route=='/404':continue
  text=fetch(base,route)[2].decode();nodes=[]
  def walk(v,faq=False):
   if isinstance(v,dict):
    faq=faq or v.get('@type')=='FAQPage'
    if '@type' in v:nodes.append(v)
    assert v.get('@type') not in ['Offer','Review','AggregateRating','LocalBusiness']
    assert not any(k in v for k in ['price','lowPrice','highPrice','priceRange','priceSpecification','aggregateRating','review'])
    for x in v.values():walk(x,faq)
   elif isinstance(v,list):
    for x in v:walk(x,faq)
   elif isinstance(v,str) and ('₹3 lakh' in v or '₹15 lakh' in v):assert faq,(route,'Range outside FAQ schema')
  for raw in re.findall(r'<script type="application/ld\+json">(.*?)</script>',text,re.S):walk(json.loads(raw))
  org=[n for n in nodes if n.get('@id')=='https://ilmerastudyabroad.com/#organization' and n.get('@type')=='Organization'];assert len(org)==1
  assert org[0]['founder']=={'@id':'https://ilmerastudyabroad.com/#jabir'} and 'identifier' not in org[0]
  for member in team:
   persons=[n for n in nodes if n.get('@type')=='Person' and n.get('name')==member['name']];assert len(persons)==1,(route,member['name'],'Duplicate/missing Person')
   for field in ['@id','name','jobTitle','worksFor','image','description']:assert persons[0][field]==member[field],(route,field)
  for tag in re.findall(r'<meta\b[^>]*>',text):assert '₹3 lakh' not in html.unescape(tag) and '₹15 lakh' not in html.unescape(tag)
  assert not re.search(r'co[\s\-\u2010-\u2015]?found(?:er|ed)',text,re.I),(route,'Joint-founder wording')
  assert not re.search(r'udyam|not supplied|will disclose|No hidden fees|No hidden charges',text,re.I),(route,'Unsupplied registration/stale claim')
  visible=plain(re.sub(r'<script\b.*?</script>','',text,flags=re.S))
  assert not re.search(r'\bILMERA(?: Study Abroad)?\s+(?:is|ranks|stands|remains)\s+(?:(?:the|India.s)\s+)?(?:best|top|leading|no\.?\s*1)\b',visible,re.I),(route,'Self-ranking claim')
  for tag in re.findall(r'<img\b[^>]*>',text):
   attrs={k:html.unescape(v) for k,v in re.findall(r'([\w:-]+)="([^"]*)"',tag)};path=urlsplit(attrs.get('src','')).path
   if path in asset_map:
    member=asset_map[path];assert attrs['alt']==member['name']+', '+member['jobTitle']+', ILMERA Study Abroad',(route,'Photo alt',attrs)
    assert int(attrs.get('width','0'))>0 and int(attrs.get('height','0'))>0 and attrs['loading']=='lazy',(route,'Photo layout/loading')
    photo_instances+=1
  sections=re.findall(r'<section[^>]*class="[^"]*payment-disclosure[^>]*>(.*?)</section>',text,re.S)
  if route in expected_pages:
   assert len(sections)==1 and expected_disclosure in plain(sections[0]),route
   questions={n['name']:n['acceptedAnswer']['text'] for n in nodes if n.get('@type')=='Question'}
   assert questions['Does ILMERA charge a fee?']==payment['student_charge']+' '+payment['policy']+' '+payment['before_paying']
   assert questions['Does ILMERA receive payments from universities?']==payment['university_payments']
  else:assert not sections,route
  if route=='/blog/how-to-choose-study-abroad-consultant-karnataka':assert payment['no_feedback'] in visible and payment['future_feedback'] in visible
  pages+=1
 for file in ['llms.txt','llms-full.txt']:
  text=(root/file).read_text();assert payment['university_payments'] in text and payment['no_feedback'] in text and payment['future_feedback'] in text
  assert not re.search(r'co[\s\-\u2010-\u2015]?found(?:er|ed)|udyam|will disclose|not supplied',text,re.I)
  for line in text.splitlines():
   if '₹3 lakh' in line or '₹15 lakh' in line:assert line.startswith('A: '),(file,'Fee range outside FAQ text')
 return dict(published_pages=pages,team_members=3,photos_and_bios_preserved=True,photo_instances=photo_instances,oversized_originals=oversized,registration_output='ABSENT; both owner values missing',fee_proof='EMPTY',fee_range_only_visible_or_faq=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--root',type=pathlib.Path,default=pathlib.Path(__file__).resolve().parents[1]);p.add_argument('--base-url',required=True);a=p.parse_args();print('PASS',json.dumps(validate(a.root,a.base_url)))
