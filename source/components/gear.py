# 齿轮
import pygame

from . import Spirte
from .. import setup, tools


class Gear(Spirte.MySprite):
    def __init__(self, x, y, name, resize):  # resize = 1
        frame_rects = [(72, 8, 50, 50), (128, 8, 50, 50), (189, 8, 50, 50), (251, 8, 50, 50)]
        super().__init__(x, y, name, resize, frame_rects)
        self.frames_rects = frame_rects

        # 加载墙面的图片

    def load_frames(self):
        self.sheet = setup.GRAPHIC['main']
        for frame_rect in self.frame_rects:
            image = tools.get_image(self.sheet, *frame_rect, (255, 255, 255), self.resize)
            ground_image = pygame.transform.scale(image, (50, 52))
            self.frames.append(ground_image)

    def gear_change_1(self, resize):
        frames = []
        for frame_rect in self.frame_rects:
            frames.append(tools.get_image(self.sheet, *frame_rect, (255, 255, 255), resize))
        self.frames = frames
        # 改变完尺寸后得重新放入精灵族

        self.image = self.frames[0]
        self.rect = self.image.get_rect()
        self.rect.center = self.center

    def update(self):
        self.current_time = pygame.time.get_ticks()
        frame_durations = [200, 200, 200, 200]

        if self.timer == 0:
            self.timer = self.current_time
        elif self.current_time - self.timer > frame_durations[self.frame_index]:
            self.frame_index += 1
            self.frame_index %= len(frame_durations)
            self.timer = self.current_time

        self.image = self.frames[self.frame_index]
