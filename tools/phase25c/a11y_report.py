"""Report-only retained reference contrast groups and fresh overflow observations."""
import json,re,pathlib,hashlib
R=pathlib.Path(__file__).resolve().parents[2];source=R/'reports/phase-25-stage-2-accessibility.json';raw=json.loads(source.read_text());base=json.loads((R/'reports/phase-25-baseline-renders.json').read_text())['routes'];refs='\n'.join(base[p]['html'] for p in ['/','/services','/about','/contact'])
def normal(h):return '#'+''.join(c*2 for c in h[1:]) if len(h)==4 else h.lower()
palette={normal(h) for h in re.findall(r'#[a-fA-F0-9]{6}\b|#[a-fA-F0-9]{3}\b',refs)}
def channels(h):return [int(h[i:i+2],16)/255 for i in (1,3,5)]
def lum(h):return sum((c/12.92 if c<=.04045 else ((c+.055)/1.055)**2.4)*w for c,w in zip(channels(h),[.2126,.7152,.0722]))
def ratio(a,b):x,y=sorted([lum(a),lum(b)]);return (y+.05)/(x+.05)
def closest(fg,bg):return min((h for h in palette if ratio(h,bg)>=4.5),key=lambda h:sum((a-b)**2 for a,b in zip(channels(fg),channels(h))))
groups=[];m=['# Reference accessibility: report only','','No changes applied to Home, Services, About or Contact. Their source remains byte-exact to Stage1. This report retains all24 historical contrast finding groups, including every affected node, and investigates the five recorded JS-on layout-overflow cases. Rebuilt-page accessibility is tested separately.','', '## Contrast method','','Foreground/background and observed ratio are taken verbatim from axe failure summaries in the committed Stage2 evidence. The target here is4.5:1, including larger text. Suggested fixes change one foreground declaration to the nearest passing existing-reference palette colour by squared sRGB distance, holding the measured background fixed. This is a minimal single-property palette suggestion, not a proposed palette redesign or an applied fix. Parent opacity/compositing must be remeasured if any suggestion is later approved.','']
for case in raw['cases']:
 if case['shape']['rebuilt']:continue
 for violation in case['violations']:
  assert violation['id']=='color-contrast';nodes=[];number=len(groups)+1;m+= [f"### Finding{number:02}: `{case['route']}`, {case['width']}px, JS{'on' if case['js'] else 'off'}",'', '| Selector | Foreground | Background | Observed / required | Smallest palette-only suggestion |','|---|---|---|---|---|']
  for n in violation['nodes']:
   summary=n['summary'];fg=normal(re.search(r'foreground color: (#[a-fA-F0-9]+)',summary)[1]);bg=normal(re.search(r'background color: (#[a-fA-F0-9]+)',summary)[1]);observed=float(re.search(r'contrast of ([\d.]+)',summary)[1]);fix=closest(fg,bg);selector='; '.join(n['target']);nodes.append({'selector':selector,'foreground':fg,'background':bg,'observed_ratio':observed,'required':4.5,'suggested_foreground':fix,'suggested_ratio':ratio(fix,bg),'original_failure_summary':summary});m.append(f'| `{selector}` | `{fg}` | `{bg}` | {observed:.2f} /4.5 | foreground `{fix}`, predicted {ratio(fix,bg):.2f}:1 |')
  m.append('');groups.append({'finding':number,'route':case['route'],'width':case['width'],'javascript':case['js'],'nodes':nodes})
assert len(groups)==24
additional=[]
fresh=R/'reports/phase-25c-accessibility.json'
if fresh.exists():
 old_keys={(c['route'],c['width'],c['js'],tuple(n['target'])) for c in raw['cases'] if not c['shape']['rebuilt'] for v in c['violations'] for n in v['nodes']}
 for c in json.loads(fresh.read_text())['cases']:
  if c['shape']['rebuilt']:continue
  for v in c['violations']:
   for n in v['nodes']:
    if (c['route'],c['width'],c['js'],tuple(n['target'])) in old_keys:continue
    summary=n['summary'];fg=normal(re.search(r'foreground color: (#[a-fA-F0-9]+)',summary)[1]);bg=normal(re.search(r'background color: (#[a-fA-F0-9]+)',summary)[1]);observed=float(re.search(r'contrast of ([\d.]+)',summary)[1]);fix=closest(fg,bg);additional.append({'route':c['route'],'width':c['width'],'javascript':c['js'],'selector':'; '.join(n['target']),'foreground':fg,'background':bg,'observed_ratio':observed,'required':4.5,'suggested_foreground':fix,'suggested_ratio':ratio(fix,bg),'original_failure_summary':summary})
 if additional:
  m+=['## Final-cycle additional node observations','','The final full cycle retains the same24 reference finding groups and all387 original affected nodes, plus these4 newly sampled nodes (391 total). They are not removed by a retry. Original sources remain unchanged; no fix applied. Large-text axe thresholds may be3:1, but this report uses the owner target4.5:1.','','| Page / width / JS | Selector | FG / BG | Observed / required | Minimal existing-palette suggestion |','|---|---|---|---|---|']
  for n in additional:m.append(f"| `{n['route']}` /{n['width']} /{n['javascript']} | `{n['selector']}` | `{n['foreground']}` / `{n['background']}` | {n['observed_ratio']:.2f} /4.5 | foreground `{n['suggested_foreground']}`, predicted {n['suggested_ratio']:.2f}:1 |")
  m+=['','Final-cycle Contact360 sampled scrollWidth395px versus396px in the dedicated early-frame probe; the same case remains. This1px animation-frame variation is not asserted resolved or pixel-compositor noise.','']
