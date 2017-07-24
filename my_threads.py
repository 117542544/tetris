import pygame
import threading
from time import sleep

import game_functions as gf


class ThreadCubicFall(threading.Thread):
    """线程类对应game_functions.py函数check_events()"""
    def __init__(self, screen, game_settings, all_cubics, thread_lock):
        super(ThreadCubicFall, self).__init__()
        self.screen = screen
        self.game_settings = game_settings
        self.cubics = all_cubics
        self.thread_lock = thread_lock
        self.exit_flag = False
        # self.fps_clock = pygame.time.Clock()

    def run(self):
        while not self.exit_flag:
            # 限制速度
            # self.fps_clock.tick(self.game_settings.FPS)

            # 方块下落的速度
            sleep(self.game_settings.fall_interval)

            # 到底部边界则停止
            to_edge = gf.check_edge(pygame.K_DOWN, self.game_settings, self.cubics)
            if not to_edge:
                self.thread_lock.acquire()
                self.cubics.cubics.update(self.game_settings, None, True, False)
                gf.update_screen(self.screen, self.game_settings, self.cubics)
                self.thread_lock.release()