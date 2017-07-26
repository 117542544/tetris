"""TETRIS by Royson"""
import pygame
import threading
from pygame.sprite import Group

from settings import Settings
from my_class import FallCubic, DeadCubic, BlackLines
from score_board import ScoreBoard
import game_functions as gf
import start_stop_func as ss


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
    fall_cubics = FallCubic(screen, game_settings)

    # 创建检测碰撞用的临时方块实例组
    temp_cubics = Group()

    # 创建被固定的dead方块
    dead_cubics = DeadCubic(screen, game_settings)

    # 创建消除时显示的黑行组
    black_lines = BlackLines()

    # 创建得分板
    score_board = ScoreBoard(screen, game_settings)

    # 创建多线程
    thread_lock = threading.Lock()

    # 初始化游戏
    game_settings.game_over = True
    game_settings.game_wait = True
    ss.game_start(screen, game_settings, fall_cubics, dead_cubics, temp_cubics, thread_lock, black_lines, score_board)

    while True:
        # 限制运行速度
        fps_clock.tick(game_settings.FPS)
        # game_over后重启程序
        ss.game_start(screen, game_settings, fall_cubics, dead_cubics, temp_cubics, thread_lock, black_lines, \
                          score_board)
        # 事件检测
        gf.check_events(screen, game_settings, fall_cubics, dead_cubics, temp_cubics, black_lines, score_board)
        # 更新所有屏幕元素
        gf.update_screen(screen, game_settings, fall_cubics, dead_cubics, black_lines, score_board)

# 开始游戏主进程
run_game()