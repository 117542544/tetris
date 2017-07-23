class Settings():
    """创建游戏的静态初始设置"""
    def __init__(self):
        # 屏幕设置
        self.screen_width = 400
        self.screen_height = 600
        self.screen_bgcolor = (0, 0, 0)

        # 元方块宽度设置
        self.metacubic_width = 25
        # 方块单次下落距离
        self.cubic_fall_dist = 25
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
        self.init_dynamic_setting()

    def init_dynamic_setting(self):
        """初始化动态参数"""
        # 方块下落的时间间隔
        self.fall_interval = 1.0

    def increase_speed(self):
        """下落加速"""
        self.fall_interval *= 0.8