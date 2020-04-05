#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Logger 对象可以设置多个 Handler 对象和 Filter 对象，
# Handler 对象又可以设置 Formatter 对象。
# Formatter 对象用来设置具体的输出格式


import logging
import logging.handlers

logger = logging.getLogger()  #得到一个Logger 对象
handle1 = logging.StreamHandler()	#设置控制台输出
handle2 = logging.FileHandler(filename="text.log")	#设置文件输出日志

formatter = logging.Formatter("%(asctime)s-%(levelname)s-%(message)s")	#设置 Formatter 对象	
logger.setLevel(logging.INFO)		#设置级别
handle1.setLevel(logging.WARNING)
handle2.setLevel(logging.DEBUG)

handle1.setFormatter(formatter)		#将格式对象加入 Handle 对象
handle2.setFormatter(formatter)

logger.addHandler(handle1)		#将 Handle 队象加入 Logger 对象
logger.addHandler(handle2)

logger.debug("is debug")
logger.info("is info")
logger.warning("is warning")
logger.error("is error")
logger.critical("is critical")


# 创建了自定义的 Logger 对象，就不要在用 logging 中的日志输出方法了，
# 这些方法使用的是默认配置的 Logger 对象，否则会输出的日志信息会重复。