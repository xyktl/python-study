#用循环嵌套打印九九乘法表
row = 1
while row <= 9:
    col = 1
    while col <= row:
        print("%d*%d=%d"%(col,row,col*row),end=("\t")) #制表符\t 使文本在垂直方向上对齐
        #print("*",end(" "))     不换行
        col += 1
    row += 1
    print("")   #增加一个换行
