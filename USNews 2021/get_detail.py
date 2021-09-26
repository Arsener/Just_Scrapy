from const import *
import requests
import json
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as bs

'''
https://www.usnews.com/education/best-global-universities/tsinghua-university-503146?format=json
'''

url = "https://www.usnews.com/education/best-global-universities/tsinghua-university-503146"

# for page in range(1, 169):
#     querystring = {"format": "json", "page": page}

agent = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'}
response = requests.request("GET", url, headers=agent)

print(response.text)
# res = urlopen(response)
# html = res.read().decode('utf-8')