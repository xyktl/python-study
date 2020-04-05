#/usr/bin/python
# coding:utf-8
#打印九九乘法表

row = 1
while row <= 9:
	col = 1
	while col <= row:

		'''if col == 1 :
			print("%d*%d=%d"%(col,row,col*row),end=" ")
		else:	
			print("\t%d*%d=%d"%(col,row,col*row),end=" ")'''
		print("%d*%d=%d"%(col,row,col*row),end=("\t"))
		col += 1
	row += 1
	print("")