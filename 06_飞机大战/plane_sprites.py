import  os
import random
import pygame

SCREEN_RECT = pygame.Rect(0,0,480,700)
FRAME_PRE_SCE = 60
CREATE_ENEMY_EVENY = pygame.USEREVENT
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):
    def __init__(self,image_name,speed = 1):
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.y += self.speed


class Background(GameSprite):
    def __init__(self,is_alt = False):
        super().__init__(os.path.join(r"C:\Users\Hasse\Desktop\py project\06_飞机大战\images\background.png"))
        if is_alt:
            self.rect.y = -self.rect.height
    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height

class Hero(GameSprite):
    def __init__(self):
        super().__init__(os.path.join(r"C:\Users\Hasse\Desktop\py project\06_飞机大战\images\me1.png"),0)
        #self.rect.x = SCREEN_RECT.width/2 - self.rect.width/2
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        self.bullet_group = pygame.sprite.Group()
    def update(self):
        self.rect.x += self.speed
        if self.rect.x < 0:
            self.rect.x = 0
        elif  self.rect.right > SCREEN_RECT.right:
            #self.rect.x > SCREEN_RECT.width - self.rect.width:

            self.rect.x = SCREEN_RECT.width - self.rect.width
    def fire(self):
        for i in (0,1,2):
            bullet = Bullet()
            bullet.rect.centerx = self.rect.centerx
            bullet.rect.bottom = self.rect.top - i*20
            self.bullet_group.add(bullet)




class Enemy(GameSprite):
    def __init__(self):
        super() .__init__(os.path.join(r"C:\Users\Hasse\Desktop\py project\06_飞机大战\images\enemy1.png"))
        self.speed = random.randint(1,3)
        self.rect.bottom = 0
        x_max = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, x_max)
    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()
    def __del__(self):
        pass


class Bullet(GameSprite):
    def __init__(self):
        super().__init__(os.path.join(r"C:\Users\Hasse\Desktop\py project\06_飞机大战\images\bullet1.png"),-3)
    def update(self):
        super().update()
        if self.rect.bottom < 0:
            self.kill()
    def __del__(self):
        pass
