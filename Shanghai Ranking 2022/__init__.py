from const import *
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as bs

url = 'http://www.shanghairanking.com/ARWU2020.html'
request = Request(url, headers=HEADERS)
res = urlopen(request)
html = res.read().decode('utf-8')

print(bs(html, 'html.parser').find_all('tr'))

