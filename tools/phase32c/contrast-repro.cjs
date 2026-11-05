#!/usr/bin/env node
// Capture user-visible contrast, backdrop pixels and crops for the four reference nodes.
const fs=require('node:fs');
const path=require('node:path');
const {PNG}=require('pngjs');
const BASE=process.env.PHASE32C_BASE_URL||'http://127.0.0.1:8094';
process.env.PHASE31_BASE_URL=BASE;
const {launchBrowser,routePinnedResources}=require('../phase31/browser.cjs');
const SOURCE=process.env.PHASE32C_SOURCE||'f9c96ca';
const OUT=process.env.PHASE32C_OUT||path.resolve(__dirname,'../../reports/phase-32c-contrast-'+SOURCE+'.json');
const SHOTS=process.env.PHASE32C_SHOTS||path.resolve(__dirname,'../../reports/screenshots/phase-32c/'+SOURCE);
const WIDTHS=[360,768,1280];
const STATES=[
  {name:'touch-coarse-scene-not-started',finePointer:false,hasTouch:true},
  {name:'fine-pointer-scene-eligible',finePointer:true,hasTouch:false},
  {name:'reduced-motion',finePointer:true,hasTouch:false,reducedMotion:'reduce'},
  {name:'javascript-off',finePointer:false,hasTouch:false,javascriptEnabled:false},
];
const ROUTES=[
  {name:'home',path:'/',elements:[{id:'home-em',axeSelector:'em',selector:'em'}]},
  {name:'about',path:'/about',elements:[
    {id:'about-faq-h2',axeSelector:'#faq-h2',selector:'#faq-h2'},
    {id:'about-team-label',axeSelector:'#team > .container > .team-hdr > .sec-label',selector:'#team > .container > .team-hdr > .sec-label'},
    {id:'about-kodagu-label',axeSelector:'.container > .sec-label',selector:'#kodagu > .container > .sec-label'},
  ]},
];
const sleep=ms=>new Promise(resolve=>setTimeout(resolve,ms));
const slug=s=>s.replace(/[^A-Za-z0-9_-]+/g,'_').replace(/^_|_$/g,'');
function colorChannels(value){
  const match=String(value).match(/rgba?\(\s*([\d.]+)[, ]+\s*([\d.]+)[, ]+\s*([\d.]+)(?:\s*[,/]\s*([\d.]+))?\s*\)/i);
  return match?{r:+match[1],g:+match[2],b:+match[3],a:match[4]===undefined?1:+match[4]}:null;
}
function hex({r,g,b}){return '#'+[r,g,b].map(v=>Math.round(v).toString(16).padStart(2,'0')).join('').toUpperCase();}
function linear(v){v/=255;return v<=0.04045?v/12.92:((v+0.055)/1.055)**2.4;}
function luminance(c){return .2126*linear(c.r)+.7152*linear(c.g)+.0722*linear(c.b);}
function contrast(a,b){const x=luminance(a),y=luminance(b);return (Math.max(x,y)+.05)/(Math.min(x,y)+.05);}
function quantile(values,q){const a=[...values].sort((x,y)=>x-y);if(!a.length)return null;const i=(a.length-1)*q,lo=Math.floor(i),hi=Math.ceil(i);return a[lo]+(a[hi]-a[lo])*(i-lo);}
function pixel(png,x,y){const px=Math.max(0,Math.min(png.width-1,Math.round(x))),py=Math.max(0,Math.min(png.height-1,Math.round(y))),i=(py*png.width+px)*4;return {r:png.data[i],g:png.data[i+1],b:png.data[i+2],a:png.data[i+3]};}
function writeCrop(png,clip,file){
  const x=Math.max(0,Math.floor(clip.x)),y=Math.max(0,Math.floor(clip.y));
  const width=Math.max(1,Math.min(png.width-x,Math.ceil(clip.width))),height=Math.max(1,Math.min(png.height-y,Math.ceil(clip.height)));
  const crop=new PNG({width,height});PNG.bitblt(png,crop,x,y,width,height,0,0);
  fs.mkdirSync(path.dirname(file),{recursive:true});fs.writeFileSync(file,PNG.sync.write(crop));
  return {x,y,width,height};
}
async function preparePage(page,state,width,errors,requests){
  await page.emulateMedia({reducedMotion:state.reducedMotion||'no-preference'});
  if(state.javascriptEnabled!==false){
    await page.addInitScript(({finePointer})=>{
      window.__phase32cSceneScripts=[];window.__phase32cSceneCalls=0;
      let original=null;
      Object.defineProperty(window,'__ILMERA_SCENE_INIT',{configurable:true,get:()=>original,set:fn=>{
        if(typeof fn!=='function'){original=fn;return;}
        original=function(){window.__phase32cSceneCalls++;return fn.apply(this,arguments);};
      }});
      const native=window.matchMedia.bind(window);
      window.matchMedia=function(query){
        if(query==='(pointer: fine)'||query==='(pointer:fine)')return {matches:finePointer,media:query,onchange:null,addListener(){},removeListener(){},addEventListener(){},removeEventListener(){},dispatchEvent(){return false}};
        if(query==='(pointer: coarse)'||query==='(pointer:coarse)')return {matches:!finePointer,media:query,onchange:null,addListener(){},removeListener(){},addEventListener(){},removeEventListener(){},dispatchEvent(){return false}};
        return native(query);
      };
      document.addEventListener('DOMContentLoaded',()=>{
        const append=Node.prototype.appendChild;
        Node.prototype.appendChild=function(node){
          if(this===document.head&&node&&node.tagName==='SCRIPT'&&/cdnjs\.cloudflare\.com/.test(node.src))window.__phase32cSceneScripts.push({src:node.src,at:performance.now()});
          return append.call(this,node);
        };
      },{once:true});
    },{finePointer:state.finePointer});
  }
  await routePinnedResources(page);
  page.on('pageerror',e=>errors.push({type:'pageerror',text:String(e)}));
  page.on('console',m=>{if(m.type()==='error')errors.push({type:'console',text:m.text()});});
  page.on('request',r=>{
    const url=r.url();
    if(/(?:three\.min\.js|gsap\.min\.js|ScrollTrigger\.min\.js|hero-still-\d+\.webp|\.glb(?:\?|$)|\.gltf(?:\?|$))/.test(url))requests.push({type:'request',url});
  });
  page.on('requestfailed',r=>{
    const url=r.url();
    if(/(?:three\.min\.js|gsap\.min\.js|ScrollTrigger\.min\.js|hero-still-\d+\.webp|\.glb(?:\?|$)|\.gltf(?:\?|$))/.test(url))requests.push({type:'failed',url,error:r.failure()?.errorText||null});
  });
}
async function caseOnce(route,width,state,attempt){
  const errors=[],requests=[];let browser,context,page;
  try{
    browser=await launchBrowser();
    context=await browser.newContext({viewport:{width,height:900},deviceScaleFactor:1,isMobile:!!state.hasTouch&&width<=768,hasTouch:!!state.hasTouch,javaScriptEnabled:state.javascriptEnabled!==false,reducedMotion:state.reducedMotion||'no-preference'});
    page=await context.newPage();await preparePage(page,state,width,errors,requests);
    const response=await page.goto(BASE+route.path,{waitUntil:'load',timeout:45000});
    if(!response||response.status()!==200)throw new Error(`HTTP ${response?.status()||'none'} on ${route.path}`);
    const expectedScene=state.javascriptEnabled!==false&&state.finePointer&&state.reducedMotion!=='reduce'&&width>=900;
    if(expectedScene){
      await page.waitForFunction(()=>window.__phase32cSceneCalls===1,null,{timeout:20000});
      await sleep(1200);
    }
    // Use real input scrolling so the same reveal triggers run when page JS is disabled.
    for(let step=0;step<40;step++){await page.mouse.wheel(0,800);await sleep(25);}
    await page.keyboard.press('End');
    await sleep(3000);
    const pageState=await page.evaluate(({expectedScene})=>{
      const ids=['space-canvas','vignette','nebula-t','nebula-b','gold-glow-css','grain','float-layer'];
      const layers=ids.map(id=>{const e=document.getElementById(id);if(!e)return {id,present:false};const c=getComputedStyle(e),r=e.getBoundingClientRect();return {id,present:true,display:c.display,visibility:c.visibility,opacity:c.opacity,backgroundColor:c.backgroundColor,backgroundImage:c.backgroundImage,zIndex:c.zIndex,rect:{x:r.x,y:r.y,width:r.width,height:r.height}};});
      const canvas=document.getElementById('space-canvas'),r=canvas?.getBoundingClientRect();
      return {expectedScene,sceneCalls:window.__phase32cSceneCalls||0,sceneScripts:window.__phase32cSceneScripts||[],rootClasses:document.documentElement.className,canvasPresent:!!canvas,canvasVisibility:canvas?getComputedStyle(canvas).visibility:null,canvasRect:r?{x:r.x,y:r.y,width:r.width,height:r.height}:null,layers,scrollHeight:document.documentElement.scrollHeight,scrollY};
    },{expectedScene});
    const elementResults=[];
    for(const spec of route.elements){
      const count=await page.locator(spec.selector).count();
      if(count!==1)throw new Error(`${spec.id}: expected one matching element for ${spec.selector}, got ${count}`);
      await page.locator(spec.selector).evaluate(e=>e.scrollIntoView({block:'center',inline:'nearest',behavior:'instant'}));
      await sleep(1050);
      const info=await page.evaluate(selector=>{
        const e=document.querySelector(selector);const cs=getComputedStyle(e),r=e.getBoundingClientRect(),range=document.createRange();range.selectNodeContents(e);
        const textRects=[...range.getClientRects()].map(x=>({x:x.x,y:x.y,left:x.left,top:x.top,right:x.right,bottom:x.bottom,width:x.width,height:x.height}));
        const ancestry=[];for(let n=e;n&&ancestry.length<10;n=n.parentElement){const c=getComputedStyle(n);ancestry.push({tag:n.tagName,id:n.id,className:typeof n.className==='string'?n.className:'',backgroundColor:c.backgroundColor,backgroundImage:c.backgroundImage,opacity:c.opacity,position:c.position,zIndex:c.zIndex});}
        const opacity=ancestry.reduce((v,n)=>{const value=Number(n.opacity);return v*(Number.isFinite(value)?value:1);},1);
        return {text:e.innerText||e.textContent,foreground:cs.color,fontSize:cs.fontSize,fontWeight:cs.fontWeight,elementOpacity:cs.opacity,ancestorOpacityProduct:opacity,backgroundColor:cs.backgroundColor,backgroundImage:cs.backgroundImage,visibility:cs.visibility,display:cs.display,rect:{x:r.x,y:r.y,left:r.left,top:r.top,right:r.right,bottom:r.bottom,width:r.width,height:r.height},textRects,ancestry};
      },spec.selector);
      if(!info.textRects.length)throw new Error(`${spec.id}: no visible text range`);
      const full=PNG.sync.read(await page.screenshot({type:'png'}));
      const fr=info.textRects;
      const left=Math.min(...fr.map(x=>x.left)),right=Math.max(...fr.map(x=>x.right)),top=Math.min(...fr.map(x=>x.top)),bottom=Math.max(...fr.map(x=>x.bottom));
      const clip={x:Math.max(0,left-26),y:Math.max(0,top-22),width:Math.min(width-Math.max(0,left-26),right-left+52),height:Math.min(900-Math.max(0,top-22),bottom-top+44)};
      const shotFile=path.join(SHOTS,route.name,`${state.name}-w${width}`,`${spec.id}.png`);
      const crop=writeCrop(full,clip,shotFile);
      const fore=colorChannels(info.foreground);if(!fore)throw new Error(`${spec.id}: unsupported computed color ${info.foreground}`);
      const candidatePoints=[];
      for(const line of fr){
        const ym=line.top+line.height/2;
        if(line.right+4<full.width)candidatePoints.push({x:line.right+4,y:ym,side:'right'});
        else if(line.left-4>=0)candidatePoints.push({x:line.left-4,y:ym,side:'left'});
        else candidatePoints.push({x:(line.left+line.right)/2,y:line.bottom+3,side:'below'});
      }
      const samples=[];for(const p of candidatePoints){if(p.x<0||p.y<0||p.x>=full.width||p.y>=full.height)continue;const bg=pixel(full,p.x,p.y);const alpha=fore.a*(info.ancestorOpacityProduct||1);const effectiveFg={r:fore.r*alpha+bg.r*(1-alpha),g:fore.g*alpha+bg.g*(1-alpha),b:fore.b*alpha+bg.b*(1-alpha)};samples.push({point:{x:Math.round(p.x),y:Math.round(p.y),side:p.side},backdrop:hex(bg),effectiveForeground:hex(effectiveFg),contrast:Number(contrast(effectiveFg,bg).toFixed(3))});}
      const ratios=samples.map(s=>s.contrast).sort((a,b)=>a-b),backgrounds=[...new Set(samples.map(s=>s.backdrop))];
      elementResults.push({id:spec.id,axeSelector:spec.axeSelector,selector:spec.selector,...info,effectiveBackdropSamples:samples,uniqueSampledBackdropColors:backgrounds,minimumSampledContrast:ratios[0]??null,medianSampledContrast:quantile(ratios,.5),screenshot:shotFile.replace(path.resolve(__dirname,'../..')+path.sep,'')});
    }
    return {source:SOURCE,route:route.path,template:route.name,width,state:state.name,device:{hasTouch:!!state.hasTouch,finePointer:state.finePointer,reducedMotion:state.reducedMotion||'no-preference',javascriptEnabled:state.javascriptEnabled!==false},attempt,loadedStatus:response.status(),pageState,elements:elementResults,errors,sceneRequests:requests,scrollToBottomWaitMs:3000};
  }finally{
    try{if(context)await context.close();}catch{}
    try{if(browser)await browser.close();}catch{}
  }
}
async function runCase(route,width,state){
  const attempts=[];
  for(let attempt=1;attempt<=2;attempt++){
    try{const result=await caseOnce(route,width,state,attempt);if(attempts.length)result.crashRetryHistory=attempts;return result;}
    catch(error){
      const detail=String(error?.stack||error);attempts.push({attempt,error:detail});
      const crashed=/Target page, context or browser has been closed|browserType\.launch|Page crashed|SIGSEGV|Target closed|browser process.*closed/i.test(detail);
      if(!crashed||attempt===2)throw new Error(`CASE_FAILED ${route.path} ${width} ${state.name}: ${JSON.stringify(attempts)}`);
    }
  }
}
async function main(){
  fs.mkdirSync(SHOTS,{recursive:true});const cases=[];const limit=Number(process.env.PHASE32C_LIMIT||0);
  const onlyRoute=process.env.PHASE32C_ONLY_ROUTE||null,onlyWidth=Number(process.env.PHASE32C_ONLY_WIDTH||0),onlyState=process.env.PHASE32C_ONLY_STATE||null;
  for(const route of ROUTES)for(const width of WIDTHS)for(const state of STATES){
    if(limit&&cases.length>=limit)break;
    if(onlyRoute&&route.name!==onlyRoute)continue;if(onlyWidth&&width!==onlyWidth)continue;if(onlyState&&state.name!==onlyState)continue;
    const row=await runCase(route,width,state);cases.push(row);
    console.log(`CASE ${cases.length}/${limit||24} ${route.path} ${width} ${state.name} sceneCalls=${row.pageState.sceneCalls} contrast=${row.elements.map(e=>e.minimumSampledContrast).join(',')}`);
  }
  const report={phase:32,subphase:'32c contrast reproduction',source:SOURCE,baseUrl:BASE,browser:'Chromium 143.0.7499.0 / Playwright 1.58.2',settings:{widths:WIDTHS,states:STATES.map(x=>x.name),fullPageScroll:true,settleAfterFullScrollMs:3000,freshBrowserPerCase:true,retryLimit:1},caseCount:cases.length,cases};
  fs.writeFileSync(OUT,JSON.stringify(report,null,2)+'\n');
  console.log(`SAVED ${OUT} (${cases.length} cases)`);
}
main().catch(error=>{console.error(error.stack||error);process.exit(1)});
