#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 保证在多线程竞争条件下数据的安全
import queue
import threading
import time
import random
my_queue = queue.Queue(10)
thread_num = 10


def get_in_queue(in_queue, j):
    time.sleep(random.random() * 3)  # 随机休眠几秒[0~3]
    print("线程%s获取元素%s\n" % (j, in_queue))


class My_thread(threading.Thread):
    def __init__(self, target, my_queue, j):
        super(My_thread, self).__init__()
        self.my_queue = my_queue
        self.j = j
        self.target = target

    def run(self):
        self.target(self.my_queue.get(), self.j)


if __name__ == "__main__":
    for i in range(thread_num):
        my_queue.put(i)
    for j in range(thread_num):
        t = My_thread(get_in_queue, my_queue, j)
        t.start()

