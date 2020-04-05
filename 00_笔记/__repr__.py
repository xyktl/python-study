#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__repr__:自我描述的方法，可以重写这个方法改变自我描述


class Person(object):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


person1 = Person("孙悟空")
print(person1)  # 输出对象的自我描述
