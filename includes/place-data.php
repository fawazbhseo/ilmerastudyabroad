<?php
/* Shared place data normalization and publication readiness checks. */
if (!function_exists('ilmera_place_text')) {
    function ilmera_place_text($value)
    {
        if (!is_string($value)) return '';
        $text = trim(html_entity_decode(strip_tags($value), ENT_QUOTES | ENT_HTML5, 'UTF-8'));
        if (preg_match('/\[\s*(?:VERIFY|OWNER|TODO|TBD|PLACEHOLDER|CONFIRM|INSERT|ADD|FILL|PENDING|UNCONFIRMED)\b|\b(?:TODO|TBD|TBC|PLACEHOLDER)\b/iu', $text)) return '';
        return $text;
    }

    function ilmera_place_strings($value)
    {
        if (!is_array($value)) return [];
        $items = [];
        foreach ($value as $item) {
            $text = ilmera_place_text($item);
            if ($text !== '') $items[] = $text;
        }
        return $items;
    }

    function ilmera_place_normalize($data, $slug)
    {
        if (!is_array($data)) return null;
        foreach (['slug', 'name', 'type', 'district', 'status'] as $key) {
            if (!isset($data[$key]) || !is_string($data[$key])) return null;
        }
        if ($data['slug'] !== $slug || !preg_match('/^[a-z0-9]+(?:-[a-z0-9]+)*$/D', $slug)) return null;
        if (!in_array($data['type'], ['district-hub', 'town', 'city'], true)) return null;
        if (!in_array($data['status'], ['draft', 'published'], true)) return null;
        $result = array_intersect_key($data, array_flip(['slug', 'name', 'type', 'district', 'status']));
        $result['name'] = ilmera_place_text($data['name']);
        $result['district'] = ilmera_place_text($data['district']);
        if ($result['name'] === '') return null;
        foreach (['page_title', 'heading', 'meta_description', 'reviewed_on'] as $key) $result[$key] = ilmera_place_text($data[$key] ?? '');
        $result['local_facts_used'] = ($data['local_facts_used'] ?? true) === true;
        $result['local_fact_sources'] = is_array($data['local_fact_sources'] ?? null) ? $data['local_fact_sources'] : [];
        $result['sections'] = [];
        foreach (is_array($data['sections'] ?? null) ? $data['sections'] : [] as $section) {
            $heading = ilmera_place_text($section['heading'] ?? '');
            $paragraphs = ilmera_place_strings($section['paragraphs'] ?? []);
            if ($heading !== '' && $paragraphs) $result['sections'][] = ['heading' => $heading, 'paragraphs' => $paragraphs];
        }
        $result['intro_answer'] = ilmera_place_text($data['intro_answer'] ?? '');
        $words = preg_match_all('/\S+/u', $result['intro_answer']);
        if ($words < 40 || $words > 60) $result['intro_answer'] = '';
        foreach (['local_institutions', 'transcript_and_moi_steps', 'local_loan_options', 'local_notes'] as $key) {
            $result[$key] = ilmera_place_strings($data[$key] ?? []);
        }
        $result['visa_appointment_route'] = ilmera_place_text($data['visa_appointment_route'] ?? '');
        $result['faqs'] = [];
        foreach (is_array($data['faqs'] ?? null) ? $data['faqs'] : [] as $faq) {
            if (!is_array($faq)) continue;
            $question = ilmera_place_text($faq['question'] ?? '');
            $answer = ilmera_place_text($faq['answer'] ?? '');
            if ($question !== '' && $answer !== '') $result['faqs'][] = ['question' => $question, 'answer' => $answer];
        }
        $result['nearby'] = [];
        foreach (is_array($data['nearby'] ?? null) ? $data['nearby'] : [] as $nearby) {
            if (is_string($nearby) && $nearby !== $slug && preg_match('/^[a-z0-9]+(?:-[a-z0-9]+)*$/D', $nearby)) {
                $result['nearby'][] = $nearby;
            }
        }
        $result['nearby'] = array_values(array_unique($result['nearby']));
        return $result;
    }

    function ilmera_place_load($slug)
    {
        static $cache = [];
        if (!is_string($slug) || !preg_match('/^[a-z0-9]+(?:-[a-z0-9]+)*$/D', $slug)) return null;
        if (array_key_exists($slug, $cache)) return $cache[$slug];
        $path = dirname(__DIR__) . '/places/' . $slug . '.php';
        if (!is_file($path)) return $cache[$slug] = null;
        $data = (static function ($file) { return include $file; })($path);
        return $cache[$slug] = ilmera_place_normalize($data, $slug);
    }

    function ilmera_place_fact_count($data)
    {
        $count = 0;
        foreach (['intro_answer', 'local_institutions', 'transcript_and_moi_steps', 'local_loan_options', 'visa_appointment_route', 'local_notes', 'faqs'] as $key) {
            if (!empty($data[$key])) $count++;
        }
        return $count;
    }

    function ilmera_place_content_hash($data)
    {
        $payload = [];
        foreach (['page_title', 'heading', 'meta_description', 'intro_answer', 'sections', 'faqs'] as $field) $payload[] = $data[$field] ?? null;
        return hash('sha256', json_encode($payload, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES));
    }

    function ilmera_place_evidence_matches($data)
    {
        if (!is_array($data)) return false;
        static $journal = null, $cohortValid = null;
        if ($journal === null) {
            $file = dirname(__DIR__) . '/phase14-location-review.json';
            $journal = is_file($file) ? json_decode(file_get_contents($file), true) : [];
            if (!is_array($journal)) $journal = [];
        }
        $entry = $journal['locations'][$data['slug']] ?? [];
        if (($entry['copy_reviewed'] ?? false) !== true || ($entry['schema_reviewed'] ?? false) !== true ||
            ($data['local_facts_used'] ?? true) !== false || !empty($data['local_fact_sources']) ||
            ilmera_place_content_hash($data) !== ($entry['content_sha256'] ?? '') ||
            ($journal['max_shared_percent'] ?? 100) > 15 || ($journal['rendered_main_overlap']['max_shared_percent'] ?? 100) > 15) return false;
        foreach (['local_institutions', 'transcript_and_moi_steps', 'local_loan_options', 'visa_appointment_route', 'local_notes'] as $field) if (!empty($data[$field])) return false;
        if ($data['reviewed_on'] !== ($entry['checked_on'] ?? '')) return false;
        $prose = $data['intro_answer'];
        foreach ($data['sections'] as $section) $prose .= ' ' . implode(' ', $section['paragraphs']);
        if (preg_match_all('/\S+/u', $prose) < 350 || !$data['page_title'] || !$data['heading'] || !$data['meta_description'] || !$data['faqs']) return false;
        // An edited peer also needs another pairwise check, not a stale score.
        if ($cohortValid === null) {
            $cohortValid = !empty($journal['locations']);
            foreach ($journal['locations'] ?? [] as $slug => $peerReview) {
                $peer = ilmera_place_load($slug);
                if (!$peer || ilmera_place_content_hash($peer) !== ($peerReview['content_sha256'] ?? '')) $cohortValid = false;
            }
        }
        return $cohortValid;
    }

    function ilmera_place_indexable($data)
    {
        return is_array($data) && $data['status'] === 'published' && ilmera_place_evidence_matches($data);
    }

    function ilmera_place_url($data)
    {
        $prefix = $data['type'] === 'district-hub' && in_array($data['slug'], ['karnataka', 'kodagu'], true)
            ? '/study-abroad-consultants-in-' : '/study-abroad-counselling-';
        return $prefix . $data['slug'];
    }

    function ilmera_place_escape($text)
    {
        return htmlspecialchars($text, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8');
    }

    function ilmera_place_inline($text, $linkDestinations = false)
    {
        $escaped = ilmera_place_escape($text);
        return preg_replace_callback('/\[([^\[\]]+)\]\((\/[^\s()]*)\)/u', static function ($match) use ($linkDestinations) {
            $path = html_entity_decode($match[2], ENT_QUOTES | ENT_HTML5, 'UTF-8');
            $parts = parse_url($path);
            if ($parts === false || isset($parts['host']) || isset($parts['scheme']) || strpos($path, '//') === 0 || strpos($path, '\\') !== false) return $match[1];
            require_once __DIR__ . '/links.php';
            if ($linkDestinations && preg_match('#^/services(?:\.php)?/?$#i', $parts['path'] ?? '') && in_array($parts['fragment'] ?? '', ilmera_destination_slugs(), true)) $path = ilmera_destination_target($parts['fragment']);
            if (!ilmera_target_published($path)) return $match[1];
            return '<a href="' . ilmera_place_escape($path) . '" style="color:var(--gold);">' . $match[1] . '</a>';
        }, $escaped);
    }
}
