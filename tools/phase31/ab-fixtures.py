#!/usr/bin/env python3
"""Freeze the Task2 no-still arm and Task3 still arm for the authorized local A/B."""
from __future__ import annotations
import hashlib,json,pathlib,re,subprocess
ROOT=pathlib.Path(__file__).resolve().parents[2]
EVIDENCE=pathlib.Path('/home/user/phase31/task4')
A_RENDER=EVIDENCE/'a-evidence/render-before'
B_RENDER=pathlib.Path('/home/user/phase31/task3/render-before')
A_SOURCE=EVIDENCE/'source-a'
FIXTURE_OUT=EVIDENCE/'fixtures.json'
ROUTES=['/','/services','/about','/contact','/study-in-germany','/study-abroad-counselling-mysuru','/blog/how-to-choose-study-abroad-consultant-karnataka','/blog/']
CONTROLS=ROUTES[:4]
TARGETS=ROUTES[4:]

def sha(data:bytes)->str:return hashlib.sha256(data).hexdigest()
def git(*args:str)->str:return subprocess.check_output(['git',*args],cwd=ROOT,text=True).strip()
def load_render(directory:pathlib.Path)->dict:
    index=json.loads((directory/'routes.json').read_text())
    return {row['url']:row for row in index['routes']}
def html_for(directory:pathlib.Path,index:dict,route:str)->str:
    row=index[route]
    return (directory/row['evidence']).read_text(encoding='utf-8')

def main()->None:
    EVIDENCE.mkdir(parents=True,exist_ok=True)
    a_source=json.loads((ROOT/'reports/phase-31-task2-render-comparison.json').read_text())['source_head']
    b_source=json.loads((ROOT/'reports/phase-31-task3-render-comparison.json').read_text())['source_head']
    if a_source!='7d1bb9ec0522bcbc7953262920fafb50bf04ab72':raise SystemExit(f'Unexpected Task2 A source {a_source}')
    if b_source!='806769a0d379e2059f654ba96be1561484d64598':raise SystemExit(f'Unexpected Task3 B source {b_source}')
    a_index=load_render(A_RENDER);b_index=load_render(B_RENDER)
    if set(a_index)!=set(b_index) or len(a_index)!=43:raise SystemExit('A/B local route captures must each contain the frozen 43 routes')
    if set(ROUTES)-set(a_index):raise SystemExit('A/B route missing from frozen captures')
    source=(ROOT/'includes/visual-system.php').read_text(encoding='utf-8')
    match=re.search(r"\$css\s*\.\=\s*<<<'CSS'\s*\r?\n(.*?)\r?\nCSS;",source,re.S)
    if not match or 'Phase31 Task3 static still' not in match.group(1):raise SystemExit('Could not identify the exact approved Task3 CSS block')
    still_block=match.group(1)
    if git('hash-object',str(A_SOURCE/'includes/visual-system.php'))!=git('rev-parse',f'{a_source}:includes/visual-system.php'):
        raise SystemExit('A source archive does not match the frozen Task2 commit')
    if git('rev-parse',f'{b_source}:includes/visual-system.php')!=git('hash-object','includes/visual-system.php'):
        raise SystemExit('Current Task3 template CSS does not match the frozen B source commit')
    asset_hashes={}
    for asset in ['assets/images/hero-still-720.webp','assets/images/hero-still-1440.webp']:
        a_bytes=subprocess.check_output(['git','show',f'{a_source}:{asset}'],cwd=ROOT)
        b_bytes=subprocess.check_output(['git','show',f'{b_source}:{asset}'],cwd=ROOT)
        if a_bytes!=b_bytes:raise SystemExit(f'Still asset changed between A/B: {asset}')
        asset_hashes[asset]={'sha256':sha(a_bytes),'bytes':len(a_bytes),'identical_in_A_and_B':True}
    fixtures={};rows=[]
    for route in ROUTES:
        a_row,b_row=a_index[route],b_index[route]
        if a_row['status']!=200 or b_row['status']!=200:raise SystemExit(f'Non-200 A/B render for {route}')
        a_html,b_html=html_for(A_RENDER,a_index,route),html_for(B_RENDER,b_index,route)
        if route in CONTROLS:
            if a_html!=b_html:raise SystemExit(f'Reference control differs between Task2 and Task3: {route}')
            if 'hero-still-' in a_html+b_html:raise SystemExit(f'Still CSS escaped to reference control: {route}')
            role='control'
            normalized_sha=sha(b_html.encode())
            block_count=0
        else:
            if 'hero-still-' in a_html:raise SystemExit(f'Task2 A unexpectedly has a still: {route}')
            block_count=b_html.count(still_block)
            if block_count!=1:raise SystemExit(f'Expected exactly one Task3 CSS block on {route}, got {block_count}')
            normalized=b_html.replace(still_block,'',1)
            if normalized!=a_html:raise SystemExit(f'Unexpected non-CSS A/B difference on {route}')
            if normalized.count('hero-still-') or a_html.count('hero-still-'):raise SystemExit(f'Unexpected still URL in the normalized baseline: {route}')
            if b_html.count('/assets/images/hero-still-')!=2:raise SystemExit(f'Expected both responsive still URLs in B HTML: {route}')
            role='static-still target'
            normalized_sha=sha(normalized.encode())
        fixtures[route]={'A':a_html,'B':b_html}
        rows.append({'route':route,'role':role,'http_status_A':a_row['status'],'http_status_B':b_row['status'],'A_source_commit':a_source,'B_source_commit':b_source,'A_html_bytes':len(a_html.encode()),'B_html_bytes':len(b_html.encode()),'A_html_sha256':sha(a_html.encode()),'B_html_sha256':sha(b_html.encode()),'Task3_css_block_count_in_B':block_count,'normalized_B_equals_A':True,'normalized_html_sha256':normalized_sha})
    FIXTURE_OUT.write_text(json.dumps(fixtures,ensure_ascii=False,separators=(',',':'))+'\n',encoding='utf-8')
    report={'phase':31,'task':4,'freeze_status':'PASS','scope':'local-only A/B; no live or field-speed claim','A_variant':'Task2 source before Task3 static hero still CSS','A_source_commit':a_source,'B_variant':'Task3 source with approved static still CSS','B_source_commit':b_source,'route_count':len(ROUTES),'control_routes':CONTROLS,'target_routes':TARGETS,'round_order':'A/B on even rounds, B/A on odd rounds; seven rounds per route; one fresh Chromium process per arm sample; serial, no overlapping browser QA','fixture_server':'same local HTTP origin and paths for A and B; identical static asset delivery; offline npm mirrors','fixture_json_external':str(FIXTURE_OUT),'fixture_json_sha256':sha(FIXTURE_OUT.read_bytes()),'fixture_json_bytes':FIXTURE_OUT.stat().st_size,'source_diff_guard':'Controls are byte-identical. On each of the four targets, removing the exact Task3 CSS heredoc from B makes its full rendered HTML byte-identical to A. No content, image, metadata or other style changes enter the candidate.','static_assets':asset_hashes,'routes':rows,'performance_claims':False}
    (ROOT/'reports/phase-31-task4-ab-fixtures.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(f'PASS frozen A/B fixtures: {len(ROUTES)} routes, {len(CONTROLS)} controls, {len(TARGETS)} static-still targets; byte-exact scoped difference only')
if __name__=='__main__':main()
