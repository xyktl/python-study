# -*- coding: utf-8 -*-
# 弹窗

import tkinter as tk
import tkinter.messagebox

window = tk.Tk()
window.title("window")
window.geometry("300x300")
var = tk.StringVar()


def pop_window():
    #tk.messagebox.showinfo(title="Hi", message="nonono")
    tk.messagebox.askokcancel(title="Hi",message="nonono")


b = tk.Button(text="hit it", width="10", height="2", command=pop_window, anchor="center")
b.pack()
window.mainloop()
