"""Owner decision C. Never use these limits for content/schema comparisons."""
import json,pathlib,sys,math
from PIL import Image,ImageChops
ROOT=pathlib.Path(__file__).resolve().parents[3]
def compare(left,right,mask=None):
 a=Image.open(left).convert('RGB');b=Image.open(right).convert('RGB');assert a.size==b.size,(left,right,a.size,b.size)
 d=ImageChops.difference(a,b)
 if mask:d.paste((0,0,0),tuple(mask))
 n=sum(p!=(0,0,0) for p in d.get_flattened_data());mx=max(x[1] for x in d.getextrema());pct=n/(a.width*a.height)*100
 return {'changed_pixels':n,'page_pixels':a.width*a.height,'max_channel_delta':mx,'percent':pct,'bounds':d.getbbox(),'passed':mx<=2 and pct<=.01,'mask':mask}
if __name__=='__main__':
 left,right=map(pathlib.Path,sys.argv[1:3]);mode=sys.argv[3];rows=[]
 for name in ['home','services','about','contact']:
  for w in [360,768,1280]:
   mask=None
   if mode=='after' and name in ['home','about']:
    before=json.loads((left/'before-layout.json').read_text());after=json.loads((right/'after-layout.json').read_text());b=next(x for x in before if x['name']==name and x['width']==w);a=next(x for x in after if x['name']==name and x['width']==w);assert a['teamSection']==b['teamSection'];s=b['teamSection'];mask=[0,math.floor(s['y']),w,math.ceil(s['y']+s['height'])]
   rows.append(dict(name=name,width=w,**compare(left/f'before-{name}-{w}.png',right/f'{mode}-{name}-{w}.png',mask)))
 result={'owner_rule':{'max_channel_delta':2,'max_different_percent':.01},'comparison':mode,'passed':all(r['passed'] for r in rows),'rows':rows}
 p=ROOT/'reports'/('phase-25-stage-2-reference-raster.json' if mode=='after' else 'phase-25-stage-2-controlled-noise.json');p.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result));sys.exit(0 if result['passed'] else 1)
