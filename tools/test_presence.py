#!/usr/bin/env python3
"""Regression boundaries for online-only presence checks."""
import unittest
from check_discovery import PublishedContent, physical_presence_matches


class PresenceTests(unittest.TestCase):
    def test_offers_of_local_presence_fail(self):
        for value in ('Visit us in Madikeri', 'Our office in Bengaluru', 'Walk-in counselling', 'Near you', 'Near me', 'In-person counselling', 'ILMERA has a branch in Mysuru', 'Book an office appointment'):
            self.assertTrue(physical_presence_matches(value), value)

    def test_narrow_owner_denials_and_travel_sentence(self):
        for value in ('ILMERA has no physical office or branch anywhere.', 'ILMERA does not operate a physical office or branch anywhere.', 'Counselling is online, and students from Madikeri do not need to travel to an office.', 'Postal locality only; not a counselling location.'):
            self.assertFalse(physical_presence_matches(value), value)

    def test_negation_does_not_hide_another_offer(self):
        self.assertTrue(physical_presence_matches('No physical office or branch. Walk-in counselling is available.'))
        self.assertTrue(physical_presence_matches('Students do not need to travel to an office, but visit our branch.'))

    def test_government_process_is_not_counselling_presence(self):
        self.assertFalse(physical_presence_matches('A video or in-person interview with the embassy.'))
        self.assertFalse(physical_presence_matches('Office of Citizenship and Migration Affairs'))
        self.assertTrue(physical_presence_matches('In-person counselling is available before an interview with the embassy.'))

    def test_metadata_alt_link_and_decoded_schema(self):
        html = '<meta name="description" content="Near me"><img alt="Local office"><a href="/contact">Visit us</a><script type="application/ld+json">{"description":"Walk\\u002din counselling"}</script>'
        self.assertTrue(physical_presence_matches(' '.join(PublishedContent(html).parts)))

    def test_academic_branches_not_business_premises(self):
        self.assertFalse(physical_presence_matches('International branch campuses'))
        self.assertTrue(physical_presence_matches('International branch campuses. ILMERA has a branch in Coorg.'))

    def test_plain_online_copy(self):
        self.assertFalse(physical_presence_matches('Online counselling for students from Kodagu by video call.'))


if __name__ == '__main__':
    unittest.main()
