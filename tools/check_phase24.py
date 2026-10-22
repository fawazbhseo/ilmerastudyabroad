#!/usr/bin/env python3
"""Phase 24 exact owner exceptions with inherited Phase 22/23 protections."""
import argparse,hashlib,html,json,pathlib,re,subprocess
from urllib.parse import urlsplit
from check_discovery import routes,fetch,PublishedContent,validate_llm_text
BASELINE='9157825'
def old(root,file):return subprocess.check_output(['git','show',BASELINE+':'+file],cwd=root)
def plain(value):return ' '.join(html.unescape(re.sub('<[^>]+>',' ',value)).split())

NUMBER='UDYAM-KR-18-0023330'
STATEMENT='ILMERA Study Abroad is registered under Udyam (MSME), registration number '+NUMBER+'.'
CAVEAT="Udyam registration is a business registration. It does not mean any authority has approved or endorsed ILMERA's services."
IDENTIFIER={'@type':'PropertyValue','propertyID':'Udyam','value':NUMBER}
ZAHEER="Zaheer KJ is the Chief Financial Officer of ILMERA Study Abroad, responsible for the company's finance function."
OLD_ZAHEER='Zaheer KJ is CFO at ILMERA Study Abroad. Ask ILMERA to identify the person responsible for any additional tasks in your written service scope.'
HOME_PLACEHOLDER='CFO at ILMERA Study Abroad. Ask which person is responsible for any further agreed tasks.'
def proof_source(root):
 original=old(root,'data/proof.php')
 return original.replace(b'All slots intentionally empty; see reports/proof-slots.md.',b'Only the exact approved registration record is populated.').replace(b"'registration_details' => [],",b"""'registration_details' => [[
        'label' => 'Udyam registration',
        'value' => 'UDYAM-KR-18-0023330',
        'approved' => true,
        'source' => 'Owner-supplied Udyam certificate',
        'reviewed_on' => '2026-10-22',
    ]],""")

def validate_scope(root,base):
 scope=json.loads((root/'data/service-scope.json').read_text());entity=json.loads((root/'data/entity.json').read_text())
 assert scope['reviewed_on']=='2026-10-22'
 assert list(scope['services'])==['admissions','finance','scholarships','budgets','visa','documents','aps','medicine']
 assert entity['services']==list(scope['services'].values())
 assert scope['not_offered']=='ILMERA does not provide advice on working during study or staying after study.'
 bio='Jabir KJ is the founder of ILMERA Study Abroad, focused on helping students explore affordable international education opportunities.'
 assert scope['founder_bio']==bio and scope['not_offered'] in entity['description']
 for file in ['data/seo-map.json','.htaccess','includes/posts.php']:
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

