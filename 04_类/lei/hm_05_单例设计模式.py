#实现单例设计模式，比如播放器同时只能播放一首歌(创建一个对象)
#类属性  intance 接受返回的对象的引用的值
#      init_flag 判断 __init__() 执行的次数
class Musicplay(object):
    intance = None
    init_flag = False
    #重写内置函数__new__()  使每次创建的对象分配的都是同一个空间
    def __new__(cls, *args, **kwargs):
        if cls.intance is None:
            cls.intance = super().__new__(cls)
        return cls.intance
    #重写__init__() 函数，使初始化动作只执行一次
    def __init__(self):
        if Musicplay.init_flag:
            return
        Musicplay.init_flag = True


def main():
    play1 = Musicplay()
    print(play1)
    play2 = Musicplay()
    print(play2)
    #无论创建多少个对象，他们的引用输出的都是同一个值，这就是单例设计模式


if __name__ == "__main__":
    main()
