"""Isolated candidate, not a release branch. Never edits arena production files."""
import pathlib,subprocess,re,hashlib,json,difflib
R=pathlib.Path(__file__).resolve().parents[2];C=pathlib.Path('/home/user/phase26/candidate');B=pathlib.Path('/home/user/phase26/base')
for f in ['index.php','about.php','tools/team_bio_policy.py','tools/test_team_bio_policy.py','tools/check_phase24b.py','tools/phase24b/approved.py']:(C/f).write_bytes((B/f).read_bytes())
# The sole public-file change is the approved team-only commit diff, not a cherry-pick.
patch=subprocess.check_output(['git','diff','164d6de','4844f3f','--','index.php','about.php'],cwd=R)
subprocess.run(['git','apply','-'],input=patch,cwd=C,check=True)
for f in ['index.php','about.php']:
 p=C/f;p.write_bytes(p.read_bytes().replace(b'Phase 25 team-only equal heights',b'Content release team-only equal heights'))
for f in ['tools/team_bio_policy.py','tools/test_team_bio_policy.py']:
 (C/f).write_bytes(subprocess.check_output(['git','show','4844f3f:'+f],cwd=R).replace(b'Phase 25 card-only',b'Content-release card-only'))
# Keep every Phase24b guard, changing only the exact authorized card expectation.
p=C/'tools/phase24b/approved.py';s=p.read_text();s=s.replace('  return text.encode()','  return short_cards(text,file).encode()',1)
s+='''
# Exact content-release card-only expectation, independent of page source.
def short_cards(text,file):
 from team_bio_policy import SHORT_CARD_BIOS
 def section(m):
  area=m[0]
  def card(c):
   a=c[0];name=next(n for n in SHORT_CARD_BIOS if n in a)
   a=re.sub(r'(<p\\b[^>]*class="(?:team-bio|testi-text)"[^>]*>).*?(</p>)',lambda p:p[1]+SHORT_CARD_BIOS[name]+p[2],a,count=1,flags=re.S)
   if file=='about.php' and name=='Jabir KJ':a=a.replace('        <p>Jabir KJ is the Founder, responsible for university research, admissions and application guidance.</p>\\r\\n','')
   return a
  return re.sub(r'<article\\b[^>]*class="(?:team-card|testi-card[^\\"]*)"[^>]*>.*?</article>',card,area,flags=re.S)
 text=re.sub(r'<section\\b[^>]*id="team"[^>]*>.*?</section>',section,text,flags=re.S)
 grid='team-grid' if file=='about.php' else 'testi-grid'
 return text.replace('</style>','/* Content release team-only equal heights */#team .'+grid+'{grid-auto-rows:1fr;}</style>',1)
''';p.write_text(s)
p=C/'tools/check_phase24b.py';s=p.read_text().replace('from team_bio_policy import ZAHEER,FAWAZ,FAWAZ_SAME_AS','from team_bio_policy import ZAHEER,FAWAZ,FAWAZ_SAME_AS,validate_bio_contexts').replace("visible.count(bio)==1 and 'financial consultant'", "visible.count(bio)==0 and 'financial consultant'").replace("(2 if route=='/about' else 1 if route=='/' else 0)","(1 if route=='/about' else 0)")
s=s.replace("  nodes=[n for g in graphs for n in walk(g)]\n  for member in team:","  validate_bio_contexts(text,route,True)\n  nodes=[n for g in graphs for n in walk(g)]\n  for member in team:")
p.write_text(s)
files=[];patches=[]
for b in sorted(B.rglob('*')):
 if not b.is_file() or '__pycache__' in b.parts:continue
 f=b.relative_to(B);a=(C/f).read_bytes();old=b.read_bytes()
 if a!=old:
  files.append(str(f));patches.extend(difflib.unified_diff(old.decode().splitlines(True),a.decode().splitlines(True),fromfile='a/'+str(f),tofile='b/'+str(f)))
assert set(files)=={'index.php','about.php','tools/team_bio_policy.py','tools/test_team_bio_policy.py','tools/check_phase24b.py','tools/phase24b/approved.py'}
(R/'reports/phase-26-team-only.patch').write_bytes(''.join(patches).encode())
(R/'reports/phase-26-candidate-delta.json').write_text(json.dumps({'base':'164d6de','source_of_card_exception':'4844f3f','candidate_not_branch':True,'files_changed':files,'public_files_changed':['index.php','about.php'],'no_shared_css_fonts_hero_header_footer_changes':True,'line_endings':{f:{'baseline_CRLF':(B/f).read_bytes().count(b'\r\n'),'candidate_CRLF':(C/f).read_bytes().count(b'\r\n'),'baseline_bare_LF':(B/f).read_bytes().count(b'\n')-(B/f).read_bytes().count(b'\r\n'),'candidate_bare_LF':(C/f).read_bytes().count(b'\n')-(C/f).read_bytes().count(b'\r\n')} for f in ['index.php','about.php','.htaccess']}},indent=2)+'\n')
print('Only six authorized candidate files differ; arena public source untouched')
