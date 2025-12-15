import pygame
from settings import *

#Crating the player class
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE - 6, TILE_SIZE - 6))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x * TILE_SIZE + 3, y * TILE_SIZE + 3)

        self.speed = 3

    # Player Movment and collision detection with walls
    def manage_player(self, walls):
        keys = pygame.key.get_pressed()
        player_x, player_y = 0,0

        if keys[pygame.K_w]:
            player_y -= self.speed
        if keys[pygame.K_a]:
            player_x -= self.speed
        if keys[pygame.K_s]:
            player_y += self.speed
        if keys[pygame.K_d]:
            player_x += self.speed

        # x-axis collision detection
        self.rect.x += player_x
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if player_x > 0: self.rect.right = wall.rect.left
                if player_x < 0: self.rect.left = wall.rect.right

        # y-axis collision detection
        self.rect.y += player_y
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if player_y > 0: self.rect.bottom = wall.rect.top
                if player_y < 0: self.rect.top = wall.rect.bottom