#!/usr/bin/env node
'use strict';

// Phase32c Task 2: compare the reference pages to the Phase31b render outside
// scene layers. Each route-width-state case gets a fresh Chromium context and
// baseline/current navigations on one page, with incremental full-page scroll,
// reveal-settle time, and a 0.1 CSS-pixel geometry comparison. The disabled-
// switch state uses adapters whose only test-tree change is ILMERA_SCENES_ENABLED=false.

const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const { launchBrowser } = require('../phase31/browser.cjs');

const ROOT = path.resolve(__dirname, '../..');
const BASELINE_URL = process.env.PHASE32C_BASELINE_URL || 'http://127.0.0.1:8097';
const CURRENT_URL = process.env.PHASE32C_CURRENT_URL || 'http://127.0.0.1:8096';
const BASELINE_DISABLED_URL = process.env.PHASE32C_BASELINE_DISABLED_URL || 'http://127.0.0.1:8098';
const CURRENT_DISABLED_URL = process.env.PHASE32C_CURRENT_DISABLED_URL || 'http://127.0.0.1:8099';
const OUTPUT = process.env.PHASE32C_REFERENCE_OUT || path.join(ROOT, 'reports/phase-32c-reference-safeguards.json');
const RUNTIME = process.env.PHASE31_RUNTIME || '/home/user/phase32c-runtime/node_modules';
const ROUTES = ['/','/services','/about','/contact'];
const WIDTHS = [360,768,1280];
const STATES = [
  {name:'scene', finePointer:true, reducedMotion:'no-preference', blockThreeOnly:false, javascriptEnabled:true, disabledSwitch:false},
  {name:'still', finePointer:false, reducedMotion:'no-preference', blockThreeOnly:true, javascriptEnabled:true, disabledSwitch:false},
  {name:'reduced-motion', finePointer:true, reducedMotion:'reduce', blockThreeOnly:false, javascriptEnabled:true, disabledSwitch:false},
  {name:'disabled-scene-switch', finePointer:true, reducedMotion:'no-preference', blockThreeOnly:false, javascriptEnabled:true, disabledSwitch:true},
  {name:'javascript-off', finePointer:false, reducedMotion:'no-preference', blockThreeOnly:false, javascriptEnabled:false, disabledSwitch:false},
];
const SCENE_URLS = [
  'https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js',
  'https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js',
  'https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js',
];
const SCENE_LAYER_SELECTOR = '#space-canvas,#vignette,#nebula-t,#nebula-b,#gold-shimmer,#gold-glow-css,#grain,#float-layer';
const POINTER_OVERLAY_SELECTOR = '#cur-ring,#cur-dot';
const ELEMENT_SELECTOR = 'body,body *';
const NONVISUAL_TAGS = new Set(['script','style','link','meta','noscript','template']);

function selectedList(envName, fallback) {
  const raw = process.env[envName];
  if (!raw) return fallback;
  const wanted = new Set(raw.split(',').map(value=>value.trim()).filter(Boolean));
  return fallback.filter(value=>wanted.has(String(value)));
}
function atomicJson(file, value) {
  fs.mkdirSync(path.dirname(file), {recursive:true});
  const temp = `${file}.tmp`;
  fs.writeFileSync(temp, JSON.stringify(value, null, 2) + '\n');
  fs.renameSync(temp, file);
}
function fnvHash(value) {
  let h=2166136261;
  for(let i=0;i<value.length;i++){h^=value.charCodeAt(i);h=Math.imul(h,16777619);}
  return (h>>>0).toString(16).padStart(8,'0');
}
function caseKey(route,width,state) { return `${route}|${width}|${state}`; }
function parseExisting() {
  if (process.env.PHASE32C_REF_RESUME !== '1' || !fs.existsSync(OUTPUT)) return null;
  try { return JSON.parse(fs.readFileSync(OUTPUT,'utf8')); }
  catch (error) { throw new Error(`Cannot resume ${OUTPUT}: ${error.message}`); }
}

