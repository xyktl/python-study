# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Event 是一种非常简单的线程通信机制，一个线程发出一个 Event，另一个线程可通过该 Event 被触发。

# Event 本身管理一个内部旗标，程序可以通过 Event 的 set() 方法将该旗标设置为 True，也可以调用 clear() 方法将该旗标设置为 False。
# 程序可以调用 wait() 方法来阻塞当前线程，直到 Event 的内部旗标被设置为 True。

# Event 提供了如下方法：
# is_set()：该方法返回 Event 的内部旗标是否为True。
# set()：该方法将会把 Event 的内部旗标设置为 True，并唤醒所有处于等待状态的线程。
# clear()：该方法将 Event 的内部旗标设置为 False，通常接下来会调用 wait() 方法来阻塞当前线程。
# wait(timeout=None)：该方法会阻塞当前线程。直到内部旗标为True 是才会启动
import threading
import time


event = threading.Event()


def cal():
    print("%s启动了" % threading.currentThread().getName())
    event.wait()		#事件进入阻塞状态
    print("%s收到通知了" % threading.currentThread().getName())

threading.Thread(target=cal).start()
time.sleep(2)		#主线程暂停（阻塞）了2秒
print("-" * 50)
print("主线程开始运行")
event.set()		#唤醒所有等待的线程
