"""Validate editable content and generated internal links using Python's standard library."""
import json,sys,re
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
ROOT=Path(__file__).resolve().parents[1]
def validate_publications(records,themes):
 errors=[];seen=set()
 for p in records:
  key=p.get('id','<missing>')
  for field in ('id','title','authors','year','status','url'):
   if not p.get(field):errors.append(f'{key}: missing {field}')
  if key in seen:errors.append(f'{key}: duplicate ID')
  seen.add(key)
  if p.get('status') not in ('published','accepted','preprint'):errors.append(f'{key}: invalid status')
  if not isinstance(p.get('year'),int):errors.append(f'{key}: year must be an integer')
  if not set(p.get('themes',[])) <= themes:errors.append(f'{key}: unknown theme')
  for field in ('url','doi','arxiv','code','data'):
   if p.get(field) and urlsplit(p[field]).scheme!='https':errors.append(f'{key}: unsafe {field}')
 for p in records:
  if p.get('related_id') and p['related_id'] not in seen:errors.append(f"{p['id']}: unknown related work")
 return errors
class Page(HTMLParser):
 def __init__(self):super().__init__();self.links=[];self.ids=set();self.h1=0;self.images=[];self.lang=None
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if a.get('id'):self.ids.add(a['id'])
  if tag=='html':self.lang=a.get('lang')
  if tag=='h1':self.h1+=1
  if tag=='a' and 'href' in a:self.links.append(a['href'])
  if tag in ('img','script') and a.get('src'):self.links.append(a['src'])
  if tag=='link' and a.get('rel')=='stylesheet':self.links.append(a['href'])
  if tag=='img' and 'alt' not in a:self.images.append('Missing alt')
def validate_build(folder):
 errors=[];pages={}
 for path in folder.rglob('*.html'):
  page=Page();text=path.read_text();page.feed(text);pages[path.resolve()]=page
  if page.lang!='en':errors.append(f'{path}: document language must be English')
  if page.h1!=1:errors.append(f'{path}: expected one h1')
  errors.extend(f'{path}: {e}' for e in page.images)
  if re.search('[\uac00-\ud7af]',text):errors.append(f'{path}: Korean text remains')
  if '{{' in text or '{%' in text:errors.append(f'{path}: unrendered template')
 for path,page in pages.items():
  for link in page.links:
   u=urlsplit(link)
   if u.scheme or u.netloc:continue
   target=(folder/unquote(u.path.lstrip('/')) if u.path.startswith('/') else path.parent/unquote(u.path)) if u.path else path
   if target.is_dir():target=target/'index.html'
   if not target.exists():errors.append(f'{path.name}: broken local link {link}')
   elif u.fragment and target.resolve() in pages and unquote(u.fragment) not in pages[target.resolve()].ids:errors.append(f'{path.name}: missing anchor {link}')
 return errors
if __name__=='__main__':
 data=lambda n:json.loads((ROOT/'_data'/f'{n}.json').read_text())
 errors=validate_publications(data('publications'),{x['id'] for x in data('research')})
 people=data('people');ids=[p['id'] for p in people]
 if len(ids)!=len(set(ids)):errors.append('Duplicate person IDs')
 for p in people:
  if not all(p.get(k) for k in ('id','name','role','group')):errors.append('Incomplete person record')
 if '--site' in sys.argv:errors+=validate_build(ROOT/'_site')
 if errors:print('\n'.join(errors));sys.exit(1)
 print('Content and link validation passed.' if '--site' in sys.argv else 'Content validation passed.')
