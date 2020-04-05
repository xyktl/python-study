#!/usr/bin/python
# coding:utf-8
# 无线程购买火车票  改进版1
import time
import threading
from datetime import datetime


tickets_list = [
    ["2018-4-7 8:00", "北京", "沈阳", 10, 120],
    ["2018-4-7 9:00", "上海", "宁波", 5, 100],
    ["2018-4-7 12:00", "天津", "北京", 20, 55],
    ["2018-4-7 14:00", "广州", "武汉", 0, 200],
    ["2018-4-7 16:00", "重庆", "西安", 3, 180],
    ["2018-4-7 18:00", "深圳", "上海", 49, 780],
    ["2018-4-7 18：10", "武汉", "长沙", 10, 210]
]


def buy_tickets(name, nums, data, start_station):
    '''输入信息购票'''
    time.sleep(1)  # 暂停1秒
    for get_record in tickets_list:
        if get_record[0] == data and get_record[1] == start_station:
            if nums <= get_record[3]:
                get_record[3] -= nums
                print("%s购买%s张票成功!" % (name, nums))
                return nums
            else:
                print("%s 现存票数不够！" % name)
                return -1
    print("今日无票，无法购买！")
    return -1


if __name__ == "__main__":
    print("开始时间：", datetime.now())
    start_time = time.time()
    t1 = threading.Thread(target=buy_tickets, args=("张三", 3, "2018-4-7 9:00", "上海"))
    t2 = threading.Thread(target=buy_tickets, args=("李四", 1, "2018-4-7 14:00", "广州"))
    t3 = threading.Thread(target=buy_tickets, args=("王五", 2, "2018-4-7 9:00", "上海"))
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    print("结束时间：", datetime.now())
    end_time = time.time()
    use_time = end_time - start_time
    print("使用了 %s 秒" % use_time)
    for i in tickets_list:
        print(i)
