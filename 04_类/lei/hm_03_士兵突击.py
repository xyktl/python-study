#枪类  包含  model(型号)   bullet(弹夹剩余子弹)  属性
#            add_bullet  方法


class Gun(object):
    def __init__(self,model,bullet):
        self.model = model
        self.bullet = bullet


    def __str__(self):
        return "%s [%s]"%(self.model,self.bullet)



#士兵类   包含  name(姓名)   gun(枪)   属性
#             add_bullet    fire     方法


class Solder(object):
    def __init__(self,name):
        self.name = name
        self.gun = None
        self.bullet = 200


    def __str__(self):
        return "士兵：%s\n枪：%s\n备弹：%s发"%(self.name,self.gun,self.bullet)


    def add_gun(self,gun):
        """给士兵发枪
        :param gun: 枪对象
        """
        self.gun = gun


    def help_bullet(self):
        """给士兵补充备弹
        """
        self.bullet = 200

    def add_bullet(self):
        """为枪补充弹药，并且计算枪的子弹数量和备弹数量 ， 并输出

        :return: 判断： 如果符合要求 没枪  or 没备弹，则停止执行
                                    如果备弹少于50发，则枪的子弹+备弹剩余的数量
        """
        if self.gun is None:
            print("%s还没有枪！"%(self.name))
            return
        elif self.bullet <= 0:
            print("弹尽粮绝了！上刺刀，决一死战！")
            return
        elif self.bullet < 50:
            self.gun.bullet += self.bullet
            print("增加%s发子弹！备弹为0"%(self.bullet))
            self.bullet = 0
            return
        self.bullet -= (50 - self.gun.bullet)
        print("增加%s发子弹！备弹剩%s发" % ((50 - self.gun.bullet), self.bullet))
        self.gun.bullet += (50 - self.gun.bullet)


    def fire(self):
        """开火  枪的子弹-1
        """
        while True:
            if self.gun is None:
                print("%s没有枪！"%(self.name))
                break
            elif self.gun.bullet == 0 and self.bullet == 0:
                print("弹尽粮绝了！上刺刀，决一死战！")
                break
            elif self.gun.bullet == 0:
                print("%s没有子弹了!"%(self.gun.model))
                break
            self.gun.bullet -= 1
            print("突突突......  [%s]"%(self.gun.bullet))

#测试代码
def main():
    AK47 = Gun("AK47",20 )
    xusanduo = Solder("许三多")
    print(xusanduo)
    xusanduo.add_gun(AK47)
    print(xusanduo)
    while xusanduo.bullet > 0:
        xusanduo.add_bullet()
        xusanduo.fire()
if __name__ == "__main__":
     main()







