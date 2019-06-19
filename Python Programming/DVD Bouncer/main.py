import pygame
from objects import Dvd
from settings import *

dvd = Dvd()

game_exit = False

while not game_exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_exit = True

    GAMEDISPLAY.fill(BLACK)
    dvd.movement()
    dvd.update()

    pygame.display.update()
    CLOCK.tick(FPS)

pygame.quit()
quit()
