#!/usr/bin/env python
# -*- coding: utf-8 -*-
# multiprocessing : Process pool 类
# pool 进程池
import multiprocessing
from datetime import datetime


def print_1(i):
    print("进程%d" % i)


if __name__ == "__main__":
    print("开始时间：", datetime.now())
    thread_pool = multiprocessing.Pool()
    for i in range(10):
        thread_pool.apply_async(print_1, (i,))
    thread_pool.close()  # 等待进程池执行完毕后，关闭进程
    thread_pool.join()  # 阻塞直到所有进程关闭，才可往下执行 打印主进程
    print("结束时间：", datetime.now())
