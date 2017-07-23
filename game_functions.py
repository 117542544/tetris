import pygame
import sys
from time import sleep


def check_keydown_events(event, game_settings, all_cubics, thread):
    """处理按键事件"""
    if event.key == pygame.K_q:
        thread.exit_flag = True
        sys.exit()
    if (event.key == pygame.K_DOWN) or (event.key == pygame.K_LEFT) or (event.key == pygame.K_RIGHT):
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


def update_screen(screen, game_settings, all_cubics, time_wait=False):
    """更新屏幕"""
    # 重绘屏幕
    screen.fill(game_settings.screen_bgcolor)

    # 重绘方块
    if time_wait:
        sleep(time_wait)
    all_cubics.drawme()

    # 让最近绘制的屏幕可见
    pygame.display.flip()