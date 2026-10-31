#!/usr/bin/env node
// Single-page diagnostic for attributing Phase32 CLS. Not part of the frozen 11-route samples.
const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto');
const {pathToFileURL}=require('node:url');
const {chromium}=require('playwright'),packed=require('@sparticuz/chromium');
const {resources}=require('../phase25/resources.cjs');
const ROOT=path.resolve(__dirname,'../..');
const RUNTIME=process.env.PHASE32_RUNTIME||'/home/user/phase32-runtime/node_modules';
const {inflate}=require(path.join(RUNTIME,'@sparticuz/chromium/build/cjs/lambdafs.cjs'));
const EVIDENCE=path.resolve(process.env.PHASE32_AB_EVIDENCE||'/home/user/phase32-runtime/phase32-ab');
const FIXTURES=JSON.parse(fs.readFileSync(path.join(EVIDENCE,'fixtures.json'),'utf8'));
const SELECTED=path.join(EVIDENCE,'selected.json');
const PORT=Number(process.env.PHASE32_AB_PORT||8082),BASE=`http://127.0.0.1:${PORT}`;
const ROUTE=process.env.PHASE32_CLS_ROUTE||'/';
const ARM=process.env.PHASE32_CLS_ARM||'B';
const OUTPUT=path.resolve(process.env.PHASE32_CLS_OUTPUT||path.join(EVIDENCE,'cls-attribution.json'));
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
function chromeArgs(){return[...packed.args.filter(a=>!['--single-process','--in-process-gpu'].includes(a)),'--remote-debugging-port=9222'];}
async function main(){
 if(!FIXTURES[ROUTE]?.[ARM])throw Error(`Missing frozen fixture ${ARM} ${ROUTE}`);
 if(fs.existsSync(OUTPUT))throw Error(`Refusing to overwrite diagnostic output ${OUTPUT}`);
 const selectionTmp=SELECTED+'.tmp';fs.writeFileSync(selectionTmp,JSON.stringify({route:ROUTE,variant:ARM}));fs.renameSync(selectionTmp,SELECTED);
 const bytes=fs.readFileSync(path.join(EVIDENCE,'fixtures.json'));
 let extracted;
 extracted=await inflate(path.join(RUNTIME,'@sparticuz/chromium/bin/al2023.tar.br'));
 process.env.LD_LIBRARY_PATH=path.join(extracted,'lib')+':'+(process.env.LD_LIBRARY_PATH||'');
 const {default:lighthouse}=await import(pathToFileURL(require.resolve('lighthouse/core/index.js')));
 let browser,cdp;const events=[];
 try{
  browser=await chromium.launch({executablePath:await packed.executablePath(),args:chromeArgs(),headless:true});
  const version=browser.version();if(!version.startsWith('143.'))throw Error(`Expected Chromium143, got ${version}`);
  cdp=await chromium.connectOverCDP('http://127.0.0.1:9222');
  const context=cdp.contexts()[0];await context.route('**/*',resources);
  await context.exposeBinding('__p32ClsEmit',(_,event)=>events.push(event));
  await context.addInitScript(()=>{
   const emit=event=>window.__p32ClsEmit(event).catch(()=>{});
   try{new PerformanceObserver(list=>{for(const e of list.getEntries())emit({kind:'layout-shift',time:e.startTime,value:e.value,hadRecentInput:e.hadRecentInput,sources:(e.sources||[]).map(s=>({tag:s.node?.tagName||null,id:s.node?.id||null,className:typeof s.node?.className==='string'?s.node.className:null,text:s.node?.textContent?.trim().slice(0,120)||null,previous:s.previousRect?.toJSON?.()||null,current:s.currentRect?.toJSON?.()||null}))});}).observe({type:'layout-shift',buffered:true});}catch(e){emit({kind:'observer-error',message:String(e)});}
   try{document.fonts?.addEventListener('loadingdone',e=>emit({kind:'fonts-ready',time:performance.now(),faces:e.fontfaces.map(f=>({family:f.family,weight:f.weight,style:f.style,status:f.status}))}));}catch(e){emit({kind:'font-observer-error',message:String(e)});}
   try{new PerformanceObserver(list=>{for(const e of list.getEntries())emit({kind:'long-task',startTime:e.startTime,duration:e.duration,attribution:(e.attribution||[]).map(a=>({name:a.name,containerType:a.containerType,containerName:a.containerName,containerId:a.containerId,containerSrc:a.containerSrc}))});}).observe({type:'longtask',buffered:true});}catch(e){emit({kind:'longtask-observer-error',message:String(e)});}
  });
  const {lhr}=await lighthouse(BASE+ROUTE,{port:9222,output:'json',logLevel:'error',onlyCategories:['performance'],disableFullPageScreenshot:true,maxWaitForLoad:15000,disableStorageReset:false});
  if(lhr.runtimeError)throw Error(JSON.stringify(lhr.runtimeError));
  const audits={};for(const [id,a] of Object.entries(lhr.audits||{}))if(/layout.shift|cumulative-layout-shift|main-thread-tasks|long-tasks|bootup-time/i.test(id))audits[id]={score:a.score,numericValue:a.numericValue,displayValue:a.displayValue,details:a.details};
  const result={phase:32,purpose:'single-run CLS and long-task attribution diagnostic; excluded from the seven-sample 11-route A/B',local_only:true,route:ROUTE,arm:ARM,fixture_sha256:sha(bytes),browser:version,playwright:require('playwright/package.json').version,lighthouse:require('lighthouse/package.json').version,metrics:{lcp_ms:lhr.audits['largest-contentful-paint']?.numericValue,cls:lhr.audits['cumulative-layout-shift']?.numericValue,tbt_ms:lhr.audits['total-blocking-time']?.numericValue},diagnostic_audits:audits,observer_events:events,warnings:lhr.runWarnings||[],interpretation:'Diagnostic source attribution only. One Lighthouse run is not a release metric or a frozen-A/B sample.'};
  fs.writeFileSync(OUTPUT,JSON.stringify(result,null,2)+'\n');
  console.log(JSON.stringify({route:ROUTE,arm:ARM,lcp_ms:result.metrics.lcp_ms,cls:result.metrics.cls,tbt_ms:result.metrics.tbt_ms,audits:Object.keys(audits),shifts:events.filter(x=>x.kind==='layout-shift').length,output:OUTPUT},null,2));
 }finally{if(cdp)await cdp.close().catch(()=>{});if(browser)await browser.close().catch(()=>{});}
}
main().catch(error=>{console.error(error.stack||error);process.exitCode=1;});
