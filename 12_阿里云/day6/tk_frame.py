# -*- coding: utf-8 -*-
# 框架
import tkinter as tk

window = tk.Tk()
window.title("my window")
# 设置窗口尺寸
width = 300
height = 300
# 获取屏幕尺寸以计算布局参数，使窗口居屏幕中央
screenwidth = window.winfo_screenmmwidth()
screenheight = window.winfo_screenmmheight()
alignstr = f"{width}x{height}+" + str((screenwidth - width) // 2) + "+" + str((height - screenheight) // 2)
#传入窗口的尺寸和窗口的位置
window.geometry(alignstr)
f1 = tk.Frame(window).pack(side="left")
f2 = tk.Frame(window).pack(side="right")
f3 = tk.Frame(f1).pack(side="top")
f4 = tk.Frame(f1).pack(side="bottom")
l1 = tk.Label(f1, text="frame 1", bg="green").pack(side="top")
l2 = tk.Label(f2, text="frame 2", bg="yellow").pack(side="top")
l3 = tk.Label(f3, text="frame 3", bg="white").pack(side="left")
l4 = tk.Label(f4, text="frame 4", bg="blue").pack(side="right")


window.mainloop()
