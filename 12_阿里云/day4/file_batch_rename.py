# *-* coding:utf-8 *-*
import os
base = "C:\\Users\\Hasse\\Desktop\\py project\\test\\"

# 创建10个txt文件
for i in range(1, 16):
    file_name = base + "abc.com" + str(i) + ".txt"
    open(file_name, "w")

# 批量重命名
for i in range(1, 16):
    oldpath = base + "abc.com" + str(i) + ".txt"
    newpath = base + f"{str(i)}.txt"
    #newpath = base + str(i) + ".txt"
    os.rename(oldpath, newpath)
