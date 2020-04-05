# 文件的创建和读写操作
# *-* coding:utf-8 *-*
import os
os.chdir(r"C:\Users\Hasse\Desktop")
# 在指定路径创建文件
file = open("sayhello.txt", "a+")
#file = open("sayhello.txt", "r+", encoding="utf8")
"""
r  rb 读取文件的内容  如果打开的文件不存在，就会报错
r+ rb+  读取并可以追加内容，如果打开的文件不存在，就会报错
w 在文件中添加内容（会覆盖原有的内容），如果文件不存在，则会新建文件,没有read（）
w+  可以read（）
a 在文件中追加内容（不会覆盖原有的内同），如果文件不存在，则会新建文件，没有read()
a+  可以read（）
b   新建二进制文件  如音频文件
x  以可写方式新建一个文件，如果文件存在，则会报错
"""
while True:
    text = file.readline()
    if not text:
        break
    print(text, end="")
file.write("hello\n")
file.close()
# 删除指定的文件
os.remove(r"C:\Users\Hasse\Desktop\sayhello.txt")
# os.remove("C:\\Users\\HasseDesktop\\sayhello.txt")
