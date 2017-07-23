import pygame
from pygame.sprite import Group
from pygame.sprite import Sprite
from random import randint
from time import sleep


class AllCubic():
    """所有方块组的类"""
    def __init__(self, screen, game_settings):
        """创建方块组"""
        # 获取屏幕
        self.screen = screen
        # 创建编组
        self.cubics = Group()

        # 随机选择一种形状并创建方块组实例
        randnum_shape = randint(1, 7)
        chosen_shape = game_settings.cubic_shape[randnum_shape]
        shape_image_path = chosen_shape[0]
        dir_dict = chosen_shape[1]

        # 随机选择一种方向并创建为一组
        randnum_dir = randint(1, 4)
        chosen_dir = dir_dict[randnum_dir]
        for value in chosen_dir.values():
            new_cubic = MetaCubic(shape_image_path)
            # 把方块的初始位置放到预设位置
            new_cubic.rect.x = value[0]
            new_cubic.rect.y = value[1]
            # 加入组
            self.cubics.add(new_cubic)

    def drawme(self):
        """绘制方块编组"""
        for cubic in self.cubics.sprites():
            self.screen.blit(cubic.image, cubic.rect)

    def in_position(self):
        """落到底部处理"""
        pass


class MetaCubic(Sprite):
    """创建元方块"""
    def __init__(self, path):
        super(MetaCubic, self).__init__()
        # 加载方块图像并获取外接矩形
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()

    def update(self, game_settings, event_key, fall=False, move=False):
        """处理方块自然下降与按键移动"""
        # 处理自然下降
        if fall:
            sleep(game_settings.fall_interval)
            self.rect.y += game_settings.cubic_fall_dist

        # 处理按键移动
        if move:
            if event_key == pygame.K_DOWN:
                self.rect.y += game_settings.cubic_fall_dist
            if event_key == pygame.K_LEFT:
                self.rect.x -= game_settings.cubic_fall_dist
            if event_key == pygame.K_RIGHT:
                self.rect.x += game_settings.cubic_fall_dist