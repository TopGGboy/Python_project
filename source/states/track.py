# 陷阱触发 文件
import pygame
from .. import setup
from . import level_map


# 初始化陷阱位置以及触发位置
def setup_trap_track_xy(data):
    for trap_name in data:
        for trap_number in data[trap_name]:
            print(data[trap_name][trap_number]['trap_xy'])
            setup.TRAP_XY[trap_name].append(data[trap_name][trap_number]['trap_xy'])
            setup.TRAP_TRACK[trap_name].append(data[trap_name][trap_number]['trap_track'])

    print(setup.TRAP_XY)
    print(setup.TRAP_TRACK)


# 陷阱检测
class Track:
    def __init__(self):
        # self.gear_trap_list = level.Level.TRAP_GEAR_LIST
        # self.wall_trap_lit = level.Level.GROUND_LIST
        # self.janci_trap_lit = level.Level.TRAP_JANCI_LIST

        self.wall_move = False
        self.wall_move_timer = 0

        # self.janci_number = []
        # self.janci_move_timer = 0
        # self.janci_move_flage = False

    def check_trap(self, player_rect):
        self.player_right = player_rect.right
        self.player_bottom = player_rect.bottom
        for trap_name in setup.TRAP_TRACK:
            if trap_name == 'gear_trap':
                # self.track_gear(trap_name)
                pass
            elif trap_name == 'wall_trap':
                self.track_wall(trap_name)
            elif trap_name == 'janci_trap':
                pass
                # self.track_janci(trap_name)

    def track_wall(self, trap_name):
        for trap_xy in setup.TRAP_TRACK[trap_name]:
            for wall_number in setup.TRAP_XY[trap_name]:
                way = wall_number[-1]
                if ((trap_xy[0] + 5 >= self.player_right >= trap_xy[0] - 5 and
                     trap_xy[1] - 5 <= self.player_bottom <= trap_xy[1] + 5)) or self.wall_move:
                    self.wall_move = True
                    self.wall_move_timer += 1

                    if self.wall_move_timer > 100:
                        self.wall_move = False

                    for number in wall_number:
                        for wall in level_map.MAP.WALL_S_GROUP:
                            if wall.name == "ground_" + str(number):
                                wall.wall_change_1(way)

    # def track_gear(self, trap_name):
    #     number = -1
    #     for trap_xy in self.trap[trap_name]:
    #         number += 1
    #         gear = self.gear_trap_list[number]
    #         if (trap_xy[0] + 5 >= self.player_right >= trap_xy[0] and
    #                 trap_xy[1] - 5 <= self.player_bottom <= trap_xy[1] + 5):
    #             gear.gear_1()

    # def track_janci(self, trap_name):
    #     number = -1
    #     for trap_xy in self.trap[trap_name]:
    #         number += 1
    #         if not self.janci_number:
    #             janci = self.janci_trap_lit[number]
    #         elif number in self.janci_number:
    #             janci = self.janci_trap_lit[number]
    #
    #         if ((trap_xy[0] + 5 >= self.player_right >= trap_xy[0] - 5 and
    #              trap_xy[1] - 5 <= self.player_bottom <= trap_xy[1] + 5)) or self.janci_move_flage:
    #
    #             self.janci_number.append(number)
    #             self.janci_move_timer += 1
    #             self.janci_move_flage = True
    #
    #             if (self.janci_move_timer > 100):
    #                 self.janci_move_flage = False
    #                 self.janci_number = []
    #                 if self.janci_number:
    #                     self.janci_number.remove(number)
    #
    #             janci.janci_1()
