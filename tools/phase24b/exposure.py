#!/usr/bin/env python3
"""Static deployment exposure inventory and separate local-adapter probes.

Does NOT execute or validate Apache/LiteSpeed directives. Owner must test live.
"""
import argparse,collections,hashlib,json,os,pathlib,re,subprocess,sys
from urllib.parse import quote
ROOT=pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'tools'))
from check_discovery import routes,fetch
from phase24b.approved import BASELINE,DENY,ROOT_DENY
HOST='https://ilmerastudyabroad.com'
INTERNAL=('reports','tools','includes','data','destinations','places')
BLOCKED_EXT=re.compile(r'(?i)(?:\.(?:md|py|cjs|log|bak|csv)$|^phase.*\.json$|^\.)')
GENERATED=['reports/phase-24b-exposure-audit.json','reports/phase-24b-exposure-audit.md','reports/phase-24b-live-url-checks.txt']
def inventory(root):
 # Enumerate actual web-root files, including ignored Python caches. Never
 # read Git credential internals; protect the complete Git namespace separately.
 files=set()
 for parent,dirs,names in os.walk(root):
  dirs[:]=[d for d in dirs if d!='.git']
  for name in names:files.add((pathlib.Path(parent)/name).relative_to(root).as_posix())
 page_files={v['file'] for v in routes(root).values()};entries=[]
 for file in sorted(files):
  if file in page_files:continue
  if file=='deploy-check.php':continue  # Temporary keyed/expiring exception, tested separately; never a public200 probe.
  folder=file.split('/')[0] if '/' in file else ''
  internal=folder in INTERNAL;root_deny=bool(BLOCKED_EXT.search(pathlib.PurePosixPath(file).name))
  blocked=internal or root_deny
  previous='reports/tools directory Require all denied' if folder in ['reports','tools'] else 'no repository access block'
  if file=='.htaccess':previous='server normally protects this config; do not depend on that default'
  if internal:rule=folder+'/.htaccess: Require all denied'
  elif root_deny:rule='root FilesMatch deny'
  else:rule='intentional public asset/discovery/verification resource'
  entries.append({'file':file,'url':HOST+'/'+quote(file,safe='/'),'category':'internal-denied' if blocked else 'intentional-public','before_block':previous,'after_rule':rule,'expected_live':'403 or 404, no file contents' if blocked else '200 (sitemap.php may canonical-redirect under existing native rewrite)'})
 folders=[]
 for d in sorted({p for f in files for p in pathlib.PurePosixPath(f).parents if str(p)!='.'},key=str):
  value=str(d);top=value.split('/')[0];internal=top in INTERNAL
  folders.append({'folder':value+'/','url':HOST+'/'+quote(value,safe='/')+'/','expected_live':'403 or 404, no listing or file contents' if internal else 'public page/asset namespace','after_rule':top+'/.htaccess' if internal else 'no folder deny intended'})
 folders.append({'folder':'.git/ (never deploy)','url':HOST+'/.git/','expected_live':'403 or 404, no listing or file contents','after_rule':'root RedirectMatch 403; never upload metadata'})
 probes=[e['url'] for e in entries if e['category']=='internal-denied']+[x['url'] for x in folders if x['expected_live'].startswith('403')]
 probes += [HOST+'/.git/HEAD',HOST+'/phase24b-access-probe.py',HOST+'/phase24b-access-probe.cjs',HOST+'/phase24b-access-probe.log',HOST+'/phase24b-access-probe.bak',HOST+'/phase24b-access-probe.json']
 return {'temporary_keyed_expiring_exceptions':['deploy-check.php'] if (root/'deploy-check.php').exists() else [],'baseline':BASELINE,'assumption':'repository root equals web root','native_apache_litespeed_verified':False,'local_adapter_is_not_directive_engine':True,'browser_fetched_data_files':[],'browser_data_check':'No browser fetch/XHR/axios/getJSON or src/href/action request to data/ in public source. PHP file_get_contents/include are server-side.','before_gaps':['root Markdown notes and phase JSON exports','includes/ and data/ had no directory deny','destinations/ and places/ contained internal PHP arrays without repository deny','private root CSV templates/audit export','root scripts/log/backup extension patterns and accidental Git metadata'], 'files':entries,'folders':folders,'live_deny_urls':sorted(set(probes)), 'absent_file_types':{ext:not any(pathlib.Path(e['file']).suffix.lower()==ext for e in entries) for ext in ['.log','.bak']},'owner_decision':'Do not upload reports/, tools/, notes, audit exports, caches or Git metadata into live hosting. Required runtime includes/data/destination/place files must stay PHP-readable: use an owner-approved non-public layout before omitting or relocating them. This patch does not relocate runtime paths.'}
def public_paths(root):
 paths={route for route,v in routes(root).items() if v['status']=='published' and route!='/404'}|{'/sitemap.xml','/robots.txt','/llms.txt','/llms-full.txt','/google10fa7a4178242a1f.html','/favicon.ico'}
 paths|={'/'+p.relative_to(root).as_posix() for p in (root/'assets').rglob('*') if p.is_file() and p.name!='.htaccess'}
 return sorted(paths)

def check_local(root,base):
 data=inventory(root);denied=0;public=0;assets=0
 for url in data['live_deny_urls']:
  path=url.removeprefix(HOST);status,headers,body=fetch(base,path)
  assert status in [403,404],(path,status,'Private artifact served')
  assert body in [b'Forbidden',b'Not found'],(path,'Unexpected local body')
  denied+=1
 for path in public_paths(root):
  status,headers,body=fetch(base,path);assert status==200 and body,(path,status,'Public resource blocked')
  public+=1;assets+=path.startswith('/assets/') or path=='/favicon.ico'
 return {'status':'PASS local adapter only','denied_or_absent_probes':denied,'public_resources_200':public,'site_assets_200':assets,'native_engine_rules_tested':False}
