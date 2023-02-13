import pygame


class Missile(pygame.sprite.Sprite):

    def __init__(self, height, width):
      super().__init__()
      self.image = pygame.Surface((10, 10))
      self.image.fill('blue')
      self.rect = self.image.get_rect()
      
      

    def movement(self):
      self.speed = 3 
    def update(self):
      self.movement()
#werkt bijna
