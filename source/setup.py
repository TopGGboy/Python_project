# 游戏初始启动

import pygame
from source import constants as C
from . import tools

# from source import run_, tools

pygame.init()
SCREEN = pygame.display.set_mode((C.SCREEN_W, C.SCREEN_H))

GRAPHIC = tools.load_graphics('resources/graphics')

# 字体初始化
Level_font = pygame.font.Font('./resources/font/font_1.ttf', 50)
Other_font = pygame.font.Font('./resources/font/font_1.ttf', 30)
Main_menu_font = pygame.font.Font('./resources/font/font_1.ttf', 40)

# 是否在主页面
MAIN_MENU_FLAGE = True

# 关卡数字
LEVEL_NUMBER = tools.r_w_memory("memory.json", "r")['level_number']

# 是否结束程序
QUIT_GAME = False

# 地图
MAP = None

# 玩家状态
PLAYER_BUFF = None

PLAYER = None

# 陷阱位置
TRAP_XY = {'gear_trap': [], 'Ground_thorn_trap': [], 'wall_trap': [], 'janci_trap': []}
# 陷阱触发位
TRAP_TRACK = {'gear_trap': [], 'Ground_thorn_trap': [], 'wall_trap': [], 'janci_trap': []}

# TRAP_DATA = tools.load_map_data('trap.json')
#

#
#
#
# # 初始化陷阱
# def set_up_trap():
#     # 陷阱位置
#     C.TRAP_XY = {'gear_trap': [], 'Ground_thorn_trap': [], 'wall_trap': [], 'janci_trap': []}
#     # 陷阱触发位置
#     C.TRAP_TRACK = {'gear_trap': [], 'Ground_thorn_trap': [], 'wall_trap': [], 'janci_trap': []}
