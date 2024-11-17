import pygame


# 自定义精灵类，继承自pygame.sprite.Sprite类
class MySprite(pygame.sprite.Sprite):
    def __init__(self, x, y, name, resize, frame_rects):
        super().__init__()
        self.name = name
        self.resize = resize

        self.frames = []
        self.frame_index = 0

        self.frame_rects = frame_rects

        # 加载精灵图像的函数
        self.load_frames()

        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
        self.center = self.rect.center
        self.timer = 0
