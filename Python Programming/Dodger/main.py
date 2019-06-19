import pygame
pygame.init()
from settings import *
from game_objects import Player, Asteroid, Bullet
from threading import Timer
import random

asteroid = Asteroid()
player = Player(asteroid)
bullets = []
objects = []
direction = 0


game_exit = False
summon = False

def new_object():
    objects.append(Asteroid())

def summon():
    pass



while not game_exit:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

            # Key events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    direction = -1

                elif event.key == pygame.K_d:
                    direction = 1

                elif event.key == pygame.K_SPACE:
                    bullets.append(Bullet(player, player.x))

            if event.type ==  pygame.KEYUP:
                if event.key == pygame.K_a:
                    direction = 0

                elif event.key == pygame.K_d:
                    direction = 0


    GAMEDISPLAY.fill(WHITE)




    player.movement(direction)
    asteroid.movement()

    for bullet in bullets:
        bullet.movement()
        if bullet.y < 0:
            del bullet

    pygame.display.update()
    CLOCK.tick(FPS)
