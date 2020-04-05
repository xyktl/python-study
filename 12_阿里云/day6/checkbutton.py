# -*- coding: utf-8 -*-
#checkbutton 勾选项
import tkinter as tk
window = tk.Tk()
window.title("my window")
window.geometry("200x100")


# 创建标签

l = tk.Label(window, text="empty", bg="yellow", width=20)
l.pack()  # 将创建的标签放到窗口上

#定义按钮函数
def print_selection():
    if (var1.get() == 1) and (var2.get() == 0):
        l.config(text="I love only Python")
    elif (var1.get() == 0) and (var2.get() == 1):
        l.config(text="I love only C++")
    elif (var1.get() == 1) and (var2.get() == 1):
        l.config(text="I love both")
    else:
        l.config(text="I do not like either")



# 创建选择按钮和变量
var1 = tk.IntVar()
var2 = tk.IntVar()
c1 = tk.Checkbutton(window, text="Python", variable=var1, onvalue=1, offvalue=0, command=print_selection)
c2 = tk.Checkbutton(window, text="C++", variable=var2, onvalue=1, offvalue=0, command=print_selection)
c1.pack()
c2.pack()
window.mainloop()
