import pygame
from tiles import Tile
from settings import TILESIZE, screen_width, screen_height
from player import Player

class Level:
  def __init__(self,level_data, surface):
    self.display_surface = surface
    self.setup_level(level_data)	#roept de setup_level functie aan
    self.world_shift = 0
    
  #creert alle sprites
  def setup_level(self, layout):
    self.tiles = pygame.sprite.Group()
    self.player = pygame.sprite.GroupSingle()
    for row_index, row in enumerate(layout): #geeft nummer aan elke regel
      for col_index,cell in enumerate(row):  #geeft nummer aan elke kolom
        x = col_index * TILESIZE
        y = row_index * TILESIZE
        if cell == 'x': 
          tile = Tile((x,y),TILESIZE)
          self.tiles.add(tile)
        if cell == 'p':
          player = Player((x,y))
          self.player.add(player)
  
 
  #laat de gameplay werken
  def run(self):
    self.tiles.update(self.world_shift)
    self.tiles.draw(self.display_surface)

    self.player.update()
    self.player.draw(self.display_surface)
    

