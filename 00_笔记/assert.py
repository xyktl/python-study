#关键字 assert（断言）用于判断一个表达式，如果表达式条件为False 的时候 触发异常AssertionError
#!/usr/bin/python
# coding: utf-8
'''
assert expression  
等价于
if not expression:
    raise AssertionError(arguments)
'''
assert 2 >= 1
assert 2 >= 3

