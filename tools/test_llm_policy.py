#!/usr/bin/env python3
"""Reject content regressions after owner-authorized LLM edits."""
from pathlib import Path
import re
import unittest

from check_discovery import blocked_names, validate_llm_text
from check_italy_claims import EXACT, OWNER, CAUTION

ROOT = Path(__file__).resolve().parents[1]


class LLMPolicyTests(unittest.TestCase):
    def reject(self, edit):
        for name in ('llms.txt', 'llms-full.txt'):
            with self.subTest(name=name):
                text = (ROOT / name).read_text()
                changed = edit(text)
                self.assertNotEqual(changed, text)
                with self.assertRaises(AssertionError):
                    validate_llm_text(ROOT, name, changed)

    def test_authorized_documents(self):
        for name in ('llms.txt', 'llms-full.txt'):
            result = validate_llm_text(ROOT, name, (ROOT / name).read_text())
            self.assertEqual(result['content_policy'], 'PASS')

    def test_removed_alias_rejected(self):
        self.reject(lambda s: s + '\n' + blocked_names(ROOT)[-1])

    def test_cost_wording_rejected(self):
        self.reject(lambda s: s + '\nTuition-free study.')

    def test_italy_requires_exact_sentence(self):
        self.reject(lambda s: s.replace(EXACT, 'Funding of 8k euros.'))

    def test_italy_requires_local_owner_label(self):
        self.reject(lambda s: s.replace(OWNER, ''))

    def test_italy_requires_written_award_caution(self):
        self.reject(lambda s: s.replace(CAUTION, ''))

    def test_online_only_explicit(self):
        self.reject(lambda s: re.sub(r'online[ -]only', 'remotely', s, flags=re.I))

    def test_offered_meeting_rejected(self):
        self.reject(lambda s: s + '\nVisit our office for counselling.')

    def test_gcc_caveat_required(self):
        self.reject(lambda s: s.replace('Kuwait information is not yet available', 'Kuwait information is available'))

    def test_draft_promotion_rejected(self):
        self.reject(lambda s: s + '\nStudy in Czech Republic.')

    def test_draft_url_rejected(self):
        self.reject(lambda s: s + '\nhttps://ilmerastudyabroad.com/study-in-russia')

    def test_markdown_outline_required(self):
        self.reject(lambda s: s.replace('\n## ', '\n'))


if __name__ == '__main__':
    unittest.main()
