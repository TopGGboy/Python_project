import pygame.sprite

from .. import setup
from ..components import wall, gear, Ground_thorn, spine
from . import level


class MAP:
    # 墙壁精灵族
    WALL_S_GROUP = pygame.sprite.Group()
    # 陷阱精灵族
    TRAP_S_GROUP = pygame.sprite.Group()

    # # 墙壁列表
    # WALL_LIST = []

    def __init__(self, player_, door):
        MAP.WALL_S_GROUP = pygame.sprite.Group()
        MAP.TRAP_S_GROUP = pygame.sprite.Group()
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

        self.load_trap()

    # 加载陷阱
    def load_trap(self):
        trap_number = 0
        for trap_xy in setup.TRAP_XY['gear_trap']:
            self.setup_trap(name='gear_trap', x=trap_xy[0], y=trap_xy[1], resize=trap_xy[2],
                            trap_number=trap_number)
            trap_number += 1

        trap_number = 0
        for trap_xy in setup.TRAP_XY['Ground_thorn_trap']:
            self.setup_trap(name='Ground_thorn_trap', x=trap_xy[0], y=trap_xy[1], resize=trap_xy[2],
                            way=trap_xy[-1], trap_number=trap_number)
            trap_number += 1
        trap_number = 0
        for trap_xy in setup.TRAP_XY['spine_trap']:
            self.setup_trap(name='spine_trap', x=trap_xy[0], y=trap_xy[1], resize=trap_xy[2],
                            way=trap_xy[-1], trap_number=trap_number)
            trap_number += 1

    # 初始化 陷阱 并放入列表和精灵组
    def setup_trap(self, name, x, y, resize, trap_number, way=None):
        if name == 'gear_trap':
            gear_trap_name = "gear_" + str(trap_number)
            gear_trap = gear.Gear(x, y, gear_trap_name, resize)
            MAP.TRAP_S_GROUP.add(gear_trap)
        elif name == 'Ground_thorn_trap':
            ground_thorn_trap_name = "Ground_thorn_" + str(trap_number)
            ground_thorn_trap = Ground_thorn.ground_thron(x, y, ground_thorn_trap_name, resize, way)
            MAP.TRAP_S_GROUP.add(ground_thorn_trap)
        elif name == 'spine_trap':
            spine_trap_name = "spine_" + str(trap_number)
            spine_trap = spine.Spine(x, y, spine_trap_name, resize, way)
            MAP.TRAP_S_GROUP.add(spine_trap)

    # 初始化路面并放入列表和精灵组
    def setup_ground(sels, x, y, ground_number):
        ground_name = "ground_" + str(ground_number)
        ground = wall.Wall(x, y, ground_name, 1)
        MAP.WALL_S_GROUP.add(ground)

    def draw(self, surface):
        surface.fill((255, 255, 255))
        self.draw_map(surface)
        surface.blit(self.door.image, self.door.rect)
        surface.blit(self.player_.image, self.player_.rect)

    # 画路面 以及 陷阱等
    def draw_map(self, surface):
        for wall in MAP.WALL_S_GROUP:
            wall.update()
            surface.blit(wall.image, wall.rect)
        for trap in MAP.TRAP_S_GROUP:
            trap.update()
            surface.blit(trap.image, trap.rect)
