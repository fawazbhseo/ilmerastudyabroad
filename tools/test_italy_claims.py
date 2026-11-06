#!/usr/bin/env python3
import unittest
from check_italy_claims import check_parts, EXACT, OWNER, CAUTION


class ItalyClaimTests(unittest.TestCase):
    def test_exact_with_local_attribution(self):
        self.assertEqual(check_parts([OWNER + EXACT + CAUTION]), 1)
        self.assertEqual(check_parts(['No. ' + OWNER + EXACT + CAUTION]), 1)

    def test_missing_attribution_or_caution(self):
        for text in (EXACT, OWNER + EXACT, EXACT + CAUTION):
            with self.assertRaises(AssertionError):
                check_parts([text])

    def test_nonexact_amount_variants(self):
        for amount in ('8,000', '8.000', '8000', '8 000', '8k', 'eight thousand', 'eight-thousand'):
            with self.assertRaises(AssertionError):
                check_parts(['A scholarship of ' + amount + ' euros.'])

    def test_other_fees_are_not_the_owner_amount(self):
        self.assertEqual(check_parts(['Tuition starts from 1,300 euros; living costs vary.']), 0)


if __name__ == '__main__':
    unittest.main()
