#!/usr/bin/env python
# -*- coding: utf-8 -*-
from multiprocessing import Process
from datetime import datetime


def print_1(i):
    print("进程：%d" % i)


if __name__ == "__main__":
    print("开始时间：", datetime.now())
    for i in range(10):
        my_process = Process(target=print_1, args=(i,))
        my_process.start()
        my_process.join()
    print("结束时间：", datetime.now())
