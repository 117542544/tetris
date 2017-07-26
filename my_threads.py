import pygame
import threading
import time
from time import sleep

import game_functions as gf


class ThreadCubicFall(threading.Thread):
    """线程类对应game_functions.py函数check_events()"""
    def __init__(self, screen, game_settings, all_cubics, dead_cubics, temp_cubics, thread_lock, black_lines, \
                 score_board):
        super(ThreadCubicFall, self).__init__()
        self.screen = screen
        self.game_settings = game_settings
        self.all_cubics = all_cubics
        self.dead_cubics = dead_cubics
        self.temp_cubics = temp_cubics
        self.thread_lock = thread_lock
        self.black_lines = black_lines
        self.score_board = score_board

    def run(self):
        while not self.game_settings.exit_threads_flag:
            # 方块下落的速度
            sleep(self.game_settings.fall_interval)

            gf.key_down_update_cubics(self.screen, 'down', self.game_settings, self.all_cubics, self.dead_cubics, \
                                      self.temp_cubics, self.thread_lock, self.black_lines, self.score_board)


class ThreadCheckKeyDown(threading.Thread):
    """线程类对应game_functions.py函数check_events()"""
    def __init__(self, screen, game_settings, all_cubics, dead_cubics, temp_cubics, thread_lock, black_lines, \
                 score_board):
        super(ThreadCheckKeyDown, self).__init__()
        self.screen = screen
        self.game_settings = game_settings
        self.all_cubics = all_cubics
        self.dead_cubics = dead_cubics
        self.temp_cubics = temp_cubics
        self.thread_lock = thread_lock
        self.black_lines = black_lines
        self.score_board = score_board

    def run(self):
        while not self.game_settings.exit_threads_flag:
            # 限制检测间隔
            sleep(0.05)

            # 检测时间间隔如果大于0.5秒,则连续更新位置
            while (self.game_settings.key_down) and (time.time() - self.game_settings.key_down_timestamp > 0.5):
                gf.key_down_update_cubics(self.screen, pygame.K_DOWN, self.game_settings, self.all_cubics, \
                                          self.dead_cubics, self.temp_cubics, self.thread_lock, self.black_lines, \
                                          self.score_board)
                sleep(0.03)

            while (self.game_settings.key_left) and (time.time() - self.game_settings.key_left_timestamp > 0.5):
                gf.key_down_update_cubics(self.screen, pygame.K_LEFT, self.game_settings, self.all_cubics, \
                                          self.dead_cubics, self.temp_cubics, self.thread_lock, self.black_lines, \
                                          self.score_board)
                sleep(0.08)

            while (self.game_settings.key_right) and (time.time() - self.game_settings.key_right_timestamp > 0.5):
                gf.key_down_update_cubics(self.screen, pygame.K_RIGHT, self.game_settings, self.all_cubics, \
                                          self.dead_cubics, self.temp_cubics, self.thread_lock, self.black_lines, \
                                          self.score_board)
                sleep(0.08)