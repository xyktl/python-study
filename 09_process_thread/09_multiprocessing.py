#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 用对列 queue 实现进程之间的数据通信
from multiprocessing import Process
from multiprocessing import Queue


def send_data(my_queue, data):
    my_queue.put(data)


def rece_data(my_queue):
    if my_queue.qsize() == 0:

        print("对列为空！")
    else:
        data = my_queue.get()
        print("输出；", data)


if __name__ == "__main__":
    my_queue = Queue(5)
    my_list = [0, "tom", 10, "China"]
    for i in range(5):
        my_list[0] = i
        p1 = Process(target=send_data, args=(my_queue, my_list))
        p1.start()
        p2 = Process(target=rece_data, args=(my_queue,))
        p2.start()
