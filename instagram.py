import time
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver

base_url = 'https://www.instagram.com/'
users = ['natgeotravel', 'natgeo']
file_format = ['.jpg', '.mp4']
taken_by = '?taken-by='
dir = 'D:/instagram/'
CURRENT_USER = 0

driver = webdriver.PhantomJS(executable_path='e:/phantomjs/bin/phantomjs')
driver.get(base_url + users[CURRENT_USER])

# 点击“更多”
links = driver.find_elements_by_tag_name('a')
more = '/' + users[CURRENT_USER] + '/?max_id='
for link in links:
    if more in link.get_attribute('href'):
        link.click()
        break
time.sleep(5)

# 下滑加载更多
for i in range(5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)

html = BeautifulSoup(driver.page_source, 'html5lib')

# 获取每个图片或者视频的详情页URL
photos = html.find_all('div', {'class': '_mck9w _gvoze _f2mse'})
photo_urls = []
video_urls = []
for photo in photos:
    url = photo.find('a').get('href')

    tags = photo.find('a').find_all('div')
    # 分类图片和视频
    if len(tags) == 3:
        photo_urls.append(url[1:])
    elif len(tags) == 5:
        video_urls.append(url[1:])

for photo_url in photo_urls:
    photo_detail_url = base_url + photo_url + taken_by + users[CURRENT_USER]
    print(photo_detail_url)
    try:
        photo_request = urllib.request.urlopen(photo_detail_url)
        photo_html = BeautifulSoup(photo_request, 'html5lib')
        download_url = str(photo_html).split('"display_url": "')[1].split('", "display_resources"')[0]
        filename = download_url.split('/e35/')[1].split('.jpg')[0]
        urllib.request.urlretrieve(download_url, filename=dir + users[CURRENT_USER] + '/' + filename + file_format[0])
    except:
        print('no answer')
        # 将暂时响应失败的URL再次添加到列表中，之后重新访问
        photo_urls.append(photo_url)


for video_url in video_urls:
    video_detail_url = base_url + video_url + taken_by + users[CURRENT_USER]
    print(video_detail_url)
    try:
        video_request = urllib.request.urlopen(video_detail_url)
        video_html = BeautifulSoup(video_request, 'html5lib')
        download_url = str(video_html).split('"video_url": "')[1].split('", "video_view_count"')[0]
        filename = download_url.split('t50.2886-16/')[1].split('.mp4')[0]
        urllib.request.urlretrieve(download_url, filename=dir + users[CURRENT_USER] + '/' + filename + file_format[1])
    except:
        print('no answer')
        # 将暂时响应失败的URL再次添加到列表中，之后重新访问
        video_urls.append(video_url)

















