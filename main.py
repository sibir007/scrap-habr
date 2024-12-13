import requests as rq
from lxml import html, etree
import os
import csv


VZLJOT_PROXY = {
  'http': 'http://SibiryakovDO:vzlSofia1302@proxy:3128',
  'https': 'http://SibiryakovDO:vzlSofia1302@proxy:3128',
}

def prettyprint(element, **kwargs):
    xml = etree.tostring(
        element, 
        pretty_print=True, 
        encoding='unicode', 
        method='text', 
        **kwargs
        )
    print(xml)


parser = etree.HTMLParser(remove_blank_text=True)

if (os.environ.get('USERDOMAIN', 'NOT_VZLJOT') != 'VZLJOT'):
  VZLJOT_PROXY = None

user = 'yakvenalex'
init_page = 4
init_linc = 'https://habr.com/en/users/{user}/publications/articles/page{page}/'
domen = 'https://habr.com'

# init_linc.format()

# for page in range(init_page, 1, -1):
#     resp = rq.get(url=init_linc.format(user=user, page=page), proxies=VZLJOT_PROXY)
#     root = etree.HTML(resp.text, parser=parser).getroot()
#     root.find('//')
with open('article.csv', 'wt', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    for page in range(init_page, 1, -1):
        resp = rq.get(url=init_linc.format(user=user, page=page), proxies=VZLJOT_PROXY)
        root = etree.HTML(resp.text, parser=parser)
            
        for el in root.iterfind('.//article'):
            tm_title__link = el.find('.//a[@class="tm-title__link"]')
            tm_title__link_str = domen + tm_title__link.get('href')
            # print(tm_title__link.get('href'))
            tm_title = tm_title__link[0].text
            # print(tm_title)
            time_el = el.find('.//time[@title]').get('title')
            # print(time_el.get('title'))
            writer.writerow((time_el, tm_title, tm_title__link_str))
        
# rez = root.findall('.//article')
# with open('test_file.html', 'wt', encoding='utf-8') as f:
#      f.write(resp.text)
# prettyprint(root)
# print(resp.json())