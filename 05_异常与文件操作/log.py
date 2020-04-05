# #!/usr/bin/env python
# # -*- coding: utf-8 -*-

# # logging 日志级别：debug < info < warning < error < critical
# basicConfig()函数参数名称 	参数描述
# filename	日志输出到文件的文件名
# filemode	文件模式，r[+]、w[+]、a[+]		将日志输出到文件
# format		日志输出的格式		format="%(asctime)s-%(levelname)s-%(message)s"
# datefat		日志附带日期时间的格式
# style		格式占位符，默认为 "%" 和 “{}”
# level       设置日志输出级别
# stream      定义输出流，用来初始化 StreamHandler 对象，不能 filename 参数一起使用，否则会ValueError 异常
# handles     定义处理器，用来创建 Handler 对象，不能和 filename 、stream 参数一起使用，否则也会抛出 ValueError 异常


import logging
# logging.basicConfig(level=logging.DEBUG, format="%(asctime)s-%(levelname)s-%(message)s")
# logging.debug("start of program")


# def factorial(n):
#     logging.info("start of factorial(%s)" % n)
#     product = 1
#     for i in range(1 + n):
#         product *= i
#         logging.info("i is %s ,product is %s" % (i, product))
#     logging.info("The end of product is %s" % product)


# factorial(5)


# 但是当发生异常时，直接使用无参数的 debug()、info()、warning()、error()、critical() 方法并不能记录异常信息，
# 需要设置 exc_info 参数为 True 才可以，或者使用 exception() 方法，还可以使用 log() 方法，但还要设置日志级别和 exc_info 参数。
logging.basicConfig(filename="test.log", filemode="w+", format="%(asctime)s %(name)s:%(levelname)s:%(message)s",
                    datefmt="%d-%M-%Y %H:%M:%S", level=logging.DEBUG)
a = 5
b = 0
try:
    c = a / b
except Exception as e:
    # 下面三种方式三选一，推荐使用第一种
    logging.exception("Exception occurred")
    logging.error("Exception occurred", exc_info=True)
    logging.log(level=logging.DEBUG, msg="Exception occurred", exc_info=True)
