#!/usr/bin/env python
# -*- coding: utf-8 -*-

# raise 语句有如下三种常用的用法：
# raise：单独一个 raise。该语句引发当前上下文中捕获的异常（比如在 except 块中），或默认引发 RuntimeError 异常。
# raise 异常类名称：raise 后带一个异常类名称。该语句引发指定异常类的默认实例。
# raise 异常类名称(描述信息)：在引发指定异常的同时，附带异常的描述信息。


def main():
    try:
        # 使用try...except来捕捉异常
        # 此时即使程序出现异常，也不会传播给main函数
        mtd(3)
    except Exception as e:
        print('程序出现异常:', e)
    # 不使用try...except捕捉异常，异常会传播出来导致程序中止
    mtd(3)


def mtd(a):
    if a > 0:
        raise ValueError("a的值大于0，不符合要求")


main()


# 运行上面程序，可以看到如下输出结果：错误
# 上面第一行输出是第一次调用 mtd (3) 的结果，该方法引发的异常被 except 块捕获并处理。后面的大段输出则是第二次调用 mtd(3) 的结果，
# 由于该异常没有被 except 块捕获，导致程序中止。

# 第二次调用 mtd(3) 引发的以“File”开头的三行输出，其实显示的就是异常的传播轨迹信息。
# 也就是说，如果程序不对异常进行处理，Python 默认会在控制台输出异常的传播轨迹信息。