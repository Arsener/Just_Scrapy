from const import *
import requests
import json
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as bs

url = "https://www.usnews.com/education/best-global-universities/rankings"

for page in range(1, 169):
    querystring = {"format": "json", "page": page}

    agent = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'}
    response = requests.request("GET", url, headers=agent, params=querystring)
    data = json.loads(response.text)
    with open('details.txt', 'a', encoding='utf8') as f:
        for u in data['items']:
            f.write(u['url'] + '\n')