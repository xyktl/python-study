#搭建框架
import cards_tools

while True:
    # 选择菜单
    cards_tools.sel_menu()
    action_str = input("请选择要进行的操作：")
    num_list = ["1","2","3"]

    if action_str in num_list:
        if action_str == "1":
            cards_tools.show_card()
        if action_str == "2":
            cards_tools.add_card()
        if action_str == "3":
            cards_tools.find_card()
    elif action_str == "0":
        print("退出系统成功！")
        break
    else:
        print("输入无效！")
