import pygame
import sys
from settings import *
from map import *
from player import *
from enemy import *
#Initialize pygame
pygame.init()
pygame.display.set_caption("Escape The Lab")

# Size of screen and clock
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Main method/Loop that runs the game
def main():
    flashlight = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    flashlight.set_colorkey(TRANSPARENT)
    battery = 200
    battery_text = 100
    current_level = 0
    running = True
    
    walls, exits, enemies = build_map(current_level)
    player = Player(1, 1)
    

    while running:
        clock.tick(FPS)
        enemies.update(player, walls)

        for exit_tile in exits:
        
            if player.rect.colliderect(exit_tile.rect):
                current_level += 1

                if current_level == 1:
                    walls, exits, enemies = build_map(current_level)
                    player = Player(1, 1)
                    battery = 200
                    battery_text = 100


                elif current_level == 2:
                    walls, exits, enemies = build_map(current_level)
                    player = Player(1, 1)
                    battery = 200
                    battery_text = 100


 
                elif current_level > 2:
                    win(screen)
                    running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if pygame.sprite.spritecollideany(player, enemies):
                game_over(screen)
                running = False
            battery -= 0.5
            battery_text -=0.25
            if battery <= 0:
               game_over(screen)
               running = False

        font = pygame.font.Font(None, 30)
        battery_percentage = font.render(f"Battery: {battery_text}%", True, WHITE)

        #Draws everthing on the screen
        player.manage_player(walls)
        screen.fill(BLACK)
        walls.draw(screen)
        exits.draw(screen)
        enemies.draw(screen)
        screen.blit(player.image, player.rect)

        flashlight.fill(BLACK)
        pygame.draw.circle(flashlight, (TRANSPARENT), player.rect.center, battery)
        screen.blit(flashlight, (0, 0))
        screen.blit(battery_percentage, (20, 20))
        pygame.display.update()

    # Allows pygame to close properly
    pygame.quit()
    sys.exit()

# Runs the main method
main()