function fontCss(fontBase) {
  const faces = [
    ['Outfit','300','normal','outfit-reference-300.woff2'],
    ['Outfit','400','normal','outfit-reference-400.woff2'],
    ['Outfit','500','normal','outfit-reference-500.woff2'],
    ['Outfit','600','normal','outfit-reference-600.woff2'],
    ['Outfit','700','normal','outfit-reference-700.woff2'],
    ['Cormorant Garamond','300','normal','cormorant-garamond-reference-300.woff2'],
    ['Cormorant Garamond','400','normal','cormorant-garamond-reference-400.woff2'],
    ['Cormorant Garamond','600','normal','cormorant-garamond-reference-600.woff2'],
    ['Cormorant Garamond','700','normal','cormorant-garamond-reference-700.woff2'],
    ['Cormorant Garamond','300','italic','cormorant-garamond-reference-300-italic.woff2'],
    ['Cormorant Garamond','400','italic','cormorant-garamond-reference-400-italic.woff2'],
  ];
  return faces.map(([family,weight,style,file])=>
    `@font-face{font-family:'${family}';font-style:${style};font-weight:${weight};font-display:swap;src:url('${fontBase}/assets/fonts/${file}') format('woff2');}`
  ).join('\n');
}
function sceneFile(url) {
  const u=new URL(url);
  if(u.pathname==='/ajax/libs/three.js/r128/three.min.js')return path.join(RUNTIME,'three/build/three.min.js');
  if(u.pathname==='/ajax/libs/gsap/3.12.2/gsap.min.js')return path.join(RUNTIME,'gsap/dist/gsap.min.js');
  if(u.pathname==='/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js')return path.join(RUNTIME,'gsap/dist/ScrollTrigger.min.js');
  return null;
}

async function installRoutes(page, routeState) {
  const css=fontCss(new URL(CURRENT_URL).origin);
  await page.route('**/*',async route=>{
    const requestUrl=route.request().url();
    const u=new URL(requestUrl);
    const state=routeState.activeState;
    if(u.hostname==='cdnjs.cloudflare.com'){
      if(state?.blockThreeOnly&&u.pathname==='/ajax/libs/three.js/r128/three.min.js'){
        routeState.activeTrace?.blockedSceneResources.push(u.pathname);
        return route.abort('blockedbyclient');
      }
      const file=sceneFile(requestUrl);
      if(file&&fs.existsSync(file))return route.fulfill({status:200,contentType:'text/javascript; charset=utf-8',body:fs.readFileSync(file)});
      return route.abort('blockedbyclient');
    }
    if(u.hostname==='fonts.googleapis.com')return route.fulfill({status:200,contentType:'text/css; charset=utf-8',body:css});
    if(u.hostname==='fonts.gstatic.com')return route.abort('blockedbyclient');
    if(u.hostname==='ilmerastudyabroad.com'||u.hostname==='www.ilmerastudyabroad.com'){
      const response=await route.fetch({url:routeState.activeBase+u.pathname+u.search});
      return route.fulfill({response});
    }
    if(u.hostname==='127.0.0.1'||u.hostname==='localhost')return route.continue();
    return route.abort('blockedbyclient');
  });
  page.on('request',request=>{
    const url=request.url();
    if(/three\.min\.js|gsap\.min\.js|ScrollTrigger\.min\.js/.test(url))routeState.activeTrace?.sceneRequests.push(url);
    if(url.includes('/assets/images/hero-still-'))routeState.activeTrace?.stillRequests.push(new URL(url).pathname);
  });
  page.on('pageerror',error=>routeState.activeTrace?.pageErrors.push(String(error)));
  page.on('console',message=>{if(message.type()==='error')routeState.activeTrace?.consoleErrors.push(message.text());});
  page.on('requestfailed',request=>{
    const url=request.url(),message=request.failure()?.errorText||'';
    if(/blocked_by_client|ERR_BLOCKED_BY_CLIENT/i.test(message))return;
    routeState.activeTrace?.failedRequests.push({url,error:message});
  });
}

async function createPage(browser,width,state) {
  const context=await browser.newContext({
    viewport:{width,height:900},deviceScaleFactor:1,isMobile:width<=768,
    hasTouch:!state.finePointer,javaScriptEnabled:state.javascriptEnabled,
  });
  const page=await context.newPage();
  await page.emulateMedia({reducedMotion:state.reducedMotion});
  if(state.javascriptEnabled)await page.addInitScript(({finePointer})=>{
    window.__p32cWebGLCalls=0;
    window.__p32cSceneCalls=0;
    const originalGetContext=HTMLCanvasElement.prototype.getContext;
    HTMLCanvasElement.prototype.getContext=function(type){
      if(/^(?:webgl2?|experimental-webgl)$/i.test(String(type)))window.__p32cWebGLCalls++;
      return originalGetContext.apply(this,arguments);
    };
    let init=null;
    Object.defineProperty(window,'__ILMERA_SCENE_INIT',{
      configurable:true,
      get(){return init;},
      set(fn){init=function(){window.__p32cSceneCalls++;return fn.apply(this,arguments);};},
    });
    const originalMatchMedia=window.matchMedia.bind(window);
    window.matchMedia=function(query){
      if(query==='(pointer: fine)'||query==='(pointer: coarse)'){
        const matches=query==='(pointer: fine)'?finePointer:!finePointer;
        return {matches,media:query,onchange:null,addListener(){},removeListener(){},addEventListener(){},removeEventListener(){},dispatchEvent(){return false;}};
      }
      return originalMatchMedia(query);
    };
  },{finePointer:state.finePointer});
  return {context,page};
}

