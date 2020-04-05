#元组内得数据不能修改
name_tuple = ("chengliang","laowen","laotang")
print(name_tuple)
#遍历
for name in name_tuple:
    print(name)
print(len(name_tuple))#获取元组得长度
print(name_tuple.index("chengliang"))#获取“chengliang”得索引值
name_tuple.count("chengliang")
name_list = list(name_tuple)#元组转换为列表
tuple()#列表转换为元组
print(name_list)

#字典是python中最灵活得数据类型
room_dic = {"name":"陈亮",
            "room":507,
            "age":21,
            "gender":"boy",
            "project":"internet"}
print(room_dic)
len(room_dic)
print(room_dic["name"])#获取name键多对应的值
print(room_dic.get("name"))
append_dic = {"home":"新干"}
room_dic.update(append_dic)#将字典append_dic合并到room_dic上
print(room_dic)
#删除
room_dic.popitem()#随机删除
room_dic.pop("project")#删除project键和值
print(room_dic)
#修改或者增加
#如果原有的字典中存在，则修改  ；如若不存在，则修改
room_dic["name"] = "温常鑫"
print(room_dic)
