#!/usr/bin/env python3
"""Regression: repeated answers fail discovery/wording builds, cited answer retained."""
import pathlib,sys,unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
from phase30.duplicates import assert_no_repeated_answer,expected_delta
class DuplicateAnswers(unittest.TestCase):
 def fixture(self,tail='Same answer.'):
  return '<p class="direct-answer">Same answer.</p><p class="conversion-cta"><a href="/contact">Ask</a></p></div>\n<p>'+tail+'</p>'
 def test_repeat_fails(self):
  with self.assertRaises(AssertionError):assert_no_repeated_answer(self.fixture(),'/test')
 def test_citation_does_not_hide_repeat(self):
  with self.assertRaises(AssertionError):assert_no_repeated_answer(self.fixture('Same answer. <a class="source-citation" href="#source-1">[1]</a>'),'/test')
 def test_unique_paragraph_passes(self):assert_no_repeated_answer(self.fixture('Different useful introduction.'),'/test')
 def test_kept_citation_and_cta_order(self):
  old=self.fixture('Same answer. <a class="source-citation" href="#source-1">[1]</a>');new=expected_delta(old,'/study-in-germany')
  self.assertEqual(new.count('Same answer.'),1);self.assertLess(new.index('#source-1'),new.index('/contact'));assert_no_repeated_answer(new,'/test')
if __name__=='__main__':unittest.main()
