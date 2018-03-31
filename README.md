# Just_Scrapy

爬虫练手项目，爬各种想爬的图片或者视频的程序。不断学习中。

* bing_background.py

  爬取[必应](https://cn.bing.com)背景图

* GIF167_bilibili_frontpage.py

  抓取B站up主-[十万个内涵图](https://search.bilibili.com/all?keyword=%E5%8D%81%E4%B8%87%E4%B8%AA%E5%86%85%E6%B6%B5%E5%9B%BE)-邪恶福利GIF合集系列视频封面，使用多线程进行爬取

* baidu_biaoqingbao.py

  从百度图片中爬取文字表情包，使用多线程爬取

* instagram.py

  爬取Instagram上的图片，使用selenium模拟浏览器，单线程爬取。爬取的两个ins账户为：

    * [natgeotravel](https://www.instagram.com/natgeotravel/)
    * [natgeo](https://www.instagram.com/natgeo/)

* net_ease_roll.py

  从[网易滚动新闻](http://news.163.com/latest/?_ad0.43182716992047965)爬取400余条新闻，作为社会信息检索作业的语料库。作业内容为：

  * TFIDF: 给定用自己名字命名的文件夹，请自己爬取一定数量的网页、微博形成语料集合，存入该文件夹；在线状态下，对其中的词语进行TFIDF统计
  * SIM: 在线状态下，从网页页面输入任意两个句子，求其相似度，包括：内积，余弦及Jaccard三种度量方式；同时，可实现对导入的文件夹语料的TFIDF统计 
  * SJet：实现基于向量空间模型（VSM）的搜索引擎