function expectedScene(source,width,state) {
  if(!state.javascriptEnabled||state.blockThreeOnly||state.disabledSwitch)return false;
  if(source==='baseline')return true;
  return width>=900&&state.finePointer&&state.reducedMotion!=='reduce';
}

async function readScrollMetrics(page) {
  return page.evaluate(()=>{
    const height=Math.max(document.documentElement.scrollHeight,document.body?.scrollHeight||0);
    const viewport=window.innerHeight||document.documentElement.clientHeight;
    const clientHeight=document.documentElement.clientHeight||viewport;
    const maxScrollY=Math.max(0,height-viewport);
    return{y:window.scrollY,height,viewport,innerHeight:window.innerHeight,clientHeight,maxScrollY,fullyScrolled:window.scrollY>=maxScrollY-1};
  });
}

async function scrollToPageEnd(page,width) {
  const started=Date.now();let metrics=await readScrollMetrics(page);
  const stepSize=Math.max(160,Math.round(metrics.viewport*0.55));
  const maxSteps=Math.max(32,Math.ceil(metrics.height/stepSize)*4+20);
  const positions=[{y:metrics.y,height:metrics.height,maxScrollY:metrics.maxScrollY}];
  let steps=0,recoverySteps=0,stalled=0;
  await page.mouse.move(Math.max(0,width-1),Math.max(0,Math.min(metrics.clientHeight,metrics.viewport)-2)).catch(()=>{});
  while(!metrics.fullyScrolled&&steps<maxSteps){
    const beforeY=metrics.y,delta=Math.max(1,Math.min(stepSize,metrics.maxScrollY-metrics.y));
    await page.mouse.wheel(0,delta);
    await page.waitForTimeout(220);
    metrics=await readScrollMetrics(page);steps++;
    if(metrics.y<=beforeY+1&&!metrics.fullyScrolled){
      const recoveryDelta=Math.max(1,Math.min(stepSize,metrics.maxScrollY-metrics.y));
      await page.evaluate(amount=>window.scrollBy(0,amount),recoveryDelta).catch(()=>{});
      await page.waitForTimeout(220);
      metrics=await readScrollMetrics(page);recoverySteps++;
      stalled=metrics.y<=beforeY+1?stalled+1:0;
    }else stalled=0;
    positions.push({y:metrics.y,height:metrics.height,maxScrollY:metrics.maxScrollY});
    if(stalled>=3)break;
  }
  return{...metrics,stepSizeCssPx:stepSize,scrollSteps:steps,recoverySteps,positions,attemptLimit:maxSteps,durationMs:Date.now()-started};
}

