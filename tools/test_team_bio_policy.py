#!/usr/bin/env python3
"""Exact-context allow-entry regressions; no university-name guard is relaxed."""
import pathlib,unittest
from check_discovery import blocked_name_matches,blocked_names
from team_bio_policy import ZAHEER,FAWAZ
class BioPolicyTests(unittest.TestCase):
 def setUp(self):self.names=blocked_names(pathlib.Path(__file__).resolve().parents[1])
 def test_exact_bios_allowed(self):
  for bio in [ZAHEER,FAWAZ]:self.assertEqual(blocked_name_matches(bio,self.names),[])
 def test_context_not_a_blanket_exception(self):
  for text in ['Adrex Media School',FAWAZ+' Adrex Media School',ZAHEER.replace('including documentation','including other work')]:self.assertIn('Adrex Media School',blocked_name_matches(text,self.names))
 def test_university_guard_still_applies(self):
  for name in self.names:self.assertIn(name,blocked_name_matches(FAWAZ+' '+name,self.names))
 def test_university_name_cannot_be_inserted_in_bio(self):
  self.assertIn(self.names[0],blocked_name_matches(ZAHEER.replace('paperwork','paperwork '+self.names[0]),self.names))
if __name__=='__main__':unittest.main()
