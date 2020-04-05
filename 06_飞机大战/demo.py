import pygame
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""

    def __init__(self,image_name):

        super().__init__()

        # screen = pygame.display.set_mode((480,700))
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.image=pygame.image.load(image_name)
        self.screen.blit(self.image, (0, 0))



pygame.init()
bg = GameSprite("./images/background.png")
pygame.display.update()