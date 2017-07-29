import pygame
import sys
import time

from my_class import MetaCubic, BlackLine
import start_stop_func as ss


def update_screen(screen, game_settings, fall_cubics, dead_cubics, black_lines, score_board):
    """更新屏幕"""
    # 重绘屏幕
    screen.fill(game_settings.screen_bgcolor)

    # 重绘方块
    fall_cubics.drawme()
    dead_cubics.drawme()
    if game_settings.black_line_refresh_flag:
        black_lines.drawme()

    # 重绘记分板
    score_board.show_all()

    # 让最近绘制的屏幕可见
    pygame.display.flip()


def check_keydown_events(screen, event, game_settings, fall_cubics, dead_cubics, temp_cubics, black_lines, \
                         score_board, thread_lock):
    """处理按键事件"""
    if event.key == pygame.K_q:
        game_settings.exit_threads_flag = True
        sys.exit()

    # 如果是game_over状态就不用检测其他按键了
    if game_settings.game_over:
        return

    # 如果游戏处于运行中,只要有P键就反转暂停状态
    if not game_settings.game_over and not game_settings.game_wait:
        if event.key == pygame.K_p:
            game_settings.game_pause = not(game_settings.game_pause)

    # 如果目前是暂停状态就什么都不做
    if game_settings.game_pause:
        return

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

        # 获取按键方向后更新方块组
        key_down_update_cubics(screen, event.key, game_settings, fall_cubics, dead_cubics, temp_cubics, thread_lock, \
                               black_lines, score_board)

    if event.key == pygame.K_SPACE:
        fall_cubics.rotate()


def check_keyup_events(event, game_settings):
    """处理弹起键盘按键事件"""
    if event.key == pygame.K_DOWN:
        game_settings.key_down = False
    if event.key == pygame.K_LEFT:
        game_settings.key_left = False
    if event.key == pygame.K_RIGHT:
        game_settings.key_right = False


