const path=require('node:path');
const {launchBrowser,routePinnedResources}=require('../phase31/browser.cjs');
const BASE=process.env.PHASE31_BASE_URL||'http://127.0.0.1:8080';
const OUT=path.join(__dirname,'../../reports/phase-32-reference-scene-smoke.json');
const ROUTES=['/','/services','/about','/contact'];
const CASES=[
  {name:'mobile-coarse',width:360,height:800,finePointer:false,expected:'skip'},
  {name:'tablet-coarse',width:768,height:1024,finePointer:false,expected:'skip'},
  {name:'desktop-coarse-pointer',width:1280,height:900,finePointer:false,expected:'skip'},
  {name:'desktop-reduced-motion',width:1280,height:900,finePointer:true,reducedMotion:'reduce',expected:'skip'},
  {name:'desktop-save-data',width:1280,height:900,finePointer:true,connection:{saveData:true,effectiveType:'4g',downlink:10},expected:'skip'},
  {name:'desktop-slow-2g',width:1280,height:900,finePointer:true,connection:{saveData:false,effectiveType:'2g',downlink:0.1},expected:'skip'},
  {name:'desktop-slow-downlink',width:1280,height:900,finePointer:true,connection:{saveData:false,effectiveType:'4g',downlink:0.5},expected:'skip'},
  {name:'desktop-fine-pointer',width:1280,height:900,finePointer:true,connection:{saveData:false,effectiveType:'4g',downlink:10},expected:'load'},
  {name:'desktop-1500ms-fallback',width:1280,height:900,finePointer:true,disableIdle:true,connection:{saveData:false,effectiveType:'4g',downlink:10},expected:'load'},
];
async function main(){
  const browser=await launchBrowser();
  const context=await browser.newContext({viewport:{width:1280,height:900}});
  const results=[];
  try{
    for(const route of ROUTES){
      for(const spec of CASES){
        const page=await context.newPage();
        await page.setViewportSize({width:spec.width,height:spec.height});
        await page.emulateMedia({reducedMotion:spec.reducedMotion||'no-preference'});
        await page.addInitScript(({connection,finePointer,disableIdle})=>{
          if(disableIdle)window.requestIdleCallback=undefined;
          window.__p32LoadSeen=false;window.__p32LoadAt=null;window.__p32SceneInsertions=[];window.__p32SceneCalls=0;
          window.addEventListener('load',()=>{window.__p32LoadSeen=true;window.__p32LoadAt=performance.now();},{once:true});
          let init=null;
          Object.defineProperty(window,'__ILMERA_SCENE_INIT',{configurable:true,get:()=>init,set:fn=>{init=function(){window.__p32SceneCalls++;return fn.apply(window,arguments);};}});
          const nativeMatchMedia=window.matchMedia.bind(window);
          window.matchMedia=function(query){
            const result=nativeMatchMedia(query);
            if(query==='(pointer: fine)')return {matches:finePointer,media:query,onchange:null};
            return result;
          };
          document.addEventListener('DOMContentLoaded',()=>{
            const append=Node.prototype.appendChild;
            Node.prototype.appendChild=function(node){
              if(this===document.head&&node&&node.tagName==='SCRIPT'&&/cdnjs\.cloudflare\.com\/ajax\/libs\/(?:three\.js\/r128\/three\.min\.js|gsap\/3\.12\.2\/(?:gsap|ScrollTrigger)\.min\.js)/.test(node.src)){
                window.__p32SceneInsertions.push({src:node.src,readyState:document.readyState,loadSeen:window.__p32LoadSeen,at:performance.now(),loadAt:window.__p32LoadAt});
              }
              return append.call(this,node);
            };
          },{once:true});
          if(connection)Object.defineProperty(navigator,'connection',{configurable:true,value:connection});
        },{connection:spec.connection||null,finePointer:spec.finePointer,disableIdle:!!spec.disableIdle});
        await routePinnedResources(page);
        const errors=[];
        page.on('pageerror',error=>errors.push(String(error)));
        await page.goto(BASE+route,{waitUntil:'load',timeout:30000});
        if(spec.expected==='load'){
          await page.waitForFunction(()=>window.__p32SceneInsertions.length===3,{timeout:20000});
          await page.waitForFunction(()=>window.__p32SceneCalls===1,{timeout:20000});
        }else{
          await page.waitForTimeout(100);
        }
        const detail=await page.evaluate(()=>{
          const canvas=document.getElementById('space-canvas');
          const rect=canvas?canvas.getBoundingClientRect():null;
          return {
            href:location.pathname,
            loadSeen:window.__p32LoadSeen,
            loadAt:window.__p32LoadAt,
            insertions:window.__p32SceneInsertions,
            sceneCalls:window.__p32SceneCalls,
            fallbackClass:document.documentElement.classList.contains('p32-scene-fallback'),
            canvasVisibility:canvas?getComputedStyle(canvas).visibility:null,
            canvasRect:rect?{width:rect.width,height:rect.height}:null,
            finePointer:matchMedia('(pointer: fine)').matches,
            reducedMotion:matchMedia('(prefers-reduced-motion: reduce)').matches,
          };
        });
        const eligible=spec.width>=900&&spec.finePointer&&!detail.reducedMotion&&!spec.connection?.saveData&&spec.connection?.effectiveType!=='2g'&&!(spec.connection?.downlink>0&&spec.connection.downlink<1.1);
        const checks={
          canvas_reserved:!!detail.canvasRect&&detail.canvasRect.width>=spec.width-1&&detail.canvasRect.height>=spec.height-1,
          no_early_scene_scripts:spec.expected==='load'?detail.insertions.length===3&&detail.insertions.every(row=>row.loadSeen&&row.readyState==='complete'&&row.at>=row.loadAt):detail.insertions.length===0,
          fallback_timer_respected:spec.disableIdle?detail.insertions.length===3&&detail.insertions.every(row=>row.at-row.loadAt>=1450):true,
          init_only_when_eligible:spec.expected==='load'?detail.sceneCalls===1:detail.sceneCalls===0,
          static_fallback_when_skipped:spec.expected==='skip'?detail.fallbackClass&&detail.canvasVisibility==='hidden':true,
          all_three_requested_when_eligible:spec.expected==='skip'||(detail.insertions.length===3&&['three.min.js','gsap.min.js','ScrollTrigger.min.js'].every(name=>detail.insertions.some(row=>row.src.includes(name)))),
          expected_eligibility:eligible===(spec.expected==='load')&&detail.finePointer===spec.finePointer,
        };
        if(Object.values(checks).some(value=>value!==true)){
          throw new Error(`FAIL ${route} ${spec.name}: ${JSON.stringify({detail,checks,errors})}`);
        }
        results.push({route,case:spec.name,expected:spec.expected,checks,detail,errors});
        await page.close();
      }
    }
  }finally{
    await context.close();
    await browser.close();
  }
  const report={phase:32,status:'PASS',source:'local PHP-WASM adapter, pinned local CDN mirrors, Chromium 143',cases:results.length,results};
  require('node:fs').writeFileSync(OUT,JSON.stringify(report,null,2)+'\n');
  console.log(JSON.stringify({phase:report.phase,status:report.status,cases:report.cases,output:OUT},null,2));
}
main().catch(error=>{console.error(error.stack||error);process.exit(1);});
