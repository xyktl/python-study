liebiao=[1,5,7,8,9]
num=int(input("请输入要查找的值:"))
first=0
end=len(liebiao)
middle=int(first+end/2)
for i in range(int(len(liebiao)/2)):
	if num==liebiao[middle]:
		print("找到了:",num,"在列表中的第",middle+1,"个")
		break
	elif num>liebiao[middle]:
		first=middle
		middle=int((first+end)/2)
	elif num<liebiao[middle]:
		end=middle
		middle=int((first+end)/2)
	if i==len(liebiao)/2:
		print("您查找的数不在列表中！")
#1234567






