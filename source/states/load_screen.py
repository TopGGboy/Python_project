import pygame
from ..components import info


class LoadScreen:
    def __init__(self):
        self.finished = False
        self.next = 'level'
        self.timer = 0
        self.info = info.Info()

    def update(self, surface, keys):
        self.draw(surface)
        if self.timer == 0:
            # 获取当前时间（以毫秒为单位）并设置为计时器的初始值
            self.timer = pygame.time.get_ticks()
        # 如果从计时器开始计时到现在已经超过2000毫秒（2秒）
        elif pygame.time.get_ticks() - self.timer > 2000:
            self.finished = True
            self.timer = 0

    # 渲染
    def draw(self, surface):
        surface.fill((0, 0, 0))
        self.info.draw(surface)
