#!/usr/bin/env python
# -*- coding: utf-8 -*-

# traceback.print_exc()：将异常传播轨迹信息输出到控制台或指定文件中。
# print_exception(etype, value, tb[,limit[, file]])，在完整形式中，前面三个参数用于分别指定异常的如下信息：
# etype：指定异常类型；
# value：指定异常值；
# tb：指定异常的traceback 信息；

import traceback


class SelfException(Exception):
    pass


def main():
    firstMethod()


def firstMethod():
    secondMethod()


def secondMethod():
    thirdMethod()


def thirdMethod():
    raise SelfException("自定义异常信息")


try:
    main()
except:
    # 捕捉异常，并将异常传播信息输出控制台
    traceback.print_exc()
    # 捕捉异常，并将异常传播信息输出指定文件中
    traceback.print_exc(file=open("log.txt", 'a'))
