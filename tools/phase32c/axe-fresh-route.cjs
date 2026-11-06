#!/usr/bin/env node
// One isolated Chromium process per invocation, compared to the Phase31 A/AA node baseline.
const fs=require('node:fs');
const path=require('node:path');
const {launchBrowser,routePinnedResources}=require('../phase31/browser.cjs');
const ROOT=path.resolve(__dirname,'../..');
const RUNTIME=path.resolve(process.env.PHASE31_RUNTIME||'/home/user/phase32c-runtime/node_modules');
const BASE=process.env.PHASE31_BASE_URL||'http://127.0.0.1:8094';
const argv=process.argv.slice(2),get=(key,def='')=>{const i=argv.indexOf(key);return i<0?def:argv[i+1]};
const ROUTE=get('--route');
const OUT=path.resolve(get('--out'));
const BASELINE=path.join(ROOT,'reports/phase-31-accessibility-baseline.json');
const TAGS=['wcag2a','wcag2aa','wcag21a','wcag21aa'];
const identity=x=>`${x.route}|${x.id}|${x.impact}|${x.target}`;

async function main(){
 if(!['/','/services','/about','/contact'].includes(ROUTE))throw new Error(`Unexpected route ${ROUTE}`);
 if(!OUT)throw new Error('Missing --out path');
 const baseline=JSON.parse(fs.readFileSync(BASELINE,'utf8'));
 if(baseline.axe_core!=='4.11.0'||JSON.stringify(baseline.run_only)!==JSON.stringify(TAGS))throw new Error('Phase31 baseline axe version or A/AA tags differ');
 const baseCase=baseline.cases.find(x=>x.route===ROUTE&&x.width===1280&&x.javascript==='on'&&x.motion==='reduced');
 if(!baseCase)throw new Error(`No matching Phase31 reduced-motion baseline for ${ROUTE}`);
 const baselineKeys=new Set(baseCase.violations.map(identity));
 const browser=await launchBrowser();
 let row;
 try{
  const context=await browser.newContext({viewport:{width:1280,height:900},javaScriptEnabled:true,reducedMotion:'reduce'});
  const page=await context.newPage();
  await routePinnedResources(page);
  const response=await page.goto(BASE+ROUTE,{waitUntil:'domcontentloaded',timeout:45000});
  if(!response||response.status()!==200)throw new Error(`HTTP ${response?.status()} for ${ROUTE}`);
  await page.waitForTimeout(3000);
  const axeSource=fs.readFileSync(path.join(RUNTIME,'axe-core/axe.min.js'),'utf8');
  await page.addScriptTag({content:axeSource});
  const scan=await page.evaluate(async tags=>{
   const result=await axe.run(document,{runOnly:{type:'tag',values:tags}});
   return {version:axe.version,violations:result.violations.map(v=>({id:v.id,impact:v.impact,nodes:v.nodes.map(n=>({target:n.target.join(' '),summary:n.failureSummary||'',html:n.html.slice(0,280)}))})),incomplete:result.incomplete.map(v=>({id:v.id,impact:v.impact,nodes:v.nodes.length}))};
  },TAGS);
  const violations=scan.violations.flatMap(v=>v.nodes.map(n=>({route:ROUTE,id:v.id,impact:v.impact,target:n.target,summary:n.summary,html:n.html})));
  const currentKeys=new Set(violations.map(identity));
  const added=[...currentKeys].filter(key=>!baselineKeys.has(key)).sort();
  const removed=[...baselineKeys].filter(key=>!currentKeys.has(key)).sort();
  row={
   status:added.length?'FAIL_NEW_NODE_IDENTITY':'PASS_BASELINE_RELATIVE',
   route:ROUTE,
   width:1280,
   height:900,
   javascript:true,
   reduced_motion:true,
   settle_ms:3000,
   browser_process_launched_for_this_route:true,
   node_pid:process.pid,
   browser:browser.version(),
   http_status:response.status(),
   axe_version:scan.version,
   run_only:TAGS,
   violation_node_count:violations.length,
   violation_rule_count:scan.violations.length,
   baseline_node_count:baselineKeys.size,
   added_node_identities:added,
   removed_node_identities:removed,
   violations,
   incomplete:scan.incomplete,
   interpretation:'PASS means no route/rule/impact/target identity outside the Phase31 baseline for this route and state. Preserved findings are reported and are not described as zero violations.',
  };
  await context.close();
 }finally{
  await browser.close();
 }
 fs.mkdirSync(path.dirname(OUT),{recursive:true});
 fs.writeFileSync(OUT,JSON.stringify(row,null,2)+'\n');
 console.log(`${row.status} fresh-process axe ${ROUTE}: ${row.violation_node_count} nodes, ${row.added_node_identities.length} new identities, ${row.removed_node_identities.length} removed`);
 if(row.added_node_identities.length)process.exitCode=1;
}
main().catch(error=>{console.error(error.stack||error);process.exit(1)});
