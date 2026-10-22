<?php
/** Final owner payment facts; fee range is visible/FAQ text, never price schema. */
function ilmera_payment_data()
{
    return json_decode(file_get_contents(dirname(__DIR__) . '/data/payment-disclosure.json'), true);
}
function ilmera_payment_pages()
{
    return ['/services','/contact','/blog/how-to-choose-study-abroad-consultant-karnataka','/blog/cost-of-studying-abroad-for-indian-students'];
}
function ilmera_payment_faqs()
{
    $d = ilmera_payment_data();
    return [
        ['question'=>'Does ILMERA charge a fee?', 'answer'=>$d['student_charge'].' '.$d['policy'].' '.$d['before_paying']],
        ['question'=>'Does ILMERA receive payments from universities?', 'answer'=>$d['university_payments']],
    ];
}
function ilmera_payment_section($path)
{
    $d = ilmera_payment_data();
    $html = '<section class="s-wrap article-body payment-disclosure" aria-label="Service charges and how ILMERA is paid"><div class="container" style="max-width:960px;"><h2>Service charges and how ILMERA is paid</h2>';
    foreach (['student_charge','university_payments','policy','before_paying'] as $key) $html .= '<p>'.ilmera_presentation_escape($d[$key]).'</p>';
    $entities = [];
    foreach (ilmera_payment_faqs() as $f) {
        $html .= '<details class="il-faq" style="padding:16px 0;"><summary>'.ilmera_presentation_escape($f['question']).'</summary><div><p>'.ilmera_presentation_escape($f['answer']).'</p></div></details>';
        $entities[] = ['@type'=>'Question','name'=>$f['question'],'acceptedAnswer'=>['@type'=>'Answer','text'=>$f['answer']]];
    }
    $graph = ['@context'=>'https://schema.org','@type'=>'FAQPage','@id'=>'https://ilmerastudyabroad.com'.$path.'#payment-faq','mainEntity'=>$entities];
    return $html.'</div></section><script type="application/ld+json">'.json_encode($graph,JSON_UNESCAPED_SLASHES|JSON_HEX_TAG|JSON_HEX_AMP|JSON_HEX_APOS|JSON_HEX_QUOT).'</script>';
}
