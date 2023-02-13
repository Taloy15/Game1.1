import pygame



class Enemy(pygame.sprite.Sprite):

    def __init__(self, pos, level):
      super().__init__()
      self.image = pygame.Surface((32, 64))
      self.image.fill('blue')
      self.rect = self.image.get_rect(topleft=pos)
      self.gravity = 0.4
      self.direction = pygame.Vector2(0, 0)
      self.speed = pygame.Vector2(4, -10)
      print("enemy spawned")
    def movement(self):
      self.speed = -3
      
    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
    

    def update(self):
      self.movement()
      self.apply_gravity()