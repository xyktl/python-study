# python  的特殊函数的功能


class Person(object):
    """docstring for  Person"""

    def __init__(self, name, age):
        '''创建实例对象时自动调用'''
        super(Person, self).__init__()
        self.name = name
        self.age = age

    def __new__(cls, name, age):
        '''在__init__() 之前自动调用  为对象分配空间，返回对象的引用

        '''
        print("有地方住了")
        return super().__new__(cls)  # 必须要有返回值

    def __str__(self):
        return "%s出生了" % self.name  # 返回字符串

    def __del__(self):
        '''垃圾回收前被自动调用  垃圾：创建的对象没有被引用'''

        print("%s去世了" % self.name)

    def __bool__(self):
        '''用于实例对象的bool判断'''
        return True
        # 如果对象不为空，返回True

    def __len__(self):
        '''返回实例的长度'''
        return len(self.name)

    def __repr__(self):
        '''指定对象在 交互 模式中直接输出结果'''
        return "Hello"

    #__lt__(self,other)		小于 <
    #__le__(self,other)		小于等于 <=
    #__eq__(self,other)		等于   =
    #__ne__(self,other)		不等于  ！=
    #__gt__(self,other)		大于	>
    #__ge__(self,other)		大于等于	>=

    def __lt__(self, other):
        '''比较两个实例的年龄 age'''
        return self.age < other.age


sunwukong = Person("孙悟空", 25)
zhubajie = Person("猪八戒", 36)
print(sunwukong)
print(bool(sunwukong))
print(len(sunwukong))
print(sunwukong < zhubajie)#调用了 __lt__ 函数 返回 true
print(zhubajie)
