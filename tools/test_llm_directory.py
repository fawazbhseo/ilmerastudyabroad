#!/usr/bin/env python3
"""Regression tests for rendered metadata, coverage and draft exclusion."""
from pathlib import Path
import unittest
from unittest.mock import patch

import build_llms_directory as directory


class DirectoryTests(unittest.TestCase):
    def setUp(self):
        self.row = {'route': '/study-in-example', 'title': 'Programme guidance',
                    'description': 'Check the selected programme.', 'kind': 'destination',
                    'line': '- [Programme guidance](https://ilmerastudyabroad.com/study-in-example): Check the selected programme.'}
        self.inventory = {self.row['route']: {'status': 'published'}, '/held-example': {'status': 'draft'}}

    def test_exact_entry(self):
        self.assertEqual(directory.validate_directory(self.row['line'], [self.row], self.inventory)['published_urls'], 1)

    def test_html_entities_decoded_without_rephrasing(self):
        meta = directory.Metadata('<title>Advice &amp; planning</title><meta name="description" content="Check &quot;conditions&quot; &amp; evidence.">')
        self.assertEqual(''.join(meta.title), 'Advice & planning')
        self.assertEqual(meta.descriptions, ['Check "conditions" & evidence.'])

    def test_stale_title_rejected(self):
        with self.assertRaises(AssertionError):
            directory.validate_directory(self.row['line'].replace('Programme guidance', 'Old label'), [self.row], self.inventory)

    def test_stale_description_rejected(self):
        with self.assertRaises(AssertionError):
            directory.validate_directory(self.row['line'].replace('Check the selected programme.', 'Old summary.'), [self.row], self.inventory)

    def test_missing_entry_rejected(self):
        with self.assertRaises(AssertionError):
            directory.validate_directory('', [self.row], self.inventory)

    def test_duplicate_entry_rejected(self):
        with self.assertRaises(AssertionError):
            directory.validate_directory(self.row['line'] + '\n' + self.row['line'], [self.row], self.inventory)

    def test_missing_core_url_rejected(self):
        inventory = {**self.inventory, '/about': {'status': 'published'}}
        with self.assertRaises(AssertionError):
            directory.validate_directory(self.row['line'], [self.row], inventory)

    def test_draft_never_fetched(self):
        inventory = {'/study-in-held': {'status': 'draft', 'kind': 'destination', 'file': 'held.php'}}
        with patch.object(directory, 'routes', return_value=inventory), patch.object(directory, 'fetch') as fetch:
            self.assertEqual(directory.directory_entries('http://local.test', Path('.')), [])
            fetch.assert_not_called()

    def test_noindex_cannot_be_generated(self):
        route = self.row['route']
        inventory = {route: {'status': 'published', 'kind': 'destination', 'file': 'example.php'}}
        html = ('<title>Programme guidance</title><meta name="description" content="Check the selected programme.">'
                '<meta name="robots" content="noindex,follow"><link rel="canonical" href="https://ilmerastudyabroad.com' + route + '">').encode()
        with patch.object(directory, 'routes', return_value=inventory), patch.object(directory, 'fetch', return_value=(200, {}, html)):
            with self.assertRaises(AssertionError):
                directory.directory_entries('http://local.test', Path('.'))


if __name__ == '__main__':
    unittest.main()
