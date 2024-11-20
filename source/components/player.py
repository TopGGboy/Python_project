import json
import os

import pygame

from .. import constants
from .. import run_, setup, tools, constants as C
from . import Spirte
from ..states import level_map, level


class Player(Spirte.MySprite):
    def __init__(self, x, y, name, resize, trap_check):
        frame_rects = 0
        super().__init__(x, y, name, resize, frame_rects)

        self.setup_states()
        self.setup_velocitis()
        self.walking_time = 0

        self.trap_check = trap_check
        # self.load_images()

        # 设置速度

    # 更新玩家位置
    def update_player_position(self):
        # x方向移动
        self.rect.x += self.x_vel
        self.check_x_collision()

        # y方向移动
        self.rect.y += self.y_vel
        self.check_y_collision()

        # 陷阱启位置检测
        self.trap_check.check_trap(self.rect)

        # 人物与陷阱的碰撞检测
        # self.check_player_trap()
        # 检测是否掉出屏幕， 掉出屏幕死亡
        self.check_in_screen()
        self.check_player_trap()

        # 检测y方向是否碰撞

        # 检测是否掉出屏幕， 掉出屏幕死亡

    # 检测是否调出屏幕
    def check_in_screen(self):
        if (self.rect.x < 0 or
                self.rect.x > C.SCREEN_W or
                self.rect.y < 0 or self.rect.y > C.SCREEN_H):
            self.dead_player()

    # 检测是否碰到陷阱
    def check_player_trap(self):
        for trap in level_map.MAP.TRAP_S_GROUP:
            trap_item = pygame.sprite.collide_mask(self, trap)
            if trap_item:
                self.dead_player()
                break

    # 主角死亡
    def dead_player(self):
        print("死亡")
        self.dead = True
        self.rect.x = 1000
        self.rect.y = 1000

    # 主角复活
    def back_life_player(self):
        print("复活啦")

    # 检测x方向是否碰撞
    def check_x_collision(self):
        ground_item = pygame.sprite.spritecollideany(self, level_map.MAP.WALL_S_GROUP)
        if ground_item:
            self.adjust_player_x(ground_item)

    # 判断 x 方向 是 才能够左边还是右边 碰撞
    def adjust_player_x(self, sprite):
        if self.rect.x < sprite.rect.left:
            self.rect.right = sprite.rect.left
        else:
            self.rect.left = sprite.rect.right
        self.x_vel = 0

    def check_y_collision(self):
        ground_item = pygame.sprite.spritecollideany(self, level_map.MAP.WALL_S_GROUP)
        if ground_item:
            self.adjust_player_y(ground_item)

        # 检测是否一会会掉落
        self.check_will_fall(self)

    # 判断 y 方向 是 才能够上边还是下边 碰撞
    def adjust_player_y(self, sprite):
        # downwards
        if self.rect.bottom < sprite.rect.bottom:
            self.y_vel = 0
            self.rect.bottom = sprite.rect.top
            self.state = 'run'
        #  upwards
        else:
            self.y_vel = 7
            self.rect.top = sprite.rect.bottom
            self.state = 'fall'

    def check_will_fall(self, sprite):
        sprite.rect.y += 1
        collided = pygame.sprite.spritecollideany(sprite, level_map.MAP.WALL_S_GROUP)
        if not collided and sprite.state != "jump":
            sprite.state = "fall"
        sprite.rect.y -= 1

    def setup_velocitis(self):
        self.x_vel = 0
        self.y_vel = 0

        self.gravity = setup.PLAYER_BUFF['gravity']

    def setup_states(self):
        self.state = 'stand'
        self.face_right = True
        self.dead = False
        self.can_jump = True
        self.dead_timer = 0

    def update(self, keys):
        if self.dead == True:
            self.dead_timer = pygame.time.get_ticks()

        self.current_time = pygame.time.get_ticks()
        self.handle_states(keys)
        # 主角状态

    def handle_states(self, keys):
        # 是否可以跳跃
        self.can_jump_or_not(keys)

        if self.state == 'stand':
            self.stand_state(keys)
        if self.state == 'run':
            self.run_state(keys)
        if self.state == 'jump':
            self.jump_state(keys)
        if self.state == 'fall':
            self.fall_state(keys)

        self.update_image()

    # 更新图片
    def update_image(self):
        if self.state == 'jump':
            self.image = self.up_frames[0]
        elif self.state == 'stand':
            self.image = self.stand[0]
        elif self.state == 'run':
            if self.face_right:
                self.image = self.right_run_frames[self.frame_index]
            else:
                self.image = self.left_run_frames[self.frame_index]

    def stand_state(self, keys):
        self.frame_index = 0
        self.x_vel = 0
        self.y_vel = 0
        if keys[pygame.K_d]:
            self.state = 'run'
            self.face_right = True
            self.frames = self.right_run_frames
        elif keys[pygame.K_a]:
            self.state = 'run'
            self.face_right = False
            self.frames = self.left_run_frames

        if keys[pygame.K_SPACE] and self.can_jump:
            self.state = 'jump'
            self.y_vel = -setup.PLAYER_BUFF['tall']
            self.frames = self.up_frames

    def run_state(self, keys):
        if self.current_time - self.walking_time > 100:
            if self.frame_index < len(self.frames) - 1:
                self.frame_index += 1
            else:
                self.frame_index = 0
            self.walking_time = self.current_time

        if keys[pygame.K_d]:
            self.face_right = True
            self.x_vel = setup.PLAYER_BUFF['x_vel']
        elif keys[pygame.K_a]:
            self.face_right = False
            self.x_vel = -setup.PLAYER_BUFF['x_vel']
        else:
            self.x_vel = 0
            self.state = 'stand'

        if keys[pygame.K_SPACE] and self.can_jump:
            self.state = 'jump'
            self.y_vel = -setup.PLAYER_BUFF['tall']  # 移动时跳跃高度
            self.frames = self.up_frames

    # 主角造型

    def load_frames(self):
        sheet = setup.GRAPHIC["main"]
        # 读取玩家json文件 请确定玩家图片位置
        self.load_data()
        frame_rects = self.player_data['image_frames']

        self.right_run_frames = []
        self.left_run_frames = []
        self.up_frames = []
        self.stand = []

        for group, group_frame_rects in frame_rects.items():
            for frame_rect in group_frame_rects:
                right_image = tools.get_image(sheet, frame_rect['x'], frame_rect['y'], frame_rect['width'],
                                              frame_rect['height'], (255, 255, 255), setup.PLAYER_BUFF['measure'])
                left_image = pygame.transform.flip(right_image, True, False)
                if group == 'right_run':
                    self.right_run_frames.append(right_image)
                    self.left_run_frames.append(left_image)
                if group == 'up':
                    self.up_frames.append(right_image)
                if group == 'stand':
                    self.stand.append(right_image)

        self.frame_index = 0
        self.frames = self.stand
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()

    # 加载玩家数据
    def load_data(self):
        file_name = self.name + '.json'
        file_path = os.path.join('source/data/player', file_name)
        with open(file_path) as f:
            self.player_data = json.load(f)

    def can_jump_or_not(self, keys):
        if not keys[pygame.K_SPACE]:
            self.can_jump = True

    def jump_state(self, keys):
        self.can_jump = False
        self.y_vel += self.gravity - 0.2

        if self.y_vel >= 0:
            self.state = 'fall'

        if keys[pygame.K_a]:
            self.x_vel = -setup.PLAYER_BUFF['x_vel']
        if keys[pygame.K_d]:
            self.x_vel = setup.PLAYER_BUFF['x_vel']

        # 小跳
        if not keys[pygame.K_SPACE]:
            self.state = 'fall'

    def fall_state(self, keys):
        self.y_vel = setup.PLAYER_BUFF['gravity']

        if keys[pygame.K_a]:
            self.x_vel = -setup.PLAYER_BUFF['x_vel']
        elif keys[pygame.K_d]:
            self.x_vel = setup.PLAYER_BUFF['x_vel']
