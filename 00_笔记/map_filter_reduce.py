# map(function,iterable) : 可以对可迭代对象中的所有元素做指定的操作，然后返回一个新的对象
#function : 操作
#iterable : 可迭代对象

lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_lis = list(map(lambda x: x + 1, lis))  # 对所有元素做 +1 操作
print(lis)
print(new_lis)


# reduce(function, iterable) :对一个集合做累积操作
# 由于 reduce() 函数在 Python 3.x 中已经被移除，放入了 functools 模块，因此在使用该函数之前，需先导入 functools 模块。
import functools
listDemo = [1, 2, 3, 4, 5]
product = functools.reduce(lambda x, y: x * y, listDemo)
print(product)


# filter(function,iterable)  过滤器  :用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。
# function:  函数  序列过滤的条件
# iterable: 	序列  可迭代对象
# 该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判，
# 然后返回 True 或 False，最后将返回 True 的元素放到新列表中

lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_list = list(filter(lambda x: x % 2 == 0, lis))  # 过滤lis 列表中的偶数
print(new_list)