async function snapshotPage(page,route,width,state,source,activeBase,routeState) {
  const trace={sceneRequests:[],stillRequests:[],blockedSceneResources:[],pageErrors:[],consoleErrors:[],failedRequests:[]};
  routeState.activeBase=activeBase;routeState.activeState=state;routeState.activeTrace=trace;
  const response=await page.goto(activeBase+route,{waitUntil:'load',timeout:60000});
  if(!response||response.status()!==200)throw new Error(`${source} ${route} returned ${response?.status()||'no response'}`);
  try{await page.evaluate(()=>document.fonts?document.fonts.ready:Promise.resolve());}catch(_){}
  if(expectedScene(source,width,state)&&state.javascriptEnabled){
    try{await page.waitForFunction(()=>window.__p32cWebGLCalls>0,{timeout:12000});}catch(_){}
  }
  const initialScroll=await readScrollMetrics(page);
  const firstWalk=await scrollToPageEnd(page,width);
  try{await page.evaluate(()=>document.fonts?document.fonts.ready:Promise.resolve());}catch(_){}
  let afterFonts=await readScrollMetrics(page),postFontWalk=null;
  if(!afterFonts.fullyScrolled||Math.abs(afterFonts.height-firstWalk.height)>1){
    postFontWalk=await scrollToPageEnd(page,width);
    afterFonts=postFontWalk;
  }
  await page.waitForTimeout(3000);
  trace.infiniteCssAnimationsPaused=await page.evaluate(()=>{
    let paused=0;
    for(const animation of document.getAnimations({subtree:true})){
      const timing=animation.effect?.getTiming();
      if(animation.constructor?.name==='CSSAnimation'&&timing?.iterations===Infinity){animation.pause();animation.currentTime=0;paused++;}
    }
    return paused;
  });
  await page.waitForTimeout(80);
  let settled=await readScrollMetrics(page),finalRecovery=null;
  if(!settled.fullyScrolled){
    finalRecovery=await scrollToPageEnd(page,width);
    await page.waitForTimeout(3000);
    settled=await readScrollMetrics(page);
  }
  const fontState=await page.evaluate(()=>({status:document.fonts?.status||'unsupported',outfit300Loaded:document.fonts?.check('300 14px Outfit')??null}));
  const revealState=await page.evaluate(()=>{
    const selector='.reveal,.reveal-l,.reveal-r,.anim-fade-up,.anim-fade-left,.anim-fade-right,.anim-scale-in';
    const targets=Array.from(document.querySelectorAll(selector));
    const pending=targets.filter(node=>{const style=getComputedStyle(node),opacity=Number.parseFloat(style.opacity);return style.display==='none'||style.visibility==='hidden'||(Number.isFinite(opacity)&&opacity<0.98);});
    return{targets:targets.length,animVisible:document.querySelectorAll('.anim-visible').length,pending:pending.length,pendingExamples:pending.slice(0,12).map(node=>({tag:node.tagName.toLowerCase(),id:node.id||'',classes:String(node.className||'').slice(0,160),text:String(node.innerText||node.textContent||'').replace(/\s+/g,' ').trim().slice(0,120),opacity:getComputedStyle(node).opacity}))};
  });
  trace.scroll={initialY:initialScroll.y,initialHeight:initialScroll.height,initialClientHeight:initialScroll.clientHeight,initialViewportHeight:initialScroll.viewport,firstWalk,postFontWalk,finalRecovery,finalY:settled.y,finalHeight:settled.height,finalClientHeight:settled.clientHeight,finalViewportHeight:settled.viewport,maxScrollY:settled.maxScrollY,fullyScrolled:settled.fullyScrolled};
  trace.fonts=fontState;trace.reveals=revealState;
  const snapshot=await page.evaluate(({selector,sceneLayerSelector,pointerOverlaySelector,nonvisualTags})=>{
    const clean=value=>String(value||'').replace(/\s+/g,' ').trim();
    const hash=value=>{let h=2166136261;for(let i=0;i<value.length;i++){h^=value.charCodeAt(i);h=Math.imul(h,16777619);}return(h>>>0).toString(16).padStart(8,'0');};
    const stable=value=>{
      if(value===null||typeof value!=='object')return JSON.stringify(value);
      if(Array.isArray(value))return '['+value.map(stable).join(',')+']';
      return '{'+Object.keys(value).sort().map(key=>JSON.stringify(key)+':'+stable(value[key])).join(',')+'}';
    };
    const canonical=document.querySelector('link[rel="canonical"]')?.getAttribute('href')||null;
    const links=Array.from(document.querySelectorAll('a[href]')).map(a=>({href:a.getAttribute('href'),text:clean(a.innerText||a.textContent),rel:a.getAttribute('rel')||'',target:a.getAttribute('target')||'',ariaLabel:a.getAttribute('aria-label')||''}));
    const images=Array.from(document.querySelectorAll('img')).map(img=>({src:img.getAttribute('src')||'',srcset:img.getAttribute('srcset')||'',alt:img.getAttribute('alt')||'',width:img.getAttribute('width')||'',height:img.getAttribute('height')||'',loading:img.getAttribute('loading')||'',currentSrc:img.currentSrc?(()=>{const u=new URL(img.currentSrc);return u.pathname+u.search;})():'',naturalWidth:img.naturalWidth||0,naturalHeight:img.naturalHeight||0}));
    const pictureSources=Array.from(document.querySelectorAll('picture source')).map(source=>({srcset:source.getAttribute('srcset')||'',media:source.getAttribute('media')||'',type:source.getAttribute('type')||''}));
    const jsonLd=Array.from(document.querySelectorAll('script[type="application/ld+json"]')).map(script=>{const raw=script.textContent.trim();try{return stable(JSON.parse(raw));}catch(_){return raw;}});
    const pageText=clean(document.body?.innerText||'');
    const headings=Array.from(document.querySelectorAll('h1,h2,h3,h4,h5,h6')).map(node=>({tag:node.tagName.toLowerCase(),text:clean(node.innerText||node.textContent)}));
    const teamCards=Array.from(document.querySelectorAll('#team .team-card,.team-card')).map((node,index)=>{const r=node.getBoundingClientRect();return{index,text:clean(node.innerText||node.textContent),rect:{x:r.left+scrollX,y:r.top+scrollY,width:r.width,height:r.height}};});
    const sceneNodes=Array.from(document.querySelectorAll(sceneLayerSelector)).map(node=>({id:node.id||'',tag:node.tagName.toLowerCase(),display:getComputedStyle(node).display,visibility:getComputedStyle(node).visibility}));
    const occurrence=new Map(),elements=[];
    for(const node of document.querySelectorAll(selector)){
      if(nonvisualTags.includes(node.tagName.toLowerCase())||node.closest(sceneLayerSelector)||node.closest(pointerOverlaySelector))continue;
      const rect=node.getBoundingClientRect(),style=getComputedStyle(node);
      let opacity=1;for(let parent=node;parent&&parent.nodeType===1;parent=parent.parentElement){const value=Number.parseFloat(getComputedStyle(parent).opacity);if(Number.isFinite(value))opacity*=value;}
      if(style.display==='none'||style.visibility==='hidden'||style.visibility==='collapse'||opacity<0.02||rect.width<0.1||rect.height<0.1)continue;
      const classes=Array.from(node.classList||[]).sort();
      const stableClasses=classes.filter(c=>!/^anim-|^reveal(?:-|$)|^p32-|^is-loaded$|^(?:dk|lt)$/.test(c)).join('.');
      const text=clean(node.innerText||node.textContent),href=node.getAttribute('href')||'',src=node.getAttribute('src')||'',alt=node.getAttribute('alt')||'';
      const baseKey=[node.tagName.toLowerCase(),node.id||'',stableClasses,href,src,alt,text.slice(0,160)].join('|');
      const index=occurrence.get(baseKey)||0;occurrence.set(baseKey,index+1);
      let viewportPosition=false;for(let parent=node;parent&&parent.nodeType===1;parent=parent.parentElement){const position=getComputedStyle(parent).position;if(position==='fixed'||position==='sticky'){viewportPosition=true;break;}}
      elements.push({key:`${baseKey}#${index}`,tag:node.tagName.toLowerCase(),id:node.id||'',classes:classes.join(' '),text:text.slice(0,220),rect:{x:rect.left+(viewportPosition?0:scrollX),y:rect.top+(viewportPosition?0:scrollY),width:rect.width,height:rect.height},style:{color:style.color,backgroundColor:style.backgroundColor,fontFamily:style.fontFamily,fontSize:style.fontSize,fontWeight:style.fontWeight,lineHeight:style.lineHeight,opacity:style.opacity,position:style.position}});
    }
    const landmark=node=>{if(!node)return null;const r=node.getBoundingClientRect(),s=getComputedStyle(node),viewportPosition=s.position==='fixed'||s.position==='sticky';return{text:clean(node.innerText||node.textContent),rect:{x:r.left+(viewportPosition?0:scrollX),y:r.top+(viewportPosition?0:scrollY),width:r.width,height:r.height},fontFamily:s.fontFamily,fontSize:s.fontSize,color:s.color,backgroundColor:s.backgroundColor};};
    const canvas=document.getElementById('space-canvas'),canvasRect=canvas?.getBoundingClientRect();
    return{
      location:location.pathname,viewport:{width:innerWidth,height:innerHeight},document:{scrollWidth:document.documentElement.scrollWidth,scrollHeight:Math.max(document.documentElement.scrollHeight,document.body?.scrollHeight||0)},
      pageText:{length:pageText.length,hash:hash(pageText),text:pageText},headings,links,images,pictureSources,jsonLd,canonical,
      header:landmark(document.querySelector('header')||document.querySelector('nav#il-nav')),
      footer:landmark(document.querySelector('footer')),
      team:landmark(document.querySelector('#team')),
      teamCards,elements,
      scene:{webglCalls:window.__p32cWebGLCalls||0,sceneCalls:window.__p32cSceneCalls||0,fallbackClass:document.documentElement.classList.contains('p32-scene-fallback'),sceneLoader:!!document.getElementById('p32-scene-loader'),sceneOffStyle:!!document.getElementById('ilmera-scenes-off'),referenceFontStyle:!!document.getElementById('p32-reference-font-faces'),p25Template:document.body?.classList.contains('p25')||false,heroStillNodes:document.querySelectorAll('.p32-hero-still').length,canvas:canvasRect?{width:canvasRect.width,height:canvasRect.height,visibility:getComputedStyle(canvas).visibility}:null,layers:sceneNodes},
      pointerOverlays:Array.from(document.querySelectorAll(pointerOverlaySelector)).map(node=>node.id)
    };
  },{selector:ELEMENT_SELECTOR,sceneLayerSelector:SCENE_LAYER_SELECTOR,pointerOverlaySelector:POINTER_OVERLAY_SELECTOR,nonvisualTags:[...NONVISUAL_TAGS]});
  trace.sceneRequests=[...new Set(trace.sceneRequests)];trace.stillRequests=[...new Set(trace.stillRequests)];
  return{snapshot,trace,pageHeight:initialScroll.height};
}

