"""Exact team-only CSS generated from audited reference section footprints."""
import json

def styles(root,file):
 data=json.loads((root/'reports/phase-25-team-footprints.json').read_text());assert data['source_commit']=='164d6de41159385e151ecefec54763eab59141a5'
 name='home' if file=='index.php' else 'about';v=data['pages'][name]['baseline_heights'];assert set(v)=={'360','768','1280'} and all(0<x<10000 for x in v.values())
 h=lambda w:format(v[str(w)],'.8f').rstrip('0').rstrip('.')
 css='#team{min-height:'+h(1280)+'px;}'
 if name=='home':
  slope=(v['360']-v['768'])/(768-360)*100;intercept=v['360']+slope*3.6
  css+='@media(max-width:768px){#team{min-height:clamp('+h(768)+'px,calc('+format(intercept,'.8f').rstrip('0').rstrip('.')+'px - '+format(slope,'.8f').rstrip('0').rstrip('.')+'vw),'+h(360)+'px);padding-bottom:79.5px!important;}}'
 else:
  css+='@media(min-width:701px) and (max-width:1024px){#team{min-height:'+h(768)+'px;}}@media(max-width:600px){#team{min-height:'+h(360)+'px;}}'
 return ('/* Phase 25 team footprint */'+css+'/* End Phase 25 team footprint */').encode()
