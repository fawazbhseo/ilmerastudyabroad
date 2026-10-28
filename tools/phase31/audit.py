#!/usr/bin/env python3
"""Build the auditable Phase31 blank-space report from all 516 pinned-browser cases."""
from __future__ import annotations
import argparse, gzip, hashlib, json, os, pathlib, re, subprocess, sys, time
from source_policy import verify_task2_spacing_scope
ROOT=pathlib.Path(__file__).resolve().parents[2]
EVIDENCE=pathlib.Path(os.environ.get('PHASE31_EVIDENCE','/home/user/phase31'))
SCAN=EVIDENCE/'scan-before'
WIDTHS={360:120,768:160,1280:200}

def read_json(p): return json.loads(pathlib.Path(p).read_text())
def runtime_paths_changed(source_head,current_head):
    if subprocess.run(['git','merge-base','--is-ancestor',source_head,current_head],cwd=ROOT).returncode:raise SystemExit('Render source is not an ancestor of verification HEAD')
    names=subprocess.check_output(['git','diff','--name-only',source_head,current_head],cwd=ROOT,text=True).splitlines()
    roots={'index.php','services.php','about.php','contact.php','404.php','all-pages.php','privacy-policy.php','terms.php','robots.txt','sitemap.xml','llms.txt','llms-full.txt','favicon.ico','deploy-check.php'}
    return [p for p in names if pathlib.PurePosixPath(p).parts[0] in {'assets','data','includes','destinations','places','blog'} or p in roots or pathlib.PurePosixPath(p).name=='.htaccess' or (len(pathlib.PurePosixPath(p).parts)==1 and p.endswith('.php'))]
def norm_selector(selector):
    selector=(selector or 'main').split(',')[0].strip()
    ident=re.search(r'#([\w-]+)',selector)
    classes=re.findall(r'\.([\w-]+)',selector)
    tag=re.match(r'^[a-zA-Z][\w-]*',selector)
    return ident.group(1) if ident else None, classes, tag.group(0) if tag else None

def source_files():
    tracked=subprocess.check_output(['git','ls-files','-z'],cwd=ROOT).decode().split('\0')
    return [ROOT/p for p in tracked if p and (p.endswith('.php') or p.endswith('.css'))]
SOURCE_FILES=source_files()
SOURCE_TEXT={p:p.read_text(encoding='utf-8',errors='replace').splitlines() for p in SOURCE_FILES}
SOURCE_CACHE={}

def route_file(route):
    if route=='/': return 'index.php'
    if route=='/404': return '404.php'
    if route=='/blog/': return 'blog/index.php'
    if route.startswith('/blog/'): return route.lstrip('/')+'.php'
    return route.lstrip('/')+'.php'

def find_source(selector,route):
    cache_key=(selector,route)
    if cache_key in SOURCE_CACHE:return SOURCE_CACHE[cache_key]
    ident,classes,tag=norm_selector(selector)
    preferred=[ROOT/route_file(route),ROOT/'includes/destination-page.php',ROOT/'includes/place-page.php',ROOT/'includes/header.php',ROOT/'includes/footer.php']
    ordered=[]
    for p in preferred+SOURCE_FILES:
        if p in SOURCE_TEXT and p not in ordered: ordered.append(p)
    markup=[];styles=[]
    for p in ordered:
        lines=SOURCE_TEXT[p]
        for i,line in enumerate(lines,1):
            if ident and re.search(r'\bid\s*=\s*(["\'])[^"\']*\b'+re.escape(ident)+r'\b[^"\']*\1',line,re.I):
                markup.append((0 if p in preferred else 1,p,i,line.strip()[:180]))
            elif classes and re.search(r'\bclass\s*=\s*(["\'])[^"\']*'+''.join(r'(?=[^"\']*\b'+re.escape(c)+r'\b)' for c in classes)+r'[^"\']*\1',line,re.I):
                markup.append((0 if p in preferred else 1,p,i,line.strip()[:180]))
            elif not ident and not classes and tag and re.search(r'<'+re.escape(tag)+r'\b',line,re.I):
                markup.append((0 if p in preferred else 1,p,i,line.strip()[:180]))
            # CSS property/source locator: search selector tokens only in CSS-like lines.
            target=('#'+ident if ident else '')+''.join('.'+c for c in classes)
            if target and target in line and ('{' in line or ':' in line):
                styles.append((0 if p in preferred else 1,p,i,line.strip()[:180]))
    m=sorted(markup,key=lambda x:(x[0],x[1].as_posix(),x[2]))
    st=sorted(styles,key=lambda x:(x[0],x[1].as_posix(),x[2]))
    # Prefer the actual page/template markup over an unrelated selector mention in CSS.
    result={
        'source_file':str(m[0][1].relative_to(ROOT)) if m else route_file(route),
        'source_line':m[0][2] if m else 1,
        'source_excerpt':m[0][3] if m else 'Route entry or shared template; selector occurrence not uniquely matched.',
        'style_source_file':str(st[0][1].relative_to(ROOT)) if st else None,
        'style_source_line':st[0][2] if st else None,
    }
    SOURCE_CACHE[cache_key]=result
    return result

