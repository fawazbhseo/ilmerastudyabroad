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

class ShortCardPolicyTests(unittest.TestCase):
 def test_exact_counts_and_spread(self):
  from team_bio_policy import SHORT_CARD_BIOS
  self.assertEqual({k:len(v) for k,v in SHORT_CARD_BIOS.items()},{'Jabir KJ':127,'Zaheer KJ':130,'Fawaz BH':126})
  lengths=list(map(len,SHORT_CARD_BIOS.values()));self.assertLessEqual(max(lengths)-min(lengths),6)
 def test_narrow_context_only(self):
  from team_bio_policy import SHORT_CARD_BIOS,card_bio_allowed,APPROVED_BIOS
  for bio in SHORT_CARD_BIOS.values():
   self.assertNotIn(bio,APPROVED_BIOS)
   for route in ['/','/about']:self.assertTrue(card_bio_allowed(bio,route,True))
   for route in ['/services','/contact','/blog/','/llms.txt']:self.assertFalse(card_bio_allowed(bio,route,True))
   self.assertFalse(card_bio_allowed(bio,'/',False));self.assertFalse(card_bio_allowed(bio+' Added claim.','/',True))
 def fixture(self,route='/about'):
  import json
  from team_bio_policy import SHORT_CARD_BIOS
  root=pathlib.Path(__file__).resolve().parents[1];team=json.loads((root/'data/team.json').read_text())['members']
  cls='team-bio' if route=='/about' else 'testi-text';card='team-card' if route=='/about' else 'testi-card reveal-r'
  return '<script type="application/ld+json">'+json.dumps({'@graph':team})+'</script>'+''.join('<article class="'+card+'"><p class="'+cls+'">'+bio+'</p></article>' for bio in SHORT_CARD_BIOS.values())+(''.join('<p>'+m['description']+'</p>' for m in team) if route=='/about' else '')
 def test_full_bios_still_required_in_schema_and_about_prose(self):
  from team_bio_policy import validate_bio_contexts,FAWAZ,SHORT_CARD_BIOS
  text=self.fixture();self.assertTrue(validate_bio_contexts(text,'/about'))
  for broken in [text.replace(FAWAZ,SHORT_CARD_BIOS['Fawaz BH']),text.replace(FAWAZ,'')]:
   with self.assertRaises(AssertionError):validate_bio_contexts(broken,'/about')
 def test_short_cannot_leak_into_prose_or_another_route(self):
  from team_bio_policy import validate_bio_contexts,SHORT_CARD_BIOS
  for text,route in [(self.fixture('/')+'<p>'+SHORT_CARD_BIOS['Zaheer KJ']+'</p>','/'),(self.fixture('/'),'/contact')]:
   with self.assertRaises(AssertionError):validate_bio_contexts(text,route)

if __name__=='__main__':unittest.main()
