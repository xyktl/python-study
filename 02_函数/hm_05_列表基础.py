name_list = ["张三","李四","赵四","老温"]
#查找
index_zs = name_list.index("张三")#显示数据”张三“的下标
print(index_zs)
#列表增加
name_list.append("laowen")#在列表末尾增加数据laowen
name_list.insert(1,"猪八戒")#在索引1处插入数据”猪八戒“
name_list1 = ["孙悟空","沙僧","唐僧"]
name_list.extend(name_list1)#将列表name_list1 与列表name_list 合并
#列表删除
name_list.pop(8)#删除索引是8的数据
name_list.remove("沙僧")#删除数据”沙僧“
#name_list.clear()  清空列表
#列表统计
print(len(name_list))#获取列表的长度
print(name_list.count("laowen"))#统计laowen在列表中出现的次数
#列表排序
name_list2 = [2,4,9,3,1]
name_list2.sort()#升序
name_list.sort()#
name_list2.sort(reverse = True)#降序
name_list2.reverse()#逆序



print(name_list)
print(name_list2)