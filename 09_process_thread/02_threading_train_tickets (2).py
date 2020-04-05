#!/usr/bin/python
# coding:utf-8
# 有线程购买火车票  改进版2 将进程放入一个列表中
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
                print("%s 购买%s张票成功" % (name, nums))
                return nums
            else:
                print("%s 现存票数不够！" % name)
                return -1
    print("今日无票，无法购买！")
    return -1


class My_thread(threading.Thread):
    def __init__(self, target, args):
        super().__init__()
        self.target = target
        self.args = args

    def run(self):
        self.target(*self.args)


if __name__ == "__main__":
    #start_time = datetime.now()
    print("开始时间：", datetime.now())
    start_time = time.time()

    vistor_list = [("张三", 3, "2018-4-7 9:00", "上海"),
                   ("李四", 1, "2018-4-7 14:00", "广州"),
                   ("王五", 2, "2018-4-7 9:00", "上海")]
    thread_list = []
    PEOPLE_NUM = 3
    for i in vistor_list:  # 循环创建抢票线程 并 装入多线程列表中
        my_thread = My_thread(target=buy_tickets, args=i)
        thread_list.append(my_thread)
    for my_thread in thread_list:  # 循环启动线程
        my_thread.start()
    for my_thread in thread_list:  # 循环进行线程堵塞    join():等待该线程执行完才会执行主线程（打印时间 和 剩余票数）
        my_thread.join()

    #end_time = datetime.now()
    print("结束时间：", datetime.now())
    end_time = time.time()
    use_time = end_time - start_time
    print("使用了 %s 秒" % use_time)
    print("剩余票数为：")
    for i in tickets_list:
        print(i)
