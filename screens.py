import pygame
from settings import *
from database import *
# Start screen
def start(screen):
    title_font = pygame.font.Font(None, 80)
    title_text = title_font.render("ESCAPE THE LAB", True, (RED))
    title_rect = title_text.get_rect(center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

    begin_font = pygame.font.Font(None, 40)
    begin_text = begin_font.render("Press SPACE to Begin", True, (WHITE))
    begin_rect = begin_text.get_rect(center = (640, 450))

    screen.fill(BLACK)
    screen.blit(title_text, title_rect)
    screen.blit(begin_text, begin_rect)
    pygame.display.update()

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

# Leaderbord_screen
def leaderboard(screen):
    title_font = pygame.font.Font(None, 80)
    title_text = title_font.render("LEADERBOARD", True, (GREEN))
    title_rect = title_text.get_rect(center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 6))
    
    score_font = pygame.font.Font(None, 40)

    scores = get_highscores(7)
    screen.fill(BLACK)
    screen.blit(title_text, title_rect)

    for i, (name, score) in enumerate(scores):
        score_text = score_font.render(f"{i+1}. {name}: {score} pts", True, WHITE)
        score_rect = (SCREEN_WIDTH // 2 - 70, 300 + i * 40)
        screen.blit(score_text, score_rect)
    pygame.display.update()
    pygame.time.wait(8000) # 8 sec
       
