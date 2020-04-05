#!/usr/bin/python
# coding:utf-8
#无线程购买火车票
import time
from datetime import datetime 


tickets_list = [
				["2018-4-7 8:00","北京","沈阳",10,120],
				["2018-4-7 9:00","上海","宁波",5,100],
				["2018-4-7 12:00","天津","北京",20,55],
				["2018-4-7 14:00","广州","武汉",0,200],
				["2018-4-7 16:00","重庆","西安",3,180],
				["2018-4-7 18:00","深圳","上海",49,780],
				["2018-4-7 18：10","武汉","长沙",10,210]
				]
def buy_tickets(name,nums,data,start_station):
	'''输入信息购票'''
	time.sleep(1)#暂停1秒
	for get_record in tickets_list:
		if get_record[0] == data and get_record[1] == start_station:
			if nums <= get_record[3]:
				get_record[3] -= nums
				return nums
			else:
				print("现存票数不够！")
				return -1
	print("今日无票，无法购买！")
	return -1


if __name__ == "__main__":
	print("开始时间：",datetime.now())
	result = buy_tickets("张三",3,"2018-4-7 9:00","上海")
	if result > 0:
		print("张三购买%d票成功"%(3))
	result = buy_tickets("李四",1,"2018-4-7 14:00","广州")
	if result > 0:
		print("李四购买%d票成功"%(1))
	result = buy_tickets("王五",2,"2018-4-7 9:00","上海")
	if result > 0:
		print("王五购买%d票成功"%(2))
	print("结束时间：",datetime.now())
	print("剩余票数为：")
	for i in tickets_list:
		print(i)



