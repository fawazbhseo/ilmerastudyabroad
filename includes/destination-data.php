<?php
require_once __DIR__ . '/place-data.php';

function ilmera_destination_slugs()
{
    return ['germany', 'italy', 'uk', 'czech-republic', 'lithuania', 'latvia', 'slovakia', 'russia', 'gcc'];
}

function ilmera_destination_groups()
{
    return ['who_its_for' => 'Who it is for', 'english_requirements' => 'English requirements', 'costs' => 'Costs', 'scholarships' => 'Scholarships', 'visa_steps' => 'Visa steps', 'intakes' => 'Intakes', 'documents' => 'Documents', 'work_and_stay' => 'Work and stay'];
}

function ilmera_destination_date($value)
{
    if (!is_string($value) || !preg_match('/^(\d{4})-(\d{2})-(\d{2})$/D', $value, $parts)) return '';
    return checkdate((int) $parts[2], (int) $parts[3], (int) $parts[1]) ? $value : '';
}

function ilmera_destination_source($item, $hosts)
{
    if (!is_array($item)) return null;
    $label = ilmera_place_text($item['source_label'] ?? '');
    $url = ilmera_place_text($item['source_url'] ?? '');
    if ($label === '' || $url === '' || !filter_var($url, FILTER_VALIDATE_URL)) return null;
    $parts = parse_url($url);
    if (!$parts || ($parts['scheme'] ?? '') !== 'https' || isset($parts['user']) || isset($parts['pass']) || isset($parts['port'])) return null;
    $host = strtolower($parts['host'] ?? '');
    $approved = false;
    foreach ($hosts as $allowedHost) {
        if ($host === $allowedHost || substr($host, -strlen('.' . $allowedHost)) === '.' . $allowedHost) {
            $approved = true;
            break;
        }
    }
    if (!$approved) return null;
    return ['source_label' => $label, 'source_url' => $url, 'checked_on' => ilmera_destination_date($item['checked_on'] ?? '')];
}

function ilmera_destination_normalize($data, $slug)
{
    if (!is_array($data) || !in_array($slug, ilmera_destination_slugs(), true) || ($data['slug'] ?? '') !== $slug) return null;
    if (!in_array($data['status'] ?? '', ['draft', 'published'], true)) return null;
    $name = ilmera_place_text($data['name'] ?? '');
    if ($name === '') return null;
    $result = ['slug' => $slug, 'name' => $name, 'status' => $data['status'], 'official_source_hosts' => []];
    foreach (is_array($data['official_source_hosts'] ?? null) ? $data['official_source_hosts'] : [] as $host) {
        if (is_string($host) && preg_match('/^(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z]{2,}$/iD', $host)) $result['official_source_hosts'][] = strtolower($host);
    }
    $result['official_source_hosts'] = array_values(array_unique($result['official_source_hosts']));
    $result['ilmera_summary'] = ilmera_place_text($data['ilmera_summary'] ?? '');
    $result['facts_last_checked'] = ilmera_destination_date($data['facts_last_checked'] ?? '');
    $result['intro_answer'] = '';
    $result['intro_source'] = null;
    $intro = ilmera_place_text($data['intro_answer'] ?? '');
    $words = preg_match_all('/\S+/u', $intro);
    $source = ilmera_destination_source(['source_url' => $data['intro_answer_source_url'] ?? '', 'source_label' => $data['intro_answer_source_label'] ?? '', 'checked_on' => $data['intro_answer_checked_on'] ?? ''], $result['official_source_hosts']);
    if ($words >= 40 && $words <= 60 && $source) {
        $result['intro_answer'] = $intro;
        $result['intro_source'] = $source;
    }
    foreach (ilmera_destination_groups() as $field => $heading) {
        $result[$field] = [];
        foreach (is_array($data[$field] ?? null) ? $data[$field] : [] as $item) {
            $source = ilmera_destination_source($item, $result['official_source_hosts']);
            $text = ilmera_place_text(is_array($item) ? ($item['text'] ?? '') : '');
            if ($source && $text !== '') $result[$field][] = array_merge(['text' => $text], $source);
        }
    }
    $result['faqs'] = [];
    foreach (is_array($data['faqs'] ?? null) ? $data['faqs'] : [] as $faq) {
        $source = ilmera_destination_source($faq, $result['official_source_hosts']);
        $question = ilmera_place_text(is_array($faq) ? ($faq['question'] ?? '') : '');
        $answer = ilmera_place_text(is_array($faq) ? ($faq['answer'] ?? '') : '');
        if ($source && $question !== '' && $answer !== '') $result['faqs'][] = array_merge(['question' => $question, 'answer' => $answer], $source);
    }
    return $result;
}

function ilmera_destination_load($slug)
{
    static $cache = [];
    if (!is_string($slug) || !in_array($slug, ilmera_destination_slugs(), true)) return null;
    if (array_key_exists($slug, $cache)) return $cache[$slug];
    $file = dirname(__DIR__) . '/destinations/' . $slug . '.php';
    if (!is_file($file)) return $cache[$slug] = null;
    $data = (static function ($path) { return include $path; })($file);
    return $cache[$slug] = ilmera_destination_normalize($data, $slug);
}

function ilmera_destination_fact_count($data)
{
    if (!is_array($data)) return 0;
    $count = $data['intro_answer'] !== '' ? 1 : 0;
    foreach (array_merge(array_keys(ilmera_destination_groups()), ['faqs']) as $field) if (!empty($data[$field])) $count++;
    return $count;
}

function ilmera_destination_indexable($data)
{
    return is_array($data) && $data['status'] === 'published' && ilmera_destination_fact_count($data) >= 5;
}

function ilmera_destination_url($data)
{
    return '/study-in-' . $data['slug'];
}

function ilmera_destination_sources($data)
{
    $sources = [];
    if ($data['intro_source']) $sources[] = $data['intro_source'];
    foreach (array_merge(array_keys(ilmera_destination_groups()), ['faqs']) as $field) {
        foreach ($data[$field] as $item) $sources[] = array_intersect_key($item, array_flip(['source_url', 'source_label', 'checked_on']));
    }
    $unique = [];
    foreach ($sources as $source) $unique[json_encode($source)] = $source;
    return array_values($unique);
}

function ilmera_destination_citation($item, $sources)
{
    foreach ($sources as $index => $source) {
        if ($source['source_url'] === $item['source_url'] && $source['source_label'] === $item['source_label'] && $source['checked_on'] === $item['checked_on']) return ' <a class="source-citation" href="#source-' . ($index + 1) . '" aria-label="Source ' . ($index + 1) . '">[' . ($index + 1) . ']</a>';
    }
    return '';
}
