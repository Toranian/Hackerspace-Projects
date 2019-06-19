import pygame
from objects import *
from settings import *

player = Player()
object = Object(10, 10)

game_exit = False

while not game_exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_exit = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            player.on_click(mouse_x, mouse_y)
            print(player.x, player.y)
            print(mouse_x, mouse_y)

    GAMEDISPLAY.fill(BLACK)
    player.movement()
    player.update()

    pygame.display.update()
    CLOCK.tick(FPS)

pygame.quit()
quit()
