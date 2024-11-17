import pygame
from source import setup, tools
from . import Spirte


class Door(Spirte.MySprite):
    def __init__(self, x, y, name, resize):
        frame_rects = [(11, 12, 51, 79)]
        super().__init__(x, y, name, resize, frame_rects)

        # 计时器
        # self.timer = 0
        # 是否通过
        self.door_finish = False

    # 判断玩家是否到达了门前 是否可以进入下一关
    def player_check_door(self, player):
        if (player.rect.left >= self.rect.left and
                player.rect.right <= self.rect.right and
                player.rect.top >= self.rect.top and
                player.rect.bottom <= self.rect.bottom):
            self.door_finish = True

    # 加载门的图片
    def load_frames(self):
        sheet = setup.GRAPHIC['main']
        for frame_rect in self.frame_rects:
            self.frames.append(tools.get_image(sheet, *frame_rect, (255, 255, 255), self.resize))

    def update(self):
        #  动态效果
        # self.current_time = pygame.time.get_ticks()
        # frame_durations = [200, 200, 200, 200]
        #
        # if self.timer == 0:
        #     self.timer = self.current_time
        # elif self.timer < self.current_time + frame_durations[self.frame_index]:
        #     self.frame_index += 1
        #     self.frame_index %= len(self.frames)
        #     self.timer = self.current_time

        self.image = self.frames[self.frame_index]
