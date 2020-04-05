#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 使用 Lock，若对一个线程重复加锁，则会导致线程死锁
# Rlock  解决了这个问题，可以重复加锁
import threading


def show_ok():
    print("OK")


if __name__ == "__main__":
    t = threading.Thread(target=show_ok)
    lock = threading.RLock()
    lock.acquire()		#重复加锁
    lock.acquire()
    t.start()
    lock.release()
    lock.release()
    print("锁死了吗？")
