# coding:utf-8
'''
从百度图片爬取文字表情包
'''
import urllib.request
import requests
import threading

base_url = 'https://image.baidu.com/search/acjson'
dir = 'D:/文字表情包/'

threads = []

def scrapy(i):
    params = {'tn': 'resultjson_com',
              'ipn': 'rj',
              'ct': 201326592,
              'is': '',
              'fp': 'result',
              'queryWord': '表情包 文字',
              'cl': 2,
              'lm': -1,
              'ie': 'utf-8',
              'oe': 'utf-8',
              'adpicid': '',
              'st': -1,
              'z': '',
              'ic': 0,
              'word': '表情包 文字',
              's': '',
              'se': '',
              'tab': '',
              'width': '',
              'height': '',
              'face': 0,
              'istype': 2,
              'qc': '',
              'nc': 1,
              'fr': '',
              'pn': 30 * i,
              'rn': 30,
              'gsm': '1e',
              '1488942260214': ''}
    re = requests.get(base_url, params=params).json()
    for data in re.get('data'):
        print(i)
        pic_url = data.get('thumbURL')
        try:
            file_name = pic_url.split('u=')[1].split('&fm')[0]
            file_format = pic_url.split('gp=')[1][-4:]
            urllib.request.urlretrieve(pic_url, filename=dir + file_name + file_format)
        except:
            pass

for i in range(0,21):
    t = threading.Thread(target=scrapy, args=(i,))
    threads.append(t)


for t in threads:
    t.start()




