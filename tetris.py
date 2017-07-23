import pygame

from settings import Settings
from all_cubic import AllCubic
from my_threads import ThreadCheckEvents
import game_functions as gf


def run_game():
    """游戏主进程"""

    # 创建游戏设置类
    game_settings = Settings()

    # 初始化pygame并创建屏幕
    pygame.init()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Tetris (Roy)")

    # 创建方块
    newcubics = AllCubic(screen, game_settings)

    # 创建事件检测线程
    thread_check_event = ThreadCheckEvents()

    while True:
        gf.check_events(game_settings, newcubics.cubics)
        newcubics.cubics.update(game_settings, None, True, False)
        gf.update_screen(screen, game_settings, newcubics)

# 开始游戏主进程
run_game()