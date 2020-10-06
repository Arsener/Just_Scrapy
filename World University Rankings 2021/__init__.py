import re
import json
from const import *
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as bs

url = 'https://www.timeshighereducation.com/world-university-rankings/2021/world-ranking#!/page/0/length/25/sort_by/rank/sort_order/asc/cols/stats'
request = Request(url, headers=HEADERS)
res = urlopen(request)
html = res.read().decode('utf-8')

print(html)