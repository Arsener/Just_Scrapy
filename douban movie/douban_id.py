from const import *
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as bs
import time
import datetime
import re


def parse(mid):
    url = DETAIL_URL.format(mid)
    request = Request(url, headers=HEADERS)
    # proxy = ProxyHandler({'https': '163.125.159.190:8888'})
    # opener = build_opener(proxy)
    # install_opener(opener)
    # res = opener.open(url)
    res = urlopen(request)

    html = res.read().decode('utf-8')
    a = bs(html, 'html.parser').find_all(name='a', attrs={'class': '', 'href': re.compile('.from=subject-page')})

    rec = set()
    for i in range(1, len(a), 2):
        s = re.findall(re.compile('\d+'), str(a[i]))
        rec.add(s[0])

    return rec


def main():
    # 先取出所有的电影id
    undo = None
    with open('all_movie.txt', 'r', encoding='utf8') as f:
        undo = [m.strip() for m in f.readlines()]
    # print(undo)
    # 已经获得了多少
    cnt = len(undo)

    # 取出所有已经获取过推荐电影的id
    done = None
    with open('done.txt', 'r', encoding='utf8') as f:
        done = set(m.strip() for m in f.readlines())
    # print(done)

    # 找到起始
    while undo[0] in done:
        undo.pop(0)
    print(undo[0])
    # print(undo[0])

    # 需要操作的id集合
    movie_set = set(undo)
    for m in undo:
        # 获取这个电影的推荐
        new_rec = parse(m)
        for n in new_rec:
            # 如果这个电影不在两个集合中，则添加到undo列表中和movie_set集合中，以及all_movie.txt中
            if n not in movie_set and n not in done:
                print(m + ' + ' + n)
                undo.append(n)
                movie_set.add(n)
                with open('all_movie.txt', 'a', encoding='utf8') as f:
                    f.write(n + '\n')
                # 计数加一并log
                cnt += 1
                with open('log.txt', 'a', encoding='utf8') as log:
                    log.write('{}  source:{}  rec:{}  cnt:{}\n'.format(datetime.datetime.now(), m, n, cnt))

        # 将m设置为done
        done.add(m)
        with open('done.txt', 'a', encoding='utf8') as f:
            f.write(m + '\n')
        time.sleep(2)

    with open('log.txt', 'a', encoding='utf8') as log:
        log.write('{}  cnt:{}  All done!\n'.format(datetime.datetime.now(), cnt))

if __name__ == '__main__':
    main()
