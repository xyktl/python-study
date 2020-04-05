import pygame
from plane_sprites import *
class PlaneGame(object):
    def __init__(self):
        #初始化游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        #设置游戏时钟
        self.clock = pygame.time.Clock()
        #创建精灵和精灵组
        self.__create_sprites()
        pygame.time.set_timer(CREATE_ENEMY_EVENY,1000)
        pygame.time.set_timer(HERO_FIRE_EVENT,500)


    def start_game(self):
        #设置帧率
        while True:
            self.clock.tick(FRAME_PRE_SCE)
            #事件监听
            self.__event_hander()
            #碰撞检测
            self.__collide_detic()
            #更新绘制精灵和精灵组
            self.__sprites_update()
            #刷新屏幕
            pygame.display.update()


    def __create_sprites(self):
        #背景组
        bg1 = Background()
        bg2 = Background(True)
        self.bg_group = pygame.sprite.Group(bg1,bg2)

        # 敌机组
        self.enemy_group = pygame.sprite.Group()
        # 英雄和英雄组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)



    def __event_hander(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__game_over()
            elif event.type == CREATE_ENEMY_EVENY:
                enemy = Enemy()
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT]:
            self.hero.speed = 3
        elif key_pressed[pygame.K_LEFT]:
            self.hero.speed = -3
        else:
            self.hero.speed = 0


    def __collide_detic(self):

        pygame.sprite.groupcollide(self.hero.bullet_group,self.enemy_group,True,True)
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        if len(enemies) > 0:
            self.__game_over()

    def __sprites_update(self):

        self.bg_group.update()
        self.bg_group.draw(self.screen)
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        self.hero.bullet_group.update()
        self.hero.bullet_group.draw(self.screen)

    def __game_over(self):
        pygame.quit()
        print("游戏结束！")
        exit()



if __name__ == "__main__":
    game = PlaneGame()
    game.start_game()

