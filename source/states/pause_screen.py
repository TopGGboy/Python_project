import pygame
from pygame import Surface
from source import setup, constants
from source.components import info


class Pause_screen:
    def __init__(self):
        self.setup_pause()
        self.info = info.pause_screen_info()

        # 状态机
        self.pause = False
        self.next = None
        self.finished = False

    def setup_pause(self):
        self.pause_image = setup.GRAPHIC['pause']
        self.pause_image = pygame.transform.scale(self.pause_image, (480, 300))

    def update(self, surface):
        self.draw(surface)

    # 渲染
    def draw(self, surface):
        surface.blit(self.pause_image, (190, 130))
        self.info.draw(surface)

    # pause界面的鼠标检测和功能
    def pause_mouse_event(self, event):
        if event.button == 1:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if (constants.LOAD_SCREEN_RECT['return_home'][0] < mouse_x < constants.LOAD_SCREEN_RECT['return_home'][
                2] and
                    constants.LOAD_SCREEN_RECT['return_home'][1] < mouse_y < constants.LOAD_SCREEN_RECT['return_home'][
                        3]):
                print("返回主界面")
                # # 返回主界面
                self.next = "main_menu"
                self.finished = True
                self.pause = False
                # self.return_home_flage = True
                # self.state.finished = True
                # constants.MAIN_MENU_FLAGE = True
            elif (constants.LOAD_SCREEN_RECT['up_level'][0] < mouse_x < constants.LOAD_SCREEN_RECT['up_level'][2] and
                  constants.LOAD_SCREEN_RECT['up_level'][1] < mouse_y < constants.LOAD_SCREEN_RECT['up_level'][3]):
                print("上一关")
                self.next = "load_screen"
                self.finished = True
                self.pause = False

                if setup.LEVEL_NUMBER > 1:
                    setup.LEVEL_NUMBER -= 1

                # constants.button_down = 1
                # self.pause = not self.pause
            elif (constants.LOAD_SCREEN_RECT['down_level'][0] < mouse_x < constants.LOAD_SCREEN_RECT['down_level'][
                2] and
                  constants.LOAD_SCREEN_RECT['down_level'][1] < mouse_y < constants.LOAD_SCREEN_RECT['down_level'][3]):
                print("下一关")
                self.next = "load_screen"
                self.finished = True
                self.pause = False

                setup.LEVEL_NUMBER += 1

                # constants.button_down = 2
                # self.pause = not self.pause
