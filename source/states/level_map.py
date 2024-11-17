import pygame.sprite

from .. import setup
from ..components import wall
from . import level


class MAP:
    # 墙壁精灵族
    WALL_S_GROUP = pygame.sprite.Group()

    # # 墙壁列表
    # WALL_LIST = []

    def __init__(self, player_, door):
        MAP.WALL_S_GROUP = pygame.sprite.Group()
        self.player_ = player_
        self.door = door
        self.load_map()

    # 加载地图
    def load_map(self):
        ground_number = 0
        wall_x = 0
        wall_y = 0
        for y in setup.MAP:
            for x in y:
                # 墙
                if x == 1:
                    # 加载路面并放入列表
                    self.setup_ground(wall_x, wall_y, ground_number)
                    ground_number += 1
                elif x == 10:
                    self.player_.rect.x = wall_x
                    self.player_.rect.y = wall_y + 1
                # 门
                elif x == 100:
                    self.door.rect.x = wall_x
                    self.door.rect.y = wall_y - 12

                wall_x += 50
            wall_x = 0
            wall_y += 50

    # 初始化路面并放入列表和精灵组
    def setup_ground(sels, x, y, ground_number):
        ground_name = "ground_" + str(ground_number)
        ground = wall.Wall(x, y, ground_name, 1)
        # MAP.WALL_LIST.append(ground)
        MAP.WALL_S_GROUP.add(ground)

    def draw(self, surface):
        surface.fill((255, 255, 255))
        self.draw_map(surface)
        surface.blit(self.door.image, self.door.rect)
        surface.blit(self.player_.image, self.player_.rect)

    # 画路面 以及 陷阱等
    def draw_map(self, surface):
        for wall in MAP.WALL_S_GROUP:
            surface.blit(wall.image, wall.rect)

        # 渲染

# 判断关卡 并 加载资源
# def level_number(self):
# 初始化陷阱
# setup.set_up_trap()
# for name in self.map_data:
#     if self.map_data[name]['number'] == constans.LEVEL_NUMBER:
#         constans.MAP = self.map_data[name]['map']
#         constans.PLAYER_BUFF = self.map_data[name]['buff']
#         tools.modify_json('source/data/maps/memory.json', "level_number", constans.LEVEL_NUMBER)
#
#         # 读取陷阱信息
#         for trap_name in self.trap_data[name]:
#             for trap in self.trap_data[name][trap_name]:
#                 trap = str(trap)
#                 constans.TRAP_XY[trap_name].append(self.trap_data[name][trap_name][trap]['trap_xy'])
#                 print(self.trap_data[name][trap_name][trap]['trap_xy'])
#                 constans.TRAP_TRACK[trap_name].append(self.trap_data[name][trap_name][trap]['trap_track'])
#                 print(self.trap_data[name][trap_name][trap]['trap_track'])
