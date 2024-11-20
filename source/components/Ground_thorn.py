# 地刺陷阱
import pygame

from . import Spirte
from .. import tools, setup


class ground_thron(Spirte.MySprite):
    def __init__(self, x, y, name, resize, way):
        frame_rects = [(75, 63, 50, 35)]
        super().__init__(x, y, name, resize, frame_rects)
        self.way = way

    # 加载地刺陷阱 图像
    def load_frames(self):
        sheet = setup.GRAPHIC['main']
        for frame_rect in self.frame_rects:
            self.frames.append(tools.get_image(sheet, *frame_rect, (255, 255, 255), self.resize))

    def image_rotate(self):
        if self.way == "up":
            pass
        elif self.way == 'down':
            self.image = pygame.transform.rotate(self.image, 180)
        elif self.way == 'left':
            self.image = pygame.transform.rotate(self.image, 90)
        elif self.way == 'right':
            self.image = pygame.transform.rotate(self.image, -90)

    def update(self):
        # 动态效果
        # self.current_time = pygame.time.get_ticks()
        # frame_durations = [200, 200, 200, 200]
        #
        # if self.timer == 0:
        #     self.timer = self.current_time
        # elif self.timer - self.current_time > frame_durations[self.frame_index]:
        #     self.frame_index += 1
        #     self.frame_index %= len(frame_durations)
        #     self.timer = self.current_time

        self.image = self.frames[self.frame_index]
        self.image_rotate()
