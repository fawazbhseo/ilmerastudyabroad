#!/usr/bin/env python3
"""Byte-exact all-route/JSON-LD comparison with only the owner text substitution."""
import argparse,collections,hashlib,json,pathlib,re,subprocess,sys,urllib.request
ROOT=pathlib.Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'tools'))
from phase26b.expected import BASE,original,upgrade,PUBLIC_FILES,OLD_FULL,OLD_CARD
from team_bio_policy import ZAHEER,SHORT_CARD_BIOS,validate_bio_contexts,validate_zaheer_llm
from check_phase25 import Words
from check_cycle_consistency import Graphs
p=argparse.ArgumentParser();p.add_argument('--before',type=pathlib.Path,required=True);p.add_argument('--out',type=pathlib.Path,required=True);a=p.parse_args()
manifest=json.loads((a.before/'snapshots.json').read_text());rows=[]
for route,item in manifest.items():
 old=(a.before/item['file']).read_bytes();r=urllib.request.urlopen('http://127.0.0.1:8080'+route);now=r.read();expected=upgrade(old.decode()).encode()
 assert now==expected,(route,'Unexpected bytes outside the two exact Zaheer substitutions')
 before,after=Words(old.decode()),Words(now.decode())
 assert before.links==after.links and before.images==after.images,(route,'links/images')
 assert Words(upgrade(old.decode())).words==after.words,(route,'rendered text')
 assert Graphs(upgrade(old.decode())).graphs==Graphs(now.decode()).graphs,(route,'JSON-LD')
 validate_bio_contexts(now.decode(),route,item['info']['status']=='published' and route!='/404')
 rows.append({'route':route,'status':item['info']['status'],'http_status':r.status,'exact_bytes_after_zaheer_only_transform':True,'links_images_unchanged':True,'schema_only_zaheer_text':True,'old_bio_replacements':old.decode().count(OLD_FULL)+old.decode().count(OLD_CARD),'before_sha256':hashlib.sha256(old).hexdigest(),'after_sha256':hashlib.sha256(now).hexdigest()})
files=[]
for file in sorted(PUBLIC_FILES):
 old=original(file);now=(ROOT/file).read_bytes();assert now==upgrade(old.decode()).encode(),file
 endings=lambda b:{'CRLF':b.count(b'\r\n'),'bare_LF':b.count(b'\n')-b.count(b'\r\n')}
 assert endings(old)==endings(now),file
 files.append({'file':file,'only_two_exact_substitutions':True,'endings':endings(now)})
for file in ['llms.txt','llms-full.txt']:
 validate_zaheer_llm((ROOT/file).read_text())
 assert urllib.request.urlopen('http://127.0.0.1:8080/'+file).read()==(ROOT/file).read_bytes(),file
sitemap=urllib.request.urlopen('http://127.0.0.1:8080/sitemap.xml').read();assert len(re.findall(rb'<loc>',sitemap))==38
# Discovery source byte identity protects exact entries, not merely their count.
for file in ['sitemap.xml','sitemap.php','robots.txt','data/entity.json']:
 assert (ROOT/file).read_bytes()==original(file),file
result={'baseline_commit':BASE,'branch':'arena/48320ee5-ilmerastudyabroad','routes':rows,'published_routes':sum(r['status']=='published' and r['route']!='/404' for r in rows),'sitemap_urls':38,'public_file_deltas':files,'approved_zaheer_text':ZAHEER,'card_lengths':{n:len(b) for n,b in SHORT_CARD_BIOS.items()},'all_pass':True,'native_apache':False,'deployment':False}
a.out.write_text(json.dumps(result,indent=2)+'\n');print('PASS exact43-route previous-commit comparison, all links/images unchanged, Zaheer-only JSON-LD/text,38 sitemap URLs')
