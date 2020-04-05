# -*- coding: utf-8 -*-
def print_lx(row):
    '''打印一个row 行的菱形'''
    n = (row - 1) // 2

    i = 1
    while i <= n:
        print(" " * (n + 1 - i) + "*" * (2 * i - 1))
        i += 1
    print("*" * row)
    j = n
    while j >= 1:
        print(" " * (n + 1 - j) + "*" * (2 * j - 1))
        j -= 1


print_lx(19)


# 升级版1
def print_lx_update1(row):
    n = (row - 1) // 2
    for i in range(1, n + 1):
        print(" " * (n + 1 - i) + "*" * (2 * i - 1))
    print("*" * row)
    for i in range(n, 0, -1):
        print(" " * (n + 1 - i) + "*" * (2 * i - 1))


print_lx_update1(7)

# 升级版2


def print_lx_update2(row):
    '''打印一个row 行的菱形'''
    n = (row - 1) // 2
    for i in range(0 - n, n + 1):
        if i < 0:
            i = -i
        print(" " * i + "*" * (row - 2 * i))


print_lx_update2(9)
