# -*- coding: utf-8 -*-

import tkinter as tk
window = tk.Tk()
window.title("my window")
window.geometry("200x100")


# 创建标签

l = tk.Label(window, text="empty", bg="yellow", width=20)
l.pack()  # 将创建的标签放到窗口上


def print_selection(v):
    l.config(text="you have selected" + v)


s = tk.Scale(window, label="try me", from_=5, to=11, orient=tk.HORIZONTAL, length=200, showvalue=0,
             tickinterval=3, resolution=0.01, command=print_selection)
# tickinterval	刻度间隔	resolution	刻度精确度  orinent	反向 showvalue	滑动是是否显示数字
s.pack()

window.mainloop()
