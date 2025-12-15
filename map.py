import pygame
from settings import *
from enemy import *
# Map layouts
level_1 = [
    "1111111111111111111111111",
    "1000000000000000000000001",
    "1011111011111111110111101",
    "1010001010000000010000101",
    "1010111010111111011110101",
    "10100000100000X0000000101",
    "1011111011111111110111101",
    "1000000000000000000000001",
    "1011111111101111111111101",
    "1010000000101000000000101",
    "1010111110101011111110101",
    "1010X0000010100000X000101",
    "1010111111101111111110101",
    "1000000000000000000000EE1",
    "1111111111111111111111111"


]

level_2 = [
    "11111111111111111111111111111111",
    "10000000001111110000000000000001",
    "10011111101000010111111111111001",
    "100100X0101000010000000000001001",
    "10000000101111111111111111101001",
    "1001000010000X000000000000101001",
    "10111111111111111111100000101001",
    "10000000000000000000100000101001",
    "10000000001111111111100000101001",
    "11111111001000000000000000101001",
    "10000000001000000000000000001EE1",
    "10000000001000001111111111111111",
    "1011111110100X001000000000000001",
    "10100000001000001000000000000001",
    "10101111111000001111111111111001",
    "10000000000000000000000000000001",
    "11111111111111111111111111111111"
]

level_3 = [
    "11111111111111111111111111111111",
    "10000000000011111111110000000001",
    "10111111111010000000010111111101",
    "10100000000010111111010100000101",
    "10101111101110100001010101110101",
    "1010100X0010101011X10100X1000101",
    "10101011101010101001010101111101",
    "10101000001000101000010100000001",
    "10101111111111101111110111111111",
    "1X000000000000001000000000000001",
    "11111111111111001111111111111001",
    "10000000000001000000000000000001",
    "10111111111101011111111111111001",
    "10100000000001100000000X00010001",
    "10101111111111010111111111101001",
    "111100010001000100000001X0000001",
    "10000100010001011111110100000001",
    "10011111111111000000000000000001",
    "1EE11111111111111111111111111111"
]

levels = [level_1, level_2, level_3]

# Returns the strings to Single Charaters in a list for each level
def load_map(level_index):
    return[list(row) for row in levels[level_index]]

# Creates the Wall Class
class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(GREY)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x * TILE_SIZE, y * TILE_SIZE)
# Creates exit class
class ExitTile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(GREEN)  # green exit
        self.rect = self.image.get_rect()
        self.rect.topleft = (x * TILE_SIZE, y * TILE_SIZE)

# Builds all the walls (1), open tiles (0), and Exits (E) which creates the map!
def build_map(level_index):
    walls = pygame.sprite.Group()
    exits = pygame.sprite.Group()
    enemies = pygame.sprite.Group()

    for y, row in enumerate(load_map(level_index)):
        for x, tile in enumerate(row):
            if tile == "1":
                walls.add(Wall(x, y))
            elif tile == "E":
                exits.add(ExitTile(x, y))
            elif tile == "X":
                enemies.add(Enemy(x, y))

            
    return walls, exits, enemies