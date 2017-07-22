import pygame

from settings import Settings
from all_cubic import AllCubic
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
    cubic = AllCubic(screen)

    while True:
        gf.check_events()
        gf.update_screen(screen, game_settings, cubic)

# 开始游戏主进程
run_game()