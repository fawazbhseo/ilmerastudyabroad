#!/usr/bin/env python3
"""Validate exact-commit Task 3 HTML fixtures and freeze their hashes."""
from __future__ import annotations
import hashlib
import importlib.util
import json
import pathlib
import subprocess
import tarfile

ROOT=pathlib.Path(__file__).resolve().parents[2]
EVIDENCE=pathlib.Path('/home/user/phase32c-runtime/hero-ab')
RENDERS=EVIDENCE/'renders'
FIXTURE_OUT=EVIDENCE/'fixtures.json'
MANIFEST_OUT=ROOT/'reports/phase-32c-hero-ab-fixtures.json'
A_COMMIT='7d1bb9ec0522bcbc7953262920fafb50bf04ab72'
B_COMMIT='ac2d9b06dc85578e4b4c31ad236b228f67d44333'
ROUTES={
    '/study-abroad-counselling-mysuru':'study-abroad-counselling-mysuru.html',
    '/blog/how-to-choose-study-abroad-consultant-karnataka':'blog_how-to-choose-study-abroad-consultant-karnataka.html',
}
PROTECTED=['text','title','headings','meta','robots','canonical','anchors','images','picture_sources','json_ld']
SHA=lambda b:hashlib.sha256(b).hexdigest()

def load_comparator():
    spec=importlib.util.spec_from_file_location('phase32_content_comparator',ROOT/'tools/phase32/compare_43_route_content.py')
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def git(*args:str)->str:
    return subprocess.check_output(['git',*args],cwd=ROOT,text=True).strip()

def load_render(arm:str,route:str,filename:str,comparator):
    index_path=RENDERS/arm/'routes.json'
    index=json.loads(index_path.read_text(encoding='utf-8'))
    if index.get('arm')!=arm or index.get('routeCount')!=len(ROUTES):raise SystemExit(f'Bad render identity/count for {arm}')
    expected=A_COMMIT if arm=='A' else B_COMMIT
    if index.get('sourceCommit')!=expected:raise SystemExit(f'Unexpected source commit for {arm}: {index.get("sourceCommit")}')
    row=next((r for r in index['routes'] if r['route']==route),None)
    if not row or row['status']!=200 or row['file']!=f'renders/{arm}/{filename}':raise SystemExit(f'Bad status/file for {arm} {route}')
    raw=(EVIDENCE/row['file']).read_bytes()
    if len(raw)!=row['bytes'] or SHA(raw)!=row['sha256']:raise SystemExit(f'HTML hash/size mismatch: {arm} {route}')
    return raw,comparator.extract(raw)

def file_map(root:pathlib.Path):
    return {p.relative_to(root).as_posix():p.read_bytes() for p in root.rglob('*') if p.is_file()}

