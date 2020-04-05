# -*- coding: utf-8 -*-
#Label Button  标签和按钮
import tkinter as tk
window = tk.Tk()
window.title("my window")
window.geometry("200x100")

#字符串变量
var = tk.StringVar()
#创建标签
l = tk.Label(window, textvariable=var, bg="green", font=("Arial,12"), width=15, height=2)
l.pack()  #将创建的标签放到窗口上

on_hit = False


def hit_me():
	#button 要引用的函数
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set("OMG you hit me!")
    else:
        on_hit = False
        var.set("")

#创建按钮
b = tk.Button(window, text="hit me", width=15, height=2, command=hit_me)
b.pack()
window.mainloop()
