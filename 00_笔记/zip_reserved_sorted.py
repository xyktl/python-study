#!/usr/bin/env python
# -*- coding: utf-8 -*-
# zip() 函数可以把两个列表“压缩”成一个 zip 对象（可迭代对象），这样就可以使用一个循环并行遍历两个列表

a = ['a', 'b', 'c']
b = [1, 2, 3]
for x in zip(a, b):
    print(x)

# 将列表转换为字典
name = ['zhang', 'li']
age = [30, 25]
person = dict(zip(name, age))
print(person)

# 有些时候，程序需要进行反向遍历,此时可通过 reversed() 函数，该函数可接收各种序列（元组、列表、区间等）参数，
# 然后返回一个“反序排列”的法代器，该函数对参数本身不会产生任何影响。

a = range(10)
for i in reversed(a):
    print(i, end=" ")


# sorted() 函数与 reversed() 函数类似，该函数接收一个可迭代对象作为参数，返回一个对元素排序的列表。
print()
a = [20, 30, -1.2, 3.5, 90, 3.6]
print(sorted(a))
print(sorted(a, reverse=True))


# 调用 sorted() 函数时，还可传入一个 key 参数，该参数可指定一个函数来生成排序的关键值。
# 比如希望根据字符串长度排序，则可为 key 参数传入 len 函数。例如如下运行过程：
b = ['fkit', 'crazyit', 'charlie', 'fox', 'Emily']
print(sorted(b, key=len))  # 根据字符串长度排序
