import pygame
import threading
import time
from time import sleep

import game_functions as gf


class ThreadCubicFall(threading.Thread):
    """线程类对应game_functions.py函数check_events()"""
    def __init__(self, game_settings, all_cubics, thread_lock):
        super(ThreadCubicFall, self).__init__()
        self.game_settings = game_settings
        self.cubics = all_cubics
        self.thread_lock = thread_lock
        # self.fps_clock = pygame.time.Clock()

    def run(self):
        while not self.game_settings.exit_threads_flag:
            # 限制速度
            # self.fps_clock.tick(self.game_settings.FPS)

            # 方块下落的速度
            sleep(self.game_settings.fall_interval)

            # 到底部边界则停止
            to_edge = gf.check_edge('down', self.game_settings, self.cubics)
            if not to_edge:
                self.thread_lock.acquire()
                self.cubics.cubics.update(self.game_settings, 'down')
                self.thread_lock.release()


class ThreadCheckKeyDown(threading.Thread):
    """线程类对应game_functions.py函数check_events()"""
    def __init__(self, game_settings, all_cubics, thread_lock):
        super(ThreadCheckKeyDown, self).__init__()
        self.game_settings = game_settings
        self.cubics = all_cubics
        self.thread_lock = thread_lock
        # self.fps_clock = pygame.time.Clock()

    def run(self):
        while not self.game_settings.exit_threads_flag:
            # 限制速度
            # self.fps_clock.tick(self.game_settings.FPS)

            # 限制检测间隔
            sleep(0.1)

            # 检测时间间隔如果大于1秒,则连续更新位置
            while (self.game_settings.key_down) and (time.time() - self.game_settings.key_down_timestamp > 0.5):
                # 到边界则停止
                to_edge = gf.check_edge(pygame.K_DOWN, self.game_settings, self.cubics)
                if not to_edge:
                    self.thread_lock.acquire()
                    self.cubics.cubics.update(self.game_settings, pygame.K_DOWN)
                    self.thread_lock.release()
                sleep(0.05)

            while (self.game_settings.key_left) and (time.time() - self.game_settings.key_left_timestamp > 0.5):
                # 到边界则停止
                to_edge = gf.check_edge(pygame.K_LEFT, self.game_settings, self.cubics)
                if not to_edge:
                    self.thread_lock.acquire()
                    self.cubics.cubics.update(self.game_settings, pygame.K_LEFT)
                    self.thread_lock.release()
                sleep(0.08)

            while (self.game_settings.key_right) and (time.time() - self.game_settings.key_right_timestamp > 0.5):
                # 到边界则停止
                to_edge = gf.check_edge(pygame.K_RIGHT, self.game_settings, self.cubics)
                if not to_edge:
                    self.thread_lock.acquire()
                    self.cubics.cubics.update(self.game_settings, pygame.K_RIGHT)
                    self.thread_lock.release()
                sleep(0.08)