def validate(root,base,stage=6):
 validate_scope(root,base)
 if stage>=5:
  for file in ['CHANGELOG.md','flagged-items-for-verification.md']:
   assert (root/file).read_bytes().startswith(old(root,file)),('Append-only history',file)
  allowed={'about.php','index.php','data/proof.php','data/team.json','includes/proof.php','includes/site-presentation.php','assets/images/fawazbh-192.webp','assets/images/fawazbh-384.webp','llms.txt','llms-full.txt','CHANGELOG.md','flagged-items-for-verification.md'}
  existing=subprocess.check_output(['git','ls-tree','-r','--name-only',BASELINE],cwd=root,text=True).splitlines()
  current=set(subprocess.check_output(['git','ls-files'],cwd=root,text=True).splitlines())|set(subprocess.check_output(['git','ls-files','--others','--exclude-standard'],cwd=root,text=True).splitlines())
  def website_file(file):return not file.startswith(('reports/','tools/'))
  for file in existing:
   if website_file(file) and file not in allowed:assert (root/file).read_bytes()==old(root,file),('Unapproved website/source/contact change',file)
  assert {f for f in current-set(existing) if website_file(f)}<=allowed,'Unapproved public file, including certificate copies'
 if stage>=4:
  for folder in ['reports','tools']:
   assert (root/folder/'.htaccess').read_bytes()==b'# Internal owner evidence and verification artifacts, not website content.\r\nRequire all denied\r\n'
  for path in ['/reports/owner-inputs-needed.md','/reports/phase-23-team-inventory.json','/tools/check_phase24.py']:
   assert fetch(base,path)[0]==403,(path,'Internal artifact access')
  owner=' '.join((root/'reports/owner-inputs-needed.md').read_text().split())
  assert 'Both owner values remain missing' not in owner and '## 4. Udyam' not in owner
  for phrase in ['accommodation in student residences','ask a CA','Udyam portal','Optional Zaheer background','Ahrefs Academy and Semrush','Adrex Media School','accurate and','Payment schedule','Refund and cancellation','Future genuine feedback']:
   assert phrase in owner,('Required owner follow-up',phrase)
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
  expected_bio=ZAHEER if member['name']=='Zaheer KJ' and stage>=2 else original['bio_text']
  assert member['description']==expected_bio,'Only the approved Zaheer bio may differ'
  image_path='/assets/images/fawazbh-384.webp' if member['name']=='Fawaz BH' and stage>=3 else original['images'][0]['path']
  assert member['image']=='https://ilmerastudyabroad.com'+image_path
  for url in member.get('sameAs',[]):assert url in old(root,'about.php').decode() or url in old(root,'index.php').decode(),'New profile URL'
  for asset in original['images']:
   path=root/asset['path'].lstrip('/');content=path.read_bytes();assert content==old(root,path.relative_to(root).as_posix()),('Changed portrait',path)
   assert hashlib.sha256(content).hexdigest()==asset['sha256']
   assert fetch(base,asset['path'])[2]==content,('Real photo HTTP bytes',path)
   assert not re.search(r'placeholder|avatar|default|team[-_]?[0-9]',path.name,re.I)
   asset_map[asset['path']]=member
   if len(content)>300000:oversized.append({'path':asset['path'],'bytes':len(content),'preserved_original':True})
 # Source equivalence is stricter than only comparing selected bio fragments.
 for file in ['about.php','index.php']:
  expected=old(root,file)
  if stage>=2:
   expected=expected.replace(OLD_ZAHEER.encode(),ZAHEER.encode()).replace(HOME_PLACEHOLDER.encode(),ZAHEER.encode())
  if stage>=3:
   expected=expected.replace(b'/assets/images/fawazbh.webp',b'/assets/images/fawazbh-384.webp')
   size='88' if file=='about.php' else '96'
   expected=expected.replace(b'<img src="/assets/images/fawazbh-384.webp"', ('<img src="/assets/images/fawazbh-384.webp" srcset="/assets/images/fawazbh-192.webp 192w, /assets/images/fawazbh-384.webp 384w" sizes="'+size+'px"').encode())
  assert (root/file).read_bytes()==expected,('Unapproved source/bio/alt/layout change',file)
 for file in ['data/seo-map.json','includes/posts.php','.htaccess','data/entity.json','data/service-scope.json','data/payment-disclosure.json']:
  assert (root/file).read_bytes()==old(root,file),('Protected bytes',file)
 assert (root/'data/proof.php').read_bytes()==proof_source(root)
 for file in ['index.php','about.php','.htaccess']:
  a=(root/file).read_bytes();b=old(root,file);assert a.count(b'\n')-a.count(b'\r\n')==b.count(b'\n')-b.count(b'\r\n'),('Line endings',file)
 previous_team=json.loads(old(root,'data/team.json'))
 expected_team=json.loads(json.dumps(previous_team))
 if stage>=2:expected_team['members'][2]['description']=ZAHEER
 if stage>=3:expected_team['members'][1]['image']='https://ilmerastudyabroad.com/assets/images/fawazbh-384.webp'
 assert json.loads((root/'data/team.json').read_text())==expected_team
 presentation=old(root,'includes/site-presentation.php')
 if stage>=3:
  presentation=presentation.replace(b"if ($imagePath !== parse_url($member['image'], PHP_URL_PATH)) continue;",b"if ($imagePath !== parse_url($member['image'], PHP_URL_PATH) && !($member['name'] === 'Fawaz BH' && $imagePath === '/assets/images/fawazbh.webp')) continue;")
 assert (root/'includes/site-presentation.php').read_bytes()==presentation,'Only the original-portrait alt alias is authorized'
 if stage>=3:
  assert subprocess.run(['python3','tools/phase24/build_portraits.py'],cwd=root,capture_output=True).returncode==0,'Derivative reproduction'
  from PIL import Image
  for width in [192,384]:
   path=root/f'assets/images/fawazbh-{width}.webp';data=path.read_bytes()
   assert len(data)<60000 and data[:4]==b'RIFF' and data[8:12]==b'WEBP'
   with Image.open(path) as im:assert im.format=='WEBP' and im.size==(width,width)
   status,headers,body=fetch(base,'/'+path.relative_to(root).as_posix())
   assert status==200 and body==data and {k.lower():v for k,v in headers.items()}['content-type'].split(';')[0]=='image/webp'
  asset_map['/assets/images/fawazbh-384.webp']=team[1]
  asset_map['/assets/images/fawazbh-192.webp']=team[1]
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
  assert org[0]['founder']=={'@id':'https://ilmerastudyabroad.com/#jabir'} and org[0].get('identifier')==[IDENTIFIER]
  for member in team:
   persons=[n for n in nodes if n.get('@type')=='Person' and n.get('name')==member['name']];assert len(persons)==1,(route,member['name'],'Duplicate/missing Person')
   for field in ['@id','name','jobTitle','worksFor','image','description']:assert persons[0][field]==member[field],(route,field)
  for tag in re.findall(r'<meta\b[^>]*>',text):assert '₹3 lakh' not in html.unescape(tag) and '₹15 lakh' not in html.unescape(tag)
  assert not re.search(r'co[\s\-\u2010-\u2015]?found(?:er|ed)',text,re.I),(route,'Joint-founder wording')
  assert not re.search(r'not supplied|will disclose|No hidden fees|No hidden charges',text,re.I),(route,'Unsupplied registration/stale claim')
  visible=plain(re.sub(r'<script\b.*?</script>','',text,flags=re.S))
  expected_count=1 if route in ['/about','/contact'] else 0
  assert visible.count(STATEMENT)==expected_count and visible.count(CAVEAT)==expected_count,(route,'Visible registration scope')
  assert text.count(NUMBER)==1+expected_count,(route,'Number outside Organization/visible block')
  assert 'Owner-supplied Udyam certificate' not in text and 'reviewed_on' not in text
  if stage>=2:
   assert OLD_ZAHEER not in text and HOME_PLACEHOLDER not in text,(route,'Old Zaheer bio')
   if route in ['/','/about']:assert ZAHEER in visible,(route,'Visible Zaheer bio')
  # New certificate data is allowlisted, not inferred from existing contact data.
  registration_blocks=re.findall(r'<section class="owner-proof".*?</section>',text,re.S)
  for block in registration_blocks:
   assert plain(block)=='Published service information '+STATEMENT+' '+CAVEAT

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
  assert not re.search(r'co[\s\-\u2010-\u2015]?found(?:er|ed)|will disclose|not supplied',text,re.I)
  assert text.count(STATEMENT)==1 and text.count(CAVEAT)==1 and text.count(NUMBER)==1
  assert 'Owner-supplied Udyam certificate' not in text
  if stage>=2:assert OLD_ZAHEER not in text and HOME_PLACEHOLDER not in text and ZAHEER in text
  for line in text.splitlines():
   if '₹3 lakh' in line or '₹15 lakh' in line:assert line.startswith('A: '),(file,'Fee range outside FAQ text')
 return dict(published_pages=pages,team_members=3,original_photos_preserved=True,jabir_fawaz_bios_preserved=True,approved_zaheer_consistent=True,photo_instances=photo_instances,oversized_originals=oversized,registration_output='EXACT APPROVED PUBLIC PROJECTION',fee_proof='EMPTY',fee_range_only_visible_or_faq=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--root',type=pathlib.Path,default=pathlib.Path(__file__).resolve().parents[1]);p.add_argument('--base-url',required=True);p.add_argument('--stage',type=int,default=6);a=p.parse_args();print('PASS',json.dumps(validate(a.root,a.base_url,a.stage)))
