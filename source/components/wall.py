import pygame

from . import Spirte
from .. import setup, tools


class Wall(Spirte.MySprite):
    def __init__(self, x, y, name, resize):  # resize = 1
        frame_rects = [(746, 9, 50, 50)]
        super().__init__(x, y, name, resize, frame_rects)

        # 加载墙面的图片

    def load_frames(self):
        sheet = setup.GRAPHIC['main']
        for frame_rect in self.frame_rects:
            image = tools.get_image(sheet, *frame_rect, (255, 255, 255), self.resize)
            ground_image = pygame.transform.scale(image, (50, 52))
            self.frames.append(ground_image)

    def update(self):
        self.image = self.frames[self.frame_index]
