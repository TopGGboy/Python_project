import pygame

from . import Spirte
from .. import setup, tools


class Spine(Spirte.MySprite):
    def __init__(self, x, y, name, resize, way):  # resize = 1
        frame_rects = [(10, 197, 19, 61)]
        self.way = way
        super().__init__(x, y, name, resize, frame_rects)

    # 加载尖刺的图片
    def load_frames(self):
        self.sheet = setup.GRAPHIC['main']
        for frame_rect in self.frame_rects:
            self.frames.append(tools.get_image(self.sheet, *frame_rect, (255, 255, 255), self.resize))

    def spine_change_1(self):
        speed = 10
        if self.way == 'up':
            self.rect.y -= speed
        elif self.way == 'down':
            self.rect.y += speed
        elif self.way == 'left':
            self.rect.x -= speed
        elif self.way == 'right':
            self.rect.x += speed

    def image_rotate(self):
        if self.way == 'up':
            pass
        elif self.way == 'down':
            self.image = pygame.transform.rotate(self.image, 180)
        elif self.way == 'left':
            self.image = pygame.transform.rotate(self.image, 90)
        elif self.way == 'right':
            self.image = pygame.transform.rotate(self.image, -90)

    def update(self):
        # self.current_time = pygame.time.get_ticks()
        # frame_durations = [200, 200, 200, 200]
        #
        # if self.timer == 0:
        #     self.timer = self.current_time
        # elif self.current_time - self.timer > frame_durations[self.frame_index]:
        #     self.frame_index += 1
        #     self.frame_index %= len(frame_durations)
        #     self.timer = self.current_time

        self.image = self.frames[self.frame_index]
        self.image_rotate()
