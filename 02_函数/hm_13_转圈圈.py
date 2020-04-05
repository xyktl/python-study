# 给定一个数字，然后数字画圈


SIZE = 7
array = [[0] * SIZE]
# 创建一个长度SIZE * SIZE 的二维列表
for i in range(SIZE - 1):
    array += [[0] * SIZE]

# orientation代表方向
# 0向下，1向右，2向上，4向左
orientation = 0
# j 控制行索引，k控制列索引
j = 0
k = 0
for i in range(1, SIZE * SIZE + 1):
        # 判断转弯时 j和k 的关系
    array[j][k] = i
    if j + k == SIZE - 1 and j > k:
        orientation = 1  # 右转
    elif j == k and k >= SIZE / 2:
        orientation = 2  # 上转
    elif j + k == SIZE - 1 and j < k:
        orientation = 3  # 左转
    elif k - j == 1 and k <= SIZE / 2:
        orientation = 0  # 下转

    if orientation == 0:
        j += 1
    elif orientation == 1:
        k += 1
    elif orientation == 2:
        j -= 1
    elif orientation == 3:
        k -= 1
for k in range(SIZE):
    for j in range(SIZE):
        print("%02d" % array[k][j], end="\t")
    print("")