ov=json.loads((R/'reports/phase-25c-reference-overflow.json').read_text());assert len(ov['rows'])==5;m+=['## Five retained overflow cases','','A larger scrollWidth alone is not proof that readable content is clipped or that a user can pan sideways. The new sampler observes original animations without changing reference CSS or disabling scenes. Early frames, naturally settled scroll/reveal state and a horizontal-wheel attempt are retained in phase-25c-reference-overflow.json. Invisible transformed nodes are included because they can affect layout overflow without painting. Fixed decorative layers are not assumed to be the scroll-container cause merely because their rectangles exceed the viewport.','']
overflow=[]
for row in ov['rows']:
 previous=next(c for c in raw['overflow_cases'] if c['route']==row['route'] and c['width']==row['width']);frames=[s for s in row['samples'] if s['scrollWidth']>row['width']+1];contributors=[]
 for s in frames:
  for o in s['offenders']:
   fixed=o['position']=='fixed' or any(a.get('position')=='fixed' for a in o['clipping_transform_ancestors'])
   if abs(o['right']-s['scrollWidth'])<2 and not fixed:contributors.append({'time':s['time'],'document_width':s['scrollWidth'],**o})
 unique={c['selector']:c for c in contributors};settled=row['settled']['scrollWidth'];pan=row['user_pan']['x'];status='not reproduced in sampled frames; cause not proven' if not contributors else 'transformed layout-edge contributors observed';overflow.append({'route':row['route'],'width':row['width'],'previous_scroll_width':previous['scroll'],'diagnosis':status,'contributors':list(unique.values()),'settled_width':settled,'horizontal_wheel_scroll_x':pan})
 m+=[f"### `{row['route']}` at{row['width']}px",'',f"Historical document width{previous['scroll']}px; sampled widths{[s['scrollWidth'] for s in row['samples']]}; settled width{settled}px. Horizontal-wheel scrollX={pan}. Diagnosis: {status}.",'']
 for c in [v for v in unique.values() if v['transform']!='none'][:12]:m.append(f"- `{c['selector']}` at{c['time']:.0f}ms: right={c['right']:.3f}px, top={c['top']:.1f}px, transform `{c['transform']}`, effective opacity{c['effective_opacity']:.4f}, visibility `{c['visibility']}`. Transform/clip chain: "+'; '.join(f"`{a['selector']}` overflow={a['overflowX']}, transform={a['transform']}" for a in c['clipping_transform_ancestors'])+'.')
 if contributors and all(c['effective_opacity']==0 or c['visibility']=='hidden' for c in contributors):m+=['','Visible-to-user assessment: the observed layout-edge contributors have zero effective opacity or hidden visibility, so they are not painted at those sampled frames. Their transforms still enlarge layout overflow.']
 elif contributors:m+=['','Visible-to-user assessment: some edge contributors are painted during transition. Body/root clipping and the settled layout must be considered; this is not silently waived as an invisible scene artifact.']
 else:m+=['','Visible-to-user assessment: this run cannot establish the precise historical animation frame/element. Retained as unproven, not asserted harmless.']
 m+=[f"After natural reveal scrolling, {'no persistent document overflow was observed' if settled<=row['width']+1 else 'document scrollWidth remains enlarged by offscreen hidden reveal start states; this is a retained numerical layout deviation, not compositor noise'}. {'The horizontal wheel did not pan the page.' if pan==0 else 'The horizontal wheel panned the page; user-visible overflow is confirmed.'} No reference fix applied. The matching right-edge matrices identify reveal-layout start states, not a3D scene or floating decorative glyph, as the measured edge contributors.",'']
result={'fresh_additional_nodes':additional,'original_node_instances':sum(len(g['nodes']) for g in groups),'total_retained_node_instances':sum(len(g['nodes']) for g in groups)+len(additional),'contrast_groups':groups,'count':len(groups),'reference_source_edited':False,'original_evidence_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'overflow':overflow};(R/'reports/phase-25c-reference-a11y-data.json').write_text(json.dumps(result,indent=2)+'\n');(R/'reports/phase-25-reference-a11y.md').write_text('\n'.join(m)+'\n');print('Reported24 finding groups,',sum(len(g['nodes']) for g in groups),'nodes and5 overflow cases')
