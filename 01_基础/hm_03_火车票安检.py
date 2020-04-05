#判读是否买了火车票
has_tickt = True
knift_length = 20
if has_tickt :
    print("您好，火车票通过！")
#判读刀的长度是否能上车
    if knift_length > 20:
        print("您所携带的刀太长，不能上车！")
    else :
        print("安检通过，祝您旅途愉快！")
else:
    print("对不起，您没买票，不能上车！")