# Settings for the game
import pygame
pygame.init()
import random

TITLE = "Dodger"
WIDTH = 800
HEIGHT = 600
FPS = 60

# Define colors
WHITE = (240, 240, 240)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
VIBRANT_COLORS = (RED, GREEN, BLUE, YELLOW)
FLAT_COLORS = (WHITE, BLACK)

# RAND_COLOR = random.choice(VIBRANT_COLORS)

CLOCK = pygame.time.Clock()

GAMEDISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