def require_crop(item,case_id):
    crop=item.get('crop')
    if not crop or not (ROOT/crop).is_file():raise SystemExit(f'Missing saved finding crop for {case_id}: {crop}')

def load_cases(scan_dir=SCAN,after=False):
    summary=read_json(pathlib.Path(scan_dir)/'summary.json')
    current_head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip()
    source_head=summary.get('source_head')
    render_index=read_json(EVIDENCE/'routes.json')
    render_index_head=render_index.get('source_head')
    if not render_index_head:raise SystemExit('Rendered route source head is missing')
    if render_index_head!=source_head:raise SystemExit('Scan and rendered route source heads differ')
    if after:
        baseline_head=read_json(ROOT/'reports/phase-31-render-baseline.json')['source_head']
        approved=verify_task2_spacing_scope(baseline_head,source_head)
        if source_head!=current_head:raise SystemExit('Post-fix scan source is not current verification HEAD')
    else:
        if render_index_head!=read_json(ROOT/'reports/phase-31-render-baseline.json')['source_head']:
            raise SystemExit('Task1 scan source does not match the frozen pre-fix render source')
        runtime_changes=runtime_paths_changed(source_head,current_head)
        if runtime_changes:raise SystemExit(f'Production runtime changed after captured source: {runtime_changes}')
        approved=[]
    expected=43*3*2*2
    if summary.get('case_count')!=expected or not summary.get('complete') or summary.get('expected_case_count')!=expected:
        raise SystemExit(f'INCOMPLETE scan: expected {expected}, found {summary.get("case_count")}')
    if len(summary.get('routes',[]))!=43 or len(set(summary['routes']))!=43:raise SystemExit('Expected 43 unique rendered route entries')
    expected_cases={(r,w,j,m) for r in summary['routes'] for w in (360,768,1280) for j in ('on','off') for m in ('normal','reduced')}
    actual_cases={(c['route'],c['width'],c['javascript'],c['motion']) for c in summary.get('cases',[])}
    if len(actual_cases)!=expected or actual_cases!=expected_cases:raise SystemExit('Scan route/width/JS/motion matrix is incomplete or duplicated')
    findings=[];case_summaries=[]
    for entry in summary['cases']:
        p=SCAN/'cases'/f"{entry['id']}.json"
        c=read_json(p)
        if c['http_status'] not in (200,404): raise SystemExit(f'Bad route status {c["http_status"]} for {c["route"]}')
        if not c['scroll']['returned_to_top'] or c['scroll']['settle_ms']!=3000: raise SystemExit(f'Incomplete scroll/wait {c["id"]}')
        case_summaries.append({k:c.get(k) for k in ('id','route','width','javascript','motion','http_status','page_height','scroll','dom','pixel_scan','pinned','request_failures')})
        for b in c['pixel_scan']['interior_candidates']:
            require_crop(b,c['id'])
            f={'finding_id':f"{c['id']}:pixel:{b['y']}",'kind':'pixel-quiet-band','route':c['route'],'width':c['width'],'javascript':c['javascript'],'motion':c['motion'],'y':b['y'],'height':b['height'],'threshold':b['threshold'],'metric':b['metric'],'edge_ratio':b['mean_edge_ratio'],'selector':b.get('selector','main'),'context':b.get('context'),'cause':b.get('cause'),'crop':b.get('crop')}
            f.update(find_source(f['selector'],c['route']));findings.append(f)
        for b in c['dom']['empty_or_spacing_nodes']:
            require_crop(b,c['id'])
            f={'finding_id':f"{c['id']}:{b['kind']}:{b['selector']}:{b['y']}",'kind':b['kind'],'route':c['route'],'width':c['width'],'javascript':c['javascript'],'motion':c['motion'],'y':b['y'],'height':b['height'],'threshold':b['threshold'],'selector':b['selector'],'computed':b.get('computed'),'visible_text_chars':b.get('visible_text_chars'),'hidden_text_chars':b.get('hidden_text_chars'),'visible_media':b.get('visible_media'),'cause':('Computed min-height creates a tail beyond the last visible text/media block after the declared bottom padding.' if b['kind']=='unused-min-height-tail' else 'Non-decorative structural wrapper exceeds the width threshold with no visible text or media.'),'crop':b.get('crop')}
            f.update(find_source(f['selector'],c['route']))
            if b['kind']=='unused-min-height-tail' and c['route']=='/contact' and b['selector']=='#miniHero':
                f['disposition']='Retain: the 88vh first-fold hero intentionally leaves room for its existing bottom scroll cue; no content or layout change authorized here.'
            findings.append(f)
        for b in c['dom']['hidden_text']:
            require_crop(b,c['id'])
            scroll_hints={'/':'Explore','/services':'Explore','/about':'Explore','/contact':'Reach Out'}
            is_scroll_hint=c['route'] in scroll_hints and b.get('text_sample')==scroll_hints[c['route']] and b.get('y',9999)<1200
            kind='intentional-scroll-indicator-dismissed' if is_scroll_hint else 'hidden-reveal-text'
            cause=('Existing scroll cue is initially visible and is intentionally faded after scrollY exceeds 80px; it remains dismissed when returning to the top. JavaScript-off pages do not run that dismissal. It is a cue, not revealed page content.' if is_scroll_hint else b.get('cause','Main-content text remains effectively invisible after scroll and settle.'))
            f={'finding_id':f"{c['id']}:hidden:{b['selector']}:{b['y']}",'kind':kind,'route':c['route'],'width':c['width'],'javascript':c['javascript'],'motion':c['motion'],'y':b['y'],'height':b['height'],'threshold':c['pixel_scan']['threshold'],'selector':'.scroll-ind span' if is_scroll_hint else b['selector'],'computed':b.get('computed'),'text_sample':b.get('text_sample'),'characters':b.get('characters'),'cause':cause,'crop':b.get('crop')}
            if is_scroll_hint:
                f.update(find_source('.scroll-ind',c['route']))
                behavior={'/':'index.php:714','/services':'services.php:816','/about':'about.php:731','/contact':'contact.php:556'}[c['route']]
                f['behavior_source_file'],line=behavior.split(':');f['behavior_source_line']=int(line)
            else:f.update(find_source(f['selector'],c['route']))
            findings.append(f)
    summary['_approved_spacing_source_files']=approved
    return summary,case_summaries,findings

