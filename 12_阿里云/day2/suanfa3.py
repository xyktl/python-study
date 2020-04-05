# -*- coding: utf-8 -*-
# 判断101-200之间有多少个素数，并输出所有素数
import math
total = 0

for i in range(101, 200):
    flags = True
    for j in range(2, math.ceil(i**0.5)):
        if i % j == 0:
            flags = False
            break
    if flags:
        print(i)
        total += 1
print(total)


