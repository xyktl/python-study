
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 在实际调试程序的过程中，有时只获得异常的类型是远远不够的，还需要借助更详细的异常信息才能解决问题。

# 捕获异常时，有 2 种方式可获得更多的异常信息，分别是：
# 1 .使用 sys 模块中的 exc_info 方法；
# 2 . 使用 traceback 模块中的相关函数。

# sys.exe_info()
import sys
try:

    print(30 / 0)
except:
    print(sys.exc_info())
    print("其他异常...")


# 当输入 0 时，程序运行结果为：
# 请输入一个被除数：0
# (<class 'ZeroDivisionError'>, ZeroDivisionError('division by zero',), <traceback object at 0x000001FCF638DD48>)
# 其他异常...

# 输出结果中，第 2 行是抛出异常的全部信息，这是一个元组，有 3 个元素，
# 第一个元素是一个 ZeroDivisionError 类；第 2 个元素是异常类型 ZeroDivisionError 类的一个实例；
# 第 3 个元素为一个 traceback 对象。其中，通过前 2 个元素可以看出抛出的异常类型以及描述信息，对于第 3 个元素，
# 是一个 traceback 对象，无法直接看出有关异常的信息，还需要对其做进一步处理。

# 要查看 traceback 对象包含的内容，需要先引进 traceback 模块，然后调用 traceback 模块中的 print_tb 方法，
# 并将 sys.exc_info() 输出的 traceback 对象作为参数参入。例如：


import sys
import traceback  # 引入traceback模块
try:
    print(30 / 0)
except:
    # print(sys.exc_info())
    traceback.print_tb(sys.exc_info()[2])  # 输出元组的第三个元素 traceback
    print("其他异常...")