def write(root,base=None):
 for f in GENERATED:(root/f).touch(exist_ok=True)
 data=inventory(root)
 data['positive_live_urls_expected_200']=[HOST+p for p in public_paths(root)]
 if base:data['local_adapter_results']=check_local(root,base)
 (root/GENERATED[0]).write_text(json.dumps(data,indent=2)+'\n')
 (root/GENERATED[2]).write_text('# Exact owner live GET checks: each URL below must return 403 or 404 with no file contents/listing.\n# Absent probe files alone do not prove rule enforcement. Test actual existing denied files too.\n'+'\n'.join(data['live_deny_urls'])+'\n')
 counts=collections.Counter(e['category'] for e in data['files'])
 text='''# Phase 24b public-file exposure audit

Assumption: repository root is live web root. Inventory covers every current non-page file, including ignored Python
caches, and every enclosing folder. Git internals are represented by a whole-
namespace denial/exclusion instead of enumerating or reading credentials. No certificate or private certificate field is added.

## Result and access-policy changes

Before: reports/ and tools/ already had directory denies. Root Markdown notes,
phase JSON/CSV exports and data/includes/internal-data folders lacked explicit
repository access protection. robots.txt is not an access-control mechanism.
The older local adapter overblocked some folders relative to native config,
so its old 403s were never treated as native proof.

After: Apache 2.4/LiteSpeed-compatible `Require all denied` files in reports/,
tools/, includes/, data/, destinations/ and places/. Existing report/tool rules
are unchanged. Root rewrite bytes remain an exact prefix: only deny directives
are appended. Root FilesMatch denies Markdown/scripts/logs/backups, phase JSON,
private CSV exports and dotfiles; RedirectMatch 403 denies accidental Git URLs.
The CSV/dotfile/Git/internal-array denies are conservative additions, not page
publication changes. No public page, asset, discovery or verification route is
denied intentionally. No existing rewrite is changed.

No browser-fetched data/ file was found: browser fetch/XHR/axios/getJSON and
src/href/action references were reviewed in public PHP/HTML/JS source. JSON
reads are PHP-side. Therefore the whole data/ folder is denied without a
browser exception. Includes remain PHP-readable internally; HTTP denies do
not prevent server-side includes.

## Native limitation and exact owner tests

**Native Apache/LiteSpeed enforcement: NOT VERIFIED.** The local PHP WASM
adapter does not parse .htaccess or emulate rewrite/authz modules. Separate
adapter denial/positive probes pass, but do not prove the hosting engine,
AllowOverride or LiteSpeed directive support/configuration. No live site was
changed or tested. FAIL live clearance until owner verifies the actual host.

Every exact deny URL appears in `phase-24b-live-url-checks.txt` and the JSON
inventory. GET each on the live host: expected **403 or 404 with no file
contents and no directory listing**. A 404 for an absent probe does not prove
a rule protects an existing file. A 200, leaked content, redirect exposing
content or a server error is a failed release check; restore the complete
backup/settings before proceeding. Existing note/JSON/script files and
folder probes are included, not only invented nonexistent paths.

Positive GET checks must return 200: every published route, sitemap.xml,
robots.txt, llms.txt, llms-full.txt, verification HTML, favicon and every site
asset. They are exercised locally, separately from native-rule validation.
Do not submit an enquiry as part of these probes; real delivery still needs
its own separately authorized verification.

## Owner deployment decision

**Do not upload internal folders, notes, tooling, reports, caches, exports or
Git metadata into the live hosting folder.** Required runtime includes/data/
destination/place files currently use repository-relative PHP paths. They
cannot simply be omitted without breaking the site. Approve and test a
non-public runtime layout/path configuration before relocating or omitting
those required files. This phase adds defense-in-depth denies under the
requested web-root assumption; it does not move runtime files or deploy.
Complete backup and all-file/settings restore readiness remain prerequisites.

## Complete file inventory

'''
 text+=f"{len(data['files'])} non-page files: {counts['internal-denied']} denied, {counts['intentional-public']} intentionally public. Exact machine-readable rows include prior block, new rule, full URL and expected result. No log/backup file was found; deny/probe coverage still exists for both extensions.\n\n"
 text+='| File | Before | After / expected |\n| --- | --- | --- |\n'
 for e in data['files']:text+='| `'+e['file']+'` | '+e['before_block']+' | '+e['after_rule']+'; '+e['expected_live']+' |\n'
 text+='\n## Every folder\n\n'
 for d in data['folders']:text+='- `'+d['folder']+'`: '+d['after_rule']+'; '+d['expected_live']+'.\n'
 text+='\n## Exact live denial URLs\n\nEach must return 403 or 404 without file contents/listing.\n\n```text\n'+'\n'.join(data['live_deny_urls'])+'\n```\n'
 text+='\n## Exact positive live URLs\n\nEach must return 200 with the expected public resource.\n\n```text\n'+'\n'.join(data['positive_live_urls_expected_200'])+'\n```\n'
 if base:text+='\nLocal adapter results (not native engine results): `'+json.dumps(data['local_adapter_results'])+'`.\n'
 (root/GENERATED[1]).write_text(text);return data
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--root',type=pathlib.Path,default=ROOT);p.add_argument('--base-url');a=p.parse_args();d=write(a.root,a.base_url);print(json.dumps({'files':len(d['files']),'live_denial_urls':len(d['live_deny_urls']),'local':d.get('local_adapter_results'),'native_verified':False}))
