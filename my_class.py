import pygame
from pygame.sprite import Group
from pygame.sprite import Sprite
from random import randint


class FallCubic():
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
        self.randnum_shape = randint(1, 7)
        chosen_shape = self.game_settings.cubic_shape[self.randnum_shape]
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

    def rotate(self, temp_cubics, dead_cubics):
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
        # 清空temp_cubics
        temp_cubics.empty()
        # 遍历方块位置名,修改所有元方块位置
        for position_flag in  next_dir_dict.keys():
            # 计算位置变动值
            x_diff = next_dir_dict[position_flag][0] - self.recent_chosen_dir_dict[position_flag][0]
            y_diff = next_dir_dict[position_flag][1] - self.recent_chosen_dir_dict[position_flag][1]
            # 遍历临时方块组，找到对应的元方块修改其位置
            for cubic in self.cubics.sprites():
                if cubic.position_flag == position_flag:
                    # 把fall_cubics复制到temp_cubics
                    new_cubic = MetaCubic('images/cubic_lblue.bmp')
                    new_cubic.rect.x = cubic.rect.x + x_diff
                    new_cubic.rect.y = cubic.rect.y + y_diff
                    new_cubic.position_flag = cubic.position_flag
                    temp_cubics.add(new_cubic)
                    break

            for cubic in temp_cubics.sprites():
                # 计算越界的长度
                if cubic.rect.x >= self.game_settings.screen_width:
                    if (int((cubic.rect.x + self.game_settings.metacubic_width - self.game_settings.screen_width) \
                                    / self.game_settings.metacubic_width) > move_back_left_times):
                        move_back_left_times = int((cubic.rect.x + self.game_settings.metacubic_width \
                                                    - self.game_settings.screen_width) \
                                                   / self.game_settings.metacubic_width)

                elif cubic.rect.x < 0:
                    if (int((0 - cubic.rect.x) / self.game_settings.metacubic_width) > move_back_right_times):
                        move_back_right_times = int((0 - cubic.rect.x) / self.game_settings.metacubic_width)

                if cubic.rect.y >= self.game_settings.screen_height:
                    if (int((cubic.rect.y + self.game_settings.metacubic_width - self.game_settings.screen_height) \
                                    / self.game_settings.metacubic_width) > move_back_up_times):
                        move_back_up_times = int((cubic.rect.y + self.game_settings.metacubic_width \
                                                  - self.game_settings.screen_height) \
                                                 / self.game_settings.metacubic_width)

        # 判断是否需要旋转的标志位
        rotate = True
        # 出界判断是否需要旋转
        # 下方出界则不允许旋转
        if move_back_up_times > 0:
            rotate = False
        # 出界超过一个单位长度则不允许旋转
        if move_back_left_times > 1 or move_back_right_times > 1:
            rotate = False
        # 只有前面已经允许旋转时,尝试回移
        if rotate:
            if move_back_right_times == 1:
                temp_cubics.update(self.game_settings, pygame.K_RIGHT)
            elif move_back_left_times == 1:
                temp_cubics.update(self.game_settings, pygame.K_LEFT)
            # 再检测碰撞
                collisions = pygame.sprite.groupcollide(temp_cubics, dead_cubics.cubics, False, False)
                # 有碰撞则不做任何事情返回
                if collisions:
                    temp_cubics.empty()
                    return
        else:
            temp_cubics.empty()
            return

        # 旋转及回移后的temp_cubics与dead_cubics做碰撞判断
        # 记录碰撞后记元方块的不重复的x,y值
        x_values = []
        y_values = []
        # 记录为了解决碰撞需要做的横竖移动的方向
        x_move = 0
        y_move = 0
        collisions = pygame.sprite.groupcollide(temp_cubics, dead_cubics.cubics, False, False)
        if collisions:
            # 搜集碰撞的元方块的x,y值
            for cubic in collisions:
                if cubic.rect.x not in x_values:
                    x_values.append(cubic.rect.x)
                if cubic.rect.y not in y_values:
                    y_values.append(cubic.rect.y)
            # 如果是竖棍,则超过一个块碰撞就不允许旋转
            if self.randnum_shape == 4:
                if len(x_values) > 1 or len(y_values) > 1:
                    rotate = False
                else:
                    # 只有一个块碰撞则确定回移方向,向下碰撞则不旋转
                    for cubic in temp_cubics.sprites():
                        if x_values[0] > cubic.rect.x:
                            x_move = -1
                            break
                        elif x_values[0] < cubic.rect.x:
                            x_move = 1
                            break
                        elif y_values[0] > cubic.rect.y:
                            rotate = False
                            break
                        elif y_values[0] < cubic.rect.y:
                            y_move = 1
                            break
            else:
                # 其他形状则判断是哪个方向的多块碰撞还是单块碰撞,再作处理
                if len(x_values) > len(y_values):
                    # y方向碰撞,确定回移方向,向下碰撞则不旋转
                    for cubic in temp_cubics.sprites():
                        if y_values[0] > cubic.rect.y:
                            rotate = False
                            break
                        elif y_values[0] < cubic.rect.y:
                            y_move = 1
                            break
                elif len(x_values) < len(y_values):
                    # x方向碰撞,确定回移方向
                    for cubic in temp_cubics.sprites():
                        if x_values[0] > cubic.rect.x:
                            x_move = -1
                            break
                        elif x_values[0] < cubic.rect.x:
                            x_move = 1
                            break
                elif len(x_values) == len(y_values):
                    # 单块碰撞,同时确定两种回移方向
                    for cubic in temp_cubics.sprites():
                        if x_values[0] > cubic.rect.x:
                            x_move = -1
                            break
                        elif x_values[0] < cubic.rect.x:
                            x_move = 1
                            break
                    for cubic in temp_cubics.sprites():
                        if y_values[0] > cubic.rect.y:
                            rotate = False
                            break
                        elif y_values[0] < cubic.rect.y:
                            y_move = 1
                            break

            # 只有前面已经允许旋转时,尝试回移
            if not rotate:
                # 不允许则退出
                temp_cubics.empty()
                return
            else:
                # 优先移动x方向
                if x_move != 0:
                    if x_move == 1:
                        temp_cubics.update(self.game_settings, pygame.K_RIGHT)
                    elif x_move == -1:
                        temp_cubics.update(self.game_settings, pygame.K_LEFT)
                    # 再检测碰撞
                    collisions = pygame.sprite.groupcollide(temp_cubics, dead_cubics.cubics, False, False)
                    if collisions:
                        # 有碰撞还要检测是否属于单方块碰撞,是的话先移回x,再y向移动,否则退出
                        if y_move == 0:
                            temp_cubics.empty()
                            return
                        elif y_move == 1:
                            # 先恢复
                            if x_move == 1:
                                temp_cubics.update(self.game_settings, pygame.K_LEFT)
                            elif x_move == -1:
                                temp_cubics.update(self.game_settings, pygame.K_RIGHT)
                            temp_cubics.update(self.game_settings, 'down')
                            # 再检测碰撞
                            collisions = pygame.sprite.groupcollide(temp_cubics, dead_cubics.cubics, False, False)
                            if collisions:
                                temp_cubics.empty()
                                return
                # 移动y方向
                if y_move == 1:
                    temp_cubics.update(self.game_settings, 'down')
                    # 再检测碰撞
                    collisions = pygame.sprite.groupcollide(temp_cubics, dead_cubics.cubics, False, False)
                    if collisions:
                        temp_cubics.empty()
                        return

        # 所有移动都没碰撞则把temp_cubics的方块转移到fall_cubics,temp_cubics清空后自然返回
        for cubic_t in temp_cubics.sprites():
            for cubic_f in self.cubics.sprites():
                if cubic_t.position_flag == cubic_f.position_flag:
                    # 把fall_cubics复制到temp_cubics
                    cubic_f.rect.x = cubic_t.rect.x
                    cubic_f.rect.y = cubic_t.rect.y
                    break
        temp_cubics.empty()
        # 记录最近一次的方向值和方向字典
        self.recent_dir_num = next_dir_num
        self.recent_chosen_dir_dict = next_dir_dict


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
            self.rect.y += game_settings.cubic_move_dist
        if event_key == pygame.K_LEFT:
            self.rect.x -= game_settings.cubic_move_dist
        if event_key == pygame.K_RIGHT:
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