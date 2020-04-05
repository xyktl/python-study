def bubble_sort(items):
    for i in range(len(items) - 1):
        for j in range(len(items) - 1 - i):
            if items[j] > items[j + 1]:
            	temp=0
            	temp=items[j]
            	items[j]=items[j+1]
            	items[j+1]=temp
    return items
list1 = [2,1,9,11,10,8,7]
print(bubble_sort(list1))
