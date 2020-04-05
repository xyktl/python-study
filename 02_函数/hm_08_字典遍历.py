room_dic = {"name":"陈亮",
            "room":507,
            "age":21,
            "gender":"boy",
            "project":"internet"}
for get_key in room_dic:#遍历键
    print(get_key)
print("")
for get_value in room_dic:#遍历值
    print(room_dic[get_value])
print("")
for get in room_dic:#遍历键和值
    print("(%s , %s)"%(get,room_dic[get]))
print("")
for get in room_dic.items():#以元组数组的方式遍历键和值
    print(get)