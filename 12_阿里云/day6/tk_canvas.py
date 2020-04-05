# -*- coding: utf-8 -*-
# Canvas 画布
import tkinter as tk

window = tk.Tk()
window.title("my window")
window.geometry("200x200")

canvas = tk.Canvas(window, bg="white", height=100, width=200)
image_file = tk.PhotoImage(file="")  # 在画布中插入图片
image = canvas.create_image(0, 0, anchor="nw", image=image_file)  # anchor参数表示位置，nw代表画布center的西南
x0, y0, x1, y1 = 50, 50, 80, 80
line = canvas.create_line(x0, y0, x1, y1)  # 直线
oval = canvas.create_oval(x0, y0, x1, y1, fill="red")  # 圆形
arc = canvas.create_arc(x0 + 30, y0 + 30, x1 + 30, y1 + 30, start=0, extent=180)  # 扇形
rect = canvas.create_rectangle(100, 30, 100 + 20, 30 + 20)  # 矩形
canvas.pack()


def moveit():
    canvas.move(rect, 0, 2)


b = tk.Button(window, text="move", command=moveit)
b.pack()
window.mainloop()
