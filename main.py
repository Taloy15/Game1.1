import pygame
import sys
from settings import *
from pygame.locals import QUIT
from level import Level


pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
level = Level(level_map, screen)

pygame.display.set_caption('gekke pygame')

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.fill('black')
    level.run()

    pygame.display.update()
    clock.tick(60)
