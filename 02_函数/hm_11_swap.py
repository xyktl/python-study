a = 1
b = 2
#交换两个数字的值
#1
temp = a
a = b
b = temp
print(a,b)
#2
a = a + b
b = a - b
a = a - b
print(a,b)
#3  python 中专用
a,b = b,a
print(a,b)