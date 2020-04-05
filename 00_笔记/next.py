#next() 函数 用于返回迭代器的(iterable)下一个项目
#语法   ：next(iterator[, default])
#iterator:可迭代对象
#default -- 可选，用于设置在没有下一个元素时返回该默认值，
#如果不设置，又没有下一个元素则会触发 StopIteration 异常。
#/usr/bin/python
# coding:utf-8
list = iter([1,3,3,5,6,7])

'''
while True:
    try:
        # 获得下一个值:
        x = next(it)
        print(x)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break
'''        

while True:
	x = next(list,"")
	#第二个参数空字符串，如果没有元素时，返回这个空字符串
	print(x)
	if x == "":
		break
	


