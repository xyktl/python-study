# 装饰器   用来增加函数的功能


# 一个简单的装饰器 来增加 提示功能（开始执行了，结束执行了）


def decorator(func):
    def fun(*args, **kwargs):
        print("开始执行了！")
        func(*args, **kwargs)
        print("结束执行了！")
    return fun

#@语法糖    @后面加上装饰器可以直接为下面的函数加上装饰器
@decorator
def sum(a, b):
    r = a + b
    print(r)


sum(123, 456)
