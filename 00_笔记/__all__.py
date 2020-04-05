#!/usr/bin/env python
# -*- coding: utf-8 -*-
#在默认情况下，如果使用“from 模块名 import *”这样的语句来导入模块，程序会导入该模块中所有不以下画线开头的成员（包括变量、函数和类）。
#但在一些场景中，我们并不希望每个成员都被暴露出来供外界使用，此时可借助于模块的 __all__ 变量，将变量的值设置成一个列表，
#只有该列表中的成员才会被暴露出来。
def hello():
    print("Hello, Python")
def world():
    print("Pyhton World is funny")
def test():
    print('--test--')
# 定义__all__变量，指定默认只导入hello和world两个成员
__all__ = ['hello', 'world']
