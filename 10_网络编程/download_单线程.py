#!/usr/bin/env python
# -*- coding: utf-8 -*-
import threading
import time
from urllib.request import *


# class Download(threading.Thread):
#     def __init__(self, path, save_file):
#         super().__init__()
#         self.path = path
#         self.save_file = save_file
#         self.threads = []

#     def run(self):
#         req = Request(url=self.path, method="GET")
#         req.add_header('Accept', '*/*')
#         req.add_header('Charset', 'UTF-8')
#         req.add_header('Connection', 'Keep-Alive')
#         f = urlopen(req)
#         print(f)
#         data = f.read(1024)
#         b = open(self.save_file, "wb")
#         b.seek(0)
#         b.write(data)
#         b.close()


# down_thread = Download("http://www.crazyit.org/data/attachment/forum/201801/19/121212ituj1s9gj8g880jr.png", "b.png")
# down_thread.start()


def download(path, save_file):
    r = Request(url=path, method="GET")
    r.add_header("Accept", "*/*")
    r.add_header("Charset", "UTF-8")
    r.add_header("Connection", "Keep-Alive")
    resopnse = urlopen(r)
    d = resopnse.read(1024)
    with open(save_file, "wb") as f:
        f.seek(0)
        f.write(d)


t1 = time.clock()
t = threading.Thread(target=download, args=(
    "http://www.crazyit.org/data/attachment/forum/201801/19/121212ituj1s9gj8g880jr.png", "b.png"))
t.start()
t2 = time.clock()
print(t2 - t1)
