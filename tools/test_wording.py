#!/usr/bin/env python3
"""Technical negative fixtures for the whole-publication wording guard."""
import unittest
from phase30.duplicates import assert_no_repeated_answer
from check_discovery import PublishedContent, prohibited_wording_matches


class WordingTests(unittest.TestCase):
    def test_plain_case_insensitive(self):
        self.assertTrue(prohibited_wording_matches('FREE study'))

    def test_compound_variants(self):
        for value in ['tuition-free', 'tuition free', 'tuitionfree', 'tuition\u2011free']:
            with self.subTest(value=value):
                self.assertTrue(prohibited_wording_matches(value))

    def test_encoded_url(self):
        self.assertTrue(prohibited_wording_matches('https://example.test/tuition%2Dfr%65e'))

    def test_full_width_text(self):
        self.assertTrue(prohibited_wording_matches('\uff26\uff32\uff25\uff25'))

    def test_metadata_and_decoded_json(self):
        text = '<meta name="description" content="Free study"><script type="application/ld+json">{"description":"tuition-fr\\u0065e"}</script>'
        self.assertTrue(prohibited_wording_matches(' '.join(PublishedContent(text).parts)))

    def test_government_anchor_not_a_wording_exception(self):
        text = '<a href="https://www.gov.uk/example">Free study</a>'
        parts = PublishedContent(text, include_government_citations=True).parts
        self.assertTrue(prohibited_wording_matches(' '.join(parts)))

    def test_allowed_budget_and_consultation_copy(self):
        self.assertFalse(prohibited_wording_matches('No-charge consultation; check programme-specific fees and written award conditions.'))
        self.assertFalse(prohibited_wording_matches('Freedom to compare options.'))


if __name__ == '__main__':
    unittest.main()
