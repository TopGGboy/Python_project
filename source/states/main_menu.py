# 主菜单文件
from importlib import resources

import pygame
from .. import tools, setup
from ..components import info


# 主页面
class MainMenu:
    def __init__(self):
        # self.area_index = None
        self.setup_background()

        self.info = info.main_menu_info()
        # self.setup_player()
        self.setup_cursor()

        # 进入这个界面就初始化界面状态 # 状态机
        setup.MAIN_MENU_FLAGE = True
        self.finished = False
        self.next = "load_screen"

        self.quit = False

    # 初始化背景
    def setup_background(self):
        self.background = setup.GRAPHIC['background']
        self.background_rect = self.background.get_rect()
        self.background = pygame.transform.scale(self.background, setup.C.SCREEN_SIZE)

        self.viewport = setup.SCREEN.get_rect()

    def update(self, surface, keys):
        surface.blit(self.background, self.viewport)
        # 调用info对象的draw方法，将主菜单相关的信息（如文字提示等）绘制到游戏窗口表面上（具体绘制内容由info模块的实现决定）
        self.info.draw(surface)
        surface.blit(self.cursor.image, (445, 100))
        # 将光标图像绘制到光标对应的矩形区域位置上，从而在窗口中显示出光标
        surface.blit(self.cursor.image, self.cursor.rect)

    # def setup_player(self):
    #     pass

    # 创建光标
    def setup_cursor(self):
        self.cursor = pygame.sprite.Sprite()
        # 光标（门）
        self.cursor.image = tools.get_image(setup.GRAPHIC['main'], 11, 12, 51, 79, (255, 255, 255), 0.8)
        rect = self.cursor.image.get_rect()

        if setup.LEVEL_NUMBER != 1:
            rect.x, rect.y = 280, 260
            self.area_index = 0
        else:
            rect.x, rect.y = 280, 320
            self.area_index = 1

        self.cursor.rect = rect

        # 将光标的状态设置为当前的区域索引，用于后续判断光标所在位置对应的操作等，也是一种简单的状态机表示方式
        self.cursor.state = self.area_index  # 状态机

    # 更新光标
    def update_cursor(self, event_key):
        area = [260, 320, 380, 440]
        if event_key == pygame.K_w:
            if setup.LEVEL_NUMBER != 1:
                if self.area_index > 0:
                    self.area_index -= 1
            else:
                if self.area_index > 1:  # 防止进入0
                    self.area_index -= 1

            # 更新光标的状态为新的区域索引
            self.cursor.state = self.area_index
            # 根据新的区域索引更新光标的y坐标位置
            self.cursor.rect.y = area[self.area_index]
        elif event_key == pygame.K_s:
            # 如果当前光标所在区域索引小于3（避免越界，总共有4个可能的区域），则将区域索引加1，即向下移动光标
            if self.area_index < 3:
                self.area_index += 1
            self.cursor.state = self.area_index
            self.cursor.rect.y = area[self.area_index]
        elif event_key == pygame.K_RETURN:
            if self.cursor.state == 0:
                self.finished = True
                setup.MAIN_MENU_FLAGE = False
                # constans.LEVEL_NUMBER -= 1
            elif self.cursor.state == 1:
                self.finished = True
                setup.MAIN_MENU_FLAGE = False
                setup.LEVEL_NUMBER = 1

            elif self.cursor.state == 2:
                print(2)
            elif self.cursor.state == 3:
                # 程序结束
                setup.QUIT_GAME = True
