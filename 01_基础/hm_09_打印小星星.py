'''打印小星星
*
**
***
****
*****
'''
'''
i = 0
while i <= 4:
    print("*"*(i+1))
    i += 1
'''
#用循环嵌套打印小星星
row = 1
while row <= 5:
    col = 1
    while col <= row:
        print("*",end=(""))
        col += 1
    print("")
    row += 1