function same(a,b){return JSON.stringify(a)===JSON.stringify(b);}
function compareGeometry(baseline,current){
  const aMap=new Map(baseline.elements.map(item=>[item.key,item])),bMap=new Map(current.elements.map(item=>[item.key,item]));
  const missingCurrent=[],addedCurrent=[],overTolerance=[],styleDifferences=[],classDifferences=[];let compared=0,maxDelta=0;
  for(const [key,a] of aMap){
    const b=bMap.get(key);if(!b){missingCurrent.push({key,tag:a.tag,text:a.text,baseline:a.rect});continue;}compared++;
    const delta={};for(const prop of ['x','y','width','height']){delta[prop]=Number((b.rect[prop]-a.rect[prop]).toFixed(4));maxDelta=Math.max(maxDelta,Math.abs(delta[prop]));}
    if(Object.values(delta).some(value=>Math.abs(value)>0.1))overTolerance.push({key,tag:a.tag,text:a.text,baseline:a.rect,current:b.rect,delta});
    const changed={};for(const prop of Object.keys(a.style))if(a.style[prop]!==b.style[prop])changed[prop]={baseline:a.style[prop],current:b.style[prop]};
    if(Object.keys(changed).length)styleDifferences.push({key,tag:a.tag,text:a.text,changed});
    if(a.classes!==b.classes)classDifferences.push({key,tag:a.tag,text:a.text,baseline:a.classes,current:b.classes});
  }
  for(const [key,b] of bMap)if(!aMap.has(key))addedCurrent.push({key,tag:b.tag,text:b.text,current:b.rect});
  const rectDelta=(a,b)=>{if(!a||!b)return null;const result={};for(const p of ['x','y','width','height'])result[p]=Number((b.rect[p]-a.rect[p]).toFixed(4));return result;};
  return{
    toleranceCssPx:0.1,compared,withinTolerance:overTolerance.length===0&&missingCurrent.length===0&&addedCurrent.length===0,
    overToleranceCount:overTolerance.length,missingCurrentCount:missingCurrent.length,addedCurrentCount:addedCurrent.length,maxAbsoluteDeltaCssPx:Number(maxDelta.toFixed(4)),
    differences:overTolerance,missingCurrent,addedCurrent,styleDifferenceCount:styleDifferences.length,styleDifferences,classDifferenceCount:classDifferences.length,classDifferences,
    landmarks:{header:{baseline:baseline.header,current:current.header,delta:rectDelta(baseline.header,current.header)},footer:{baseline:baseline.footer,current:current.footer,delta:rectDelta(baseline.footer,current.footer)},team:{baseline:baseline.team,current:current.team,delta:rectDelta(baseline.team,current.team)},teamCards:{baseline:baseline.teamCards,current:current.teamCards}}
  };
}

