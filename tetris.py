import pygame
import threading

from settings import Settings
from all_cubic import AllCubic
from my_threads import ThreadCubicFall, ThreadCheckKeyDown
import game_functions as gf


def run_game():
    """游戏主进程"""

    # 创建游戏设置类
    game_settings = Settings()

    # 初始化pygame并创建屏幕
    pygame.init()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Tetris (Roy)")

    # 创建pygame时钟控制
    fps_clock = pygame.time.Clock()

    # 创建方块
    newcubics = AllCubic(screen, game_settings)

    # 创建多线程
    thread_lock = threading.Lock()
    # 创建方块自由下落线程
    thread_cubic_fall = ThreadCubicFall(game_settings, newcubics, thread_lock)
    thread_cubic_fall.start()
    # 创建连续按键检测线程
    thread_key_down = ThreadCheckKeyDown(game_settings, newcubics, thread_lock)
    thread_key_down.start()

    while True:
        # 限制运行速度
        fps_clock.tick(game_settings.FPS)
        gf.check_events(game_settings, newcubics)
        gf.update_screen(screen, game_settings, newcubics)

# 开始游戏主进程
run_game()