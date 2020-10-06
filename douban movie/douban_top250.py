from const import *
import urllib.request
import json

top250 = []

i = 1
for st in range(0, 250, 20):
    url = TOP_API.format(BASE_URL, st, 20, API_KEY)

    request = urllib.request.Request(url, headers=HEADERS)
    res = urllib.request.urlopen(request)
    data = res.read().decode('utf-8')

    data = json.loads(data)

    movies = data['subjects']
    for m in movies:
        new_m = (m['id'], i)
        top250.append(new_m)
        i += 1

with open('douban.txt', 'a', encoding='utf8') as f:
    for t in top250:
        f.write('{}{}{}\n'.format(t[0], PARTITION, t[1]))

with open('douban.txt', 'r', encoding='utf8') as f:
    print(f.readlines())


