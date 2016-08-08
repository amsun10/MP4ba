import time

import requests
from requests import ConnectionError


class MyRequest:
    def __init__(self):
        self.session = requests.session()
        self.session.headers.update({'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
                                     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                                     "Accept-Encoding": "gzip, deflate, sdch",
                                     "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4",
                                     "Cache-Control": "max-age=0",
                                     "Connection": "keep-alive",
                                     "Cookie": "__cfduid=db7a70547d472a3195d2c580c2434ef4c1457749758; cscpvcouplet_fidx=1; cscpvrich_fidx=1; CNZZDATA5925857=cnzz_eid%3D863127887-1455939943-null%26ntime%3D1470667180",
                                     "Host": "www.mp4ba.com",
                                     "Upgrade-Insecure-Requests": 1})

    def get(self, url, **kwargs):
        for i in range(10):
            try:
                return self.session.get(url, **kwargs)
                break
            except ConnectionError:
                print "connection error sleep 1 seconds"
                time.sleep(1)
