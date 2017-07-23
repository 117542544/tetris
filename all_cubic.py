import pygame
from pygame.sprite import Group
from pygame.sprite import Sprite
from random import randint


class AllCubic():
    """所有方块组的类"""
    def __init__(self, screen, game_settings):
        """创建方块组"""
        self.game_settings = game_settings
        # 获取屏幕
        self.screen = screen
        # 创建编组
        self.cubics = Group()

        # 随机选择一种形状并创建方块组实例
        randnum_shape = randint(1, 7)
        chosen_shape = self.game_settings.cubic_shape[randnum_shape]
        shape_image_path = chosen_shape[0]
        self.dir_dict = chosen_shape[1]

        # 随机选择一种方向并创建为一组
        randnum_dir = randint(1, 4)
        self.recent_dir_num = randnum_dir
        chosen_dir = self.dir_dict[randnum_dir]
        self.recent_chosen_dir_dict = chosen_dir
        for key, value in chosen_dir.items():
            new_cubic = MetaCubic(shape_image_path)
            # 把方块的初始位置放到预设位置
            new_cubic.rect.x = value[0]
            new_cubic.rect.y = value[1]
            new_cubic.position_flag = key
            # 加入组
            self.cubics.add(new_cubic)

    def drawme(self):
        """绘制方块编组"""
        for cubic in self.cubics.sprites():
            self.screen.blit(cubic.image, cubic.rect)

    def rotate(self):
        """顺时针旋转方块编组"""
        # 获取下一个方向的位置字典
        next_dir_num = self.recent_dir_num + 1
        if next_dir_num > 4:
            next_dir_num -= 4
        next_dir_dict = self.dir_dict[next_dir_num]
        # 遍历方块位置名
        for position_flag in  next_dir_dict.keys():
            # 计算位置变动值
            x_diff = next_dir_dict[position_flag][0] - self.recent_chosen_dir_dict[position_flag][0]
            y_diff = next_dir_dict[position_flag][1] - self.recent_chosen_dir_dict[position_flag][1]
            # 遍历方块组，找到对应的元方块修改其位置
            for cubic in self.cubics.sprites():
                if cubic.position_flag == position_flag:
                    cubic.rect.x += x_diff
                    cubic.rect.y += y_diff
                    break
        # 记录最近一次的方向值和方向字典
        self.recent_dir_num = next_dir_num
        self.recent_chosen_dir_dict = next_dir_dict

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
            self.rect.y += game_settings.cubic_fall_dist

        # 处理按键移动
        if move:
            if event_key == pygame.K_DOWN:
                self.rect.y += game_settings.cubic_fall_dist
            if event_key == pygame.K_LEFT:
                self.rect.x -= game_settings.cubic_fall_dist
            if event_key == pygame.K_RIGHT:
                self.rect.x += game_settings.cubic_fall_dist