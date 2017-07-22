import pygame

class AllCubic():
    """所有方块类的父类"""
    def __init__(self, screen):
        """初始化方块并设置其初始位置"""
        # 加载方块图像并获取外接矩形
        self.screen = screen
        self.image = pygame.image.load('images/cubic_red.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # 把方块的初始位置放到屏幕顶端中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.top = 0

    def drawme(self):
        """在指定位置绘制方块"""
        self.screen.blit(self.image, self.rect)