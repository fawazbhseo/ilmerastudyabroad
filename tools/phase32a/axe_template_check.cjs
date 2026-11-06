#!/usr/bin/env node
// One representative axe-core 4.11 scan per Phase32a template, with baseline deltas where available.
const fs=require('node:fs'),path=require('node:path');
const {launchBrowser,routePinnedResources}=require('../phase31/browser.cjs');
const ROOT=path.resolve(__dirname,'../..'),BASE=process.env.PHASE31_BASE_URL||'http://127.0.0.1:8094';
const ROUTES=[['destination','/study-in-germany'],['place','/study-abroad-counselling-mysuru'],['article','/blog/how-to-choose-study-abroad-consultant-karnataka'],['blog-index','/blog/'],['legal','/privacy-policy'],['utility','/all-pages']];
const OUT=process.env.PHASE32A_AXE_OUT||'/home/user/phase32a-runtime/phase32a-full-suite-run01/axe.json';
const BASELINE=path.join(ROOT,'reports/phase-31-accessibility-baseline.json');
const key=x=>`${x.route}|${x.id}|${x.impact}|${x.target}`;
(async()=>{
 const browser=await launchBrowser(),cases=[];let report;
 try{
  const axePath=require.resolve('axe-core/axe.min.js');
  for(const [template,route] of ROUTES){const context=await browser.newContext({viewport:{width:1280,height:900},javaScriptEnabled:true,reducedMotion:'reduce'}),page=await context.newPage();await routePinnedResources(page);const response=await page.goto(BASE+route,{waitUntil:'domcontentloaded',timeout:45000});if(!response||response.status()!==200)throw Error(`HTTP ${response?.status()} for ${route}`);await page.waitForTimeout(3000);await page.addScriptTag({path:axePath});const scan=await page.evaluate(async()=>{const result=await axe.run(document,{runOnly:{type:'tag',values:['wcag2a','wcag2aa','wcag21a','wcag21aa']}});return{version:axe.version,violations:result.violations.map(v=>({id:v.id,impact:v.impact,nodes:v.nodes.map(n=>({target:n.target.join(' '),summary:n.failureSummary||'',html:n.html.slice(0,280)}))}))};});const violations=scan.violations.flatMap(v=>v.nodes.map(n=>({route,id:v.id,impact:v.impact,target:n.target,summary:n.summary,html:n.html})));cases.push({template,route,width:1280,javascript:true,reduced_motion:true,http_status:response.status(),axe_version:scan.version,violation_count:violations.length,violations});await context.close();console.log(`AXE ${template} ${route} ${violations.length}`);}
 }finally{await browser.close();}
 const old=JSON.parse(fs.readFileSync(BASELINE,'utf8'));const baseKeys=new Set(old.cases.flatMap(c=>c.violations.map(key))),nowKeys=new Set(cases.flatMap(c=>c.violations.map(key)));
 const overlaps=ROUTES.slice(0,4).map(x=>x[1]);const added=[...nowKeys].filter(k=>overlaps.includes(k.split('|')[0])&&!baseKeys.has(k));const removed=[...baseKeys].filter(k=>overlaps.includes(k.split('|')[0])&&!nowKeys.has(k));
 report={status:added.length?'FAIL_NEW_BASELINE_RELATIVE_FINDINGS':'PASS_BASELINE_RELATIVE',axe_core:'4.11.0',run_only:['wcag2a','wcag2aa','wcag21a','wcag21aa'],representatives:ROUTES.map(([template,route])=>({template,route})),viewport:{width:1280,height:900},javascript:true,reduced_motion:true,settle_ms:3000,total_violation_nodes:cases.reduce((n,c)=>n+c.violation_count,0),baseline_comparison:{path:BASELINE,compared_templates:overlaps,added,removed,baseline_unavailable_templates:['legal','utility']},cases,interpretation:'Baseline-relative pass means no new stable axe rule/impact/target identities on the four templates represented in the Phase31 baseline. Legal and utility are scanned and reported without a prior representative baseline. Existing findings do not mean zero violations or full-site accessibility certification.'};
 fs.mkdirSync(path.dirname(path.resolve(OUT)),{recursive:true});fs.writeFileSync(path.resolve(OUT),JSON.stringify(report,null,2)+'\n');console.log(report.status,'nodes',report.total_violation_nodes,'added',added.length,'unbaselined templates=2');if(added.length)process.exit(1);
})().catch(e=>{console.error(e.stack||e);process.exit(1)});
