'''
爬取当天必应首页背景图，以当天日期作为文件名
'''
import datetime
import urllib.request
from bs4 import BeautifulSoup

url = 'https://cn.bing.com'
dir = 'D:/必应背景/'
file_format = '.jpg'
request = urllib.request.urlopen(url)

html = BeautifulSoup(request.read(), "html5lib")
pic_url = str(html).split('g_img={url:')[1][2:].split('",id:\'bgDiv\',')[0]

now = datetime.datetime.now()
filename = now.strftime('%Y-%m-%d')
urllib.request.urlretrieve(url + pic_url, filename=dir + filename + file_format)