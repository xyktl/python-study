# 文件的创建和读写操作
# *-* coding:utf-8 *-*
import os
#os.chdir(r"C:\Users\Hasse\Desktop")
# 在指定路径创建文件
sayhello = r"C:\Users\Hasse\Desktop\sayhello.txt"
file = open(sayhello, "a+", encoding="utf8")
# r r+  rb rb+  如果打开的文件不存在，就会报错
while True:
    text = file.readline()
    if not text:
        break
    print(text, end="")
file.write("hello\n")
file.close()
# os.remove(r"C:\Users\Hasse\Desktop\sayhello.txt")
