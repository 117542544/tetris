import time
import game_functions as gf

from my_threads import ThreadCubicFall, ThreadCheckKeyDown


def game_over(screen, game_settings, fall_cubics, dead_cubics, black_lines, score_board):
    """gameover相关处理"""
    game_settings.game_over = True
    game_settings.exit_threads_flag = True
    gf.update_screen(screen, game_settings, fall_cubics, dead_cubics, black_lines, score_board)
    # 显示5秒后转到显示play按钮
    time.sleep(5)
    game_settings.game_wait = True


def game_start(screen, game_settings, fall_cubics, dead_cubics, temp_cubics, thread_lock, black_lines, score_board):
    """游戏开始时的初始化函数"""
    '''
    game_over标志位    game_wait标志位           表示状态

    True                AnyAny                  游戏结束，其他线程停止，check事件只检查退出和鼠标事件
    True                False                   游戏结束后，出现play标志位前,只显示game_over框，不显示play
    True                True                    游戏结束后或第一次开始前，只显示play按钮，接受鼠标点击
    False               True                    play按钮接受鼠标点击后,本函数开始初始化,游戏重置并开始
    False               False                   游戏正式play状态
    '''
    # 判断是否需要重置游戏
    if game_settings.game_wait and not game_settings.game_over:
        pass
    else:
        return

    # 重置动态置与各种标志位
    game_settings.init_dynamic_setting()
    # 为方块组添加新落下的方块
    fall_cubics.cubics.empty()
    fall_cubics.add_cubics()
    # 清空dead_cubics
    dead_cubics.cubics.empty()
    # 创建方块自由下落线程
    thread_cubic_fall = ThreadCubicFall(screen, game_settings, fall_cubics, dead_cubics, temp_cubics, thread_lock, \
                                        black_lines, score_board)
    thread_cubic_fall.start()
    # 创建连续按键检测线程
    thread_key_down = ThreadCheckKeyDown(screen, game_settings, fall_cubics, dead_cubics, temp_cubics, thread_lock, \
                                         black_lines, score_board)
    thread_key_down.start()


def check_play_button(screen, game_settings, score_board, mouse_x, mouse_y):
    """检查是否按了play按钮,如果点击了则设置game_over标志位,触发game_start函数开始重置游戏"""
    if game_settings.game_over and game_settings.game_wait:
        button_clicked = score_board.playbutton_rect.collidepoint(mouse_x, mouse_y)
        if button_clicked:
            game_settings.game_over = False