# # -*- coding: utf-8 -*-
'''
mkdir:创建文件夹
rmdir:删除文件夹
'''
# # 创建day4-day30 文件
import os
base = "C:\\Users\\Hasse\\Desktop\\pyproject\\12_阿里云\\"
for i in range(31, 36):
    file_name = ".\\" + "day" + str(i)
    os.mkdir(file_name)


# 删除 day4 - day30 文件
# for i in range(4, 31):
#     file_name = base + "day" + str(i)
#     os.rmdir(file_name)
