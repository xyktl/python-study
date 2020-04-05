# -*- coding: utf-8 -*-
# 1.创建一个包含1-100之间所有素数的列表，排序后打印显示该列表；
# 2.随后只保留该列表前5个数字，删除其余内容并打印输出相应结果；
# 3.再将每个元素值加上100，显示列表内容；把列表转化为字符串。

list_1 = []
for i in range(2, 101):
    j = 2
    flags = True
    while j <= i ** 0.5:
        if i % j == 0:
            flags = False
            break
        j += 1
    if flags:
        list_1.append(i)
print(list_1)

list_2 = list_1[0:5]
print(list_2)

list_1 = {i + 100 for i in list_1}
print(list_1)
