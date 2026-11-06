#!/usr/bin/env python3
"""Regression tests for the published institution-name guard."""
import unittest
from pathlib import Path
from check_discovery import PublishedContent, blocked_name_matches, blocked_names


class InstitutionGuardTests(unittest.TestCase):
    def setUp(self):
        self.names = blocked_names(Path(__file__).resolve().parents[1])

    def matches(self, markup):
        return blocked_name_matches(' '.join(PublishedContent(markup).parts), self.names)

    def test_visible_faq_and_link_text(self):
        self.assertIn('Oxford', self.matches('<details><summary>Can I apply?</summary><a href="/contact">OXFORD</a></details>'))

    def test_metadata_and_alt(self):
        self.assertIn('Cambridge', self.matches('<meta name="description" content="Cambridge"><img alt="Cambridge">'))

    def test_json_escapes_and_url_alias(self):
        markup = '<script type="application/ld+json">{"name":"Oxf\\u006frd","sameAs":"https://example.com/Tor_Vergata"}</script>'
        self.assertIn('Oxford', self.matches(markup))
        self.assertIn('Tor Vergata', self.matches(markup))

    def test_government_citation_only(self):
        self.assertFalse(self.matches('<a href="https://www.gov.uk/official-guidance">Oxford</a>'))
        self.assertIn('Oxford', self.matches('<a href="https://example.edu/">Oxford</a>'))
        self.assertIn('Oxford', self.matches('<a href="https://www.gov.uk/official-guidance">Source</a><p>Oxford</p>'))

    def test_styles_and_ordinary_scripts_are_not_copy(self):
        self.assertFalse(self.matches('<style>.Oxford{color:red}</style><script>let Cambridge = 1;</script>'))

    def test_plain_llm_text_and_word_boundaries(self):
        self.assertIn('UCL', blocked_name_matches('UK: UCL and other options', self.names))
        self.assertFalse(blocked_name_matches('nuclear research', self.names))


if __name__ == '__main__':
    unittest.main()
