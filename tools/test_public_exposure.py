#!/usr/bin/env python3
"""Policy-pattern tests, NOT a native Apache/LiteSpeed execution test."""
import pathlib,re,unittest
from phase24b.approved import ROOT_DENY,DENY,BASELINE
from phase24b.exposure import BLOCKED_EXT,INTERNAL
class ExposureTests(unittest.TestCase):
 def test_native_pattern_matches_policy(self):
  native=re.compile(ROOT_DENY.decode().split('<FilesMatch "')[1].split('"')[0])
  for name in ['README.md','flagged-items-for-verification.md','CHANGELOG.MD','phase14-validation.json','phase24b-access-probe.py','probe.cjs','probe.log','probe.bak','private.csv','.gitignore','llms.txt','llms-full.txt','robots.txt','sitemap.xml','favicon.ico','fawazbh-192.webp','google10fa7a4178242a1f.html']:
   self.assertEqual(bool(native.search(name)),bool(BLOCKED_EXT.search(name)),name)
 def test_public_resources_not_extension_blocked(self):
  for name in ['llms.txt','llms-full.txt','robots.txt','sitemap.xml','logo.png','fawazbh-384.webp','style.css','script.js']:self.assertIsNone(BLOCKED_EXT.search(name),name)
 def test_no_legacy_access_syntax_or_new_rewrite(self):
  self.assertIn(b'Require all denied',ROOT_DENY);self.assertIn(b'RedirectMatch 403',ROOT_DENY)
  self.assertNotIn(b'RewriteRule',ROOT_DENY);self.assertNotIn(b'RewriteCond',ROOT_DENY);self.assertNotIn(b'Order ',ROOT_DENY)
 def test_all_private_runtime_folders_covered(self):
  self.assertEqual(set(INTERNAL),{'reports','tools','includes','data','destinations','places'})
if __name__=='__main__':unittest.main()
