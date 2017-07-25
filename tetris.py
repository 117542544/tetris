import pygame
import threading
from pygame.sprite import Group

from settings import Settings
from my_class import AllCubic, DeadCubic, BlackLines
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

    # 创建新落下的方块
    newcubics = AllCubic(screen, game_settings)
    newcubics.add_cubics()

    # 创建检测碰撞用的临时方块实例组
    tempcubics = Group()

    # 创建被固定的dead方块
    deadcubics = DeadCubic(screen, game_settings)

    # 创建消除时显示的黑行组
    blacklines = BlackLines()

    # 创建多线程
    thread_lock = threading.Lock()
    # 创建方块自由下落线程
    thread_cubic_fall = ThreadCubicFall(screen,game_settings, newcubics, deadcubics, tempcubics, thread_lock, \
                                        blacklines)
    thread_cubic_fall.start()
    # 创建连续按键检测线程
    thread_key_down = ThreadCheckKeyDown(screen,game_settings, newcubics, deadcubics, tempcubics, thread_lock, \
                                         blacklines)
    thread_key_down.start()

    while True:
        # 限制运行速度
        fps_clock.tick(game_settings.FPS)
        # 事件检测
        gf.check_events(screen, game_settings, newcubics, deadcubics, tempcubics, blacklines)
        # 更新所有屏幕元素
        gf.update_screen(screen, game_settings, newcubics, deadcubics, blacklines)

# 开始游戏主进程
run_game()