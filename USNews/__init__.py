from const import *
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as bs

headers = {
    ':authority': 'www.usnews.com',
    ':method': 'GET',
    ':path': '/education/best-global-universities/rankings?format=json&page=1',
    ':scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    'cookie': 'usn_visitor_id=2cf93dd23a320000de57905f2e01000074160000; akacd_www=2177452799~rv=81~id=ed9c7dbf3b77d89e75e0fc4021bf5c51; usn_session_id=32951987420960274; usprivacy=1YNY; s_cc=true; s_fid=1186B98E981C29EF-215F1ED5CC106C7B; ak_bmsc=DAB7BFFA0CAF5AA0FE3F94C1C923CCB4D23DF92C3A320000DE57905F1A96C518~ply9urIgzMRyQEq9yWJctuvZeD+99tOIrU/zMuaW5fZbfahs+u4qPcikv6E64MpO4mkWQ/dokslWOeBej5vzcdUYKyyJswXHkHlG8gFBsD3iS9fc3J1uYYHXMe9/N6nrJ8ZFyhA1TVFZucZYicQDD2+Tb/+ZUHrZauoHP8woS2lAX1Epap+B5yX5WzUyr8UYTwaxycYFiksF3v3azWbMSlaD7xN2qT8bag7CHBUMuIvPfkva5E3I+kX/q5zNj7AE+t; _ga=GA1.2.1340016819.1603295206; _gid=GA1.2.605462900.1603295206; ntv_as_us_privacy=1YNY; _fbp=fb.1.1603295206673.1256085974; __gads=ID=61546c678f75d679:T=1603295206:S=ALNI_MZDDv-kcQA1d033ThVe2OM4PNNoiQ; permutive-id=1dcdba52-95f9-4541-915d-1939dfe4d2b5; _sp_ses.26f9=*; _ntv_uid=20fe92fb-3496-4a0c-a837-e7d5337934be; kw.session_ts=1603297180859; edu-page-views=12; s_sq=%5B%5BB%5D%5D; kw.pv_session=3; permutive-session=%7B%22session_id%22%3A%22fa1a583e-4985-4f0c-9593-82f795d19a66%22%2C%22last_updated%22%3A%222020-10-21T16%3A21%3A39.343Z%22%7D; sailthru_pageviews=23; utag_main=v_id:01754bd74a6d00156996677eb4a903073006206b00720$_sn:1$_ss:0$_pn:12%3Bexp-session$_st:1603299272159$ses_id:1603295201901%3Bexp-session$_prevpage:www.usnews.com%2Feducation%2Fbest-global-universities%2Frankings%3Bexp-1603301072067; sailthru_content=372ca0ca2c8977db1366580f73410ec20f8fdbf92b84b2e53c28bdba1b1f5628; sailthru_visitor=fa55978e-148e-4fb8-836e-57a7ca1cc700; bm_sv=7880E11345017289BFBF41AA65CA013A~YlkknUUyPUXlD20ubHzdBsPRFsD2KUWkyGsWhFuRm8csNFUC+34OgCy+V6GcVzmx49uO8I2CGtdSwEcLgj9ioy3ulRIOo54JFl2n2YCuhFj9AbwJh5e9PFzF/apwQQuliBx308qL8ydOs+52EZkSYlsDzWf/jw54TKmHwIqMMu8=; RT="z=1&dm=usnews.com&si=17aec90d-5366-4a15-94ac-e4c42269e945&ss=kgjkkcck&sl=8&tt=6hdq&bcn=%2F%2F684d0d3d.akstat.io%2F"; _sp_id.26f9=ddbbfd70-a58b-4f33-9c94-3c50ce8bb797.1603295208.1.1603297840.1603295208.8fb04bb6-1a47-4749-a512-e1b57e5cc1e4',
    'sec-ch-ua': '"Chromium";v="86", "\"Not\\A;Brand";v="99", "Google Chrome";v="86"',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': 1,
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
}

# print(HEADERS)
url = 'http://www.usnews.com/education/best-global-universities/rankings?format=json&page=1'
request = Request(url, headers=HEADERS)
res = urlopen(request)
print('jjj')
data = res.read().decode('utf-8')
print(data)