#!/usr/bin/env python
# -*- coding: utf-8 -*-
# eval() 和 exec() 函数的功能是相似的，都可以执行一个字符串形式的 Python 代码（代码以字符串的形式提供），相当于一个 Python 的解释器。
# 二者不同之处在于，eval() 执行完要返回结果，而 exec() 执行完不返回结果


a = 1
a = exec("2+3")  # 相当于直接执行 2+3，但是并没有返回值，a 应为 None
print(a)
a = eval("2+3")  # 执行 2+3，并把结果返回给 a
print(a)


# eval() 和 exec() 函数的应用场景:
# 在使用 Python 开发服务端程序时，这两个函数应用得非常广泛。
# 例如，客户端向服务端发送一段字符串代码，服务端无需关心具体的内容，直接跳过 eval() 或 exec() 来执行，
# 这样的设计会使服务端与客户端的耦合度更低，系统更易扩展。

# exec(source, globals=None, locals=None, /)
# 如果只是提供了 globals 参数，而没有提供自定义的 __builtins__，则系统会将当前环境中的 __builtins__ 复制到自己提供的 globals 中，
# 然后才会进行计算；如果连 globals 这个参数都没有被提供，则使用 Python 的全局命名空间。
a = 10
b = 20
c = 30
g = {"a": 6, "b": 8}  # 定义一个字典
t = {"a": 100, "c": 10}  # 定义一个字典
print(eval("a+b+c", g, t))  # 定义一个字典 116
