import pygame
from settings import *


class Player:

    def __init__(self):
        self.size = 20
        self.speed = 2
        self.color = self.color = random.choice(VIBRANT_COLORS)

        self.x = (WIDTH / 2) - (self.size / 2)
        self.y = (HEIGHT / 2) - (self.size / 2)

        self.vx = 0
        self.vy = 0

        self.target_x = 0
        self.target_y = 0


    def on_click(self, target_x, target_y):
        self.target_x = target_x
        self.target_y = target_y

        self.vx = (self.target_x - self.x) / 10
        self.vy = (self.target_y - self.y) / 10

        if self.x < self.target_x:
            self.vx *= -1

        if self.y < self.target_y:
            self.vy *= -1

    def update(self):
        self.square = pygame.Rect(self.x, self.y, self.size, self.size)
        pygame.draw.rect(GAMEDISPLAY, self.color, self.square)

    def movement(self):
        self.x += self.vx
        self.y += self.vy

        self.update()

        if self.x >= self.target_x:
            self.vx = 0

        if self.y >= self.target_y:
            self.vy = 0

        if self.x <= self.target_x:
            self.vx =
