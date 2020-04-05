#捕获异常的格式
"""
try:
    pass
except Exception as result:
    print(result)
"""
import os
try:
    num = (input("请输入一个整数:"))
    if type(num) is not int:
        ex = Exception("%s类型出错" % (num))
        raise ex
    #关键字 raise 抛出异常
    else:
        print(num)
except ValueError:
    pass
except SyntaxError:
    pass
except AttributeError:
    pass
except Exception as result:
    print(result)
    #捕获异常
else:
    #没有异常才会执行的代码
    print("")
finally:
    #无论是否异常，都会执行的代码
    print("")
print(os.__file__)
