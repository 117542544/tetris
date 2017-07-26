import pygame


class ScoreBoard():
    """记分板类"""
    def __init__(self, screen, game_settings):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.game_settings = game_settings

        # 字体与颜色设置
        self.text_color = (255, 255, 255)
        self.rect_color = (128, 128, 128)
        self.text_font = pygame.font.SysFont(None, 22)
        self.number_font = pygame.font.SysFont(None, 30)
        self.rect_line_thickness = 4

        # 准备得分板图像
        self.prep_rect()
        self.prep_text()
        #self.prep_lines()
        #self.prep_level()


    def create_text(self, text, text_left_x, text_right_x, text_bottom_y):
        """把文本或数字绘制为图像"""
        if type(text) is str:
            image = self.text_font.render(text, True, self.text_color, self.game_settings.screen_bgcolor)
        else:
            image = self.number_font.render(str(text), True, self.text_color, self.game_settings.screen_bgcolor)
        rect = image.get_rect()
        # 放置到参数定义的位置
        if text_left_x:
            rect.left = text_left_x
        if text_right_x:
            rect.right = text_right_x
        rect.bottom = text_bottom_y
        return (image, rect)

    def create_rect(self, rect_width, rect_height, rect_left_x, rect_bottom_y):
        """绘制得分板矩形"""
        # 在(0,0)处创建矩形， 后面再放置到参数定义的位置
        rect = pygame.Rect(0, 0, rect_width, rect_height)
        rect.left = rect_left_x
        rect.bottom = rect_bottom_y
        return rect

    def prep_rect(self):
        """绘制方框"""
        # 横向上面一条粗线
        self.horizontal_rect_1 = self.create_rect(self.game_settings.screen_width / 8 * 7, \
                                                  self.rect_line_thickness, self.game_settings.screen_width / 8 / 2, 35)
        # 横向上面第二条粗线
        self.horizontal_rect_2 = self.create_rect(self.game_settings.screen_width / 8 * 5, \
                                                  self.rect_line_thickness, self.game_settings.screen_width / 8 / 2 \
                                                  * 3, 70)
        # 纵向中线
        self.vertical_rect_2 = self.create_rect(self.rect_line_thickness, 60, self.screen_rect.centerx - \
                                                self.rect_line_thickness / 2 - 10, 70)
        # 纵向左中线
        self.vertical_rect_1 = self.create_rect(self.rect_line_thickness, 60, self.screen_rect.centerx - \
                                                self.rect_line_thickness / 2 - 85, 70)
        # 纵向左中线
        self.vertical_rect_3 = self.create_rect(self.rect_line_thickness, 60, self.screen_rect.centerx - \
                                                self.rect_line_thickness / 2 + 75, 70)
        # 纵向上左线
        self.vertical_up_short_rect_1 = self.create_rect(self.rect_line_thickness, 25, \
                                                         self.game_settings.screen_width / 8 / 2, 35)
        # 纵向上右线
        self.vertical_up_short_rect_2 = self.create_rect(self.rect_line_thickness, 25, \
                                                         self.game_settings.screen_width / 8 / 2 + \
                                                         self.game_settings.screen_width / 8 * 7 - \
                                                         self.rect_line_thickness, 35)
        # 纵向下左线
        self.vertical_down_short_rect_1 = self.create_rect(self.rect_line_thickness, 25, \
                                                           self.game_settings.screen_width / 8 / 2 * 3, 70)
        # 纵向下右线
        self.vertical_down_short_rect_2 = self.create_rect(self.rect_line_thickness, 25, \
                                                           self.game_settings.screen_width / 8 / 2 * 3  + \
                                                           self.game_settings.screen_width / 8 * 5 - \
                                                           self.rect_line_thickness, 70)

    def prep_text(self):
        """绘制文字与数字"""
        # 文字转图像
        self.text_score_image, self.text_score_rect = self.create_text('SCORE', False, \
                                                             self.screen_rect.centerx - 20, 27)
        self.text_hiscore_image, self.text_hiscore_rect = self.create_text('HISCORE', self.screen_rect.centerx\
                                                                         - 2, False, 27)
        self.text_level_image, self.text_level_rect = self.create_text('LEVEL', False, \
                                                                       self.screen_rect.centerx - 25, 62)
        self.text_lines_image, self.text_lines_rect = self.create_text('LINES', self.screen_rect.centerx \
                                                                           + 8, False, 62)
        # 数字转图像
        self.num_score_image, self.num_score_rect = self.create_text(self.game_settings.score, False, \
                                                                       self.screen_rect.centerx - 95, 30)
        self.num_hiscore_image, self.num_hiscore_rect = self.create_text(self.game_settings.hiscore, False, \
                                                                     self.screen_rect.centerx + 165, 30)
        self.num_level_image, self.num_level_rect = self.create_text(self.game_settings.level, False, \
                                                                     self.screen_rect.centerx - 95, 65)
        self.num_lines_image, self.num_lines_rect = self.create_text(self.game_settings.lines, False, \
                                                                         self.screen_rect.centerx + 115, 65)

    def show_all(self):
        pygame.draw.rect(self.screen, self.rect_color, self.horizontal_rect_1)
        pygame.draw.rect(self.screen, self.rect_color, self.horizontal_rect_2)
        pygame.draw.rect(self.screen, self.rect_color, self.vertical_rect_1)
        pygame.draw.rect(self.screen, self.rect_color, self.vertical_rect_2)
        pygame.draw.rect(self.screen, self.rect_color, self.vertical_rect_3)
        pygame.draw.rect(self.screen, self.rect_color, self.vertical_up_short_rect_1)
        pygame.draw.rect(self.screen, self.rect_color, self.vertical_up_short_rect_2)
        pygame.draw.rect(self.screen, self.rect_color, self.vertical_down_short_rect_1)
        pygame.draw.rect(self.screen, self.rect_color, self.vertical_down_short_rect_2)
        self.screen.blit(self.text_score_image, self.text_score_rect)
        self.screen.blit(self.text_hiscore_image, self.text_hiscore_rect)
        self.screen.blit(self.text_lines_image, self.text_lines_rect)
        self.screen.blit(self.text_level_image, self.text_level_rect)
        self.screen.blit(self.num_score_image, self.num_score_rect)
        self.screen.blit(self.num_hiscore_image, self.num_hiscore_rect)
        self.screen.blit(self.num_level_image, self.num_level_rect)
        self.screen.blit(self.num_lines_image, self.num_lines_rect)