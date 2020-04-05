#sort()  对列表对象排序，无返回值
#sorted(iterable，cmp=None,key=None,reverse=Flase):对所有可迭代对象排序，返回
#的是一个新的可迭代对象
#iterable:可迭代对象 cmp:比较的函数  key：用来比较的元素  reverse：正序或逆序

list = [1,6,5,3,6,6,30,19]
set = set((3,6,1,68,399))
new_list = sorted(list,reverse=True)
new_set = sorted(set)
print(new_list)
print(new_set) 



