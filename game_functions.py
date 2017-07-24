import pygame
import sys
import time
from all_cubic import MetaCubic

def check_keydown_events(event, game_settings, all_cubics, dead_cubics, temp_cubics):
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
                deal_collision(game_settings, all_cubics, dead_cubics, event.key)

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


def check_events(game_settings, all_cubics, dead_cubics, temp_cubics):
    """检测鼠标键盘事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_settings.exit_threads_flag = True
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, game_settings, all_cubics, dead_cubics, temp_cubics)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, game_settings)


def update_screen(screen, game_settings, all_cubics, dead_cubics):
    """更新屏幕"""
    # 重绘屏幕
    screen.fill(game_settings.screen_bgcolor)

    # 重绘方块
    all_cubics.drawme()
    dead_cubics.drawme()

    # 让最近绘制的屏幕可见
    pygame.display.flip()


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


def deal_collision(game_settings, all_cubics, dead_cubics, event_key):
    """碰撞处理"""
    # 如果是横向碰撞,则不做更新即可
    if (event_key != pygame.K_LEFT) and (event_key != pygame.K_RIGHT):
        # 否则就是按了向下键,需要固定方块
        # 从all_cubics取出所有元方块,改变颜色,并加入到dead_cubics组
        for cubic in all_cubics.cubics.copy():
            cubic.image = pygame.image.load('images/cubic_lblue.bmp')
            dead_cubics.cubics.add(cubic)
            all_cubics.cubics.remove(cubic)
        # 重置按键的保持按下状态
        game_settings.key_down = False
        game_settings.key_left = False
        game_settings.key_right = False
        # 载入新方块组落下
        time.sleep(0.5)
        all_cubics.add_cubics()


def key_down_update_cubics(event_key, game_settings, all_cubics, dead_cubics, temp_cubics, thread_lock):
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
            deal_collision(game_settings, all_cubics, dead_cubics, event_key)
            thread_lock.release()