#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Pipe() 方法：用管道实现进程之间的通信  Pipe直接发送和接收字节流
# 创建两个管道对象，用send() 方法发送   recv() 接收

from multiprocessing import Process
from multiprocessing import Pipe


def send_data(send_connect):
    send_connect.send("hello world")
    send_connect.close()


if __name__ == "__main__":
    receive_connect, send_connect = Pipe()  #返回两个来连接对象
    p1 = Process(target=send_data, args=(send_connect,))		#创建管道发送数据进程
    p1.start()
    data = receive_connect.recv()		#接收管道发送的数据
    print("接收数据：", data)
    p1.join()
    p1.close()