def main():
    if MANIFEST_OUT.exists() or FIXTURE_OUT.exists():raise SystemExit('Refusing to overwrite existing Task 3 fixture evidence')
    comparator=load_comparator()
    a_tree=git('rev-parse',f'{A_COMMIT}^{{tree}}')
    b_tree=git('rev-parse',f'{B_COMMIT}^{{tree}}')
    a_manifest=json.loads((RENDERS/'A'/'routes.json').read_text(encoding='utf-8'))
    b_manifest=json.loads((RENDERS/'B-plain'/'routes.json').read_text(encoding='utf-8'))
    if a_manifest.get('sourceCommit')!=A_COMMIT or b_manifest.get('sourceCommit')!=B_COMMIT:raise SystemExit('Exact source commit check failed')

    source_a=file_map(EVIDENCE/'source/A')
    source_plain=file_map(EVIDENCE/'source/B-plain-ac2')
    source_still=file_map(EVIDENCE/'source/B-still-ac2')
    if source_plain.keys()!=source_still.keys():raise SystemExit('B source trees do not contain the same files')
    source_changes={name for name in source_plain if source_plain[name]!=source_still[name]}
    if source_changes!={'includes/visual-config.php'}:raise SystemExit(f'Expected only the test toggle to differ between B arms, got {sorted(source_changes)}')
    plain_config=source_plain['includes/visual-config.php'].decode('utf-8')
    still_config=source_still['includes/visual-config.php'].decode('utf-8')
    plain_line="define('ILMERA_VISUAL_PLAIN_HERO_TEMPLATES', ['place','article']);"
    still_line="define('ILMERA_VISUAL_PLAIN_HERO_TEMPLATES', []);"
    if plain_config.count(plain_line)!=1 or still_config.count(still_line)!=1:raise SystemExit('B hero toggle values do not match the planned arms')
    if plain_config.replace(plain_line,'<HERO_TOGGLE>')!=still_config.replace(still_line,'<HERO_TOGGLE>'):
        raise SystemExit('B configuration differs outside the one test-only hero toggle')

    fixtures={}
    route_rows=[]
    for route,filename in ROUTES.items():
        pages={}
        digests={}
        for arm in ['A','B-still','B-plain']:
            raw,parsed=load_render(arm,route,filename,comparator)
            pages[arm]=(raw,parsed)
            digests[arm]={'bytes':len(raw),'sha256':SHA(raw)}
        checks={
            'A_vs_B_still':comparator.compare(pages['A'][1],pages['B-still'][1]),
            'A_vs_B_plain':comparator.compare(pages['A'][1],pages['B-plain'][1]),
            'B_still_vs_B_plain':comparator.compare(pages['B-still'][1],pages['B-plain'][1]),
        }
        if not all(all(value.values()) for value in checks.values()):raise SystemExit(f'Protected content parity failed for {route}: {checks}')
        still_html=pages['B-still'][0].decode('utf-8')
        plain_html=pages['B-plain'][0].decode('utf-8')
        if still_html.count('<canvas class="p32-hero-still"')!=1:raise SystemExit(f'Expected one still canvas on {route}')
        if 'hero-still-' not in still_html or 'p32-hero-still' not in still_html:raise SystemExit(f'Still loader/fallback missing on {route}')
        if '<canvas class="p32-hero-still"' in plain_html or '/assets/images/hero-still-' in plain_html:raise SystemExit(f'Unexpected still markup or image URL in plain arm on {route}')
        if plain_html.count(':is(.mini-hero,.article-hero,.blog-hero,.legal-hero,.directory-hero,.err-wrap){background:#04060f;}')!=1:
            raise SystemExit(f'Plain hero palette override missing or duplicated on {route}')
        fixtures[route]={arm:pages[arm][0].decode('utf-8') for arm in ['A','B-still','B-plain']}
        route_rows.append({
            'route':route,
            'http_status':{'A':200,'B-still':200,'B-plain':200},
            'html':digests,
            'protected_content_checks':checks,
            'still_toggle_checks':{'B_still_has_one_canvas':True,'B_still_has_loader_and_no_script_fallback':True,'B_plain_has_no_still_markup_or_urls':True,'B_plain_has_one_plain_palette_rule':True},
        })

    legacy_tar=ROOT/'reports/phase-31-task4-ab-fixtures.tar.gz'
    legacy_report=json.loads((ROOT/'reports/phase-31-task4-ab-fixtures.json').read_text(encoding='utf-8'))
    legacy_archive_bytes=legacy_tar.read_bytes()
    with tarfile.open(legacy_tar,'r:gz') as archive:
        legacy_bytes=archive.extractfile('fixtures.json').read()
    if SHA(legacy_bytes)!=legacy_report['fixture_json_sha256']:raise SystemExit('Prior Task31 fixture archive does not match its committed hash')
    legacy_fixtures=json.loads(legacy_bytes)
    legacy_comparison={}
    for route,filename in ROUTES.items():
        current_a=load_render('A',route,filename,comparator)[1]
        previous_a=comparator.extract(legacy_fixtures[route]['A'].encode('utf-8'))
        check=comparator.compare(previous_a,current_a)
        legacy_comparison[route]={'matches_exact_A_commit_render':all(check.values()),'differing_protected_invariants':[key for key,value in check.items() if not value]}
    mismatch=any(not row['matches_exact_A_commit_render'] for row in legacy_comparison.values())

    fixture_bytes=(json.dumps(fixtures,ensure_ascii=False,separators=(',',':'))+'\n').encode('utf-8')
    FIXTURE_OUT.write_bytes(fixture_bytes)
    still_assets={}
    for rel in ['assets/images/hero-still-640.webp','assets/images/hero-still-1440.webp']:
        data=(EVIDENCE/'source/B-plain-ac2'/rel).read_bytes()
        still_assets[rel]={'bytes':len(data),'sha256':SHA(data),'identical_in_B_still_and_B_plain':data==(EVIDENCE/'source/B-still-ac2'/rel).read_bytes()}
    report={
        'phase':'32c','task':'3_hero_still_ab_fixtures',
        'fixture_status':'PASS',
        'scope':'Local simulated experiment only. No browser performance sample is included in this fixture manifest.',
        'source_commits':{'A':A_COMMIT,'B_current':'ac2d9b06dc85578e4b4c31ad236b228f67d44333'},
        'source_trees':{'A':a_tree,'B_current':b_tree},
        'rendering':{'runtime':'PHP-WASM 8.5.8 via @php-wasm/* 3.1.50','routes_per_arm':len(ROUTES),'arms':['A','B-still','B-plain'],'A_source_exact_commit_render':True},
        'routes':route_rows,
        'B_arm_guard':{'source_tree_file_changes':['includes/visual-config.php'],'only_difference':'One test-only value in ILMERA_VISUAL_PLAIN_HERO_TEMPLATES. B-plain keeps place/article plain; B-still empties that list so the existing still loader is eligible. No production source was edited for this comparison.'},
        'still_assets':still_assets,
        'fixture_json_external':str(FIXTURE_OUT),
        'fixture_json_bytes':len(fixture_bytes),
        'fixture_json_sha256':SHA(fixture_bytes),
        'prior_phase31_fixture_audit':{'archive':'reports/phase-31-task4-ab-fixtures.tar.gz','archive_sha256':SHA(legacy_archive_bytes),'declared_A_source_commit':legacy_report.get('A_source_commit'),'exact_commit_render_comparison':legacy_comparison,'mismatch_detected':mismatch,'handling':'The prior artifact is retained unchanged. Task 3 uses a fresh PHP-WASM render of the exact declared A commit because its stored A HTML differs on protected content for these routes.' if mismatch else 'The prior artifact matches the exact source render.'},
        'budgets_fixed_before_sampling':{'added_transfer_bytes_strictly_less_than':150000,'no_new_render_blocking_resource':True,'CLS_no_worse_than_A_and_below':0.1,'LCP_B_over_A_at_most':1.10,'TBT_increase_ms_at_most':50},
        'next_step':'Run nine fresh Chromium samples for A, B-still and B-plain on each route in balanced alternating order, plus nine paired A/A repeats on Mysuru. Preserve the raw sample file and push it before analysis.',
    }
    MANIFEST_OUT.write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(json.dumps({'fixture_status':'PASS','routes':len(route_rows),'content_invariant_failures':0,'B_arm_source_file_changes':sorted(source_changes),'fixture_json_bytes':len(fixture_bytes),'fixture_json_sha256':SHA(fixture_bytes),'prior_fixture_A_mismatch':mismatch,'prior_fixture_differing_invariants':{route:row['differing_protected_invariants'] for route,row in legacy_comparison.items()}},indent=2))

if __name__=='__main__':main()
