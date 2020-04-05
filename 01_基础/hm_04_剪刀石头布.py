#用户输入代表所出的拳，电脑随机出拳，1代表石头，2代表剪刀，3代表布
import random
player = int(input("（1）石头 （2）剪刀 （3）布："))
computer = random.randint(1,3)#电脑随机出1~3的数
print("玩家出的是%d，电脑出的是%d" %(player,computer))
if ((player ==1 and computer == 2)
        or(player == 2 and computer == 3)
        or(player ==3 and computer == 1)):
    print("欧耶，你弱爆了！")
#平局
elif player == computer:
    print("打平了，再来一局！")
else :
    print("我输了，决战到天亮！")