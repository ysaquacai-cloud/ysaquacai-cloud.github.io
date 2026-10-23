require 'minitest/autorun'
require 'jekyll'
Liquid::Template.register_filter(Jekyll::Filters)
ROOT = File.expand_path('..', __dir__)
class TemplateRegressionTest < Minitest::Test
  def test_missing_email_has_no_empty_mailto
    text = File.read(File.join(ROOT, 'people/index.html'))
    result = Liquid::Template.parse(text).render('site' => {'data' => {'people' => [{'name'=>'Example','group'=>'Graduate students','role'=>'MS Student'}]}})
    refute_includes result, 'href="mailto:"'
  end
  def test_accepted_records_have_a_rendering_group
    text = File.read(File.join(ROOT, 'publications/index.html'))
    result = Liquid::Template.parse(text).render('site' => {'data' => {'publications'=>[{'id'=>'accepted-example','title'=>'Accepted paper','year'=>2026,'date'=>'2026-01-01','status'=>'accepted'}]}})
    assert_includes result, 'accepted-2026'
  end
end
