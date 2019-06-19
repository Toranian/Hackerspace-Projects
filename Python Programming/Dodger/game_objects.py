import pygame; pygame.init()
from settings import *
import random

class Player:

    def __init__(self, obstacle):
        self.object = obstacle

        self.size = 20
        self.speed = 6
        self.color = BLACK
        self.x = (WIDTH / 2) - (self.size / 2)
        self.y = (HEIGHT - 30) - (self.size / 2)
        self.square = pygame.Rect(self.x, self.y, self.size, self.size)
        self.direction = 1

    def update(self):
        self.square = pygame.Rect(self.x, self.y, self.size, self.size)
        pygame.draw.rect(GAMEDISPLAY, self.color, self.square)

    def movement(self, direction):
        self.direction = direction
        self.x += self.speed * self.direction
        self.update()

        if self.x < 0:
            self.x = WIDTH
        elif self.x > WIDTH:
            self.x = 0

    def stop(self):
        self.direction = 0


class Asteroid:

    def __init__(self):
        self.size = random.randint(25, 50)
        self.speed = random.uniform(1, 5)
        self.x = random.randint(1, WIDTH)
        self.y = -self.size
        self.square = pygame.Rect(self.x, self.y, self.size, self.size)

        if self.speed >= 2.5:
            self.color = RED

        else:
            self.color = GREEN

    def update(self):
        self.square = pygame.Rect(self.x, self.y, self.size, self.size)
        pygame.draw.rect(GAMEDISPLAY, self.color, self.square)

    def movement(self):
        self.update()
        self.y += self.speed

        if self.y <= 0:
            self.reset()

    def reset(self):
        self.size = random.randint(25, 50)
        self.speed = random.uniform(1, 5)
        self.x = random.randint(1, WIDTH)
        self.y = -self.size

        if self.speed >= 2.5:
            self.color = RED

        else:
            self.color = GREEN


class Bullet:

    def __init__(self, player, x):
        self.player = player

        self.width = 7
        self.height = 15
        self.color = BLACK
        self.y = (HEIGHT - 40)
        self.x = self.player.x + self.width
        self.speed = -7


    def update(self):
        self.square = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(GAMEDISPLAY, self.color, self.square)

    def movement(self):
        self.y += self.speed
        self.update()
