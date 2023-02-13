import pygame



class LUKAS(pygame.sprite.Sprite):

    def __init__(self, pos, level):
      super().__init__()
      self.image = pygame.Surface((300, 300))
      self.image.fill('blue')
      self.rect = self.image.get_rect(topleft=pos)
      self.gravity = 1.2
      self.direction = pygame.Vector2(0, 0)
      self.speed = pygame.Vector2(4, -10)
      print("Lukas spawned")
    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def movement(self):
        self.speed = -2
    
    def update(self):
      self.apply_gravity()
      self.movement()