class Settings():
    """创建游戏的静态初始设置"""
    def __init__(self):
        # 屏幕设置
        self.screen_width = 400
        self.screen_height = 600
        self.screen_bgcolor = (0, 0, 0)
        self.FPS = 30

        # 元方块宽度设置
        self.metacubic_width = 25
        # 方块单次下落距离
        self.cubic_move_dist = 25
        # 放置方块的起始高度
        self.cubic_start_height = 75
        # 方块形状对应的图片路径,排列的位置与顺时针四种方向设置
        self.cubic_shape = {
            1 : ('images/cubic_red.bmp', {
                1 : {
                    "cub1": (self.screen_width / 2 - self.metacubic_width, 0),
                    "cub2": (self.screen_width / 2, 0),
                    "cub3": (self.screen_width / 2 - self.metacubic_width, self.metacubic_width),
                    "cub4": (self.screen_width / 2, 0 + self.metacubic_width)
                },
                2: {
                    "cub1": (self.screen_width / 2 - self.metacubic_width, 0),
                    "cub2": (self.screen_width / 2, 0),
                    "cub3": (self.screen_width / 2 - self.metacubic_width, self.metacubic_width),
                    "cub4": (self.screen_width / 2, 0 + self.metacubic_width)
                },
                3: {
                    "cub1": (self.screen_width / 2 - self.metacubic_width, 0),
                    "cub2": (self.screen_width / 2, 0),
                    "cub3": (self.screen_width / 2 - self.metacubic_width, self.metacubic_width),
                    "cub4": (self.screen_width / 2, 0 + self.metacubic_width)
                },
                4: {
                    "cub1": (self.screen_width / 2 - self.metacubic_width, 0),
                    "cub2": (self.screen_width / 2, 0),
                    "cub3": (self.screen_width / 2 - self.metacubic_width, self.metacubic_width),
                    "cub4": (self.screen_width / 2, 0 + self.metacubic_width)
                }
            }),
            2 : ('images/cubic_yellow.bmp', {
                1: {
                    "cub1": (self.screen_width / 2 - self.metacubic_width, self.metacubic_width),
                    "cub2": (self.screen_width / 2, 0),
                    "cub3": (self.screen_width / 2, self.metacubic_width),
                    "cub4": (self.screen_width / 2, 2 * self.metacubic_width)
                },
                2: {
                    "cub1": (self.screen_width / 2, 0),
                    "cub2": (self.screen_width / 2 - self.metacubic_width, self.metacubic_width),
                    "cub3": (self.screen_width / 2, self.metacubic_width),
                    "cub4": (self.screen_width / 2 + self.metacubic_width, self.metacubic_width)
                },
                3: {
                    "cub1": (self.screen_width / 2 + self.metacubic_width, self.metacubic_width),
                    "cub2": (self.screen_width / 2, 0),
                    "cub3": (self.screen_width / 2, self.metacubic_width),
                    "cub4": (self.screen_width / 2, 2 * self.metacubic_width)
                },
                4: {
                    "cub1": (self.screen_width / 2, 2 * self.metacubic_width),
                    "cub2": (self.screen_width / 2 - self.metacubic_width, self.metacubic_width),
                    "cub3": (self.screen_width / 2, self.metacubic_width),
                    "cub4": (self.screen_width / 2 + self.metacubic_width, self.metacubic_width)
                }
            }),
            3 : ('images/cubic_orange.bmp', {
                1: {
                    "cub1": (self.screen_width / 2 - self.metacubic_width, self.metacubic_width),
                    "cub2": (self.screen_width / 2 - self.metacubic_width, 2 * self.metacubic_width),
                    "cub3": (self.screen_width / 2, 0),
                    "cub4": (self.screen_width / 2, self.metacubic_width)
                },
                2: {
                    "cub1": (self.screen_width / 2 - self.metacubic_width, self.metacubic_width),
                    "cub2": (self.screen_width / 2, self.metacubic_width),
                    "cub3": (self.screen_width / 2 - 2 * self.metacubic_width, 0),
                    "cub4": (self.screen_width / 2 - self.metacubic_width, 0)
                },
                3: {
                    "cub1": (self.screen_width / 2 - self.metacubic_width, self.metacubic_width),
                    "cub2": (self.screen_width / 2 - self.metacubic_width, 2 * self.metacubic_width),
                    "cub3": (self.screen_width / 2, 0),
                    "cub4": (self.screen_width / 2, self.metacubic_width)
                },
                4: {
                    "cub1": (self.screen_width / 2 - self.metacubic_width, self.metacubic_width),
                    "cub2": (self.screen_width / 2, self.metacubic_width),
                    "cub3": (self.screen_width / 2 - 2 * self.metacubic_width, 0),
                    "cub4": (self.screen_width / 2 - self.metacubic_width, 0)
                }
            }),
            4 : ('images/cubic_lblue.bmp', {
                1: {
                    "cub1": (self.screen_width / 2, 0),
                    "cub2": (self.screen_width / 2, self.metacubic_width),
                    "cub3": (self.screen_width / 2, 2 * self.metacubic_width),
                    "cub4": (self.screen_width / 2, 3 * self.metacubic_width)
                },
                2: {
                    "cub1": (self.screen_width / 2 - 2 * self.metacubic_width, self.metacubic_width),
                    "cub2": (self.screen_width / 2 - 1 * self.metacubic_width, self.metacubic_width),
                    "cub3": (self.screen_width / 2, self.metacubic_width),
                    "cub4": (self.screen_width / 2 + self.metacubic_width, self.metacubic_width)
                },
                3: {
                    "cub1": (self.screen_width / 2, 0),
                    "cub2": (self.screen_width / 2, self.metacubic_width),
                    "cub3": (self.screen_width / 2, 2 * self.metacubic_width),
                    "cub4": (self.screen_width / 2, 3 * self.metacubic_width)
                },
                4: {
                    "cub1": (self.screen_width / 2 - 2 * self.metacubic_width, self.metacubic_width),
                    "cub2": (self.screen_width / 2 - 1 * self.metacubic_width, self.metacubic_width),
                    "cub3": (self.screen_width / 2, self.metacubic_width),
                    "cub4": (self.screen_width / 2 + self.metacubic_width, self.metacubic_width)
                }
            }),
            5 : ('images/cubic_dblue.bmp', {
                1: {
                    "cub1": (self.screen_width / 2 - self.metacubic_width, 0),
                    "cub2": (self.screen_width / 2 - self.metacubic_width, self.metacubic_width),
                    "cub3": (self.screen_width / 2, self.metacubic_width),
                    "cub4": (self.screen_width / 2 + self.metacubic_width, self.metacubic_width)
                },
                2: {
                    "cub1": (self.screen_width / 2 - self.metacubic_width, 0),
                    "cub2": (self.screen_width / 2 - self.metacubic_width, self.metacubic_width),
                    "cub3": (self.screen_width / 2 - self.metacubic_width, 2 * self.metacubic_width),
                    "cub4": (self.screen_width / 2, 0)
                },
                3: {
                    "cub1": (self.screen_width / 2 - 2 * self.metacubic_width, 0),
                    "cub2": (self.screen_width / 2 - self.metacubic_width, 0),
                    "cub3": (self.screen_width / 2, 0),
                    "cub4": (self.screen_width / 2, self.metacubic_width)
                },
                4: {
                    "cub1": (self.screen_width / 2 - self.metacubic_width, 2 * self.metacubic_width),
                    "cub2": (self.screen_width / 2, 0),
                    "cub3": (self.screen_width / 2, self.metacubic_width),
                    "cub4": (self.screen_width / 2, 2 * self.metacubic_width)
                }
            }),
            6 : ('images/cubic_purple.bmp', {
                1: {
                    "cub1": (self.screen_width / 2 - self.metacubic_width, self.metacubic_width),
                    "cub2": (self.screen_width / 2, self.metacubic_width),
                    "cub3": (self.screen_width / 2, 0),
                    "cub4": (self.screen_width / 2 + self.metacubic_width, 0)
                },
                2: {
                    "cub1": (self.screen_width / 2 + self.metacubic_width, self.metacubic_width),
                    "cub2": (self.screen_width / 2, self.metacubic_width),
                    "cub3": (self.screen_width / 2, 0),
                    "cub4": (self.screen_width / 2 + self.metacubic_width, 2 * self.metacubic_width)
                },
                3: {
                    "cub1": (self.screen_width / 2 - self.metacubic_width, self.metacubic_width),
                    "cub2": (self.screen_width / 2, self.metacubic_width),
                    "cub3": (self.screen_width / 2, 0),
                    "cub4": (self.screen_width / 2 + self.metacubic_width, 0)
                },
                4: {
                    "cub1": (self.screen_width / 2 + self.metacubic_width, self.metacubic_width),
                    "cub2": (self.screen_width / 2, self.metacubic_width),
                    "cub3": (self.screen_width / 2, 0),
                    "cub4": (self.screen_width / 2 + self.metacubic_width, 2 * self.metacubic_width)
                }
            }),
            7 : ('images/cubic_green.bmp', {
                1: {
                    "cub1": (self.screen_width / 2, 0),
                    "cub2": (self.screen_width / 2 - 2 * self.metacubic_width, self.metacubic_width),
                    "cub3": (self.screen_width / 2 - self.metacubic_width, self.metacubic_width),
                    "cub4": (self.screen_width / 2, self.metacubic_width)
                },
                2: {
                    "cub1": (self.screen_width / 2 - self.metacubic_width, 0),
                    "cub2": (self.screen_width / 2 - self.metacubic_width, self.metacubic_width),
                    "cub3": (self.screen_width / 2 - self.metacubic_width, 2 * self.metacubic_width),
                    "cub4": (self.screen_width / 2, 2 * self.metacubic_width)
                },
                3: {
                    "cub1": (self.screen_width / 2 - self.metacubic_width, 0),
                    "cub2": (self.screen_width / 2, 0),
                    "cub3": (self.screen_width / 2 + self.metacubic_width, 0),
                    "cub4": (self.screen_width / 2 - self.metacubic_width, self.metacubic_width)
                },
                4: {
                    "cub1": (self.screen_width / 2 - self.metacubic_width, 0),
                    "cub2": (self.screen_width / 2, 0),
                    "cub3": (self.screen_width / 2, self.metacubic_width),
                    "cub4": (self.screen_width / 2, 2 * self.metacubic_width)
                }
            })
        }

        # 黑行设置
        self.black_line_width = self.screen_width
        self.black_line_height = self.metacubic_width
        self.black_line_color = self.screen_bgcolor

        # 消行记分设置
        self.earn_score = {
            1 : 100,
            2 : 300,
            3 : 500,
            4 : 800
        }
        # 最高分
        self.hiscore = 0
        # 每升一级需要消除的行数
        self.levelup_lines = 30

        # 初始化动态参数
        self.init_dynamic_setting()

    def init_dynamic_setting(self):
        """初始化动态参数"""
        # 退出所有子线程标志
        self.exit_threads_flag = False

        # 方块下落的时间间隔
        self.fall_interval = 1.0

        # 按键标志
        self.key_down = False
        self.key_left = False
        self.key_right = False
        self.key_down_timestamp = 0
        self.key_left_timestamp = 0
        self.key_right_timestamp = 0

        # 黑行更新标志位
        self.black_line_refresh_flag = False

        # 记录游戏得分,最高分，关卡级别,消行总数
        self.score = 0
        self.level = 0
        self.lines = 0


    def increase_speed(self):
        """下落加速"""
        self.fall_interval *= 0.8