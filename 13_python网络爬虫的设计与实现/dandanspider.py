# -*- coding: utf-8 -*-
import scrapy


class DandanspiderSpider(scrapy.Spider):
    name = 'dandanspider'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://dangdang.com/']

    def parse(self, response):
        pass
