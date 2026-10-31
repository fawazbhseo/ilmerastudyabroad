"""Strict decoded-pixel reference parity. No tolerance/colour threshold."""
import json,math,pathlib
from PIL import Image,ImageChops
root=pathlib.Path(__file__).resolve().parents[2];out=root/'reports/screenshots/phase-25';b=json.loads((root/'reports/phase-25-before-layout.json').read_text());a=json.loads((root/'reports/phase-25-after-layout.json').read_text());rows=[]
for name in ['home','services','about','contact']:
 for width in [360,768,1280]:
  before=next(e for e in b if e['name']==name and e['width']==width);after=next(e for e in a if e['name']==name and e['width']==width)
  x=Image.open(out/f'before-{name}-{width}.png').convert('RGB');y=Image.open(out/f'after-{name}-{width}.png').convert('RGB');assert x.size==y.size,(name,width,'reference height changed',x.size,y.size)
  diff=ImageChops.difference(x,y);mask=None
  if name in ['home','about']:
   assert before['teamSection']==after['teamSection'],(name,width,'team footprint changed')
   r=before['teamSection'];mask=[0,math.floor(r['y']),width,math.ceil(r['y']+r['height'])];diff.paste((0,0,0),tuple(mask))
  bbox=diff.getbbox();rows.append({'reference':name,'width':width,'changed_pixels_outside_team':sum(1 for p in diff.get_flattened_data() if p!=(0,0,0)),'difference_bounds':bbox,'only_allowed_mask':mask})
result={'tolerance':0,'viewports':[360,768,1280],'passed':all(r['difference_bounds'] is None for r in rows),'comparisons':rows,'scope':'Required zero-tolerance comparison: all Services/Contact pixels; all Home/About pixels outside the measured unchanged original team-section footprint. Result is reported by passed/comparisons, not assumed by this scope description.'}
(root/'reports/phase-25-reference-pixels.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result));assert result['passed'],'Reference pixel change outside allowed team section'
