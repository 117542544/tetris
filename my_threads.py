import threading
import game_functions as gf

class ThreadCheckEvents(threading.Thread):
    """线程类对应game_functions.py函数check_events()"""
    def __init__(self):
        super(ThreadCheckEvents, self).__init__()

    def run(self, game_settings, cubics):
        gf.check_events(game_settings, cubics)