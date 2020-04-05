# -*- coding: utf-8 -*-
# Entry  Text  输入，文本框
import tkinter as tk


window = tk.Tk()
window.title("my window")
window.geometry("200x200")

# 创建输入框
e = tk.Entry(window, show=None)
e.pack()


def insert_point():
    var = e.get()
    t.insert("insert", var)  # 在首部插入


def insert_end():
    var = e.get()
    # t.insert("end", var)  # 在尾部插入
    t.insert(1.1, var)  # 在第一行，第1列插入  这里的第1列代表我们认为的第2列，这里有0列


b1 = tk.Button(window, text="insert point", width=15, height=2, command=insert_point)
b1.pack()
b2 = tk.Button(window, text="insert end", width=15, height=2, command=insert_end)
b2.pack()
# 创建文本框
t = tk.Text(window, height=2)
t.pack()

window.mainloop()
