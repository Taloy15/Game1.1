import pygame
from tiles import Tile
from settings import *
from player import Player
from enemy1 import Enemy
from player_ability import Missile
from GROTE_M import LUKAS


class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.setup_level(level_data)  # roept de setup_level functie aan
        self.world_shift = 0
        self.screen_shift = 6
        self.state = pygame.Vector2(0, 2)
        self.player_projectiles = pygame.sprite.Group()
        self.missile_onscreen = False
        self.missile_timer = 180
        self.cooldown = 0
    # creert alle sprites
    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.enemy = pygame.sprite.GroupSingle()
        self.boss = pygame.sprite.GroupSingle()
        self.bosstimer = 0
      
        
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
                if cell == 'e':
                    enemy = Enemy((x,y),self)
                    self.enemy.add(enemy)
                if cell == 'M':
                    Lukas = LUKAS((x,y), self)
                    self.boss.add(Lukas)

    def scroll_x(self):
        player = self.player.sprite
        
        player_x = player.rect.centerx
        direction_x = player.direction.x
        if player_x == (screen_width/4) and direction_x == -1:
          self.world_shift =  self.screen_shift 
          player.speed = 0
        elif player_x < (screen_width/4) and direction_x == -1:
          self.world_shift =  self.screen_shift + 1
          player.speed = -1

          
          
        elif player_x == (screen_width/2) and direction_x == 1:
          self.world_shift = -self.screen_shift
          player.speed = 0
        elif player_x > (screen_width/2) and direction_x == 1:
          self.world_shift = -self.screen_shift - 1
          player.speed = -1
          
        else:
          player.speed = 4
          self.world_shift = 0

   # def scroll_y(self):
      #  player = self.player.sprite
        
        #player_y = player.rect.centery
       # direction_y = player.direction.y
        #if player_y == (screen_height/4) and direction_y == -1:
        #  self.world_shift =  self.screen_shift 
        #  player.speed = 0
        #elif player_y < (screen_height/4) and direction_y == -1:
         # self.world_shift =  self.screen_shift + 1
          #player.speed = -1

          
          
      #  elif player_y == (screen_height/2) and direction_y == 1:
        #  self.world_shift = -self.screen_shift
       #   player.speed = 0
       # elif player_y > (screen_height/2) and direction_y == 1:
       #   self.world_shift = -self.screen_shift - 1
      #    player.speed = -1
          
       # else:
       #   player.speed = 4
         # self.world_shift = 0
  
    def x_movement_collision(self):
        player = self.player.sprite
        
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x > 0:
                    player.rect.right = sprite.rect.left 
                    player.direction.x = 0
                elif player.direction.x < 0:
                    player.rect.left = sprite.rect.right 
                    player.direction.x = 0
        
        
    def y_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()
        
        if self.player.sprite.rect.y > 750:
            pygame.quit()
            sys.exit()


        
        Ground = False
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    Ground = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
        if Ground:
          self.state.y -= 1
        else:
          self.state.y = 2

    def movement_collision_enemy(self):
        enemy = self.enemy.sprite
        enemy.apply_gravity()
        enemy.rect.x += enemy.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(enemy.rect):
              if enemy.direction.y > 0:
                    enemy.rect.bottom = sprite.rect.top
                    enemy.direction.y = 0
                    
              elif enemy.direction.y < 0:
                    sprite.rect.top = sprite.rect.bottom
                    enemy.direction.y = 0
              else: 
                enemy.direction.y = -12
                enemy.speed = 0
                  
    # def movement_collision_boss(self):
    #     Lukas = self.boss.sprite
    #     Lukas.apply_gravity()
    #     Lukas.rect.x += -2
    #     for sprite in self.tiles.sprites():
    #         if sprite.rect.colliderect(Lukas.rect):
    #           if Lukas.direction.y > 0 and self.bosstimer < 0:
    #                 Lukas.rect.bottom = sprite.rect.top
    #                 Lukas.direction.y = -20
    #                 self.bosstimer = 60
    #           elif Lukas.direction.y > 0:
    #                 Lukas.rect.bottom = sprite.rect.top
    #                 Lukas.direction.y = 0
    #           elif Lukas.direction.y < 0:
    #                 Lukas.rect.top = sprite.rect.bottom
    #                 Lukas.direction.y = 0
    #     self.bosstimer -= 1
        
  
    def player_projectile(self):
        player = self.player.sprite
        keys = pygame.key.get_pressed()
        self.cooldown -= 1
        
        if keys[pygame.K_1] and self.cooldown < 0:
          missile1 = Missile(10,10)
          missile1.rect.x = player.rect.x
          missile1.rect.y = player.rect.y
          missile1_speed = 3
          self.player_projectiles.add(missile1)
          self.missile_onscreen = True
          self.missile_timer = 180
          missile_direction = player.direction.x
          self.cooldown = 30
        if self.missile_onscreen:
          self.missile_timer -= 1
          missile1.rect.x += missile1_speed * missile_direction
        
        #HELPPPPPP!!!!!!
        #HELPPPPPP!!!!!!
          #HELPPPPPP!!!!!!
          #HELPPPPPP!!!!!!
          #HELPPPPPP!!!!!!
          #HELPPPPPP!!!!!!
          #HELPPPPPP!!!!!!
          #HELPPPPPP!!!!!!
          #HELPPPPPP!!!!!!
    def collision(self):
        self.x_movement_collision()
        self.y_movement_collision()
        self.movement_collision_enemy()
        #self.movement_collision_boss()
    # laat de gameplay werken

    def run(self, running):
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.scroll_x()
        self.enemy.update()
        
                

        
        self.player_projectile()
        
        self.player.update()
        self.collision()
         
        
        self.player.draw(self.display_surface)
        self.enemy.draw(self.display_surface)
        self.boss.draw(self.display_surface)
        
        self.player_projectiles.draw(self.display_surface)
        