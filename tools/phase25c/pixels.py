"""Full-resolution RGB SSIM7x7; strips retain the convolution halo, no resizing."""
from pathlib import Path
import json,math
import numpy as np
from PIL import Image
from skimage.metrics import structural_similarity
R=Path(__file__).resolve().parents[2];P=Path('/home/user/phase25c-evidence/references')
def metrics(a,b,boxes):
 a=np.asarray(Image.open(a).convert('RGB'));b=np.asarray(Image.open(b).convert('RGB'));assert a.shape==b.shape
 h,w,_=a.shape;valid=np.ones((h,w),bool)
 for x,y,bw,bh in boxes:valid[max(0,math.floor(y)):min(h,math.ceil(y+bh)),max(0,math.floor(x)):min(w,math.ceil(x+bw))]=False
 d=np.abs(a.astype(np.int16)-b.astype(np.int16));mx=int(d[valid].max(initial=0));count=int(np.count_nonzero(np.any(d!=0,axis=2)&valid));total=0.;n=0
 for start in range(3,h-3,256):
  end=min(h-3,start+256);left=a[start-3:end+3];right=b[start-3:end+3]
  _,s=structural_similarity(left,right,channel_axis=2,data_range=255,win_size=7,full=True)
  good=valid[start:end,3:w-3].copy()
  # Exclude windows intersecting an approved card, not just their centre pixel.
  for x,y,bw,bh in boxes:
   ya=max(start,math.floor(y)-3);yb=min(end,math.ceil(y+bh)+3);xa=max(3,math.floor(x)-3);xb=min(w-3,math.ceil(x+bw)+3)
   if yb>ya and xb>xa:good[ya-start:yb-start,xa-3:xb-3]=False
  v=s[3:-3,3:-3].mean(axis=2);total+=float(v[good].sum());n+=int(good.sum())
 return {'max_delta':mx,'differing_pixels':count,'ssim':total/n,'outside_card_pixels':int(valid.sum())}
report=json.loads((R/'reports/phase-25c-reference-structure.json').read_text());rows=[]
for r in report['rows']:
 stem=f"{r['name']}-{r['width']}";noise=[]
 for k in range(3):noise.append(metrics(P/f'{stem}-a{k*2}.png',P/f'{stem}-a{k*2+1}.png',r['cardBoxes']))
 floor={'max_delta':max(x['max_delta'] for x in noise),'differing_pixels':max(x['differing_pixels'] for x in noise),'ssim':min(x['ssim'] for x in noise)}
 current=metrics(P/f'{stem}-a0.png',P/f'{stem}-b.png',r['cardBoxes']);back=current['max_delta']<=4 and current['ssim']>=.999;within=current['max_delta']<=floor['max_delta'] and current['differing_pixels']<=floor['differing_pixels'] and current['ssim']>=floor['ssim']
 passed=r['structural_pass'] and (back or within);reason='Structural difference' if not r['structural_pass'] else 'Structure exact; pixel backstop met' if back else 'Structure exact; rendering difference within measured noise floor' if within else 'Structure exact but pixel difference exceeds backstop and measured noise floor; unresolved'
 rows.append({**r,'noise_pairs':noise,'noise_floor':floor,'current_pixels':current,'pixel_backstop_pass':back,'within_noise_floor':within,'passed':passed,'reason':reason});print(stem,passed,reason,current,flush=True)
 (R/'reports/phase-25c-reference-gate.json').write_text(json.dumps({'structural_pass_criterion':True,'max_delta':4,'minimum_ssim':.999,'rows':rows,'passed':len(rows)==12 and all(x['passed'] for x in rows)},indent=2)+'\n')
