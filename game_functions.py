import pygame
import sys
import time

from my_class import MetaCubic, BlackLine, BlackLines


def update_screen(screen, game_settings, all_cubics, dead_cubics, black_lines):
    """更新屏幕"""
    # 重绘屏幕
    screen.fill(game_settings.screen_bgcolor)

    # 重绘方块
    all_cubics.drawme()
    dead_cubics.drawme()
    if game_settings.black_line_refresh_flag:
        black_lines.drawme()

    # 让最近绘制的屏幕可见
    pygame.display.flip()


def check_keydown_events(screen, event, game_settings, all_cubics, dead_cubics, temp_cubics, black_lines):
    """处理按键事件"""
    if event.key == pygame.K_q:
        game_settings.exit_threads_flag = True
        sys.exit()

    if (event.key == pygame.K_DOWN) or (event.key == pygame.K_LEFT) or (event.key == pygame.K_RIGHT):
        # 记录按下键的标志位,并打上按键事件戳
        if event.key == pygame.K_DOWN:
            game_settings.key_down = True
            game_settings.key_down_timestamp = time.time()
        if event.key == pygame.K_LEFT:
            game_settings.key_left = True
            game_settings.key_left_timestamp = time.time()
        if event.key == pygame.K_RIGHT:
            game_settings.key_right = True
            game_settings.key_right_timestamp = time.time()

        # 到底部或左右边界则停止
        to_edge = check_edge(event.key, game_settings, all_cubics)

        # 并且检测下一步是否会碰撞
        if not to_edge:
            if not check_collision(game_settings, all_cubics, dead_cubics, temp_cubics, event.key):
                all_cubics.cubics.update(game_settings, event.key)
            else:
                deal_collision(screen, game_settings, all_cubics, dead_cubics, event.key, black_lines)

    if event.key == pygame.K_SPACE:
        all_cubics.rotate()


def check_keyup_events(event, game_settings):
    """处理弹起键盘按键事件"""
    if event.key == pygame.K_DOWN:
        game_settings.key_down = False
    if event.key == pygame.K_LEFT:
        game_settings.key_left = False
    if event.key == pygame.K_RIGHT:
        game_settings.key_right = False


