import re
import json
from const import *
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as bs


def get_detail(movie_id):
    url = DETAIL_URL.format(movie_id)
    request = Request(url, headers=HEADERS)
    res = urlopen(request)

    return res.read().decode('utf-8')


def parse_name(html):
    actors = bs(html, 'html.parser').find('script', {'type': 'application/ld+json'})
    print(actors)
    actors = json.loads(actors.get_text().replace('\r', '').replace('\n', '').replace('\t', ''))['actor']
    print(actors)
    actors_list = []
    for a in actors:
        actor_id = re.findall(re.compile('\d+'), a['url'])[0]
        name = a['name']
        cn, first_en, last_en = name.split(' ', 2)
        if '·' in cn:
            first_cn, last_cn = cn.split('·', 1)
        else:
            first_cn, last_cn = cn[0:1], cn[1:]

        actors_list.append((actor_id, name, first_cn, last_cn, first_en, last_en))
    return actors_list


def main(movie_id):
    # 构造url，请求json数据
    api_url = ITEM_API.format(BASE_URL, movie_id, API_KEY)
    request = Request(api_url, headers=HEADERS)
    res = urlopen(request)
    # 解码为json
    data = res.read().decode('utf-8')
    data = json.loads(data)
    # print(data)
    movie_name_cn = data['title']
    movie_name_ori = data['original_title']
    # 别名返回的是list，需要组合成str
    other_name = '/'.join(data['aka'])
    # float
    db_rating = data['rating']['average']
    poster_url = data['images']['large']
    # 上映日期返回的是list，需要组合成str
    date = '/'.join(data['pubdates'])
    # 年份返回str，转为int
    year = int(data['year'])
    # 语言返回的是list，需要组合成str
    language = '/'.join(data['languages'])
    # 片长返回的是list，需要组合成str
    length = '/'.join(data['durations'])
    # 国家返回的是list，需要组合成str
    movie_country = '/'.join(data['countries'])
    summary = data['summary'].split('©')[0]

    # 获取电影类型
    type_name = data['genres']
    # TODO 对已有的类别进行判断

    # 获取评论并提取出需要的信息
    # TODO 当前方法获取的评论是随机的，若要获取前几名可能需要进入详细页面获取
    comments_list = []
    comments = data['popular_comments']
    for c in comments:
        comment = (c['created_at'], c['rating']['value'], c['useful_count'], c['content'])
        comments_list.append(comment)

    # 获取详细网页信息
    html = get_detail(movie_id)
    # 获取imdb链接
    imdb_link = re.findall(re.compile('https://www.imdb.com/title/tt\d+'), html)[0]

    # 通过是否含有·判断是否为外国人名。中国人名则默认第一个字为姓。
    actors_list = parse_name(html)


    # print(html)
    for actor in actors_list:
        print(actor)




if __name__ == '__main__':
    m_id = '26147417'
    main(m_id)
