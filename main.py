import pygame
import sys
from settings import *
from pygame.locals import QUIT
from level import Level

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
level = Level(level_map, screen)

pygame.display.set_caption('shitty ass game waar iedere line 5 uur aan bugfixing nodig heeft en niks standaard is want alles is kut help help help')


while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.fill('black')
    level.run(running,)
  

    pygame.display.update()
    clock.tick(60)
