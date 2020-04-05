#当i=5时，不执行后续的循环
i = 0
while i <= 10:
    if i == 5:
        i += 1
        #使用continue关键字时，要对循环的计数进行处理
        continue
    print(i)
    i += 1