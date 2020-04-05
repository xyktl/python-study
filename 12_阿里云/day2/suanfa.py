
# for i in range(10):
#     print("*" * 10)

# 打印金字塔
for i in range(-4, 1):
    if i < 0:
        i = -i
    print(" " * i + "*" * (9 - 2 * i))

# 打印菱形
for i in range(-9, 10):
    if i < 0:
        i = -i
    print(" " * i + "*" * (19 - 2 * i))


# 打印九九乘法表
for i in range(1, 10):
    for j in range(1, 10):
        if j <= i:
            print("%d*%d=%d" % (j, i, i * j), end="\t")
    print("")

# 打印10行的金字塔
n = 20
for i in range(1, n + 1, 2):
    print(" " * ((n - i) // 2) + "*" * i)


m = 10
for i in range(1, m + 1):
    print(" " * (m - i) + "*" * (i * 2 - 1))

# 查重两个列表
list_1 = [1, 3, 5, 7, 9]
list_2 = [2, 5, 7, 6, 8]
list_3 = []
for i in list_1:
    for j in list_2:
        if i == j:
            list_3.append(i)
print(list_3)


# 答应100-999 的水仙花数,abc = a*a*a + b*b*b + c*c*c
import math
l = []
for i in range(100, 1000):
    bai = i // 100
    shi = (i - bai * 100) // 10
    ge = i - bai * 100 - shi * 10
    if math.pow(bai, 3) + math.pow(shi, 3) + math.pow(ge, 3) == i:
        l.append(i)
print(l)

# 打印水仙花数(四位数)
list_3 = []
for a in range(1, 10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                if a * a * a * a + b * b * b * b + c * c * c * c + d * d * d * d == 1000 * a + b * 100 + c * 10 + d:
                    list_3.append(1000 * a + b * 100 + c * 10 + d)


print(list_3)
