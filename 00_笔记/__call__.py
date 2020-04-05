# -*- coding: utf-8 -*-
# 魔术方法 __call__
# 在一个类中写入一个 __call__ 方法 这个类就是一个可调用的对象


class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __call__(self, name, age):
        self.name = name
        self.age = age
        return self.name, self.age


p = Person("xyktl", 21)
print(p("chenliang", 54))


# 实现类装饰器  装饰器要为一个可调用对象，在类中写一个__call__方法这个类就有装饰器的功能

class Count():
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("这个函数是将0-n的数插入列表中:")
        return self.func(*args, **kwargs)


@Count
def count(n):
    for i in range(n):
        l.append(i)
    print(l)


l = []
count(10)
