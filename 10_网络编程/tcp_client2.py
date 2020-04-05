# -*- coding: utf-8 -*
# 返回新浪的网页
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.sina.com.cn", 80))
s.send(b"GET / HTTP/1.1\r\nHost:www.sina.com.cn\r\nConnection:close\r\n\r\n")
l = []
while True:
    data = s.recv(1024)
    if data:
        l.append(data)
    else:
        break
s.close
print(len(l))
data = b"".join(l)
print(data)
new_l = data.decode("utf-8").split("\r\n\r\n", 1)  # 返回一个两个元素的列表
print(new_l[0])
with open("sina.html", "wb") as f:
    f.write(new_l[1].encode("utf-8"))
