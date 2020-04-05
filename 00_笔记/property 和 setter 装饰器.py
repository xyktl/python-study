#!/usr/bin/env python
# -*- coding: utf-8 -*-
# property 装饰器用来将一个 get 方法 ，转换为对象的隐藏属性
# 添加 property 装饰器后，我们就可以像调用属性一样调用 get 方法
# 使用 property 的方法 必须和属性名一样

#setter 装饰器用来将一个 set 方法 ， 来设置对象的隐藏属性

class Person(object):
    """创建一个人"""

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 为了调用隐藏的属性  单下划线  _name
    @property
    def name(self):
        print("get方法被执行了~~")
        return self._name
    #为了修改隐藏的属性
    @name.setter
    def name(self, name):
        print("set方法被执行了~~")
        self._name = name


person1 = Person("孙悟空", 12222)
person2 = Person("猪八戒", 7445)

print(person1.name)
person1.name = "孙空悟"
print(person1.name)
