#计算0~100之间偶数的和
#1.定义一个记录最终结果的变量
sum = 0
i = 0
while i <= 100:
    if i % 2 == 0:
        print(i)
        sum += i
    i += 1
print("0~100之间偶数的和是%d"%sum)