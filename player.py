import pygame




class Player(pygame.sprite.Sprite):

    def __init__(self, pos, level):
        super().__init__()
        self.image = pygame.Surface((32, 64))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft=pos)
        self.level = level 
        self.timer = 15
        # movement
        self.cooldown1 = 0
        self.cooldown2 = 0
        self.speed = pygame.Vector2(4, -10)
        self.direction = pygame.Vector2(0, 0)
        self.gravity = 0.4
        self.jump_speed = -10
        
    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]:
          self.direction.x = 0
          self.speed = 4
        elif keys[pygame.K_RIGHT]:
          self.direction.x = 1
          if self.speed < 6:
            self.speed += 0.1
        elif keys[pygame.K_LEFT]:
          self.direction.x = -1
          if self.speed < 6:
            self.speed += 0.1
        else:
          self.direction.x = 0
          self.speed = 4
      
        if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
          self.jump()
        if keys[pygame.K_d] and self.cooldown1 <= 0:
          self.dash()
          print("DASH")
        self.cooldown1 -= 1
        if keys[pygame.K_t] and self.cooldown2 <= 0:
          self.teleport()
          print("TELEPORT")
        self.cooldown2 -= 1
       
        
          
          
          
    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        state = self.level.state
        if state.y == 1:
          self.direction.y = -12
        elif state.y <= 0:
          self.direction.y = -8

    def dash(self):
        self.timer -= 1
        self.speed = 15
        self.direction.y = -10 + (self.timer/3)
        if self.timer <= 0:
          self.cooldown1 = 300
        if self.timer <= 0:
          self.speed = 4
          self.timer = 15

    
    def teleport(self):
        self.rect.x += 200 * self.direction.x
        self.cooldown2 = 300
        
    

      
    
    def update(self):
        self.get_input()
        

