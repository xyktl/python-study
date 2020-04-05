# -*- coding: utf-8 -*-

import tkinter as tk

# 创建窗口
window = tk.Tk()
window.title("my window")
window.geometry("200x200")

# 创建标签和标签变量var1
var1 = tk.StringVar()
l = tk.Label(window, bg="yellow", width=4, textvariable=var1)
l.pack()

# 创建按钮函数


def insert_selection():
    var = lb.get(lb.curselection())  # 得到lb(listbox)的光标所选处
    var1.set(var)


# 创建按钮
b1 = tk.Button(window, text="insert_selection", width=15, height=2, command=insert_selection)
b1.pack()

# 创建列表部件和列表部件变量var2
var2 = tk.StringVar()
# 设置变量的值
var2.set((11, 22, 33, 44))
lb = tk.Listbox(window, listvariable=var2)  # 将值传入listbox
# 在listbox 中循环插入一个列表的值
list_items = [1, 2, 3, 4]
for item in list_items:
    lb.insert("end", item)
lb.insert(1, "first")  # 用索引插入，在索引1的位置插入
lb.insert(2, "second")
lb.delete(2)
lb.pack()

window.mainloop()
