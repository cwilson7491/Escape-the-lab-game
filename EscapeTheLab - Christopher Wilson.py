import pygame
import sys
from settings import *
from map import *
from player import *
from enemy import *
from database import *
from screens import *
#Initialize pygame
pygame.init()
pygame.display.set_caption("Escape The Lab")

# Size of screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Main method/Loop that runs the game
def main():
    init_database() #Initalizes the database
    score = 500

    #Loop that shows only start screen unitl spacebar is pressed
    start_screen = True
    while start_screen:
        start(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:   # starts the game!
                if event.key == pygame.K_SPACE:
                    start_screen = False

    # "Flashlight effect"
    flashlight = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    flashlight.set_colorkey(TRANSPARENT)
    battery = 200 # how big the circle is
    battery_text = 100
    current_level = 2
    running = True
    
    # Builds the first level
    walls, exits, enemies = build_map(current_level)
    player = Player(1, 1)
    

    while running:
        clock.tick(FPS) # Game runs at 60 FPS
        enemies.update(player, walls)

        #For exit tiles to go to next level & win!
        for exit_tile in exits:
        
            if player.rect.colliderect(exit_tile.rect):
                current_level += 1

                # Level 2
                if current_level == 1:
                    walls, exits, enemies = build_map(current_level)
                    player = Player(1, 1)
                    battery = 200
                    battery_text = 100
                    score += 600
                    break
                
                # Level 3
                elif current_level == 2:
                    walls, exits, enemies = build_map(current_level)
                    player = Player(1, 1)
                    battery = 200
                    battery_text = 100
                    score += 700
                    break

                # Save score and shows win & leaderboard screens!
                elif current_level == 3:
                    save_scores("CHRIS", score)
                    win(screen)
                    leaderboard(screen)
                    running = False
                    break

        # This make the game window acttually close when you press X 
        # and lose when you collide with an enemy or "battery" runs out!
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if pygame.sprite.spritecollideany(player, enemies):
                game_over(screen)
                running = False
            battery -= 0.5 # battery drain
            score -=0.5 #score drain
            battery_text -=0.25 # battery percentage
            if battery <= 0:
               game_over(screen)
               running = False
        
        # Shows battery percentage
        font = pygame.font.Font(None, 30)
        battery_percentage = font.render(f"Battery: {battery_text}%", True, WHITE)

        #Draws everthing on the screen
        player.manage_player(walls)
        screen.fill(BLACK)
        walls.draw(screen)
        exits.draw(screen)
        enemies.draw(screen)
        screen.blit(player.image_scaled, player.rect)

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