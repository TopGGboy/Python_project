# 工具和游戏主控
import os
import pygame
import random
import json
from .states import main_menu, pause_screen, level, load_screen
from . import setup


# 游戏主控
class Game:
    def __init__(self):
        # 获取游戏窗口的显示表面
        self.screen = pygame.display.get_surface()
        # 创建一个用于控制游戏帧率的时钟对象
        self.clock = pygame.time.Clock()
        # # 获取当前按下的键盘按键状态，初始化为当前的按键状态（字典形式，按键对应布尔值表示是否按下）
        self.keys = None

        self.pause_screen = pause_screen.Pause_screen()

        # self.state_dict = None
        # 将主页面类实例化
        self.page = main_menu.MainMenu()
        # self.return_home_flage = False

    # 主控
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                elif event.type == pygame.KEYDOWN:
                    # 判断是否在主页面
                    in_main_Menu = setup.MAIN_MENU_FLAGE
                    if in_main_Menu:
                        self.page.update_cursor(event.key)

                    self.keys = pygame.key.get_pressed()
                    # 暂停
                    if event.key == pygame.K_ESCAPE and not in_main_Menu:
                        self.pause_screen.pause = not self.pause_screen.pause
                        self.pause_screen.finished = False

                elif event.type == pygame.KEYUP:
                    self.keys = pygame.key.get_pressed()
                elif self.pause_screen.pause:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        # 暂停界面的鼠标检测
                        self.pause_screen.pause_mouse_event(event)
                        # 如果暂停界面结束， 则切换状态
                        if self.pause_screen.finished:
                            self.page.next = self.pause_screen.next
                            self.page.finished = True

            if not self.pause_screen.pause:
                self.update()
            else:
                self.pause_screen.update(self.screen)

            pygame.display.update()
            self.clock.tick(60)

            if setup.QUIT_GAME:
                break

    def update(self):
        # if self.state.finished and self.return_home_flage == False:
        #     next_state = self.state.next
        #
        #     if next_state == 'load_screen':
        #         self.state_dict = {
        #             "load_screen": load_screen.LoadScreen(),
        #         }
        #     elif next_state == 'level':
        #         self.state_dict = {
        #             "level": level.Level(),
        #         }
        #
        #     self.state.finished = False
        #     self.state = self.state_dict[next_state]
        #
        # elif self.state.finished and self.return_home_flage == True:
        #     self.state.finished = False
        #     self.return_home_flage = False
        #     self.state = main_menu.MainMenu()
        if self.page.finished:
            next_page = self.page.next
            if next_page == "load_screen":
                self.page = load_screen.LoadScreen()
            elif next_page == "level":
                self.page = level.Level()
            elif next_page == "main_menu":
                self.page = main_menu.MainMenu()

        # 更新主界面
        self.page.update(self.screen, self.keys)

    # # pause界面的鼠标检测和功能
    # def pause_mouse_event(self, event):
    #     if event.button == 1:
    #         mouse_x, mouse_y = pygame.mouse.get_pos()
    #         if (constans.LOAD_SCREEN_RECT['return_home'][0] < mouse_x < constans.LOAD_SCREEN_RECT['return_home'][2] and
    #                 constans.LOAD_SCREEN_RECT['return_home'][1] < mouse_y < constans.LOAD_SCREEN_RECT['return_home'][
    #                     3]):
    #             self.pause = not self.pause
    #             # 返回主界面
    #             self.return_home_flage = True
    #             self.state.finished = True
    #             constans.MAIN_MENU_FLAGE = True
    #         elif (constans.LOAD_SCREEN_RECT['up_level'][0] < mouse_x < constans.LOAD_SCREEN_RECT['up_level'][2] and
    #               constans.LOAD_SCREEN_RECT['up_level'][1] < mouse_y < constans.LOAD_SCREEN_RECT['up_level'][3]):
    #             constans.button_down = 1
    #             self.pause = not self.pause
    #         elif (constans.LOAD_SCREEN_RECT['down_level'][0] < mouse_x < constans.LOAD_SCREEN_RECT['down_level'][2] and
    #               constans.LOAD_SCREEN_RECT['down_level'][1] < mouse_y < constans.LOAD_SCREEN_RECT['down_level'][3]):
    #             constans.button_down = 2
    #             self.pause = not self.pause