async function runCase(route,width,state){
  const urls=state.disabledSwitch?{baseline:BASELINE_DISABLED_URL,current:CURRENT_DISABLED_URL}:{baseline:BASELINE_URL,current:CURRENT_URL};
  const browser=await launchBrowser();const {context,page}=await createPage(browser,width,state);
  const routeState={activeBase:'',activeState:state,activeTrace:null};const result={};
  try{
    await installRoutes(page,routeState);
    for(const source of ['baseline','current'])result[source]=await snapshotPage(page,route,width,state,source,urls[source],routeState);
  }finally{await context.close();await browser.close();}
  const a=result.baseline.snapshot,b=result.current.snapshot;
  const geometry=compareGeometry(a,b);
  const content={
    visibleTextExact:a.pageText.text===b.pageText.text,
    visibleTextEvidence:{baseline:{length:a.pageText.length,hash:a.pageText.hash},current:{length:b.pageText.length,hash:b.pageText.hash}},
    headingsExact:same(a.headings,b.headings),linksExact:same(a.links,b.links),linkCounts:{baseline:a.links.length,current:b.links.length},
    imagesExact:same(a.images,b.images),imageCounts:{baseline:a.images.length,current:b.images.length},pictureSourcesExact:same(a.pictureSources,b.pictureSources),
    structuredDataExact:same(a.jsonLd,b.jsonLd),structuredDataBlocks:{baseline:a.jsonLd.length,current:b.jsonLd.length},canonicalExact:a.canonical===b.canonical,
  };
  const baselineExpected=expectedScene('baseline',width,state),currentExpected=expectedScene('current',width,state);
  const stateChecks={
    baselineSceneExpected:baselineExpected,currentSceneExpected:currentExpected,
    baselineWebGLObserved:a.scene.webglCalls>0,currentWebGLObserved:b.scene.webglCalls>0,
    baselineSceneExpectationMatches:(a.scene.webglCalls>0)===baselineExpected,
    currentSceneExpectationMatches:(b.scene.webglCalls>0)===currentExpected,
    baselineSceneRequestCount:result.baseline.trace.sceneRequests.length,currentSceneRequestCount:result.current.trace.sceneRequests.length,
    stillRequestsBaseline:result.baseline.trace.stillRequests,stillRequestsCurrent:result.current.trace.stillRequests,
    baselineSceneFallback:a.scene.fallbackClass,currentSceneFallback:b.scene.fallbackClass,
    baselineDisabledSwitchStyle:a.scene.sceneOffStyle,currentDisabledSwitchStyle:b.scene.sceneOffStyle,
    baselineHeroStillNodes:a.scene.heroStillNodes,currentHeroStillNodes:b.scene.heroStillNodes,
    heroStillAbsentOnReferencePages:a.scene.heroStillNodes===0&&b.scene.heroStillNodes===0&&result.baseline.trace.stillRequests.length===0&&result.current.trace.stillRequests.length===0,
    baselineFullyScrolled:result.baseline.trace.scroll?.fullyScrolled===true,
    currentFullyScrolled:result.current.trace.scroll?.fullyScrolled===true,
    baselineRevealTargetCount:result.baseline.trace.reveals?.targets||0,currentRevealTargetCount:result.current.trace.reveals?.targets||0,
    baselineRevealPendingCount:result.baseline.trace.reveals?.pending||0,currentRevealPendingCount:result.current.trace.reveals?.pending||0,
    baselineRevealsSettled:!state.javascriptEnabled||(result.baseline.trace.reveals?.pending||0)===0,
    currentRevealsSettled:!state.javascriptEnabled||(result.current.trace.reveals?.pending||0)===0,
  };
  const errors=[...result.baseline.trace.pageErrors.map(error=>({source:'baseline',error})),...result.current.trace.pageErrors.map(error=>({source:'current',error})),...result.baseline.trace.failedRequests.map(item=>({source:'baseline',...item})),...result.current.trace.failedRequests.map(item=>({source:'current',...item}))];
  const parity=Object.values(content).every(value=>typeof value!=='boolean'||value);
  const sceneMatches=stateChecks.baselineSceneExpectationMatches&&stateChecks.currentSceneExpectationMatches;
  const fullScroll=stateChecks.baselineFullyScrolled&&stateChecks.currentFullyScrolled;
  const revealsSettled=stateChecks.baselineRevealsSettled&&stateChecks.currentRevealsSettled;
  return{
    route,width,state:state.name,
    baseline:{pageHeight:result.baseline.pageHeight,trace:result.baseline.trace,scene:a.scene},
    current:{pageHeight:result.current.pageHeight,trace:result.current.trace,scene:b.scene},
    content,geometry,stateChecks,errors,
    status:parity&&geometry.withinTolerance&&sceneMatches&&fullScroll&&revealsSettled&&errors.length===0?'PASS':'DIFFERENCES'
  };
}

