import requests as rq
from lxml import html
import os

VZLJOT_PROXY = {
  'http': 'http://SibiryakovDO:vzlSofia1302@proxy:3128',
  'https': 'http://SibiryakovDO:vzlSofia1302@proxy:3128',
}

if (os.environ.get('USERDOMAIN', 'NOT_VZLJOT') != 'VZLJOT'):
  VZLJOT_PROXY = None

user = 'yakvenalex'
init_page = 4
init_linc = 'https://habr.com/en/users/{user}/publications/articles/page{page}/'

# init_linc.format()

for page in range(init_page, 1, -1):
    resp = rq.get(url=init_linc.format(user=user, page=page))