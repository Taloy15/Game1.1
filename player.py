import pygame



class Player(pygame.sprite.Sprite):

    def __init__(self, pos, level):
        super().__init__()
        self.image = pygame.Surface((32, 64))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft=pos)
        self.level = level 

        # movement
        self.speed = 5
        self.direction = pygame.Vector2(0, 0)
        self.gravity = 0.4
        self.jump_speed = -10

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]:
          self.direction.x = 0
        elif keys[pygame.K_RIGHT]:
          self.direction.x = 1
        
        elif keys[pygame.K_LEFT]:
          self.direction.x = -1
        else:
          self.direction.x = 0
        if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
          self.jump()

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
      self.rect.y += 1
      for tile in self.level.tiles: 
        if self.rect.colliderect(tile.rect):
          self.direction.y = self.jump_speed
      self.rect.y -= 1
      self.rect.x += 1
      for tile in self.level.tiles: 
        if self.rect.colliderect(tile.rect):
          self.direction.y = self.jump_speed
      self.rect. x -= 1
      self.rect.x -= 1
      for tile in self.level.tiles: 
        if self.rect.colliderect(tile.rect):
          self.direction.y = self.jump_speed
      self.rect.x += 1

    def update(self):
        self.get_input()

