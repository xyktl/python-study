#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 创建一个tcp 客户端
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 1000))
s.send("hello ".encode("utf-8"))
while True:
    data = s.recv(1024)
    if data:
        print(data.decode("gb2312"))
    else:
        break
print("断开连接")
