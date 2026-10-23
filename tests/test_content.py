import importlib.util, unittest
from pathlib import Path
spec=importlib.util.spec_from_file_location('validate',Path(__file__).parents[1]/'scripts/validate.py')
validate=importlib.util.module_from_spec(spec);spec.loader.exec_module(validate)
class ContentTests(unittest.TestCase):
 def record(self):return dict(id='a',title='Example',authors=['A. Author'],year=2026,status='preprint',url='https://arxiv.org/abs/2605.09316',themes=['information'])
 def test_preprint_can_become_published_without_duplicate(self):
  p=self.record();p.update(status='published',venue='Journal',doi='https://doi.org/10.1234/example')
  self.assertEqual(validate.validate_publications([p],{'information'}),[])
 def test_optional_links_are_optional(self):self.assertEqual(validate.validate_publications([self.record()],{'information'}),[])
 def test_duplicate_id_rejected(self):self.assertTrue(validate.validate_publications([self.record(),self.record()],{'information'}))
 def test_missing_title_rejected(self):
  p=self.record();p.pop('title');self.assertTrue(validate.validate_publications([p],{'information'}))
 def test_unknown_theme_rejected(self):self.assertTrue(validate.validate_publications([self.record()],{'computing'}))
 def test_bad_status_rejected(self):
  p=self.record();p['status']='draft';self.assertTrue(validate.validate_publications([p],{'information'}))
 def test_unsafe_url_rejected(self):
  p=self.record();p['url']='javascript:alert(1)';self.assertTrue(validate.validate_publications([p],{'information'}))
if __name__=='__main__':unittest.main()
