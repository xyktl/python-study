#!/usr/bin/env python
# -*- coding: utf-8 -*-
import threading


class My_thread(threading.Thread):
    def __init__(self, target, args):
        super().__init__()
        self.target = target
        self.arg = args
        self.thread_lock = threading.Lock()  # 创建线程锁  确保这个线程在运行时 ，其他线程处于等待状态

    def run(self):
        self.thread_lock.acquire()  # 线程运行前，先锁定
        self.target(*self.args)
        self.thread_lock.release()  # 线程运行后，释放

    # 执行 with 语句的代码块，with语句会在这个代码块执行前自动获取锁 ，在执行结束后自动结束锁
    # def run1(self):
    #     with self.thread_lock
    #         self.target(*self.args)
