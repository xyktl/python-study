# -*- coding: utf-8 -*-
from urllib.request import *
import threading


class Down(object):
    def __init__(self, path, save_file, thread_num):
        #定义下载资源的路径
        self.path = path
        #指定资源保存的文件
        self.save_file = save_file
        #指定线程数
        self.thread_num = thread_num
        self.threads = []

    def download(self):
        headers = {"Accept": "*/*",
                   "Charset": "utf-8",
                   "Connection": "Keep-Alive"
                   }
        req = Request(url=self.path, headers=headers, method="GET")
        response = urlopen(req)
        print(response.headers)
        #获取下载的文件大小
        self.file_size = int(dict(response.headers).get("Content-Length", 0))
        response.close()
        #计算每个线程要下载的资源的大小
        average_size = self.file_size // self.thread_num + 1
        for i in range(self.thread_num):
            #计算每个线程下载的开始位置
            start_pos = i * average_size
            file = open(self.save_file, "wb")
            #定义该线程的下载位置
            file.seek(start_pos, 0)
            #创建下载线程
            t = DownThread(self.path, average_size, start_pos, file)
            self.threads.append(t)
            t.start()


    def get_download_rate(self):
        '''获取所下载所占的百分比'''
        sum_size = 0
        for i in range(self.thread_num):
            sum_size += self.threads[i].length
        if sum_size / self.file_size > 1:
            return 1
        return sum_size / self.file_size

    def show_download_rate(self):
        '''以指定格式输出'''
        d = self.get_download_rate()
        print("已完成：{:.0%}".format(d))
        if d < 1:
            #每过0.5秒执行show_download_rate函数
            t = threading.Timer(0.5, self.show_download_rate)
            t.start()


class DownThread(threading.Thread):
    def __init__(self, path, average_size, start_pos, download_part):
        super().__init__()
        #当前线程的下载位置
        self.path = path
        self.average_size = average_size
        self.start_pos = start_pos
        #当前线程需要下载的文件块
        self.download_part = download_part
        self.length = 0

    def run(self):
        headers = {"Accept": "*/*",
                   "Charset": "utf-8",
                   "Connection": "Keep-Alive"
                   }
        req = Request(url=self.path, headers=headers, method="GET")
        response = urlopen(req)
        #跳过self.start_pos个字节，表面该线程只下载自己负责的那部分内容
        for i in range(self.start_pos):
            response.read(1)
        #读取网络数据，并写入本地文件
        while self.length < self.average_size:
            data = response.read(1024)
            if data is None or len(data) <= 0:
                break
            self.download_part.write(data)
            #累计该线程下载的总大小
            self.length += len(data)
        self.download_part.close()
        response.close()


down = Down("http://pic16.nipic.com/20111006/6239936_092702973000_2.jpg", 'a.jpg', 3)
down.download()
down.show_download_rate()
