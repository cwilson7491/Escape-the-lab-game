import pygame
from settings import *
from pygame.math import Vector2

# Creating the enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        # https://opengameart.org/content/scientist-0 (Creator: Min)
        self.enemy_image = pygame.image.load("Enemy_Skeleton.png")# loads enemy image
        self.image = pygame.transform.scale(self.enemy_image, (TILE_SIZE - 8, TILE_SIZE - 8)) # Makes it smaller to fit in tiles!
        self.rect = self.image.get_rect()
        self.rect.topleft = (x * TILE_SIZE + 3, y * TILE_SIZE + 3)

        self.speed = 1
    
    #Gets the position and direction the enemy has to go to reach the player
    def update(self, player, walls):
        enemy_pos = Vector2(self.rect.center)
        player_pos = Vector2(player.rect.center)
        direction = player_pos - enemy_pos

        if direction.length() > 0:
            direction.normalize_ip() # Makes the enemy move at a the same speed in the right direction

            move_amount = direction * self.speed
            move_x = move_amount.x
            move_y = move_amount.y

            # x-axis collision detection
            self.rect.x += move_x
            for wall in walls:
                if self.rect.colliderect(wall.rect):
                    if move_x > 0: 
                        self.rect.right = wall.rect.left
                    if move_x < 0: 
                        self.rect.left = wall.rect.right

            # y-axis collision detection
            self.rect.y += move_y
            for wall in walls:
                if self.rect.colliderect(wall.rect):
                    if move_y > 0: 
                        self.rect.bottom = wall.rect.top
                    if move_y < 0: 
                        self.rect.top = wall.rect.bottom