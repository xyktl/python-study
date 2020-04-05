#掌握 类属性 类方法  实例属性 实例方法  静态方法
#类属性：top_score  类方法：show_top_score   实例属性：player_name  实例方法:start_game
#静态方法  show_game_help
import hm_03_士兵突击
class Game:
    top_score = 0
    def __init__(self,player_name):
        self.player_name = player_name
    @staticmethod
    def show_game_help():
        print("游戏帮助：推开大门！")
    @classmethod
    def show_top_score(cls):
        print("游戏最高分：%d"%(cls.top_score))
    def start_game(self):
        print("游戏开始了！")


def main():
    zhansheng = Game("战神")
    print(zhansheng.show_game_help())
    print(zhansheng.show_top_score())


if __name__== "__main__":
    main()