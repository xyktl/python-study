#!/usr/bin/env python
# -*- coding: utf-8 -*-
import multiprocessing
import requests
from requests.exceptions import ConnectionError


def scrape(url):
    try:
        print("爬取%s成功！，收到%s" % (url, requests.get(url)))
    except ConnectionError:
        print("爬取%s出错" % url)


if __name__ == "__main__":
    pool = multiprocessing.Pool()
    urls = ["http://www.metro.cn/",
            "http://www.shuichan.cc/",
            "http://www.51sole.com/",
            "http://www.x009.com/",
            "http://www.x009.comd/",
            "http://c.biancheng.net/",
            "http://www.baidu.com/",
            "http://www.w3school.com.cn/"
            "http://www.xy16.app"]

    pool.map(scrape, urls)
