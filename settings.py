import pygame
# All Settings for the game!
TILE_SIZE = 40

MAP_WIDTH = 32   # tiles
MAP_HEIGHT = 19 # tiles

SCREEN_WIDTH = MAP_WIDTH * TILE_SIZE
SCREEN_HEIGHT = MAP_HEIGHT * TILE_SIZE


# All Game colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 200, 0)
GREY = (40, 40, 40)
YELLOW = (255, 200, 0)
TRANSPARENT = (0, 0, 1) # this is the "transparent" color which makes the light work"

FPS = 60

#flashlight effect 


# GAME OVER screen
def game_over(screen):
    font = pygame.font.Font(None, 80)
    text = font.render("GAME OVER", True, (RED))
    rect = text.get_rect(center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

    screen.fill(BLACK)
    screen.blit(text, rect)
    pygame.display.update()
    pygame.time.wait(3000) # 3 sec

# YOU ESCAPED screen
def win(screen):
    font = pygame.font.Font(None, 80)
    text = font.render("YOU ESCAPED!", True, (GREEN))
    rect = text.get_rect(center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

    screen.fill(BLACK)
    screen.blit(text, rect)
    pygame.display.update()
    pygame.time.wait(3000) # 3 sec