def check_events(screen, game_settings, fall_cubics, dead_cubics, temp_cubics, black_lines, score_board, thread_lock):
    """检测鼠标键盘事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_settings.exit_threads_flag = True
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(screen, event, game_settings, fall_cubics, dead_cubics, temp_cubics, black_lines, \
                                 score_board, thread_lock)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            ss.check_play_button(screen, game_settings, score_board, mouse_x, mouse_y)

        # 如果是game_over状态就不用做后面的事了
        if game_settings.game_over:
            return
        if event.type == pygame.KEYUP:
            check_keyup_events(event, game_settings)


def check_edge(event_key, game_settings, fall_cubics):
    """检测已到边界,底部边界为最底下一排以下,最底下一排属于碰撞检测的范围"""
    for cubic in fall_cubics.cubics.sprites():
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


def check_collision(game_settings, fall_cubics, dead_cubics, temp_cubics, event_key):
    """检测碰撞"""
    # 如果按向下键,判断是否落到最底下一排
    if (event_key == pygame.K_DOWN) or (event_key == 'down'):
        for cubic in fall_cubics.cubics.sprites():
            if cubic.rect.y + game_settings.cubic_move_dist >= game_settings.screen_height:
                return True

    # 复制正在下落的方块组
    for cubic in fall_cubics.cubics.sprites():
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


def deal_collision(screen, game_settings, fall_cubics, dead_cubics, event_key, black_lines, score_board):
    """碰撞处理"""
    # 如果是横向碰撞,则不做更新即可
    if (event_key != pygame.K_LEFT) and (event_key != pygame.K_RIGHT):
        # 否则就是按了向下键,需要固定方块
        # 从fall_cubics取出所有元方块,改变颜色,并加入到dead_cubics组
        for cubic in fall_cubics.cubics.sprites():
            # game_over检测,如果最高的高度超过放下高度则进入dead处理,并退出函数
            if cubic.rect.y == game_settings.cubic_start_height:
                ss.game_over(screen, game_settings, fall_cubics, dead_cubics, black_lines, score_board)
                return
            cubic.image = pygame.image.load(game_settings.cubic_shape[game_settings.level % 7 + 1][0])
            dead_cubics.cubics.add(cubic)
        # 清除fall_cubics的所有元方块
        fall_cubics.cubics.empty()

        # 消除填满的行
        clear_lines(screen, game_settings, fall_cubics, dead_cubics, black_lines, score_board)

        # 载入新方块组落下
        fall_cubics.add_cubics()

        # 重置按键的保持按下状态
        game_settings.key_down = False
        game_settings.key_left = False
        game_settings.key_right = False


def show_full_lines(screen, game_settings, fall_cubics, dead_cubics, full_line_y, black_lines, score_board):
    """动画显示被消除的行"""
    # 按消除的行数与y值建立黑行并加入黑行组
    for y in full_line_y:
        new_black_line = BlackLine(screen, game_settings)
        new_black_line.rect.y = y
        black_lines.line.add(new_black_line)

    # 闪烁
    game_settings.black_line_refresh_flag = True
    update_screen(screen, game_settings, fall_cubics, dead_cubics, black_lines, score_board)
    time.sleep(0.3)
    game_settings.black_line_refresh_flag = False
    update_screen(screen, game_settings, fall_cubics, dead_cubics, black_lines, score_board)
    time.sleep(0.3)

    # 删除黑行组里的黑行
    black_lines.line.empty()


def clear_lines(screen, game_settings, fall_cubics, dead_cubics, black_lines, score_board):
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

    if len(full_line_y) > 0:
        # 动画显示已填满的行
        show_full_lines(screen, game_settings, fall_cubics, dead_cubics, full_line_y, black_lines, score_board)

        # 消除已填满的行
        for y in full_line_y:
            for cubic in dead_cubics.cubics.copy():
                if cubic.rect.y == y:
                    dead_cubics.cubics.remove(cubic)

        # 空行的上一行方块下移
        for y in full_line_y:
            for cubic in dead_cubics.cubics.copy():
                if cubic.rect.y < y:
                    cubic.rect.y += game_settings.metacubic_width

        #更新记分与升级处理
        update_score_and_levelup(game_settings, dead_cubics, score_board, len(full_line_y))

def update_score_and_levelup(game_settings, dead_cubics, score_board, clear_lines):
    """处理消行后的记分更新与升级"""
    # 记分记行并更新最高分
    game_settings.score += game_settings.earn_score[clear_lines]
    game_settings.lines += clear_lines
    if game_settings.score > game_settings.hiscore:
        game_settings.hiscore = game_settings.score

    # 按目前行数判断与处理升级
    if game_settings.lines >= game_settings.level * game_settings.levelup_lines:
        game_settings.level += 1
        # 刷新dead_cubics的颜色
        for cubic in dead_cubics.cubics.sprites():
            cubic.image = pygame.image.load(game_settings.cubic_shape[game_settings.level % 7 + 1][0])
        # 显示升级图像
        score_board.prep_levelup()
        game_settings.level_up = True
        time.sleep(2)
        game_settings.level_up = False
        # 游戏加速
        game_settings.increase_speed()

    # 重新把记分板的数值转换为图像
    score_board.prep_text()


def key_down_update_cubics(screen, event_key, game_settings, fall_cubics, dead_cubics, temp_cubics, thread_lock, \
                           black_lines, score_board):
    """获取按键方向后更新方块组"""
    thread_lock.acquire()
    # 到边界则停止,并做碰撞检测与处理
    to_edge = check_edge(event_key, game_settings, fall_cubics)
    if not to_edge:
        if not check_collision(game_settings, fall_cubics, dead_cubics, temp_cubics, event_key):
            fall_cubics.cubics.update(game_settings, event_key)
        else:
            deal_collision(screen, game_settings, fall_cubics, dead_cubics, event_key, black_lines, \
                           score_board)
    thread_lock.release()