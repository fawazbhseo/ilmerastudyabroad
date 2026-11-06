#!/usr/bin/env node
// Supplemental desktop-only interleaved A/B for Blog-index TBT and scene safeguards.
const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto');
const {pathToFileURL}=require('node:url');
const {chromium}=require('playwright'),packed=require('@sparticuz/chromium');
const {resources}=require('../phase25/resources.cjs');
const ROOT=path.resolve(__dirname,'../..');
const RUNTIME=process.env.PHASE32_RUNTIME||'/home/user/phase32-runtime/node_modules';
const {inflate}=require(path.join(RUNTIME,'@sparticuz/chromium/build/cjs/lambdafs.cjs'));
const EVIDENCE=path.resolve(process.env.PHASE32_AB_EVIDENCE||'/home/user/phase32-runtime/phase32-ab-run02');
const FIXTURE_PATH=path.join(EVIDENCE,'fixtures.json'),SELECTED_PATH=path.join(EVIDENCE,'selected.json');
const PORT=Number(process.env.PHASE32_AB_PORT||8085),BASE=`http://127.0.0.1:${PORT}`;
const ROUTE='/blog/';
const OUTPUT=path.resolve(process.env.PHASE32_DESKTOP_BLOG_OUTPUT||path.join(EVIDENCE,'desktop-blog-ab.json'));
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const quantile=(values,q)=>{const x=[...values].sort((a,b)=>a-b),p=(x.length-1)*q,i=Math.floor(p);return x[i]+(x[Math.ceil(p)]-x[i])*(p-i);};
const summarize=samples=>Object.fromEntries(['lcp_ms','cls','tbt_ms','transfer_bytes','requests'].map(key=>{const v=samples.map(x=>x[key]);return[key,{median:quantile(v,.5),q1:quantile(v,.25),q3:quantile(v,.75),iqr:quantile(v,.75)-quantile(v,.25)}];}));
const writeJson=(file,value)=>fs.writeFileSync(file,JSON.stringify(value,null,2)+'\n');
function setSelection(variant){const temp=SELECTED_PATH+'.tmp';writeJson(temp,{route:ROUTE,variant});fs.renameSync(temp,SELECTED_PATH);}
function chromeArgs(){return[...packed.args.filter(a=>!['--single-process','--in-process-gpu'].includes(a)),'--remote-debugging-port=9222'];}
async function main(){
 if(fs.existsSync(OUTPUT))throw Error(`Refusing to overwrite desktop A/B output ${OUTPUT}`);
 const fixtureBytes=fs.readFileSync(FIXTURE_PATH),fixture=JSON.parse(fixtureBytes);
 if(!fixture[ROUTE]?.A||!fixture[ROUTE]?.B)throw Error('Frozen Blog-index A/B fixture is incomplete');
 const manifest=JSON.parse(fs.readFileSync(path.join(ROOT,'reports/phase-32-11-route-ab-fixtures.json'),'utf8'));
 if(sha(fixtureBytes)!==manifest.fixture_json_sha256)throw Error('Desktop A/B fixture hash does not match the committed manifest');
 const {default:lighthouse}=await import(pathToFileURL(require.resolve('lighthouse/core/index.js')));
 const {default:desktopConfig}=await import(pathToFileURL(require.resolve('lighthouse/core/config/desktop-config.js')));
 const bytes=await inflate(path.join(RUNTIME,'@sparticuz/chromium/bin/al2023.tar.br'));
 process.env.LD_LIBRARY_PATH=path.join(bytes,'lib')+':'+(process.env.LD_LIBRARY_PATH||'');
 const report={phase:32,task:'supplemental_blog_index_desktop_ab',status:'RUNNING',started_at:new Date().toISOString(),environment:{local_only:true,route:ROUTE,base_url:BASE,browser:'Chromium143 via @sparticuz/chromium',playwright:require('playwright/package.json').version,lighthouse:require('lighthouse/package.json').version,fixture_sha256:sha(fixtureBytes),A_source_commit:manifest.A_source_commit,B_source_commit:manifest.B_source_commit},method:{samples_per_arm:7,total_expected_samples:14,fresh_chromium_process_per_sample:true,storage_reset_each_navigation:true,order:'Round0 A then B, round1 B then A, alternating through round6',serial:true,parallel_samples:0,desktop_config:'Lighthouse core desktop-config, desktopDense4G throttling, desktop screen emulation',local_resource_mirrors:true,metrics:['LCP','CLS','TBT','transfer bytes','requests','render blockers','still-image requests','LCP element','font requests','warnings'],interpretation:'Local desktop-simulated audit for Blog index only. It is not production or field data.'},A:[],B:[],session:{status:'RUNNING'}};
 writeJson(OUTPUT,report);
 try{
  for(let round=0;round<7;round++){
   const arms=round%2?['B','A']:['A','B'];
   for(const arm of arms){
    setSelection(arm);const sample={round,arm,order:arms.join(''),started_at:new Date().toISOString(),status:'STARTED'};report[arm].push(sample);writeJson(OUTPUT,report);
    let browser,cdp;
    try{
     browser=await chromium.launch({executablePath:await packed.executablePath(),args:chromeArgs(),headless:true});
     const browserVersion=browser.version();if(!browserVersion.startsWith('143.'))throw Error(`Expected Chromium143, got ${browserVersion}`);
     cdp=await chromium.connectOverCDP('http://127.0.0.1:9222');const context=cdp.contexts()[0];await context.route('**/*',resources);
     const events=[];await context.exposeBinding('__p32DesktopEmit',(_,event)=>events.push(event));
     await context.addInitScript(()=>{
      const emit=event=>window.__p32DesktopEmit(event).catch(()=>{});
      try{new PerformanceObserver(list=>{for(const e of list.getEntries())emit({kind:'lcp',time:e.startTime,tag:e.element?.tagName||null,id:e.element?.id||null,className:typeof e.element?.className==='string'?e.element.className:null});}).observe({type:'largest-contentful-paint',buffered:true});}catch(_){}
      try{new PerformanceObserver(list=>{for(const e of list.getEntries())emit({kind:'layout-shift',time:e.startTime,value:e.value,hadRecentInput:e.hadRecentInput});}).observe({type:'layout-shift',buffered:true});}catch(_){}
      try{new PerformanceObserver(list=>{for(const e of list.getEntries())emit({kind:'long-task',startTime:e.startTime,duration:e.duration});}).observe({type:'longtask',buffered:true});}catch(_){}
      try{document.fonts?.addEventListener('loadingdone',()=>emit({kind:'fonts-ready',time:performance.now(),faces:[...document.fonts].map(f=>({family:f.family,weight:f.weight,style:f.style,status:f.status}))}));}catch(_){}
     });
     const {lhr}=await lighthouse(BASE+ROUTE,{port:9222,output:'json',logLevel:'error',onlyCategories:['performance'],disableFullPageScreenshot:true,maxWaitForLoad:15000,disableStorageReset:false},desktopConfig);
     if(lhr.runtimeError)throw Error(JSON.stringify(lhr.runtimeError));
     const audits=lhr.audits,network=audits['network-requests']?.details?.items||[];
     Object.assign(sample,{status:'PASS',completed_at:new Date().toISOString(),lcp_ms:audits['largest-contentful-paint']?.numericValue,cls:audits['cumulative-layout-shift']?.numericValue,tbt_ms:audits['total-blocking-time']?.numericValue,transfer_bytes:audits['total-byte-weight']?.numericValue,requests:network.length,render_blocking:(audits['render-blocking-resources']?.details?.items||[]).map(x=>x.url),lcp_element:audits['largest-contentful-paint-element']?.details?.items?.[0]?.items?.[0]?.node?.snippet||null,still_requests:network.filter(x=>String(x.url).includes('hero-still-')).map(x=>({url:x.url,resourceType:x.resourceType,transferSize:x.transferSize,resourceSize:x.resourceSize,statusCode:x.statusCode})),font_network:network.filter(x=>x.resourceType==='Font').map(x=>({url:x.url,bytes:x.transferSize,start:x.startTime,end:x.endTime})),observer_events:events,warnings:lhr.runWarnings||[]});
     for(const key of ['lcp_ms','cls','tbt_ms','transfer_bytes','requests'])if(!Number.isFinite(sample[key]))throw Error(`Missing non-finite Lighthouse metric ${key}`);
     console.log(`SAMPLE ${round} ${arm} LCP=${sample.lcp_ms} CLS=${sample.cls} TBT=${sample.tbt_ms} bytes=${sample.transfer_bytes}`);
    }catch(error){sample.status='FAIL';sample.completed_at=new Date().toISOString();sample.error=String(error.stack||error);report.session.status='INCOMPLETE';report.status='INCOMPLETE';report.session.failed_sample={round,arm,error:String(error.message||error)};writeJson(OUTPUT,report);throw error;}
    finally{if(cdp)await cdp.close().catch(()=>{});if(browser)await browser.close().catch(()=>{});}
    writeJson(OUTPUT,report);
   }
  }
  report.session.status='COMPLETE';report.session.finished_at=new Date().toISOString();report.session.performance_release_certified=false;
  report.summary={A:summarize(report.A),B:summarize(report.B),lcp_ratio_b_over_a:quantile(report.B.map(x=>x.lcp_ms),.5)/quantile(report.A.map(x=>x.lcp_ms),.5),tbt_delta_ms:quantile(report.B.map(x=>x.tbt_ms),.5)-quantile(report.A.map(x=>x.tbt_ms),.5)};
  report.session.tbt_delta_pass=report.summary.tbt_delta_ms<=50;report.session.samples_complete=report.A.length===7&&report.B.length===7;
  report.status='COMPLETE';writeJson(OUTPUT,report);
  console.log('SUMMARY',JSON.stringify({A:report.summary.A,B:report.summary.B,lcp_ratio:report.summary.lcp_ratio_b_over_a,tbt_delta_ms:report.summary.tbt_delta_ms,tbt_delta_pass:report.session.tbt_delta_pass,release_certified:false}));
 }catch(error){console.error(error.stack||error);process.exitCode=1;}
}
main();
