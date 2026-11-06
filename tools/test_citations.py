#!/usr/bin/env python3
import unittest
from published_citations import References, external_reference


class CitationTests(unittest.TestCase):
    def test_no_destination_host_filter(self):
        p = References()
        p.feed('<section class="source-review"><a href="https://www.minedu.sk/rules">Ministry</a><a href="https://www.universitaly.it/procedures">Government portal</a><a href="https://new-official-host.example/rules">New reference needs review</a></section>')
        self.assertEqual(len(p.urls), 3)

    def test_schema_only_reference(self):
        p = References()
        p.feed('<script type="application/ld+json">{"@graph":[{"citation":["https://official.example/rule",{"url":"https://official.example/second"}]}]}</script>')
        self.assertEqual(p.urls, {'https://official.example/rule', 'https://official.example/second'})

    def test_social_contact_and_self_exclusions(self):
        for url in ('https://wa.me/421944485186', 'https://www.linkedin.com/company/example', 'https://ilmerastudyabroad.com/services', '/services', 'tel:+919019557427'):
            self.assertFalse(external_reference(url))
        self.assertTrue(external_reference('https://www.gov.uk/student-visa'))


if __name__ == '__main__':
    unittest.main()
