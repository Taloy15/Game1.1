import pygame
from tiles import Tile
from settings import TILESIZE, screen_width, screen_height
from player import Player

class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.setup_level(level_data)  # roept de setup_level functie aan
        self.world_shift = 0

    # creert alle sprites
    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        for row_index, row in enumerate(layout):  # geeft nummer aan elke regel
            # geeft nummer aan elke kolom
            for col_index, cell in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if cell == 'x':
                    tile = Tile((x, y), TILESIZE)
                    self.tiles.add(tile)
                if cell == 'p':
                    player = Player((x, y),self)
                    self.player.add(player)

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x
        if player_x < (screen_width/4) and direction_x == -1:
            self.world_shift = 8
            player.speed = 0
        elif player_x > (screen_width*0.75) and direction_x == 1:
            self.world_shift = -8
            player.speed = 0
        else:
            player.speed = 20
            self.world_shift = 0

    def x_movement_collision(self):
        player = self.player.sprite

        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x > 0:
                    player.rect.right = sprite.rect.left - 1
                    player.direction.x = 0
                elif player.direction.x < 0:
                    player.rect.left = sprite.rect.right + 1
                    player.direction.x = 0

    def y_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    ground = 1
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    ground = 0

    def collision(self):
        self.x_movement_collision()
        self.y_movement_collision()

    # laat de gameplay werken

    def run(self):
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.scroll_x()

        self.player.update()
        self.collision()
        self.player.draw(self.display_surface)
