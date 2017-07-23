import threading
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

    def run(self):
        while not self.exit_flag:
            self.thread_lock.acquire()
            self.cubics.cubics.update(self.game_settings, None, True, False)
            gf.update_screen(self.screen, self.game_settings, self.cubics, self.game_settings.fall_interval)
            self.thread_lock.release()