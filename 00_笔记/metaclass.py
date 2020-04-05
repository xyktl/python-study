# -*- coding: utf-8 -*-
# 元类:创建类的类 metaclass
# https://www.liaoxuefeng.com/wiki/897692888725344/923030550637312
from metaclass_module import *
h = Hello()
print(type(Hello))  # 类Hello 的类型是 类type   <class 'type'>
print(type(h))  # 实例h 的类型是类 mataclass_module    <class 'metaclass_module.Hello'>

'''
那么问题来了，type 类到底是什么
type()函数既可以返回一个对象的类型，又可以创建出新的类型(动态创建一个类)
我们可以通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义：

type('Hello', (object,), dict(hello=fn)
要创建一个class对象，type()函数依次传入3个参数：
		1.class的名称；
		2.继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
		3class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
			通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建出class。

正常情况下，我们都用class Xxx...来定义类，但是，type()函数也允许我们动态创建出类来，
也就是说，动态语言本身支持运行期动态创建类，这和静态语言有非常大的不同，要在静态语言运行期创建类，必须构造源代码字符串再调用编译器，或者借助一些工具生成字节码实现
，本质上都是动态编译，会非常复杂。
'''


# class Print():
# 	def  print(self):
# 		print("我爱你，中国")

# 上面的这部分代码和下面这部分有相同的作用
# class Print  其实是一个函数的“语义化简称”，只为了让代码更浅显易懂，它的另一个写法是：
#  Print = type("Print", (object,), dict())
def prin(self):
    print("我爱你，中国")


Print = type("Print", (object,), dict())
p = Print()
p.print()

# 道生一，一生二，二生三，三生万物。
# 道 即是 type
# 一 即是 metaclass(元类，或者叫类生成器)
# 二 即是 class(类，或者叫实例生成器)
# 三 即是 instance(实例)
# 万物 即是 实例的各种属性与方法，我们平常使用python时，调用的就是它们。


# class Print  其实是一个函数的“语义化简称”，只为了让代码更浅显易懂，它的另一个写法是：
#  Print = type("Print", (object,), dict())
#
