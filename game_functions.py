import pygame
import sys


def check_keydown_events(event, game_settings, all_cubics, thread):
    """处理按键事件"""
    if event.key == pygame.K_q:
        thread.exit_flag = True
        sys.exit()
    if (event.key == pygame.K_DOWN) or (event.key == pygame.K_LEFT) or (event.key == pygame.K_RIGHT):
        # 到底部或左右边界则停止
        to_edge = check_edge(event.key, game_settings, all_cubics)
        if not to_edge:
            all_cubics.cubics.update(game_settings, event.key, False, True)
    if event.key == pygame.K_SPACE:
        all_cubics.rotate()


def check_events(game_settings, all_cubics, thread):
    """检测鼠标键盘事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            thread.exit_flag = True
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, game_settings, all_cubics, thread)


def update_screen(screen, game_settings, all_cubics):
    """更新屏幕"""
    # 重绘屏幕
    screen.fill(game_settings.screen_bgcolor)

    # 重绘方块
    all_cubics.drawme()

    # 让最近绘制的屏幕可见
    pygame.display.flip()


def check_edge(event_key, game_settings, all_cubics):
    """检测已到边界"""
    for cubic in all_cubics.cubics.sprites():
        if (event_key == pygame.K_DOWN) and (cubic.rect.y + game_settings.cubic_move_dist >= \
    game_settings.screen_height):
            return True
        if (event_key == pygame.K_LEFT) and (cubic.rect.x <= 0):
            return True
        if (event_key == pygame.K_RIGHT) and (cubic.rect.x + game_settings.cubic_move_dist >= \
     game_settings.screen_width):
            return True