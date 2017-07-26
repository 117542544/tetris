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

    def add_cubics(self):
        """为空组随机加入处于任意方位的方块形状"""
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
            # 把方块的初始位置放到预设位置,高度要加上预设的起始投放高度
            new_cubic.rect.x = value[0]
            new_cubic.rect.y = value[1] + self.game_settings.cubic_start_height
            new_cubic.position_flag = key
            # 加入组
            self.cubics.add(new_cubic)

    def drawme(self):
        """绘制方块编组"""
        for cubic in self.cubics.sprites():
            self.screen.blit(cubic.image, cubic.rect)

    def rotate(self):
        """顺时针旋转方块编组"""
        # 设置转出屏幕后的回移次数
        move_back_right_times = 0
        move_back_left_times = 0
        move_back_up_times = 0
        # 获取下一个方向的位置字典
        next_dir_num = self.recent_dir_num + 1
        if next_dir_num > 4:
            next_dir_num -= 4
        next_dir_dict = self.dir_dict[next_dir_num]
        # 遍历方块位置名,修改所有元方块位置
        for position_flag in  next_dir_dict.keys():
            # 计算位置变动值
            x_diff = next_dir_dict[position_flag][0] - self.recent_chosen_dir_dict[position_flag][0]
            y_diff = next_dir_dict[position_flag][1] - self.recent_chosen_dir_dict[position_flag][1]
            # 遍历方块组，找到对应的元方块修改其位置
            for cubic in self.cubics.sprites():
                if cubic.position_flag == position_flag:
                    cubic.rect.x += x_diff
                    cubic.rect.y += y_diff
                    # 计算需要回移的次数
                    if cubic.rect.x >= self.game_settings.screen_width:
                        if (int((cubic.rect.x + self.game_settings.metacubic_width - self.game_settings.screen_width) \
                            /self.game_settings.metacubic_width) >  move_back_left_times):
                            move_back_left_times = int((cubic.rect.x + self.game_settings.metacubic_width \
                                                        - self.game_settings.screen_width)\
                                                       /self.game_settings.metacubic_width)

                    elif cubic.rect.x < 0:
                        if (int((0 - cubic.rect.x) / self.game_settings.metacubic_width) > move_back_right_times):
                            move_back_right_times = int((0 - cubic.rect.x) / self.game_settings.metacubic_width)

                    if cubic.rect.y >= self.game_settings.screen_height:
                        if (int((cubic.rect.y + self.game_settings.metacubic_width - self.game_settings.screen_height) \
                            / self.game_settings.metacubic_width) > move_back_up_times):
                            move_back_up_times = int((cubic.rect.y + self.game_settings.metacubic_width \
                                                    - self.game_settings.screen_height) \
                                                     / self.game_settings.metacubic_width)

                    break
        # 记录最近一次的方向值和方向字典
        self.recent_dir_num = next_dir_num
        self.recent_chosen_dir_dict = next_dir_dict

        # 将旋转后超出显示范围的方块组移回屏幕内
        while move_back_right_times > 0:
            self.cubics.update(self.game_settings, pygame.K_RIGHT)
            move_back_right_times -= 1
        while move_back_left_times > 0:
            self.cubics.update(self.game_settings, pygame.K_LEFT)
            move_back_left_times -= 1
        while move_back_up_times > 0:
            self.cubics.update(self.game_settings, 'up')
            move_back_up_times -= 1
        # 重置按键的保持按下状态
        self.game_settings.key_down = False
        self.game_settings.key_left = False
        self.game_settings.key_right = False


class MetaCubic(Sprite):
    """创建元方块"""
    def __init__(self, path):
        super(MetaCubic, self).__init__()
        # 加载方块图像并获取外接矩形
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()

    def update(self, game_settings, event_key):
        """处理方块自然下降与按键移动"""
        if event_key == pygame.K_DOWN:
            game_settings.key_down = True
            self.rect.y += game_settings.cubic_move_dist
        if event_key == pygame.K_LEFT:
            game_settings.key_left = True
            self.rect.x -= game_settings.cubic_move_dist
        if event_key == pygame.K_RIGHT:
            game_settings.key_right = True
            self.rect.x += game_settings.cubic_move_dist
        if event_key == 'up':
            self.rect.y -= game_settings.cubic_move_dist
        if event_key == 'down':
            self.rect.y += game_settings.cubic_move_dist


class DeadCubic():
    """已固定的方块组的类"""
    def __init__(self, screen, game_settings):
        """创建方块组"""
        self.game_settings = game_settings
        # 获取屏幕
        self.screen = screen
        # 创建编组
        self.cubics = Group()

    def drawme(self):
        """绘制方块编组"""
        for cubic in self.cubics.sprites():
            self.screen.blit(cubic.image, cubic.rect)


class BlackLines():
    """黑行组"""
    def __init__(self):
        self.line = Group()
    def drawme(self):
        """在屏幕上绘制黑行组"""
        for black_line in self.line.sprites():
            black_line.drawme()


class BlackLine(Sprite):
    """消除整行时的黑色行"""
    def __init__(self, screen, game_settings):
        super(BlackLine, self).__init__()
        self.game_settings = game_settings
        self.screen = screen

        # 在(0,0)处创建矩形， 后面再放到正确的位置
        self.rect = pygame.Rect(0, 0, self.game_settings.black_line_width, self.game_settings.black_line_height)
        self.color = self.game_settings.black_line_color

    def drawme(self):
        """在屏幕上绘制黑行"""
        pygame.draw.rect(self.screen, self.color, self.rect)