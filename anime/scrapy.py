import urllib.request
import re
from bs4 import BeautifulSoup as bs
from selenium import webdriver

url = 'http://movie.douban.com/subject/1300282/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}


request = urllib.request.Request(url, headers=headers)
proxy = urllib.request.ProxyHandler({'http': '206.125.41.135:808'})
opener = urllib.request.build_opener(proxy)
urllib.request.install_opener(opener)
res = urllib.request.urlopen(request)
# res = opener.open(url)
print(5)

html = res.read().decode('utf-8')
a = bs(html, 'html.parser').find_all(name='a', attrs={'class':'', 'href':re.compile('.from=subject-page')})
for _ in a:
    print(_, type(str(a)), '\n')

for i in range(1, len(a), 2):
    s = re.findall(re.compile('\d+'), str(a[i]))
    print(s)


