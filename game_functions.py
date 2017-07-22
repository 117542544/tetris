import pygame
import sys


def check_keydown_events(event):
    """处理按键事件"""
    if event.key == pygame.K_q:
        sys.exit()


def check_events():
    """检测鼠标键盘事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event)


def update_screen(screen, game_settings, cubic):
    """更新屏幕"""
    # 重绘屏幕
    screen.fill(game_settings.screen_bgcolor)

    # 重绘方块
    cubic.drawme()

    # 让最近绘制的屏幕可见
    pygame.display.flip()