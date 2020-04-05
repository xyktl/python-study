#创建一个包含 name weight 属性
#            run   eat   方法       的类


class Person:
    #类的初始化内置函数，是专门来定义一个类具有哪些属性的方法
    #创建对象时自动调用__init__()方法
    def __init__(self,name,weight):
        self.name = name
        self.weight = weight
    #方法__str__()使用print输出对象时自定义内容
    def __str__(self):
        #return必须返回一个字符串
        return "%s 的体重是%s"%(self.name,self.weight)
    def run(self):
        print("%s爱跑步"%(self.name))
        self.weight -= 0.5
    def eat(self):
        print("%s吃零食"%(self.name))
        self.weight += 1


def main():
    xiaoming = Person("小明",70)
    xiaoming.run()
    xiaoming.eat()
    print(xiaoming)
    xiaohong = Person("小红",50)
    print(xiaohong)
if __name__ == "__main__":
    main()