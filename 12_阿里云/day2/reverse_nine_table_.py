# -*- coding: utf-8 -*-
import math
for i in range(-9, 0):
    for j in range(1, 10):
        if abs(i) >= abs(j):
            print("%d*%d=%d" % (j, abs(i), abs(i * j)), end="\t")
    print("")
