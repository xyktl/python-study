# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import re

class MyspiderPipeline(object):
    def process_item(self, item, spider):

        conn = pymysql.connect(host="127.0.0.1",user="root",passwd="c1635976271",db="dd")
        for i in range(0,len(item["title"])):

            title = item["title"][i]
            price = item["price"][i]
            comment = item["comment"][i]
            sql = "insert into books(title,price,comments) values(%s,%s,%s)"

            try:
                cursor.execute(sql,
                               (item['userIcon'], item['userName'], item['content'], item['like'], item['comment']))
                conn.commit()
            except Exception as e:
                print(e)
                conn.rollback()
            cursor = conn.cursor()
            cursor.execute(sql,(title,price,comment))
            #conn.query(sql)
            conn.commit()
        conn.close()
        return item