def check_events(screen, game_settings, all_cubics, dead_cubics, temp_cubics, black_lines):
    """检测鼠标键盘事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_settings.exit_threads_flag = True
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(screen, event, game_settings, all_cubics, dead_cubics, temp_cubics, black_lines)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, game_settings)


def check_edge(event_key, game_settings, all_cubics):
    """检测已到边界,底部边界为最底下一排以下,最底下一排属于碰撞检测的范围"""
    for cubic in all_cubics.cubics.sprites():
        if ((event_key == pygame.K_DOWN) or (event_key == 'down')) and (cubic.rect.y + game_settings.cubic_move_dist \
            > game_settings.screen_height):
            return True
        if (event_key == pygame.K_LEFT) and (cubic.rect.x <= 0):
            return True
        if (event_key == pygame.K_RIGHT) and (cubic.rect.x + game_settings.cubic_move_dist >= \
            game_settings.screen_width):
            return True
        if event_key == 'up':
            return False


def check_collision(game_settings, all_cubics, dead_cubics, temp_cubics, event_key):
    """检测碰撞"""
    # 如果按向下键,判断是否落到最底下一排
    if (event_key == pygame.K_DOWN) or (event_key == 'down'):
        for cubic in all_cubics.cubics.sprites():
            if cubic.rect.y + game_settings.cubic_move_dist >= game_settings.screen_height:
                return True

    # 复制正在下落的方块组
    for cubic in all_cubics.cubics.sprites():
        new_cubic = MetaCubic('images/cubic_lblue.bmp')
        new_cubic.rect.x = cubic.rect.x
        new_cubic.rect.y = cubic.rect.y
        temp_cubics.add(new_cubic)
    #对复制后的类进行下一步的位置更新
    temp_cubics.update(game_settings, event_key)
    # 判断是否碰撞
    collisions =  pygame.sprite.groupcollide(temp_cubics, dead_cubics.cubics, False, False)
    # 清空临时组
    for cubic in temp_cubics.copy():
        temp_cubics.remove(cubic)
    if collisions:
        return True
    else:
        return False


def deal_collision(screen, game_settings, all_cubics, dead_cubics, event_key, black_lines):
    """碰撞处理"""
    # 如果是横向碰撞,则不做更新即可
    if (event_key != pygame.K_LEFT) and (event_key != pygame.K_RIGHT):
        # 否则就是按了向下键,需要固定方块
        # 从all_cubics取出所有元方块,改变颜色,并加入到dead_cubics组
        for cubic in all_cubics.cubics.sprites():
            cubic.image = pygame.image.load('images/cubic_lblue.bmp')
            dead_cubics.cubics.add(cubic)
        # 清除all_cubics的所有元方块
        all_cubics.cubics.empty()

        # 消除填满的行
        clear_lines(screen, game_settings, all_cubics, dead_cubics, black_lines)

        # 重置按键的保持按下状态
        game_settings.key_down = False
        game_settings.key_left = False
        game_settings.key_right = False
        # 载入新方块组落下
        all_cubics.add_cubics()


def show_full_lines(screen, game_settings, all_cubics, dead_cubics, full_line_y, black_lines):
    """动画显示被消除的行"""
    # 按消除的行数与y值建立黑行并加入黑行组
    for y in full_line_y:
        new_black_line = BlackLine(screen, game_settings)
        new_black_line.rect.y = y
        black_lines.line.add(new_black_line)

    # 闪烁
    game_settings.black_line_refresh_flag = True
    update_screen(screen, game_settings, all_cubics, dead_cubics, black_lines)
    time.sleep(0.3)
    game_settings.black_line_refresh_flag = False
    update_screen(screen, game_settings, all_cubics, dead_cubics, black_lines)
    time.sleep(0.3)

    # 删除黑行组里的黑行
    black_lines.line.empty()


def clear_lines(screen, game_settings, all_cubics, dead_cubics, black_lines):
    """消除填满的行"""
    # 扫描全屏,检测并记录已填满的行
    full_line_y = []
    for y in range(0, game_settings.screen_height, game_settings.metacubic_width):
        cubic_count_x = 0
        for x in range(0, game_settings.screen_width, game_settings.metacubic_width):
            for cubic in dead_cubics.cubics.sprites():
                if cubic.rect.y == y:
                    if cubic.rect.x == x:
                        cubic_count_x += 1
                        break
            if cubic_count_x == game_settings.screen_width / game_settings.metacubic_width:
                full_line_y.append(y)

    # 动画显示已填满的行
    if len(full_line_y) > 0:
        show_full_lines(screen, game_settings, all_cubics, dead_cubics, full_line_y, black_lines)

    # 消除已填满的行
    if len(full_line_y) > 0:
        for y in full_line_y:
            for cubic in dead_cubics.cubics.copy():
                if cubic.rect.y == y:
                    dead_cubics.cubics.remove(cubic)

        # 空行的上一行方块下移
        for y in full_line_y:
            for cubic in dead_cubics.cubics.copy():
                if cubic.rect.y < y:
                    cubic.rect.y += game_settings.metacubic_width


def key_down_update_cubics(screen, event_key, game_settings, all_cubics, dead_cubics, temp_cubics, thread_lock, \
                           black_lines):
    """按键持续按下时连续更新方块组"""
    # 到边界则停止,并做碰撞检测与处理
    to_edge = check_edge(event_key, game_settings, all_cubics)
    if not to_edge:
        if not check_collision(game_settings, all_cubics, dead_cubics, temp_cubics, event_key):
            thread_lock.acquire()
            all_cubics.cubics.update(game_settings, event_key)
            thread_lock.release()
        else:
            thread_lock.acquire()
            deal_collision(screen, game_settings, all_cubics, dead_cubics, event_key, black_lines)
            thread_lock.release()