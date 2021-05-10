import pygame
import os
from math import atan, degrees
import random

pipe_image = "pipe.png"
bottom_pipe = pygame.transform.scale2x(pygame.image.load(os.path.join("images", pipe_image)))
top_pipe = pygame.transform.rotate(bottom_pipe, 180)

class Bird():
    allowed_keys = {}
    new_jump = False
    jump_velocity = 0
    g = 750
    BIRD_SIZE = (41, 29)
    BIRD_POS = (100, 400)

    def __init__(self, image, xy):
        self.x = xy[0]
        self.y = xy[1]
        self.surface = pygame.image.load(os.path.join("images", image)).convert_alpha()
        self.surface = pygame.transform.scale(self.surface, self.BIRD_SIZE)
        self.rect = self.surface.get_rect(center=self.BIRD_POS)

    def draw(self, win):
        self.update_shape()
        win.blit(self.surface_temp, self.rect)

    def update_shape(self):
        self.surface_temp = pygame.transform.rotozoom(self.surface, -degrees(atan(self.jump_velocity/100)), 1)

    def jump(self, dt):
        if self.new_jump:
            self.jump_velocity = -500
            self.is_jump = True
            self.init_y = self.y
        k = 1000
        self.jump_velocity += dt/k * self.g
        self.y += self.jump_velocity * dt/k + 1/2 * self.g * (dt/k)**2
        self.rect.centery = self.y
        self.new_jump = False

class Surface():
    def __init__(self, image, xy):
        self.surface = pygame.image.load(os.path.join("images", image))
        self.x = xy[0]
        self.y = xy[1]

    def draw(self, win):
        screen_size = win.get_size()
        image_size = self.surface.get_size()

        if self.x <= screen_size[0] - image_size[0]:
            self.x = 0

        win.blit(self.surface, (self.x, self.y))

    def move_right(self,v=1):
        self.x += v

    def move_left(self, v=1):
        self.x -= v

class PipePair():
    remove = False
    def __init__(self):
        self.x = 576
        self.y = random.randint(200, 600)
        self.bottom_pipe_rect = bottom_pipe.get_rect(topleft=(self.x, self.y))
        self.top_pipe_rect = top_pipe.get_rect(bottomleft=(self.x, self.y - 150))

    def draw(self, win):
        win.blit(bottom_pipe, self.bottom_pipe_rect)
        win.blit(top_pipe, self.top_pipe_rect)

    def move_right(self, v=1):
        self.bottom_pipe_rect.centerx += v
        self.top_pipe_rect -= v

    def move_left(self, v=1):
        self.bottom_pipe_rect.centerx -= v
        self.top_pipe_rect.centerx -= v
        if self.bottom_pipe_rect.topright[0] < 0: self.remove = True



