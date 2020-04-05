# -*- coding: utf-8 -*-
import socket
import threading
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 500))
s.listen()


def client_handle(s):
    s.send(b"welcome")
    while True:
        data = s.recv(1024)
        print(data.decode("gb2312"))
        if not data or data.decode("gb2312") == "exit":
            print("断开连接")
            break
        s.send(("收到%s" % data.decode("gb2312")).encode("utf-8"))
    s.close()


while True:
    sock, addr = s.accept()
    print("%s连接上了" % sock)
    t = threading.Thread(target=client_handle, args=(sock,))
    t.start()
