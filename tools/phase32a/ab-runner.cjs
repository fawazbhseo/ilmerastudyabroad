#!/usr/bin/env node
// Phase32a local six-route Lighthouse A/B. Raw samples only, no analysis or retries.
const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto');
const {pathToFileURL}=require('node:url');
const {chromium}=require('playwright'),packed=require('@sparticuz/chromium');
const {resources}=require('../phase25/resources.cjs');
const ROOT=path.resolve(__dirname,'../..');
const RUNTIME=process.env.PHASE32_RUNTIME||'/home/user/phase32a-runtime/node_modules';
const {inflate}=require(path.join(RUNTIME,'@sparticuz/chromium/build/cjs/lambdafs.cjs'));
const EVIDENCE=path.resolve(process.env.PHASE32A_AB_EVIDENCE||'/home/user/phase32a-runtime/phase32a-ab-run01');
const FIXTURE_PATH=path.join(EVIDENCE,'fixtures.json'),SELECTED_PATH=path.join(EVIDENCE,'selected.json');
const PORT=Number(process.env.PHASE32A_AB_PORT||8092),BASE=`http://127.0.0.1:${PORT}`;
const OUTPUT=path.resolve(process.env.PHASE32A_AB_OUTPUT||path.join(ROOT,'reports/phase-32a-6-route-ab-run-01-raw.json'));
const EXPECTED=['/study-in-germany','/study-abroad-counselling-mysuru','/blog/how-to-choose-study-abroad-consultant-karnataka','/blog/','/services','/contact'];
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const writeJson=(file,value)=>fs.writeFileSync(file,JSON.stringify(value,null,2)+'\n');
function select(route,variant){const tmp=SELECTED_PATH+'.tmp';writeJson(tmp,{route,variant});fs.renameSync(tmp,SELECTED_PATH);}
function chromeArgs(){return[...packed.args.filter(a=>!['--single-process','--in-process-gpu'].includes(a)),'--remote-debugging-port=9222'];}
async function ensureRuntime(){const root=await inflate(path.join(RUNTIME,'@sparticuz/chromium/bin/al2023.tar.br'));process.env.LD_LIBRARY_PATH=path.join(root,'lib')+':'+(process.env.LD_LIBRARY_PATH||'');}
async function checkFixtureServer(fixtures,manifest){
 for(const route of EXPECTED)for(const arm of ['A','B']){
  select(route,arm);const response=await fetch(BASE+route);const body=Buffer.from(await response.arrayBuffer());
  if(response.status!==200||body.toString('utf8')!==fixtures[route][arm])throw Error(`Fixture server mismatch for ${route} ${arm}: HTTP ${response.status}, sha=${sha(body)}`);
 }
 if(manifest.fixture_json_sha256!==sha(fs.readFileSync(FIXTURE_PATH)))throw Error('Fixture hash changed after freeze');
}
async function main(){
 await ensureRuntime();
 if(!fs.existsSync(FIXTURE_PATH)||!fs.existsSync(SELECTED_PATH))throw Error('Frozen six-route fixture and selected.json are required');
 const fixtureBytes=fs.readFileSync(FIXTURE_PATH),fixtures=JSON.parse(fixtureBytes),manifest=JSON.parse(fs.readFileSync(path.join(ROOT,'reports/phase-32a-six-route-fixtures.json'),'utf8'));
 if(sha(fixtureBytes)!==manifest.fixture_json_sha256)throw Error('A/B fixture hash does not match the committed six-route manifest');
 if(JSON.stringify(Object.keys(fixtures))!==JSON.stringify(EXPECTED))throw Error('Frozen fixture routes or order differ from the six-route protocol');
 if(manifest.A_source_commit!=='7d1bb9ec0522bcbc7953262920fafb50bf04ab72'||manifest.content_invariant_failures!==0)throw Error('Six-route fixture manifest does not pass required A-source/content guards');
 for(const route of EXPECTED)if(!fixtures[route]?.A||!fixtures[route]?.B)throw Error(`Missing A or B HTML for ${route}`);
 await checkFixtureServer(fixtures,manifest);
 if(process.argv.includes('--preflight-only')){
  let browser,cdp;try{browser=await chromium.launch({executablePath:await packed.executablePath(),args:chromeArgs(),headless:true});const version=browser.version();if(!version.startsWith('143.'))throw Error(`Expected Chromium143, got ${version}`);cdp=await chromium.connectOverCDP('http://127.0.0.1:9222');console.log(`PASS six-route fixture/Chromium preflight: ${version}, all twelve local A/B route bodies match the frozen fixture; zero Lighthouse samples`);}finally{if(cdp)await cdp.close().catch(()=>{});if(browser)await browser.close().catch(()=>{});}return;
 }
 if(fs.existsSync(OUTPUT))throw Error(`Refusing to overwrite prior raw evidence ${OUTPUT}`);
 const {default:lighthouse}=await import(pathToFileURL(require.resolve('lighthouse/core/index.js')));
 const report={phase:'32a',task:'six_route_interleaved_lighthouse_ab',status:'RUNNING',started_at:new Date().toISOString(),environment:{local_only:true,fixture_sha256:sha(fixtureBytes),A_source_commit:manifest.A_source_commit,B_rendered_source_head:manifest.B_rendered_source_head,B_current_head_at_fixture_freeze:manifest.B_current_head_at_freeze,browser:'Chromium 143 via @sparticuz/chromium',playwright:require('playwright/package.json').version,lighthouse:require('lighthouse/package.json').version,base_url:BASE},protocol:{route_order:EXPECTED,samples_per_arm_per_route:7,total_expected_samples:84,fresh_chromium_process_per_sample:true,serial:true,parallel_samples:0,round_order:'For each route: A/B on even rounds, B/A on odd rounds, seven rounds per arm; no retry, resume or skipped samples',lighthouse_model:'Default mobile simulated Slow4G and 4x CPU',resource_delivery:'All navigations and browser assets use the local fixture server or pinned local resource mirrors. Unsupported external requests are aborted; no production CDN or field timing.',metrics_retained:['absolute LCP ms','TBT ms','CLS','total transfer bytes','request count','LCP element','render-blocking URLs','still request URL/bytes/status','font request URLs/bytes/timings','warnings','failed sample details'],analysis:'Raw samples only. Do not derive medians, IQRs, ratios or budget outcomes until this raw file is committed and pushed.',budgets:{added_transfer_bytes_lt:150000,lcp_ratio_b_over_a_lte:1.10,tbt_delta_ms_lte:50,cls_b_no_greater_than_a:true,cls_b_lt:0.1,no_new_render_blocking:true},control_routes:['/services','/contact'],control_interpretation:manifest.reference_control_note,performance_release_certified:false},samples:[],session:{status:'RUNNING',completed_samples:0,expected_samples:84,failed_sample:null}};
 writeJson(OUTPUT,report);let browserVersion='unknown';
 try{
  for(const route of EXPECTED){for(let round=0;round<7;round++){
   const arms=round%2?['B','A']:['A','B'];
   for(const arm of arms){
    select(route,arm);const sample={route,round,arm,order:arms.join('/'),started_at:new Date().toISOString(),status:'STARTED'};report.samples.push(sample);writeJson(OUTPUT,report);
    let browser,cdp;
    try{
     browser=await chromium.launch({executablePath:await packed.executablePath(),args:chromeArgs(),headless:true});browserVersion=browser.version();if(!browserVersion.startsWith('143.'))throw Error(`Expected Chromium143, got ${browserVersion}`);
     cdp=await chromium.connectOverCDP('http://127.0.0.1:9222');const context=cdp.contexts()[0];await context.route('**/*',resources);
     const events=[];await context.exposeBinding('__p32aEmit',(_,event)=>events.push(event));
     await context.addInitScript(()=>{
      const emit=event=>window.__p32aEmit(event).catch(()=>{});
      try{new PerformanceObserver(list=>{for(const e of list.getEntries())emit({kind:'lcp',time:e.startTime,size:e.size,tag:e.element?.tagName||null,id:e.element?.id||null,class_name:typeof e.element?.className==='string'?e.element.className:null});}).observe({type:'largest-contentful-paint',buffered:true});}catch(_){}
      try{document.fonts?.addEventListener('loadingdone',()=>emit({kind:'fonts_ready',time:performance.now(),faces:[...document.fonts].map(f=>({family:f.family,weight:f.weight,style:f.style,status:f.status}))}));}catch(_){}
     });
     const {lhr}=await lighthouse(BASE+route,{port:9222,output:'json',logLevel:'error',onlyCategories:['performance'],disableFullPageScreenshot:true,maxWaitForLoad:15000,disableStorageReset:false});
     if(lhr.runtimeError)throw Error(JSON.stringify(lhr.runtimeError));
     const audits=lhr.audits,network=audits['network-requests']?.details?.items||[];
     Object.assign(sample,{status:'PASS',completed_at:new Date().toISOString(),lcp_ms:audits['largest-contentful-paint']?.numericValue,cls:audits['cumulative-layout-shift']?.numericValue,tbt_ms:audits['total-blocking-time']?.numericValue,transfer_bytes:audits['total-byte-weight']?.numericValue,requests:network.length,lcp_element:audits['largest-contentful-paint-element']?.details?.items?.[0]?.items?.[0]?.node?.snippet||null,render_blocking:(audits['render-blocking-resources']?.details?.items||[]).map(item=>item.url),still_requests:network.filter(item=>String(item.url).includes('hero-still-')).map(item=>({url:item.url,resourceType:item.resourceType,transferSize:item.transferSize,resourceSize:item.resourceSize,statusCode:item.statusCode})),font_network:network.filter(item=>item.resourceType==='Font').map(item=>({url:item.url,transferSize:item.transferSize,resourceSize:item.resourceSize,startTime:item.startTime,endTime:item.endTime,statusCode:item.statusCode})),warnings:lhr.runWarnings||[],observer_events:events});
     for(const key of ['lcp_ms','cls','tbt_ms','transfer_bytes','requests'])if(!Number.isFinite(sample[key]))throw Error(`Missing non-finite metric ${key}`);
     report.session.completed_samples++;console.log(`SAMPLE ${report.session.completed_samples}/84 ${route} round${round} ${arm} status=PASS`);
    }catch(error){sample.status='FAIL';sample.completed_at=new Date().toISOString();sample.error=String(error.stack||error);report.status='INCOMPLETE';report.session.status='INCOMPLETE';report.session.failed_sample={route,round,arm,error:String(error.message||error)};writeJson(OUTPUT,report);throw error;}
    finally{if(cdp)await cdp.close().catch(()=>{});if(browser)await browser.close().catch(()=>{});}
    writeJson(OUTPUT,report);
   }
  }}
  report.status='COMPLETE';report.finished_at=new Date().toISOString();report.environment.chromium=browserVersion;report.session.status='COMPLETE';report.session.complete_samples=report.samples.length===84;report.session.performance_release_certified=false;writeJson(OUTPUT,report);
  console.log(`RAW COMPLETE ${report.samples.length}/84 ${OUTPUT} SHA256=${sha(fs.readFileSync(OUTPUT))}`);
 }catch(error){console.error(error.stack||error);process.exitCode=1;}
}
main();