async function main(){
  const routes=selectedList('PHASE32C_REF_ROUTES',ROUTES),widths=selectedList('PHASE32C_REF_WIDTHS',WIDTHS).map(Number),stateNames=selectedList('PHASE32C_REF_STATES',STATES.map(state=>state.name)),states=STATES.filter(state=>stateNames.includes(state.name));
  if(process.env.PHASE32C_REF_ROUTES&&!routes.length)throw new Error('PHASE32C_REF_ROUTES did not match an allowed route');
  if(process.env.PHASE32C_REF_WIDTHS&&!widths.length)throw new Error('PHASE32C_REF_WIDTHS did not match an allowed width');
  if(process.env.PHASE32C_REF_STATES&&!states.length)throw new Error('PHASE32C_REF_STATES did not match an allowed state');
  const resumed=parseExisting();
  const report=resumed||{
    phase:'32c',task:2,status:'RUNNING',
    method:'Local PHP-WASM source adapters; Phase31b source 796879d versus current; one fresh Chromium browser/context per route-width-state case, navigating a shared page baseline then current to keep browser, cache and animation state comparable; identical local reference-font files; all visible DOM elements outside the listed scene-layer and pointer-following cursor overlay IDs; incremental wheel scroll in 55%-viewport steps with 220ms dwell, post-scroll font-ready check, and 3-second final settle for scroll-triggered reveals; full-scroll positions recorded per step; infinite CSS animations frozen at phase zero for deterministic geometry; 0.1 CSS-pixel geometry tolerance.',
    source:{baselineCommit:'796879d',currentCommit:process.env.PHASE32C_CURRENT_SHA||'091442f',baselineUrl:BASELINE_URL,currentUrl:CURRENT_URL,baselineDisabledUrl:BASELINE_DISABLED_URL,currentDisabledUrl:CURRENT_DISABLED_URL},
    matrix:{routes,widths,states:states.map(state=>state.name),casesExpected:routes.length*widths.length*states.length},results:[],summary:null,
  };
  const existing=new Set(report.results.map(item=>caseKey(item.route,item.width,item.state)));
  const pending=[];for(const route of routes)for(const width of widths)for(const state of states)if(!existing.has(caseKey(route,width,state.name)))pending.push({route,width,state});
  for(const spec of pending){
    let result,error;for(let attempt=0;attempt<2;attempt++){try{result=await runCase(spec.route,spec.width,spec.state);break;}catch(err){error=err;if(attempt===0)console.warn(`Retrying ${caseKey(spec.route,spec.width,spec.state.name)}: ${err.message}`);}}
    if(!result)result={route:spec.route,width:spec.width,state:spec.state.name,status:'ERROR',error:error?.stack||String(error),content:null,geometry:null,stateChecks:null,errors:[String(error)]};
    report.results.push(result);
    report.results.sort((a,b)=>ROUTES.indexOf(a.route)-ROUTES.indexOf(b.route)||a.width-b.width||STATES.findIndex(s=>s.name===a.state)-STATES.findIndex(s=>s.name===b.state));
    atomicJson(OUTPUT,report);
    console.log(`${result.status} ${caseKey(spec.route,spec.width,spec.state.name)}${result.geometry?` geometry=${result.geometry.overToleranceCount} missing=${result.geometry.missingCurrentCount} added=${result.geometry.addedCurrentCount}`:''}`);
  }
  const expected=report.matrix.casesExpected,passed=report.results.filter(item=>item.status==='PASS').length;
  report.status=report.results.length===expected&&passed===expected?'PASS':'DIFFERENCES';
  report.summary={cases:report.results.length,expectedCases:expected,passCases:passed,geometryCasesOverTolerance:report.results.filter(item=>item.geometry&&!item.geometry.withinTolerance).length,contentCasesWithDifferences:report.results.filter(item=>item.content&&Object.entries(item.content).some(([key,value])=>key.endsWith('Exact')&&value!==true)).length,casesWithRuntimeErrors:report.results.filter(item=>item.status==='ERROR'||item.errors?.length).length,casesWithoutFullScroll:report.results.filter(item=>item.stateChecks&&(!item.stateChecks.baselineFullyScrolled||!item.stateChecks.currentFullyScrolled)).length,casesWithUnsettledReveals:report.results.filter(item=>item.stateChecks&&(!item.stateChecks.baselineRevealsSettled||!item.stateChecks.currentRevealsSettled)).length,maximumElementDeltaCssPx:Number(Math.max(0,...report.results.map(item=>item.geometry?.maxAbsoluteDeltaCssPx||0)).toFixed(4))};
  atomicJson(OUTPUT,report);
  console.log(JSON.stringify({status:report.status,...report.summary,output:OUTPUT},null,2));
  if(report.results.some(item=>item.status==='ERROR'))process.exitCode=1;
}

main().catch(error=>{console.error(error.stack||error);process.exit(1);});
