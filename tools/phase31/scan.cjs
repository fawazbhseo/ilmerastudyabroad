#!/usr/bin/env node
// Phase31 43-route blank-space and reveal scan. Uses complete rendered pages and viewport-independent pixel bands.
const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto');
const sharp=require('sharp');
const {launchBrowser,routePinnedResources}=require('./browser.cjs');
const ROOT=path.resolve(__dirname,'../..');
const EVIDENCE=process.env.PHASE31_EVIDENCE||'/home/user/phase31';
const BASE=process.env.PHASE31_BASE_URL||'http://127.0.0.1:8080';
const args=process.argv.slice(2);const arg=(k,d)=>{const i=args.indexOf(k);return i<0?d:args[i+1]};
const OUT=arg('--out',path.join(EVIDENCE,'scan-before'));
const routeArg=arg('--routes','');const routeFilter=routeArg?new Set(routeArg.split(',').map(x=>x.trim())):null;
const widths=(arg('--widths','360,768,1280')).split(',').map(Number);
const caseLimit=Number(arg('--case-limit','0'))||Infinity;
const cropOn=arg('--crops','yes')!=='no';
const ROUTE_DATA=JSON.parse(fs.readFileSync(path.join(ROOT,'reports/phase-25-baseline-renders.json'),'utf8'));
const allRoutes=Object.keys(ROUTE_DATA.routes||{}).sort();
const routes=routeFilter?allRoutes.filter(r=>routeFilter.has(r)):allRoutes;
if(allRoutes.length!==43)throw new Error(`Expected frozen 43-route inventory; got ${allRoutes.length}`);
if(routeFilter&&routes.length!==routeFilter.size)throw new Error(`Unknown route in filter: ${[...routeFilter].filter(r=>!allRoutes.includes(r))}`);
fs.mkdirSync(OUT,{recursive:true});fs.mkdirSync(path.join(OUT,'cases'),{recursive:true});fs.mkdirSync(path.join(OUT,'crops'),{recursive:true});
sharp.cache({memory:128,files:16,items:32});
const motionStates=['normal','reduced'];const jsStates=['on','off'];
const thresholdByWidth={360:120,768:160,1280:200};
const slug=s=>s==='/'?'home':s.replace(/^\//,'').replace(/\/$/,'').replace(/[^a-zA-Z0-9._-]+/g,'_')||'home';
const selectorOf=e=>{if(!e)return'body';if(e.id)return'#'+e.id;const c=[...e.classList||[]].filter(x=>/^[a-zA-Z_-][\w-]*$/.test(x)).slice(0,3);return e.tagName.toLowerCase()+(c.length?'.'+c.join('.'):'');};
const caseKey=(route,width,js,motion)=>`${slug(route)}__${width}__js-${js}__motion-${motion}`;
async function analyzeScreenshot(buffer,width,route,key){
  const meta=await sharp(buffer).metadata();
  const targetWidth=Math.min(512,meta.width);
  const {data,info}=await sharp(buffer).resize({width:targetWidth,withoutEnlargement:true,fit:'inside'}).greyscale().raw().toBuffer({resolveWithObject:true});
  const rows=[];const edgeThreshold=18,quietRatio=0.006;
  for(let y=0;y<info.height;y++){
    let edges=0;
    const base=y*info.width;
    for(let x=1;x<info.width;x++)if(Math.abs(data[base+x]-data[base+x-1])>=edgeThreshold)edges++;
    rows.push({edges,ratio:edges/(info.width-1)});
  }
  const scaleY=meta.height/info.height;const limit=thresholdByWidth[width];const bands=[];
  let start=-1;
  for(let y=0;y<=rows.length;y++){
    const quiet=y<rows.length&&rows[y].ratio<quietRatio;
    if(quiet&&start<0)start=y;
    if(!quiet&&start>=0){
      const end=y-1;const top=Math.floor(start*scaleY),bottom=Math.min(meta.height,Math.ceil((end+1)*scaleY));const h=bottom-top;
      if(h>=limit){
        bands.push({kind:'pixel-quiet-band',y:top,height:h,threshold:limit,metric:'horizontal grayscale edge occupancy <0.6% at 512px-or-native scan width',mean_edge_ratio:Number((rows.slice(start,end+1).reduce((a,b)=>a+b.ratio,0)/(end-start+1)).toFixed(5)),crop:null});
      }
      start=-1;
    }
  }
  // A quiet field is a candidate only when it lies between visually active content bands.
  const activeRanges=[];let a=-1;
  for(let y=0;y<rows.length;y++){
    if(rows[y].ratio>=quietRatio){if(a<0)a=y;}
    else if(a>=0){if(y-a>=2)activeRanges.push([a,y-1]);a=-1;}
  }
  if(a>=0)activeRanges.push([a,rows.length-1]);
  const interior=bands.filter(b=>{
    const cy=(b.y+b.height/2)/scaleY;
    return activeRanges.some(r=>r[1]<cy)&&activeRanges.some(r=>r[0]>cy);
  });
  return {width:meta.width,height:meta.height,scan_width:info.width,scan_height:info.height,threshold:limit,raw_candidates:bands,interior_candidates:interior,scale_y:scaleY};
}
async function captureDOM(page,threshold){
  return page.evaluate(({threshold})=>{
    const isExcluded=e=>!!e.closest('header,nav,footer,script,style,noscript,[aria-hidden="true"],[hidden]');
    const stackVisible=e=>{let opacity=1,visible=true,reason=[];for(let n=e;n&&n.nodeType===1;n=n.parentElement){const s=getComputedStyle(n);opacity*=Number.isFinite(parseFloat(s.opacity))?parseFloat(s.opacity):1;if(s.display==='none'){visible=false;reason.push('display:none');}if(s.visibility==='hidden'||s.visibility==='collapse'){visible=false;reason.push('visibility:'+s.visibility);}if(s.contentVisibility==='hidden'){visible=false;reason.push('content-visibility:hidden');}}if(opacity<0.05){visible=false;reason.push('effective-opacity:'+opacity.toFixed(3));}return{visible,opacity,reason:[...new Set(reason)]};};
    const main=document.querySelector('main')||document.body;const mainRect=main.getBoundingClientRect();
    const selectorOf=e=>{if(e.id)return'#'+e.id;const cls=[...e.classList||[]].filter(x=>/^[a-zA-Z_-][\w-]*$/.test(x)).slice(0,3);return e.tagName.toLowerCase()+(cls.length?'.'+cls.join('.'):'');};
    const textNodes=[];const walker=document.createTreeWalker(main,NodeFilter.SHOW_TEXT);let n;
    while((n=walker.nextNode())){const text=(n.nodeValue||'').replace(/\s+/g,' ').trim();if(!text)continue;const p=n.parentElement;if(!p||isExcluded(p))continue;const vis=stackVisible(p);let r;try{const range=document.createRange();range.selectNodeContents(n);r=range.getBoundingClientRect();}catch{}if(!r||r.width<0.5||r.height<0.5)continue;textNodes.push({parent:p,text:text.slice(0,160),length:text.length,visible:vis.visible,opacity:vis.opacity,reason:vis.reason,selector:selectorOf(p),y:Math.round(r.top+scrollY),height:Math.round(r.height)});}
    const all=[...main.querySelectorAll('*')];const structural=all.filter(e=>/^(SECTION|ARTICLE|ASIDE|DIV|UL|OL)$/.test(e.tagName));
    const nodes=[];
    for(const e of structural){
      if(isExcluded(e))continue;
      const r=e.getBoundingClientRect(),y=Math.round(r.top+scrollY),h=Math.round(r.height);
      if(h<threshold)continue;
      const subtreeText=textNodes.filter(t=>e.contains(t.parent)),ownText=subtreeText.filter(t=>t.visible),allText=subtreeText;
      const mediaEls=[...e.querySelectorAll('img,svg,canvas,video,iframe,picture,[role="img"]')].filter(x=>{const b=x.getBoundingClientRect(),v=stackVisible(x);return v.visible&&b.width>2&&b.height>2&&!x.closest('[aria-hidden="true"]')});
      const mediaBoxes=mediaEls.map(x=>{const b=x.getBoundingClientRect();return{top:b.top+scrollY,bottom:b.bottom+scrollY};});
      const hasVisible=ownText.length>0||mediaEls.length>0,hasHidden=allText.some(t=>!t.visible),st=getComputedStyle(e);
      const pb=parseFloat(st.paddingBottom)||0,minH=st.minHeight==='none'||st.minHeight==='auto'?0:(parseFloat(st.minHeight)||0);
      if(!hasVisible&&h>=threshold&&st.position!=='absolute'&&st.position!=='fixed'&&!/\b(?:beam|glow|overlay|backdrop|decoration|shape|particle|scene)\b/i.test(e.className||'')){
        nodes.push({kind:hasHidden?'hidden-content-wrapper':'empty-content-wrapper',selector:selectorOf(e),tag:e.tagName.toLowerCase(),y,height:h,threshold,visible_text_chars:0,hidden_text_chars:allText.filter(t=>!t.visible).reduce((a,t)=>a+t.length,0),visible_media:mediaEls.length,computed:{display:st.display,visibility:st.visibility,opacity:st.opacity,min_height:st.minHeight,height:st.height,padding_top:st.paddingTop,padding_bottom:st.paddingBottom,margin_top:st.marginTop,margin_bottom:st.marginBottom,position:st.position},crop:null});
      }
      if(hasVisible&&minH>=threshold){
        const contentBottom=Math.max(...ownText.map(t=>t.y+t.height),...mediaBoxes.map(b=>b.bottom));
        const unused=Math.floor(y+h-pb-contentBottom);
        if(unused>=threshold)nodes.push({kind:'unused-min-height-tail',selector:selectorOf(e),tag:e.tagName.toLowerCase(),y:Math.round(contentBottom),height:unused,threshold,visible_text_chars:ownText.reduce((a,t)=>a+t.length,0),hidden_text_chars:allText.filter(t=>!t.visible).reduce((a,t)=>a+t.length,0),visible_media:mediaEls.length,computed:{display:st.display,visibility:st.visibility,opacity:st.opacity,min_height:st.minHeight,height:st.height,padding_top:st.paddingTop,padding_bottom:st.paddingBottom,position:st.position},crop:null});
      }
    }
    const hiddenRaw=textNodes.filter(t=>!t.visible&&t.length>0),hiddenGroups=new Map();
    for(const t of hiddenRaw){const k=t.selector+'@'+Math.floor(t.y/220);let g=hiddenGroups.get(k);if(!g){g={kind:'hidden-reveal-text',selector:t.selector,y:t.y,height:t.height,text_sample:t.text.slice(0,90),characters:0,computed:{effective_opacity:t.opacity,visibility_reasons:t.reason},crop:null};hiddenGroups.set(k,g);}g.characters+=t.length;g.y=Math.min(g.y,t.y);g.height=Math.max(g.height,t.height);}
    const hidden=[...hiddenGroups.values()];
    const visible=textNodes.filter(t=>t.visible);const media=[...main.querySelectorAll('img,svg,canvas,video,iframe,picture,[role="img"]')].filter(x=>{const b=x.getBoundingClientRect();const v=stackVisible(x);return v.visible&&b.width>2&&b.height>2&&!x.closest('[aria-hidden="true"]')}).length;
    return{page_height:Math.max(document.documentElement.scrollHeight,document.body.scrollHeight),main:{selector:selectorOf(main),y:Math.round(mainRect.top+scrollY),height:Math.round(mainRect.height)},visible_text_chars:visible.reduce((a,t)=>a+t.length,0),visible_text_nodes:visible.length,hidden_text_nodes:hiddenRaw.length,hidden_text_groups:hidden.length,hidden_text_chars:hidden.reduce((a,t)=>a+t.characters,0),visible_media:media,empty_or_spacing_nodes:nodes,hidden_text:hidden.slice(0,300),text_samples:visible.slice(0,24).map(t=>({selector:t.selector,y:t.y,text:t.text.slice(0,60)}))};
  },{threshold});
}
async function locateBands(page,bands){
  if(!bands.length)return [];
  return page.evaluate((bands)=>{
    const main=document.querySelector('main')||document.body;
    const selectorOf=e=>{if(e.id)return'#'+e.id;const c=[...e.classList||[]].filter(x=>/^[a-zA-Z_-][\w-]*$/.test(x)).slice(0,3);return e.tagName.toLowerCase()+(c.length?'.'+c.join('.'):'');};
    const visible=e=>{let o=1;for(let n=e;n&&n.nodeType===1;n=n.parentElement){const s=getComputedStyle(n);if(s.display==='none'||s.visibility==='hidden'||s.contentVisibility==='hidden')return false;o*=parseFloat(s.opacity)||0;}return o>=.05;};
    const texts=[];const w=document.createTreeWalker(main,NodeFilter.SHOW_TEXT);let n;
    while((n=w.nextNode())){const text=(n.nodeValue||'').replace(/\s+/g,' ').trim(),p=n.parentElement;if(!text||!p||p.closest('header,nav,footer,[aria-hidden="true"],[hidden]')||!visible(p))continue;const r=document.createRange();r.selectNodeContents(n);const b=r.getBoundingClientRect();if(b.width>0&&b.height>0)texts.push({y:b.top+scrollY,bottom:b.bottom+scrollY,selector:selectorOf(p),text:text.slice(0,90)});}
    const structures=[...main.querySelectorAll('section,article,aside,[id],.container')];
    return bands.map(g=>{
      const top=g.y,bot=g.y+g.height,mid=top+g.height/2;
      const candidates=structures.map(e=>{const r=e.getBoundingClientRect();return{e,top:r.top+scrollY,bottom:r.bottom+scrollY,height:r.height};}).filter(x=>x.top<=mid&&x.bottom>=mid).sort((a,b)=>a.height-b.height);
      const node=candidates[0]?.e,style=node?getComputedStyle(node):null;
      const prev=texts.filter(t=>t.bottom<=top).sort((a,b)=>b.bottom-a.bottom)[0]||null;
      const next=texts.filter(t=>t.y>=bot).sort((a,b)=>a.y-b.y)[0]||null;
      return{selector:node?selectorOf(node):selectorOf(main),element_tag:node?.tagName.toLowerCase()||'main',element_y:candidates[0]?Math.round(candidates[0].top):0,element_height:candidates[0]?Math.round(candidates[0].height):0,computed:style?{min_height:style.minHeight,height:style.height,padding_top:style.paddingTop,padding_bottom:style.paddingBottom,margin_top:style.marginTop,margin_bottom:style.marginBottom,position:style.position}:null,previous_visible_text:prev?{selector:prev.selector,y:Math.round(prev.y),text:prev.text}:null,next_visible_text:next?{selector:next.selector,y:Math.round(next.y),text:next.text}:null};
    });
  },bands);
}
async function makeCrop(buffer,box,file){
  const meta=await sharp(buffer).metadata();let top=Math.max(0,Math.floor(box.y-45));let height=Math.max(220,Math.min(580,Math.ceil(box.height+90)));if(top+height>meta.height)top=Math.max(0,meta.height-height);height=Math.min(height,meta.height-top);
  fs.mkdirSync(path.dirname(file),{recursive:true});
  await sharp(buffer).extract({left:0,top,width:meta.width,height}).webp({quality:68,effort:3}).toFile(file);
}
async function scrollSlow(page,jsEnabled){
  const height=await page.evaluate(()=>Math.max(document.documentElement.scrollHeight,document.body.scrollHeight));
  const viewport=await page.evaluate(()=>innerHeight);const step=Math.max(500,Math.round(viewport*.68));let samples=0;
  const width=await page.evaluate(()=>innerWidth);await page.mouse.move(Math.floor(width/2),Math.floor(viewport/2));
  for(let y=0;y<height;y+=step){await page.mouse.wheel(0,Math.min(step,height-y));await page.waitForTimeout(60);samples++;}
  await page.waitForTimeout(3000);
  // Wheel-based return works with JS disabled and preserves the final loaded visual state.
  await page.mouse.wheel(0,-(height+viewport));await page.waitForTimeout(150);
  if((await page.evaluate(()=>window.scrollY))>2){
    await page.evaluate(()=>{document.documentElement.style.scrollBehavior='auto';document.body.style.scrollBehavior='auto';window.scrollTo(0,0);});
    await page.waitForFunction(()=>window.scrollY<=2,{timeout:5000});
  }
  return{height,scroll_samples:samples,settle_ms:3000,returned_to_top:(await page.evaluate(()=>window.scrollY))<=2,final_scroll_y:await page.evaluate(()=>Math.round(window.scrollY))};
}
async function run(){
  if(routes.length===0)throw new Error('No routes selected');
  const browser=await launchBrowser();const cases=[];let done=0;const contexts={};
  for(const js of jsStates)contexts[js]=await browser.newContext({viewport:{width:360,height:900},deviceScaleFactor:1,isMobile:false,hasTouch:false,javaScriptEnabled:js==='on',reducedMotion:'no-preference'});
  try{
    for(const route of routes){for(const width of widths){for(const js of jsStates){for(const motion of motionStates){
      const context=contexts[js];
      if(done>=caseLimit)break;
      const key=caseKey(route,width,js,motion);const file=path.join(OUT,'cases',key+'.json');
      if(fs.existsSync(file))throw new Error(`Refusing to resume existing case: ${file}`);
      const page=await context.newPage();await page.setViewportSize({width,height:900});await page.emulateMedia({reducedMotion:motion==='reduced'?'reduce':'no-preference'});await routePinnedResources(page);const failed=[];page.on('requestfailed',r=>failed.push({url:r.url(),error:r.failure()?.errorText||''}));
      const url=BASE+(route==='/'?'/':route);
      const response=await page.goto(url,{waitUntil:'domcontentloaded',timeout:45000});
      await page.waitForTimeout(700);
      const scroll=await scrollSlow(page,js==='on');
      const dom=await captureDOM(page,thresholdByWidth[width]);
      const pinned=js==='on'?await page.evaluate(()=>({gsap:!!window.gsap,scrollTrigger:!!window.ScrollTrigger,three:!!window.THREE})):null;
      let shot;try{shot=await page.screenshot({fullPage:true,type:'png',timeout:90000,animations:'allow'});}catch(e){await page.close();throw new Error(`Full-page screenshot failed ${key}: ${e.message}`);}
      const pixels=await analyzeScreenshot(shot,width,route,key);const bandContexts=await locateBands(page,pixels.interior_candidates);pixels.interior_candidates.forEach((b,i)=>{b.context=bandContexts[i];b.selector=bandContexts[i]?.selector||'main';b.cause=`Low edge-density band; nearest section ${b.selector} has ${bandContexts[i]?.computed?.padding_top||'unknown'} top and ${bandContexts[i]?.computed?.padding_bottom||'unknown'} bottom padding. Compare neighboring visible blocks and source before classifying as unused space.`;});const cropDir=path.join(ROOT,'reports/screenshots/phase-31');
      let cropN=0;
      if(cropOn){for(const b of pixels.interior_candidates){const cp=path.join(cropDir,key+'-gap-'+String(++cropN).padStart(2,'0')+'.webp');await makeCrop(shot,b,cp);b.crop=path.relative(ROOT,cp);b.kind='pixel-quiet-band';}}
      if(cropOn){for(const b of dom.empty_or_spacing_nodes){const cp=path.join(cropDir,key+'-dom-'+String(++cropN).padStart(2,'0')+'.webp');await makeCrop(shot,b,cp);b.crop=path.relative(ROOT,cp);b.cause=b.kind==='empty-content-wrapper'?'Structural node exceeds the per-width height threshold with no visible text or media descendants.':'Computed vertical margin/padding reaches the per-width threshold; candidate, not automatically an error.';}}
      if(cropOn){for(const b of dom.hidden_text){const cp=path.join(cropDir,key+'-hidden-'+String(++cropN).padStart(2,'0')+'.webp');await makeCrop(shot,b,cp);b.crop=path.relative(ROOT,cp);b.cause='Non-empty main-content text remains effectively invisible after a complete slow scroll and 3-second settle.';}}
      const result={id:key,route,width,viewport_height:900,javascript:js,motion,requested_url:url,http_status:response?.status()??null,page_height:dom.page_height,scroll,dom,pixel_scan:pixels,pinned,request_failures:failed,scan_conditions:{browser:browser.version(),browser_package:'@sparticuz/chromium 143.0.4',playwright:'1.58.2',gsap:'3.12.2',axe:'4.11.0',wait_after_scroll_ms:3000,full_page_png_sha256:crypto.createHash('sha256').update(shot).digest('hex')}};
      fs.writeFileSync(file,JSON.stringify(result,null,2)+'\n');cases.push({id:key,file:path.relative(OUT,file),route,width,javascript:js,motion,page_height:dom.page_height,scroll_samples:scroll.scroll_samples,hidden_text_nodes:dom.hidden_text_nodes,empty_spacing_nodes:dom.empty_or_spacing_nodes.length,pixel_candidates:pixels.interior_candidates.length,http_status:response?.status()??null,pinned});
      await page.close();done++;console.log(`CASE ${done} ${key} h=${dom.page_height} px=${pixels.interior_candidates.length} dom=${dom.empty_or_spacing_nodes.length} hidden=${dom.hidden_text_nodes}`);
    }}}}
  }finally{await browser.close();}
  const summary={generated_at:new Date().toISOString(),source_head:require('node:child_process').execFileSync('git',['rev-parse','HEAD'],{cwd:ROOT,encoding:'utf8'}).trim(),complete:done===routes.length*widths.length*jsStates.length*motionStates.length,case_count:done,expected_case_count:routes.length*widths.length*jsStates.length*motionStates.length,routes,widths,javascript:jsStates,motion:motionStates,cases};
  fs.writeFileSync(path.join(OUT,'summary.json'),JSON.stringify(summary,null,2)+'\n');
  if(summary.complete)console.log(`SCAN COMPLETE ${done}/${summary.expected_case_count}`);else console.log(`SCAN PARTIAL ${done}/${summary.expected_case_count}`);
}
run().catch(e=>{console.error(e.stack||e);process.exit(1);});
