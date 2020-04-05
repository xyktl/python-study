# -*- coding: utf-8 -*-
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 500))
print(s.recv(1024).decode("gb2312"))
for data in ["Michael", "Tracy", "Sarah"]:
    s.send(data.encode("utf-8"))
    print(s.recv(1024).decode("utf-8"))
s.send(b"exit")
s.close()
