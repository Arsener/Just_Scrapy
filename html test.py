'''
检测是否可以通过访问url获得的html获取页面内所有元素
'''
import os
import time
import argparse
import threading
from urllib.request import Request, urlopen, urlretrieve
from bs4 import BeautifulSoup as bs

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
TITLE_DICT = dict()


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Download IJCAI papers.'
    )
    parser.add_argument('--year', type=str, default='2018',
                        help='YEAR')
    parser.add_argument('--save_path', type=str, metavar='PATH', default='paperss',
                        help='path where the papers are/should be saved')
    parser.add_argument('--thread_num', type=int, default=4,
                        help='Number of threads')

    return parser.parse_args()


def getIJCAIPapers(year, save_path, minnum, maxnum):
    url = 'https://www.ijcai.org/proceedings/{}/{:04d}.pdf'
    # maxnum = 870
    for i in range(minnum, maxnum):
        urlpath = url.format(year, i)
        file_path = '{}/{:04d}.pdf'.format(save_path, i)
        print('[{}/{}]  Downloading ->  + {}'.format(i, maxnum - 1, file_path))
        try:
            urlretrieve(urlpath, file_path)
        except Exception as err:
            print(urlpath, ' error :', err)
            continue
    # print("all download finished")


if __name__ == '__main__':
    args = parse_arguments()
    year = args.year
    save_path = args.save_path
    if not os.path.exists(save_path):
        os.makedirs(save_path)
        print('New folder is created: {}'.format(save_path))
    thread_num = args.thread_num
    url = 'https://www.ijcai.org/Proceedings/{}/'.format(year)
    request = Request(url, headers=HEADERS)
    res = urlopen(request)
    html = res.read().decode('utf-8')

    papers = bs(html, 'html.parser').find_all(class_='paper_wrapper')[:12]
    print('Paper list extracted!')
    for i, p in enumerate(papers):
        TITLE_DICT[i + 1] = p.find(class_='title').text

    threads = []
    cnt = len(papers) // thread_num
    t1 = time.time()
    # for i in range(thread_num):
    #     t = threading.Thread(target=getIJCAIPapers,
    #                          args=(year, save_path, i * cnt + 1, min((i + 1) * cnt + 1, len(papers) + 1)))
    #     threads.append(t)
    # for t in threads:
    #     t.start()
    # for t in threads:
    #     t.join()
    getIJCAIPapers(year, save_path, 1, 13)
    print('Download finished!')
    t2 = time.time()
    print(t2 - t1)