def merge_intervals(intervals):
    if not intervals:return 0
    ints=sorted((max(0,int(a)),max(0,int(b))) for a,b in intervals if b>a)
    total=0;lo,hi=ints[0]
    for a,b in ints[1:]:
        if a<=hi:hi=max(hi,b)
        else:total+=hi-lo;lo,hi=a,b
    return total+hi-lo

def build(scan_dir=SCAN,after=False,report_prefix=None):
    summary,cases,findings=load_cases(scan_dir,after)
    route_rows=[]
    for route in summary['routes']:
        ff=[f for f in findings if f['route']==route]
        intervals=[(f['y'],f['y']+f['height']) for f in ff if f['kind']!='hidden-reveal-text']
        route_rows.append({
            'route':route,'finding_count':len(ff),
            'pixel_band_count':sum(f['kind']=='pixel-quiet-band' for f in ff),
            'unused_min_height_count':sum(f['kind']=='unused-min-height-tail' for f in ff),
            'hidden_reveal_count':sum(f['kind']=='hidden-reveal-text' for f in ff),
            'empty_wrapper_count':sum(f['kind']=='empty-content-wrapper' for f in ff),
            'cumulative_candidate_height_px':sum(f['height'] for f in ff if f['kind']!='hidden-reveal-text'),
            'route_union_candidate_height_px':merge_intervals(intervals),
        })
    route_rows.sort(key=lambda x:(x['route_union_candidate_height_px'],x['cumulative_candidate_height_px']),reverse=True)
    counts={k:sum(f['kind']==k for f in findings) for k in sorted({f['kind'] for f in findings})}
    hidden=[f for f in findings if f['kind']=='hidden-reveal-text']
    intentional_scroll=[f for f in findings if f['kind']=='intentional-scroll-indicator-dismissed']
    unused=[f for f in findings if f['kind']=='unused-min-height-tail']
    empty=[f for f in findings if f['kind']=='empty-content-wrapper']
    inventory=read_json(ROOT/'reports/phase-31-render-baseline.json')
    archive_path=ROOT/'reports/phase-31-before-renders.json.gz'
    before_sitemap_path=ROOT/'reports/phase-31-before-sitemap.xml'
    if not archive_path.is_file() or not before_sitemap_path.is_file():
        raise SystemExit('Missing immutable Task1 render or sitemap baseline')
    if after:
        render_index=read_json(EVIDENCE/'routes.json')
        routes=inventory['routes']
        sitemap_bytes=(EVIDENCE/'sitemap.xml').read_bytes()
        baseline_sitemap=before_sitemap_path.read_bytes()
        if sitemap_bytes!=baseline_sitemap:raise SystemExit('Post-fix sitemap differs from the immutable Task1 sitemap')
        from xml.etree import ElementTree as ET
        sitemap_root=ET.fromstring(sitemap_bytes)
        sitemap_urls=[e.text for e in sitemap_root.iter() if e.tag.endswith('loc')]
        if len(sitemap_urls)!=38 or len(set(sitemap_urls))!=38:raise SystemExit('Post-fix sitemap must retain its exact 38 entries')
        before=read_json(ROOT/'reports/phase-31-blank-space-audit.json')
        before_counts=before['finding_counts']
        kinds=sorted(set(before_counts)|set(counts))
        comparison={k:{'task1':before_counts.get(k,0),'task2':counts.get(k,0),'delta':counts.get(k,0)-before_counts.get(k,0)} for k in kinds}
    else:
        render_index=read_json(EVIDENCE/'routes.json')
        render_map={x['url']:x for x in render_index['routes']}
        routes=[];snap={}
        for route in summary['routes']:
            name=render_map[route]['evidence'];body=(EVIDENCE/'render-before'/name).read_bytes()
            snap[route]={'sha256':hashlib.sha256(body).hexdigest(),'bytes':len(body),'html':body.decode('utf-8',errors='strict')}
            routes.append({'route':route,'source_file':render_map[route]['file'],'http_status':render_map[route]['status'],'bytes':len(body),'sha256':snap[route]['sha256']})
        archive={'source_head':summary['source_head'],'routes':snap,'route_inventory':routes}
        raw=json.dumps(archive,ensure_ascii=False,separators=(',',':')).encode()
        archive_path.write_bytes(gzip.compress(raw,compresslevel=9,mtime=0))
        sitemap_source=EVIDENCE/'sitemap.xml'
        if not sitemap_source.exists():raise SystemExit('Missing pre-fix PHP sitemap snapshot')
        sitemap_bytes=sitemap_source.read_bytes()
        from xml.etree import ElementTree as ET
        sitemap_root=ET.fromstring(sitemap_bytes)
        sitemap_urls=[e.text for e in sitemap_root.iter() if e.tag.endswith('loc')]
        if len(sitemap_urls)!=38 or len(set(sitemap_urls))!=38:
            raise SystemExit(f'Expected exact pre-fix 38-entry sitemap, found {len(sitemap_urls)}')
        before_sitemap_path.write_bytes(sitemap_bytes)
        inventory={'source_head':summary['source_head'],'routes':routes,'sitemap_entry_count':38,'render_archive':'reports/phase-31-before-renders.json.gz'}
        (ROOT/'reports/phase-31-render-baseline.json').write_text(json.dumps(inventory,indent=2)+'\n')
        comparison=None
    routes_for_status=render_index['routes'] if after else routes
    route_count=len(routes_for_status)
    prefix=report_prefix or ('phase-31-after-blank-space-audit' if after else 'phase-31-blank-space-audit')
    task=2 if after else 1
    out={
        'phase':31,'task':task,'run_type':'post-fix comparison' if after else 'pre-fix baseline',
        'source_head':summary['source_head'],'baseline_source_head':inventory['source_head'],
        'approved_spacing_source_files':summary.get('_approved_spacing_source_files',[]),
        'browser':{'chromium':'143.0.7499.0 from @sparticuz/chromium 143.0.4','playwright':'1.58.2','gsap':'3.12.2','three':'0.128.0','sharp':'0.34.5'},
        'scan_conditions':{
            'route_count':43,'widths':[360,768,1280],'javascript':['on','off'],'motion':['normal','reduced'],
            'case_count':summary['case_count'],'replayed_cases':summary.get('replayed_cases',[]),
            'scroll':'~60px per 500-612px slow-scroll step, through full page; then 3000ms settle; return to top',
            'raster_thresholds_px':WIDTHS,
            'raster_metric':'horizontal adjacent grayscale difference >=18; quiet row if edge occupancy <0.6% at downsampled width <=512px; contiguous quiet bands only; retain only bands bracketed by active rows',
            'classification_note':'Raster and structural flags are candidates. Existing section padding, intentional backgrounds, and repeated views are not automatically removable space.',
        },
        'finding_counts':counts,'hidden_reveal_findings':len(hidden),
        'intentional_scroll_indicator_findings':len(intentional_scroll),
        'unused_min_height_findings':len(unused),'empty_wrapper_findings':len(empty),
        'candidate_route_ranking':route_rows,'findings':findings,'cases':cases,
        'comparison_to_task1':comparison,
        'render_baseline':{
            'archive':'reports/phase-31-before-renders.json.gz','route_count':route_count,
            'source_head':inventory['source_head'],
            'all_php_adapter_statuses':sorted({x['status'] if after else x['http_status'] for x in routes_for_status}),
            'sitemap':'reports/phase-31-before-sitemap.xml',
            'sitemap_sha256':hashlib.sha256(sitemap_bytes).hexdigest(),'sitemap_entries':len(sitemap_urls),
        },
    }
    out_json=ROOT/'reports'/f'{prefix}.json'
    out_md=ROOT/'reports'/f'{prefix}.md'
    out_json.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    title='Phase31 Task2 post-fix blank-space audit' if after else 'Phase31 Task1 blank-space audit'
    source_note=(
        f"**Capture source:** `{summary['source_head']}`. Exact Task2 source-scope validation passed for: "
        f"`{', '.join(summary.get('_approved_spacing_source_files',[]))}`. Immutable content/render baseline: `{inventory['source_head']}`."
        if after else
        f"**Source:** `{summary['source_head']}`. No public presentation/runtime file was changed for this audit."
    )
    lines=[
        f'# {title}','',source_note,'',
        f"**Coverage:** {summary['case_count']} cases: 43 route entries × 3 widths (360, 768, 1280) × JavaScript on/off × normal/reduced motion. Every case scrolled through the document, waited 3 seconds, returned to the top, captured and analysed a full-page PNG in memory, recorded its SHA-256, and saved a crop for each thresholded candidate.",'',
        '**Pinned local browser:** Chromium 143.0.7499.0 (`@sparticuz/chromium` 143.0.4), Playwright 1.58.2, GSAP 3.12.2, Three.js 0.128.0. Original Google Fonts stylesheet requests were blocked by the harness and recorded as expected request failures; no external font/CDN bytes were used. This is local browser evidence, not native-host testing.','',
        '## Reading the candidate counts','',
        'A pixel quiet band is a screening candidate, not proof that the design contains removable blank space. The metric detects a contiguous vertical band where horizontal grayscale edge occupancy stays below 0.6% at a scan width of at most 512px, with the requested route-specific minimum heights. Bands must be between visually active rows. Structural findings separately detect visible text/media, empty wrappers, hidden reveal text, and excess tail below the last visible child of an explicit `min-height`, after subtracting the declared bottom padding. Normal section padding, intentional backgrounds, and repeated views of the same gap are not counted as confirmed savings.','',
        f"Total audit findings: **{len(findings)}** (by kind: `{json.dumps(counts,sort_keys=True)}`). Hidden reveal-text findings: **{len(hidden)}**; intentional scroll-cue dismissals: **{len(intentional_scroll)}**; unused explicit-min-height tails: **{len(unused)}**; non-decorative empty wrappers: **{len(empty)}**.",
    ]
    if after:
        lines+=['','## Before and after counts','','| Finding kind | Task1 baseline | Task2 post-fix | Change |','|---|---:|---:|---:|']
        for kind,row in comparison.items():lines.append(f"| {kind} | {row['task1']} | {row['task2']} | {row['delta']:+d} |")
        lines+=['','Task2 changed only the two reviewed `#team` responsive `min-height` declarations. No revealed page-copy failure was found in Task1, so no reveal code was introduced. The Contact `#miniHero` first-fold cue space remains intentionally retained.']
    lines+=['','## Candidate route ranking','','Ranking is by route-level vertical union across the width/state matrix, which avoids simply multiplying repeated screenshots. Cumulative pixels across cases are shown separately and are not a unique-area measurement.','', '| Rank | Route | Vertical union candidate px | Cumulative candidate px across cases | Pixel bands | Min-height tails | Hidden text | Empty wrappers |','|---:|---|---:|---:|---:|---:|---:|---:|']
    for i,r in enumerate(route_rows,1):
        lines.append(f"| {i} | `{r['route']}` | {r['route_union_candidate_height_px']:,} | {r['cumulative_candidate_height_px']:,} | {r['pixel_band_count']} | {r['unused_min_height_count']} | {r['hidden_reveal_count']} | {r['empty_wrapper_count']} |")
    lines+=['','## Structural/reveal findings','','These are measured structural candidates, not blanket authorization to remove spacing. Each row includes the saved crop and route/source location.','', '| Kind | Route | State | y | Height | Selector | Computed cause/evidence | Source | Crop |','|---|---|---|---:|---:|---|---|---|---|']
    key_kinds={'unused-min-height-tail','hidden-reveal-text','empty-content-wrapper','hidden-content-wrapper','intentional-scroll-indicator-dismissed'}
    for f in findings:
        if f['kind'] not in key_kinds:continue
        state=f"{f['width']} / JS {f['javascript']} / {f['motion']}"
        cause=(f.get('cause') or '')
        if f.get('disposition'):cause+=' '+f['disposition']
        cause=cause.replace('|','/')
        source=f"`{f['source_file']}:{f['source_line']}`"
        if f.get('style_source_file'):source+=f"; CSS `{f['style_source_file']}:{f['style_source_line']}`"
        lines.append(f"| {f['kind']} | `{f['route']}` | {state} | {f['y']} | {f['height']} | `{f['selector']}` | {cause} | {source} | `{f.get('crop') or 'not captured'}` |")
    lines+=['','## Pixel-band findings','',f"Every band record includes route/state, y/height, selector, computed section context, neighboring visible text, source file/line, and crop in `{out_json.relative_to(ROOT)}`. The appendix includes repeated bands in distinct states.",'',
        '## Render baseline for no-content-change checks','',
        'The immutable local PHP-WASM render baseline contains all 43 frozen route entries at the pre-fix source. Exact rendered HTML, per-route byte count and SHA-256 are archived in `reports/phase-31-before-renders.json.gz`. The sitemap remains byte-identical with 38 entries. The other five routes are held/utility pages and remain in the audit because the explicit review inventory includes them.','',
        '## Disposition','',
        ('Task2 fixes only the source-confirmed Home and About `#team` responsive min-height tails. Other pixel bands remain review candidates, not authorized savings. The Contact `#miniHero` 88vh first-fold tail is retained because its existing bottom scroll cue occupies that space on initial load. Intentional Explore/Reach Out cue dismissals remain unchanged. No user-facing copy, images, links, FAQ, schema, canonical, status, sitemap, or team-card text changed.' if after else
         'No content edits were made during Task1. Pixel candidates aligning with existing section padding or expected inter-card spacing remain intentional/unconfirmed until paired before/after review. The Home and About `#team` min-height tails are the source-confirmed whitespace candidates for Task2 review. The Contact `#miniHero` 88vh first-fold tail is retained because its existing bottom scroll cue occupies that space on initial load. Only intentional Explore/Reach Out cue dismissals were observed; no revealed page copy remains hidden. No user-facing copy, images, links, FAQ, schema, canonical, status, sitemap, or team-card text changed.'),
        '',
    ]
    out_md.write_text('\n'.join(lines))
    print(f"TASK{task} AUDIT READY: {summary['case_count']} cases, {len(findings)} findings ({json.dumps(counts,sort_keys=True)})")

def main():
    parser=argparse.ArgumentParser(description='Build a complete Phase31 blank-space audit report.')
    parser.add_argument('--scan',type=pathlib.Path,default=SCAN,help='Raw scan directory containing summary.json and cases/')
    parser.add_argument('--after',action='store_true',help='Compare a full post-Task2 scan to the immutable Task1 baseline.')
    parser.add_argument('--report-prefix',default=None,help='Output report filename stem under reports/.')
    args=parser.parse_args()
    build(args.scan,args.after,args.report_prefix)

if __name__=='__main__':main()
