'''
抓取B站up主-十万个内涵图-邪恶福利GIF合集系列视频封面
'''
import threading
import urllib.request
from bs4 import BeautifulSoup

url = 'https://search.bilibili.com/all?keyword=%E5%8D%81%E4%B8%87%E4%B8%AA%E5%86%85%E6%B6%B5%E5%9B%BE&page='
order_by = '&order=pubdate'
dir = 'D:/十万个内涵图封面/'
file_format = '.jpg'

def scrapy(page):
    request = urllib.request.urlopen(url + str(page) + order_by)

    html = BeautifulSoup(request.read(), 'html5lib')
    frontpages = html.find_all('li', {'class': 'video matrix '})
    for frontpage in frontpages:
        print(frontpage.find('a')['title'])
        title = frontpage.find('a')['title']
        if title[0:10] == '邪恶福利GIF图合集':
            print(frontpage.find('div', {'class': 'img'}).find('img')['data-src'])
            photo_src = frontpage.find('div', {'class': 'img'}).find('img')['data-src']
            urllib.request.urlretrieve('http:' + photo_src, filename=dir + title + file_format)

threads = []

for page in range(1, 16):
    t = threading.Thread(target=scrapy, args=(page,))
    threads.append(t)

for thread in threads:
    thread.start()
