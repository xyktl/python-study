#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 闭包 希望自己的变量不被外部访问
# 闭包形成的要件：
#				1.函数嵌套
#				2.将内部函数作为返回值返回
#				3.内部函数必须使用到外部函数的变量


def closure():

    my_list = []#希望 my_list 列表不被外界访问 ，就可以放到闭包中

    def average(l):
        my_list.append(l)
        return sum(my_list) / len(my_list)
    return average
average = closure()
print(average(10))
print(average(10))
print(average(20))
