# -*- coding: utf-8 -*-
# 做登陆窗口# -*- coding: utf-8 -*-
# 放置位置
import tkinter as tk
import tkinter.messagebox
import pickle

master = tk.Tk()
master.title("my window")
width = 400
height = 400
screenwidth = master.winfo_screenmmwidth()
screenheight = master.winfo_screenmmheight()
alignstr = f"{width}x{height}+" + str((screenwidth - width) // 2) + "+" + str((height - screenheight) // 2)
master.geometry(alignstr)

frame1 = tk.Frame(master).pack(side="left")
frame2 = tk.Frame(master).place(x=200, y=170, anchor="nw")
# 位置参数（place的参数x,y）以字符串为单位，小部件（button）参数（width,height）以像素为单位
l1 = tk.Label(frame1, text="用户：", bg="yellow", width="10", height="1").place(x=130, y=120, anchor="e")
l2 = tk.Label(frame1, text="密码：", bg="yellow", width="10", height="1").place(x=130, y=170, anchor="e")

var_user = tk.StringVar()
var_user.set("@github.com")
var_pwd = tk.StringVar()
e1 = tk.Entry(frame2, width="25", show=None, textvariable=var_user).place(x=140, y=120, anchor="w")
e2 = tk.Entry(frame2, width="25", show="*", textvariable=var_pwd).place(x=140, y=170, anchor="w")


def login_in():
    '''登陆函数'''
    user_name = var_user.get()
    user_pwd = var_pwd.get()
    user_info = {"admin": "123456"}#首次登陆初始话用户
    #判断用户名和密码是否为空
    if len(user_name) == 0 or len(user_pwd) == 0:
        tk.messagebox.showinfo(title="Info", message="please insert your login information")
        return
    # if user_name == "xyktl" and user_pwd == "c1635976271":
    #     tk.messagebox.showinfo(title="Hi", message="登陆成功")
    try:
        with open("user_info.pickle", "rb") as user_file:
            while True:
                try:
                    user_data = pickle.load(user_file)
                    for key in user_data.keys():
                        user_info[key] = user_data[key]
                    # 反序列化，将pickle文件中的数据反序列化 传入对象usrs_info中
                    # print(data)  # 打印已经注册过的用户
                except EOFError:
                    print(user_info)
                    break
    # 文件不存在，捕获异常
    except FileNotFoundError:
        with open("user_info.pickle", "wb") as user_file:
            user_info = {"admin": "123456"}  # 设置管理员的账号和密码，初始化
            pickle.dump(user_info, user_file)  # 序列化
    # 如果文件内容为空，捕获异常
    except EOFError:
        with open("user_info.pickle", "wb") as user_file:
            user_info = {"admin": "123456"}  # 设置管理员的账号和密码，初始化
            pickle.dump(user_info, user_file)  # 序列化

    # 判断用户名是否正确
    for name in user_info.keys():
        if name == user_name:
            # 判读用户密码
            if user_pwd == user_info[name]:
                tk.messagebox.showinfo(title="welocme", message="how are you " + user_name)
                break
            else:
                tk.messagebox.showerror(title="Error", message="Your password is error")
                break
    else:
        # 提示用户是否注册账号
        is_sign_up = tk.messagebox.askyesno(message="You have not sing up yet,Sign up ?")
        if is_sign_up:
            sign_up()


def sign_up():
    '''注册函数'''
    user_name = var_user.get()
    user_pwd = var_pwd.get()
    user_dic = {}  # 一个临时的字典存放user_info.pickle 文件中反序列化后的用户信息
    user_info = {user_name: user_pwd}  # 将用户的注册信息装进一个字典中，以便序列化传入pickle文件中
    if len(user_name) == 0 or len(user_pwd) == 0:
        tk.messagebox.showinfo(title="Info", message="insert your login information")
        return
    # 将用户注册的账号写入 user-info.pickle 文件中
    try:
        with open("user_info.pickle", "rb+") as user_file:
            while True:
                try:
                    user_data = pickle.load(user_file)
                    for name in user_data.keys():
                        user_dic[name] = user_data[name]
                except EOFError:
                    print(user_dic)
                    break
            for name in user_dic.keys():
                if name == user_name:
                    tk.messagebox.showinfo(message="The user is exist")
                    break
                else:
                    pickle.dump(user_info, user_file)  # 序列化，将用户的注册信息传入user_file 文件中
                    user_file.close()
    except FileNotFoundError:
        with open("user_info.pickle", "ab+") as user_file:
            pickle.dump(user_info, user_file)
            user_file.close()
    except EOFError:
        # 文件为空抛出异常
        with open("user_info.pickle", "wb") as user_file:
            pickle.dump(user_info, user_file)  # 序列化
            user_file.close()
    success_sign = tk.messagebox.showinfo(message="注册成功！")
    is_sign_up = tk.messagebox.askyesno(message="登陆？")

    # 提示用户是否登陆
    if is_sign_up:
        var_user.set(user_name)
        var_user.set(user_pwd)

        login_in()


b1 = tk.Button(master, text="login in", bg="yellow", width="8", command=login_in).place(x=150, y=220, anchor="center")
b2 = tk.Button(master, text="sign up", bg="yellow", width="8", command=sign_up).place(x=250, y=220, anchor="center")
master.mainloop()
