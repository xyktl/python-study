# -*- coding: utf-8 -*-
# 偏函数：固定原来函数的参数，改变某一个参数的默认值

from functools import partial

# 用偏函数改进，将默认的转化为10进制 改变 为默认转化为二进制
int2 = partial(int, base=2)  # base 代表进制
print(int("2"))
print(int2("10000"))


def mod(n, m):
    return n % m


# 将第一个参数设置为默认为100
mod1 = partial(mod, 100)
print(mod(100, 7))
print(mod1(7))
