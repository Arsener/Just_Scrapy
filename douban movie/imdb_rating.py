import json
from const import *
from urllib.request import Request, urlopen

url = 'http://www.omdbapi.com/?apikey={}&i={}'.format('4620c2ee', 'tt2205948')
request = Request(url, headers=HEADERS)
res = urlopen(request)

data = res.read().decode('utf-8')
data = json.loads(data)
print(type(data))

rating_dict = dict()
ratings = data.get('Ratings', dict())
# ratings = [{}]
# {'Internet Movie Database': '6.7/10', 'Rotten Tomatoes': '36%', 'Metacritic': '40/100'}
for r in ratings:
    rating_dict[r.get('Source', 'null')] = r.get('Value', 'null')

print(rating_dict)
print(rating_dict.get('Internet Movie Database', '-1'))
print(rating_dict.get('Rotten Tomatoes', '-1'))
print(rating_dict.get('Metacritic', '-1'))
