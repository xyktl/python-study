# 关键字 nonlocal :用来在函数或其他作用域中使用   外层（非全局）(闭包)变量
# 使用范围  ：全局变量 > 闭包变量 > 局部变量
# python引用变量的顺序： 当前作用域局部变量->外层作用域变量(闭包)->当前模块中的全局变量->python内置变量

ga = 2


def sum():
    b = 3  #b 为外层变量

    def sum1():
        nonlocal b
        r = ga + b
        return r

    return sum1


sum1 = sum()
print(sum1())
