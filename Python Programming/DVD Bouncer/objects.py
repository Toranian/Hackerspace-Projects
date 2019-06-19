import pygame
from settings import *


class Dvd:

    def __init__(self):
        self.size = 80
        self.speed = 2
        self.color = self.color = random.choice(VIBRANT_COLORS)

        self.x = (WIDTH / 2) - (self.size / 2)
        self.y = (HEIGHT / 2) - (self.size / 2)
        self.vx = random.choice([-self.speed, self.speed])
        self.vy = random.choice([-self.speed, self.speed])
        # self.increase = True
        # self.increase_amount = 5
        # self.square = pygame.Rect(self.x, self.y, self.size, self.size)
        # self.vx = self.speed
        # self.vy = self.speed

    def update(self):
        self.square = pygame.Rect(self.x, self.y, self.size, self.size)
        pygame.draw.rect(GAMEDISPLAY, self.color, self.square)

    def movement(self):
        self.x += self.vx
        self.y += self.vy

        self.update()

        # hit left
        if self.x <= 0:
            self.vx = self.speed
            self.color = random.choice(VIBRANT_COLORS)


        # hit right
        if self.x >= WIDTH - self.size:
            self.vx = -self.speed
            self.color = random.choice(VIBRANT_COLORS)


        # hit top
        if self.y <= 0:
            self.vy = self.speed
            self.color = random.choice(VIBRANT_COLORS)


        # hit bottom
        if self.y >= HEIGHT - self.size:
            self.vy = -self.speed
            self.color = random.choice(VIBRANT_COLORS)



        # reset size
        if self.size >= 200:
            self.increase = False
        if self.size <= 50:
            self.increase = True
