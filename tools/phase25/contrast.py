"""Conservative text/focus palette checks, including a white scene pixel behind gold."""
import json,pathlib
root=pathlib.Path(__file__).resolve().parents[2]
def rgb(h):return tuple(int(h[i:i+2],16)/255 for i in (1,3,5))
def lum(c):return sum(v*w for v,w in zip([x/12.92 if x<=.04045 else ((x+.055)/1.055)**2.4 for x in c],[.2126,.7152,.0722]))
def ratio(a,b):x,y=sorted([lum(a),lum(b)]);return (y+.05)/(x+.05)
scene=tuple(.15+.85*v for v in rgb('#0a1628'))
roles=[('body, captions, FAQ answers, category text','#4A5568','#F0F4FF'),('card prose','#4A5568','#FFFFFF'),('links/headings/focus on light','#1A2E5A','#F0F4FF'),('hover/focus light button','#FFFFFF','#1A2E5A'),('primary text/outline hover','#04060f','#C9A84C'),('dark prose/navigation','#C8D3E8','#04060f'),('footer muted text','#8A98B8','#04060f'),('dark focus/gold secondary text','#C9A84C','#04060f')]
rows=[{'role':name,'foreground':fg,'background':bg,'contrast':round(ratio(rgb(fg),rgb(bg)),3)} for name,fg,bg in roles]
rows+=[{'role':'hero gold label, worst possible WHITE scene pixel at opacity .15 over lightest hero stop (navy)','foreground':'#C9A84C','background_rgb':scene,'contrast':round(ratio(rgb('#C9A84C'),scene),3)}]
assert all(x['contrast']>=4.5 for x in rows),rows
(root/'reports/phase-25-contrast.json').write_text(json.dumps({'minimum_required':4.5,'all_states':'Explicit default/hover/focus/visited inheritance use these pairs; native link focus tested in Chromium. Whole-page axe separately recorded.','roles':rows},indent=2)+'\n')
print('PASS contrast >=4.5',min(x['contrast'] for x in rows))
