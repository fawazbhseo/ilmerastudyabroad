<?php
/** Only the dated owner answers establish ILMERA's service scope. */
function ilmera_scope_data()
{
    return json_decode(file_get_contents(dirname(__DIR__) . '/data/service-scope.json'), true);
}
function ilmera_scope_faqs()
{
    $d = ilmera_scope_data();
    return [
        ['question'=>'What admission checks does ILMERA help with?', 'answer'=>$d['services']['admissions'].' '.$d['decisions']],
        ['question'=>'What financial guidance does ILMERA provide?', 'answer'=>$d['services']['finance'].' '.$d['finance_limit']],
        ['question'=>'Does ILMERA help with scholarship and Italy DSU applications?', 'answer'=>$d['services']['scholarships'].' '.$d['decisions']],
        ['question'=>'What visa and supporting-document guidance does ILMERA provide?', 'answer'=>$d['services']['visa'].' '.$d['services']['documents']],
        ['question'=>'Does ILMERA help with Germany APS requirements?', 'answer'=>$d['services']['aps'].' '.$d['decisions']],
        ['question'=>'What counselling does ILMERA offer for medicine in Russia?', 'answer'=>$d['services']['medicine']],
        ['question'=>'Does ILMERA advise on working or staying after study?', 'answer'=>$d['not_offered']],
    ];
}
function ilmera_scope_sections()
{
    $d = ilmera_scope_data();
    $html = '<section id="scope-help"><h2>What ILMERA helps with</h2><ul>';
    foreach ($d['services'] as $text) $html .= '<li>'.ilmera_presentation_escape($text).'</li>';
    $html .= '</ul></section><section id="scope-exclusions"><h2>What ILMERA does not do</h2><p>'.ilmera_presentation_escape($d['not_offered']).'</p><p>'.ilmera_presentation_escape($d['decisions']).'</p><p>'.ilmera_presentation_escape($d['finance_limit']).'</p></section>';
    $html .= '<p>Owner-confirmed service scope: <time datetime="2026-10-22">22 October 2026</time>. This is not an update to official country rules.</p>';
    $html .= '<p>Existing guidance: <a href="/study-in-germany">Germany</a>, <a href="/study-in-italy">Italy</a>, <a href="/study-in-uk">UK</a>, <a href="/study-in-lithuania">Lithuania</a>, <a href="/study-in-gcc">GCC</a>, <a href="/blog/documents-needed-to-study-abroad-from-india">documents</a>, <a href="/blog/scholarships-for-indian-students-study-abroad">scholarships</a> and <a href="/blog/cost-of-studying-abroad-for-indian-students">budget planning</a>.</p>';
    $html .= '<section id="scope-faq"><h2>Questions about ILMERA service scope</h2>';
    $entities = [];
    foreach (ilmera_scope_faqs() as $faq) {
        $html .= '<details class="il-faq" style="padding:16px 0;"><summary>'.ilmera_presentation_escape($faq['question']).'</summary><div><p>'.ilmera_presentation_escape($faq['answer']).'</p></div></details>';
        $entities[] = ['@type'=>'Question','name'=>$faq['question'],'acceptedAnswer'=>['@type'=>'Answer','text'=>$faq['answer']]];
    }
    return $html.'</section><script type="application/ld+json">'.json_encode(['@context'=>'https://schema.org','@type'=>'FAQPage','@id'=>'https://ilmerastudyabroad.com/services#scope-faq','mainEntity'=>$entities], JSON_UNESCAPED_SLASHES|JSON_HEX_TAG|JSON_HEX_AMP|JSON_HEX_APOS|JSON_HEX_QUOT).'</script>';
}
function ilmera_scope_service_schema()
{
    $d = ilmera_scope_data();
    $labels = ['admissions'=>'Admissions review','finance'=>'Financial information','scholarships'=>'Scholarship guidance','budgets'=>'Cost comparison','visa'=>'Visa-document guidance','documents'=>'Supporting-document guidance','aps'=>'Germany APS guidance','medicine'=>'Russia medicine counselling'];
    $items = [];
    foreach ($d['services'] as $key=>$text) {
        $items[] = ['@type'=>'ListItem','position'=>count($items)+1,'item'=>['@type'=>'Service','@id'=>'https://ilmerastudyabroad.com/services#service-'.$key,'name'=>$labels[$key],'description'=>$text,'provider'=>['@id'=>'https://ilmerastudyabroad.com/#organization']]];
    }
    return ['@type'=>'ItemList','name'=>'ILMERA Study Abroad Services','numberOfItems'=>count($items),'itemListElement'=>$items];
}
