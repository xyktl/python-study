# -*- coding: utf-8 -*-
import scrapy
from myspider.items import MyspiderItem
from scrapy.http import Request
import re


class DandanspiderSpider(scrapy.Spider):
    name = 'dandanspider'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://search.dangdang.com/?key=python&act=input/page_index=1']


    def parse(self, response):
        print(type(response))
        item = MyspiderItem()
        item["title"] = response.xpath("//a[@name='itemlist-picture']/@title").extract()
        item["price"] = response.xpath("//p[@class='price']//span[@class='search_now_price']/text()").extract()
        item["comment"] = response.xpath("//p[@class='search_star_line']//a/text()").extract()

        #去除爬取项中不需要部分数据
        item["price"] = list(map(lambda x: re.sub('\?','',x),item["price"]))
        item["comment"] = list(map(lambda x: re.sub('条评论','',x),item["comment"]))
        yield item
        for i in range(2,101):
            url = 'http://search.dangdang.com/?key=python&act=input/page_index='+str(i)+'"'
            yield Request(url,callback=self.parse)

            #你到一个商店买东西，刚好你要的东西没有货，于是你在店员那里留下了你的电话，过了几天店里有货了，店员就打了你的电话，然后你接到电话后就到店里去取了货。
            # 在这个例子里，你的电话号码就叫     回调函数，
            # 你把电话留给店员就叫     登记回调函数，
            # 店里后来有货了叫做    触发了回调关联的事件，
            # 店员给你打电话叫做    调用回调函数，
            # 你到店里去取货叫做    响应回调事件。

