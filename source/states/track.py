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

        self.gear_move = False
        self.gear_move_timer = 0

        self.spine_move = False
        self.spine_move_timer = 0

        # self.janci_number = []
        # self.janci_move_timer = 0
        # self.janci_move_flage = False

    def check_trap(self, player_rect):
        self.player_right = player_rect.right
        self.player_bottom = player_rect.bottom
        for trap_name in setup.TRAP_TRACK:
            if trap_name == 'gear_trap':
                self.track_gear()
            elif trap_name == 'wall_trap':
                self.track_wall()
            elif trap_name == 'spine_trap':
                self.track_spine()

    def track_spine(self):
        trap_number = 0
        for trap_xy in setup.TRAP_TRACK['spine_trap']:
            resize = trap_xy[-1]
            for spine in level_map.MAP.TRAP_S_GROUP:
                if spine.name == "spine_" + str(trap_number):

                    trap_number += 1
                    if ((trap_xy[0] + 5 >= self.player_right >= trap_xy[0] - 5 and
                         trap_xy[1] - 5 <= self.player_bottom <= trap_xy[1] + 5)) or self.spine_move:

                        self.spine_move = True
                        self.spine_move_timer += 1

                        if self.spine_move_timer > 100:
                            self.spine_move = False
                        else:
                            spine.spine_change_1()

    def track_gear(self):
        trap_number = 0
        for trap_xy in setup.TRAP_TRACK['gear_trap']:
            resize = trap_xy[-1]
            for gear in level_map.MAP.TRAP_S_GROUP:
                if gear.name == "gear_" + str(trap_number):

                    trap_number += 1
                    if (trap_xy[0] + 5 >= self.player_right >= trap_xy[0] and
                        trap_xy[1] - 5 <= self.player_bottom <= trap_xy[1] + 5) or self.gear_move:

                        self.gear_move = True
                        self.gear_move_timer += 1

                        if self.gear_move_timer > 800:
                            self.gear_move = False
                        else:
                            gear.gear_change_1(resize)

    def track_wall(self):
        for trap_xy in setup.TRAP_TRACK['wall_trap']:
            for wall_number in setup.TRAP_XY['wall_trap']:
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
