import pygame
from settings import *

#Crating the player class
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        
        # https://opengameart.org/content/character-blue (Creator: ZackTheSpriter)
        self.image = pygame.image.load("player_blue.png")# loads player image
        self.image_scaled = pygame.transform.scale(self.image, (TILE_SIZE - 6, TILE_SIZE - 6)) # Makes it smaller to fit in tiles!
        self.rect = self.image_scaled.get_rect()
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

        
        self.rect.x += player_x
        if player_x < 0:
            flipped_image = pygame.transform.flip(self.image, True, False) # flips image on the x-axis
            self.image_scaled = pygame.transform.scale(flipped_image, (TILE_SIZE - 6, TILE_SIZE - 6)) # scales the flipped image
        elif player_x > 0:
            self.image_scaled = pygame.transform.scale(self.image, (TILE_SIZE - 6, TILE_SIZE - 6))

        # x-axis collision detection
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