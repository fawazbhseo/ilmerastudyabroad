#!/usr/bin/env node
// One authorized local-only interleaved Lighthouse A/B session. No resume or retries.
const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto');
const {pathToFileURL}=require('node:url');
const {chromium}=require('playwright'),packed=require('@sparticuz/chromium');
const {resources}=require('../phase25/resources.cjs');
const ROOT=path.resolve(__dirname,'../..');
const EVIDENCE=path.resolve(process.env.PHASE31_AB_EVIDENCE||'/home/user/phase31/task4');
const FIXTURE_PATH=path.join(EVIDENCE,'fixtures.json'),SELECTED_PATH=path.join(EVIDENCE,'selected.json');
const PORT=Number(process.env.PHASE31_AB_PORT||8082),BASE=`http://127.0.0.1:${PORT}`;
const OUTPUT=path.join(EVIDENCE,'ab-results.json');
const CONTROLS=['/','/services','/about','/contact'];
const CONTROL_RATIO_LIMIT=1.10,ROUTE_BUDGETS={added_transfer_bytes_lt:150000,lcp_ratio_lte:1.10,tbt_delta_ms_lte:50,cls_b_no_greater_than_a:true,cls_b_lt:0.1,no_new_render_blocking:true};
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const quantile=(values,q)=>{const x=[...values].sort((a,b)=>a-b),p=(x.length-1)*q,i=Math.floor(p);return x[i]+(x[Math.ceil(p)]-x[i])*(p-i);};
const summarize=samples=>Object.fromEntries(['lcp_ms','cls','tbt_ms','transfer_bytes','requests'].map(key=>{const v=samples.map(x=>x[key]);return[key,{median:quantile(v,.5),q1:quantile(v,.25),q3:quantile(v,.75),iqr:quantile(v,.75)-quantile(v,.25)}];}));
const writeJson=(file,value)=>fs.writeFileSync(file,JSON.stringify(value,null,2)+'\n');
function setSelection(route,variant){const tmp=SELECTED_PATH+'.tmp';writeJson(tmp,{route,variant});fs.renameSync(tmp,SELECTED_PATH);}
function calculateRow(row){
 if(row.A.length!==7||row.B.length!==7)throw Error(`Incomplete arm counts for ${row.route}: A=${row.A.length}, B=${row.B.length}`);
 row.summary={A:summarize(row.A),B:summarize(row.B)};const a=row.summary.A,b=row.summary.B;
 row.ratio_b_over_a=b.lcp_ms.median/a.lcp_ms.median;
 row.symmetric_lcp_ratio=Math.max(row.ratio_b_over_a,1/row.ratio_b_over_a);
 row.added_transfer_bytes=b.transfer_bytes.median-a.transfer_bytes.median;
 const blocksA=new Set(row.A.flatMap(s=>s.render_blocking||[]));
 row.new_render_blocking=[...new Set(row.B.flatMap(s=>s.render_blocking||[]))].filter(u=>!blocksA.has(u));
 row.tests={added_transfer:row.added_transfer_bytes<ROUTE_BUDGETS.added_transfer_bytes_lt,lcp:row.ratio_b_over_a<=ROUTE_BUDGETS.lcp_ratio_lte,tbt:b.tbt_ms.median<=a.tbt_ms.median+ROUTE_BUDGETS.tbt_delta_ms_lte,cls:b.cls.median<=a.cls.median&&b.cls.median<ROUTE_BUDGETS.cls_b_lt,no_new_render_blocking:row.new_render_blocking.length===0};
 row.local_budget_result=Object.values(row.tests).every(Boolean)?'PASS':'FAIL';
 row.control_reliability=CONTROLS.includes(row.route)?row.symmetric_lcp_ratio<=CONTROL_RATIO_LIMIT:null;
 row.observed_still_requests={A:row.A.flatMap(s=>s.still_requests||[]),B:row.B.flatMap(s=>s.still_requests||[])};
}
async function main(){
 if(fs.existsSync(OUTPUT))throw Error(`Refusing to overwrite existing A/B evidence: ${OUTPUT}`);
 const fixtureBytes=fs.readFileSync(FIXTURE_PATH),fixtures=JSON.parse(fixtureBytes);
 const fixtureManifest=JSON.parse(fs.readFileSync(path.join(ROOT,'reports/phase-31-task4-ab-fixtures.json'),'utf8'));
 if(sha(fixtureBytes)!==fixtureManifest.fixture_json_sha256)throw Error('Frozen A/B fixture hash does not match its committed manifest');
 const routes=Object.keys(fixtures);
 if(routes.length!==8||CONTROLS.some(r=>!fixtures[r]))throw Error(`Expected the authorized eight-route list with four controls, got ${routes.length}`);
 for(const [route,pair] of Object.entries(fixtures))if(!pair.A||!pair.B)throw Error(`Missing A/B fixture for ${route}`);
 const {default:lighthouse}=await import(pathToFileURL(require.resolve('lighthouse/core/index.js')));
 const report={phase:31,task:4,status:'RUNNING',started_at:new Date().toISOString(),environment:{local_only:true,base_url:BASE,browser:'Chromium143 via @sparticuz/chromium',playwright:require('playwright/package.json').version,lighthouse:require('lighthouse/package.json').version,fixture_sha256:sha(fixtureBytes),A_source_commit:fixtureManifest.A_source_commit,B_source_commit:fixtureManifest.B_source_commit},method:{samples_per_arm_per_route:7,total_routes:routes.length,total_expected_samples:routes.length*14,fresh_chromium_process_per_sample:true,storage_reset_each_navigation:true,order:'Round0 A then B, round1 B then A, alternating through round6 for each route',serial:true,parallel_samples:0,concurrent_capture_or_QA:false,performance_model:'Lighthouse mobile simulated Slow4G and 4x CPU',resource_delivery:'All browser traffic is intercepted to the local fixture, local static assets or exact npm mirrors; unsupported external requests are aborted. URL names are diagnostics, not live-network proof.',full_page_report_screenshot:false,metrics_retained:['LCP','CLS','TBT','total transfer bytes','request count','render-blocking request URLs','still-image requests','font network records','passive LCP/font/paint-gate events','warnings','failed/incomplete sessions'],budgets:ROUTE_BUDGETS,control_rule:`Each of the four unchanged reference routes must have symmetric median LCP ratio <= ${CONTROL_RATIO_LIMIT} for a reliable local session. No retry or resume is allowed.`,interpretation:'Local simulated evidence only. Not field data, real CDN timing, native hosting proof or a live-speed claim.'},route_order:routes,control_routes:CONTROLS,session:{routes:[],status:'RUNNING'}};
 writeJson(OUTPUT,report);
 let browserVersion='unknown';
 try{
  for(const route of routes){
   const row={route,A:[],B:[],summary:null};report.session.routes.push(row);writeJson(OUTPUT,report);
   for(let round=0;round<7;round++){
    const arms=round%2?['B','A']:['A','B'];
    for(const arm of arms){
     setSelection(route,arm);const sample={round,arm,order:arms.join(''),started_at:new Date().toISOString(),status:'STARTED'};
     row[arm].push(sample);writeJson(OUTPUT,report);
     let browser,cdp;
     try{
      browser=await chromium.launch({executablePath:await packed.executablePath(),args:[...packed.args.filter(a=>!['--single-process','--in-process-gpu'].includes(a)),'--remote-debugging-port=9222'],headless:true});
      browserVersion=browser.version();if(!browserVersion.startsWith('143.'))throw Error(`Expected pinned Chromium143, got ${browserVersion}`);
      cdp=await chromium.connectOverCDP('http://127.0.0.1:9222');const context=cdp.contexts()[0];
      await context.route('**/*',resources);const observed=[];await context.exposeBinding('__p31Emit',(_,event)=>observed.push(event));
      await context.addInitScript(()=>{
       const emit=event=>window.__p31Emit(event).catch(()=>{});
       const watch=()=>{if(!document.documentElement)return false;new MutationObserver(()=>emit({kind:'paint_gate',time:performance.now(),pending:document.documentElement.classList.contains('p25-font-pending')})).observe(document.documentElement,{attributes:true,attributeFilter:['class']});return true;};
       if(!watch()){const observer=new MutationObserver(()=>{if(watch())observer.disconnect();});observer.observe(document,{childList:true});}
       document.fonts?.addEventListener('loadingdone',()=>emit({kind:'fonts_ready',time:performance.now(),faces:[...document.fonts].map(f=>({family:f.family,weight:f.weight,status:f.status}))}));
       new PerformanceObserver(list=>{for(const entry of list.getEntries())emit({kind:'lcp',time:entry.startTime,size:entry.size,tag:entry.element?.tagName,selector:entry.element?.id?'#'+entry.element.id:entry.element?.className,html:entry.element?.outerHTML.slice(0,500),font:entry.element?{family:getComputedStyle(entry.element).fontFamily,size:getComputedStyle(entry.element).fontSize,weight:getComputedStyle(entry.element).fontWeight}:null});}).observe({type:'largest-contentful-paint',buffered:true});
      });
      const {lhr}=await lighthouse(BASE+route,{port:9222,output:'json',logLevel:'error',onlyCategories:['performance'],disableFullPageScreenshot:true,maxWaitForLoad:15000,disableStorageReset:false});
      if(lhr.runtimeError)throw Error(JSON.stringify(lhr.runtimeError));
      const audits=lhr.audits,network=audits['network-requests']?.details?.items||[];
      const sanitize=url=>url?.startsWith('data:')?'data:font;sha256='+sha(Buffer.from(url)):url;
      Object.assign(sample,{status:'PASS',completed_at:new Date().toISOString(),lcp_ms:audits['largest-contentful-paint']?.numericValue,cls:audits['cumulative-layout-shift']?.numericValue,tbt_ms:audits['total-blocking-time']?.numericValue,transfer_bytes:audits['total-byte-weight']?.numericValue,requests:network.length,render_blocking:(audits['render-blocking-resources']?.details?.items||[]).map(item=>item.url),lcp_element:audits['largest-contentful-paint-element']?.details?.items?.[0]?.items?.[0]?.node?.snippet||null,still_requests:network.filter(item=>String(item.url).includes('hero-still-')).map(item=>({url:item.url,resourceType:item.resourceType,transferSize:item.transferSize,resourceSize:item.resourceSize,statusCode:item.statusCode})),font_network:network.filter(item=>item.resourceType==='Font').map(item=>({url:sanitize(item.url),bytes:item.transferSize,start:item.startTime,end:item.endTime})),non_fixture_origin_requests:network.filter(item=>{try{return new URL(item.url).origin!==BASE}catch{return true}}).map(item=>({url:sanitize(item.url),resourceType:item.resourceType,statusCode:item.statusCode,transferSize:item.transferSize})),diagnostic:{events:observed,note:'Passive early LCP, font readiness and paint-gate observations only; not Lighthouse simulated-clock timestamps.'},warnings:lhr.runWarnings||[]});
      for(const key of ['lcp_ms','cls','tbt_ms','transfer_bytes','requests'])if(!Number.isFinite(sample[key]))throw Error(`Missing non-finite Lighthouse metric ${key}`);
      console.log(`SAMPLE ${routes.indexOf(route)+1}/${routes.length} ${route} round${round} ${arm} LCP=${sample.lcp_ms} CLS=${sample.cls} TBT=${sample.tbt_ms} bytes=${sample.transfer_bytes}`);
     }catch(error){
      sample.status='FAIL';sample.completed_at=new Date().toISOString();sample.error=String(error.stack||error);report.session.status='INCOMPLETE';report.session.failed_sample={route,round,arm,error:String(error.message||error)};report.status='INCOMPLETE';writeJson(OUTPUT,report);throw error;
     }finally{if(cdp)await cdp.close().catch(()=>{});if(browser)await browser.close().catch(()=>{});}
     report.environment.chromium=browserVersion;writeJson(OUTPUT,report);
    }
   }
   calculateRow(row);writeJson(OUTPUT,report);
  }
  const controls=report.session.routes.filter(row=>CONTROLS.includes(row.route));
  report.session.control_reliable=controls.length===4&&controls.every(row=>row.control_reliability===true);
  report.session.routes_complete=report.session.routes.length===routes.length&&report.session.routes.every(row=>row.A.length===7&&row.B.length===7);
  report.session.local_budgets_passed=report.session.routes_complete&&report.session.routes.every(row=>row.local_budget_result==='PASS');
  report.session.performance_release_certified=false;
  report.session.finished_at=new Date().toISOString();report.session.status='COMPLETE';
  report.status='COMPLETE';report.conclusion='One completed local simulated A/B session. Results describe only this pinned fixture and browser environment. No live or field-speed claim, release certification, merge, deployment or change to historical benchmark files.';
  report.session.totals={samples:report.session.routes.reduce((sum,row)=>sum+row.A.length+row.B.length,0),A:report.session.routes.reduce((sum,row)=>sum+row.A.length,0),B:report.session.routes.reduce((sum,row)=>sum+row.B.length,0),routes_passing_local_budgets:report.session.routes.filter(row=>row.local_budget_result==='PASS').length};
  writeJson(OUTPUT,report);
  for(const row of report.session.routes)console.log('SUMMARY',row.route,'A_LCP',row.summary.A.lcp_ms.median,'B_LCP',row.summary.B.lcp_ms.median,'ratio',row.ratio_b_over_a,'local',row.local_budget_result);
  console.log('COMPLETE',JSON.stringify(report.session.totals),'control_reliable',report.session.control_reliable,'release_certified',false);
 }catch(error){console.error(error.stack||error);process.exitCode=1;}
}
main();
