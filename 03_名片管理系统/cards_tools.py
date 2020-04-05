#!python C:\python\python.exe
#定义一个空列表用来存储名片
card_list = []

def sel_menu():
    """选择菜单界面

    """
    print("")
    print("*" * 50)
    print("")
    print("1.查看名片")
    print("2.增加名片")
    print("3.查找名片")
    print("0.退出系统\n")
    print("*" * 50 )



def add_card():

    """增加名片

    """
    card_dict = {}
    card_dict["name"] = input("名字：")
    card_dict["phone"] = input("电话：")
    card_dict["qq"] = input("qq:")
    card_dict["email"] = input("邮箱：")
    card_list.append(card_dict)

    print("添加 %s 的名片成功！"%(card_dict["name"]))


def show_card():
    """显示所有名片

    :return: 没有名片则返回，不执行函数体下面的代码
    """
    if len(card_list) == 0:
        print("没有名片！请添加")
        return
    for head in ["姓名","电话","qq","邮箱"]:
        print(head,end="\t\t")
    print("")
    print("=" * 50)
    #遍历列表中的每个字典，并输出
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                            card_dict["phone"],
                                            card_dict["qq"],
                                            card_dict["email"]))
    sel_operation()


def sel_operation():
    """在函数show_card中
    选择删除或者修改操作
    """
    print("")
    print("请选择要进行的操作:  (1)修改  (2)删除  (0)返回上一级")
    sel_ope = input("请输入：")
    if sel_ope == "1":
        change_card()
    elif sel_ope == "2":
        del_card()


def del_card():
    """在函数sel_operation()中
    遍历列表删除用户输入的名片
    """
    remove_card = input("请输入要删除的名片：")
    for card_dict in card_list:
        if card_dict["name"] == remove_card:
            card_list.remove(card_dict)
            print("删除成功！")
            break
    else:
        print("输入无效！")


def change_card():
    """在函数sel_operation()中
    遍历列表修改用户输入的名片
    """
    change_card = input("请输入要修改的名片：")
    for card_dict in card_list:
        if card_dict["name"] == change_card:
            card_dict["name"] = input_select(card_dict["name"],"姓名：")
            card_dict["phone"] = input_select(card_dict["phone"], "电话：")
            card_dict["qq"]= input_select(card_dict["qq"], "qq:")
            card_dict["email"] = input_select(card_dict["email"],"邮箱：")
            print("修改成功！")
            break
    else:
        print("输入无效!")




def find_card():
    """查找名片

    """
    find_card = input("请输入要查找的名字:")
    #遍历列表中的每一个字典，看是否有要查找的名片
    for card_dict in card_list:
        if find_card == card_dict["name"]:
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                                card_dict["phone"],
                                                card_dict["qq"],
                                                card_dict["email"]))
            #调用名片修改和删除的函数
            deal_card(card_dict)
            break
    #for循环中如果没有break，则会执行else的部分
    else:
        print("没有您查找的名片！")


def deal_card(find_card):
    """对名片进行修改和删除操作

    :param find_card: 查找到的名片传入的值
    """
    print("")
    print("请选择要进行的操作:  (1)修改  (2)删除  (0)返回上一级")
    print("")
    deal_str = input("请输入：")
    if deal_str == "1":
        find_card["name"] = input_select(find_card["name"],"姓名：")
        find_card["phone"] = input_select(find_card["phone"],"电话：")
        find_card["qq"] = input_select(find_card["qq"],"qq:")
        find_card["email"] = input_select(find_card["email"],"邮箱")
        print("%s\t\t%s\t\t%s\t\t%s"%(find_card["name"],
                                      find_card["phone"],
                                      find_card["qq"],
                                      find_card["email"]))
    elif deal_str == "2":
        card_list.remove(find_card)
        print("删除成功！")

def input_select(find_value,tip_message):
    """实现：如果用户直接回车则会返回原有的值，不修改

    :param find_value: 名片信息原有的值
    :param tip_message: 用户输入时的提示信息
    :return: 用户直接回车，返回原有的值；否则返回用户输入的新值
    """
    new_value = input(tip_message)
    if len(new_value) == 0:
        return find_value
    else:
        return new_value







