import pygame
from pygame.locals import *
import time
import random

# Screen initialize
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((1080, 800))
pygame.display.set_caption("Egg Catcher")

# Load images
cloud = pygame.image.load("back_img.jpeg")
cloud = pygame.transform.scale(cloud, (1080, 800))
basket = pygame.image.load("basket.png")
basket = pygame.transform.scale(basket, (80, 80))
egg = pygame.image.load("egg.png")
egg = pygame.transform.scale(egg, (35, 35))
clock = pygame.time.Clock()

# Load sounds
egg_catch_sound = pygame.mixer.Sound("Sounds_egg_catched.wav")
egg_miss_sound = pygame.mixer.Sound("Sounds_egg_cracked.mp3")
game_over_sound = pygame.mixer.Sound("Sounds_game_over.wav")

# Initialize basket position, egg properties, and lives
x = 260
y = 500
egg_x = random.randint(50, 550)
egg_y = 20
egg_speed = 5
lives = 3  # Initialize lives to 3
level = 1  # Initialize level to 1

# Movement of basket
xchange = 0
exiting = False
game_over = False

score = 0

font = pygame.font.Font(None, 45)

# Define levels with increasing difficulty
levels = {
    1: {"egg_speed": 5, "egg_interval": 2500},
    2: {"egg_speed": 6, "egg_interval": 2000},
    3: {"egg_speed": 7, "egg_interval": 1500},
    4: {"egg_speed": 9, "egg_interval": 1200},
    5: {"egg_speed": 12, "egg_interval": 1000},
}

def game_over_screen():
    screen.blit(cloud, (0, 0))
    game_over_text = font.render("GAME OVER", True, (0,0,0))  # Change color to black
    screen.blit(game_over_text, (450, 350))
    score_text = font.render("SCORE: " + str(score), True, (0, 0, 0))  # Change color to black
    screen.blit(score_text, (450, 400))
    resume_text = font.render("Press SPACE to Play Again", True, (0, 0, 0))  # Change color to black
    screen.blit(resume_text, (350, 450))

def draw_lives(lives):
    lives_text = font.render("Lives: " + str(lives), True, (255, 255, 255))
    screen.blit(lives_text, (10, 50))

def draw_level(level):
    level_text = font.render("Level: " + str(level), True, (255, 255, 255))
    screen.blit(level_text, (10, 90))

# Load and play background music
pygame.mixer.music.load("bgsound.mp3")
pygame.mixer.music.play(-1)  # -1 loops the music indefinitely

while not exiting:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exiting = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                xchange = -5
            elif event.key == pygame.K_RIGHT:
                xchange = 5
            elif event.key == pygame.K_SPACE and game_over:
                # Restart the game
                egg_x = random.randint(50, 550)
                egg_y = 20
                score = 0
                lives = 3  # Reset lives to 3
                level = 1  # Reset level to 1
                game_over = False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                xchange = 0

    if not game_over:
        # Update basket position
        x += xchange

        # Set level properties
        egg_speed = levels[level]["egg_speed"]
        egg_interval = levels[level]["egg_interval"]

        # Clear the screen
        screen.blit(cloud, (0, 0))

        # Draw basket
        screen.blit(basket, (x, y))

        # Draw egg
        screen.blit(egg, (egg_x, egg_y))

        # Update egg position
        egg_y += egg_speed

        # Check collision with basket
        if (x <= egg_x <= x + 80) and (y <= egg_y <= y + 80):
            # Collision detected
            score += 1
            egg_x = random.randint(50, 550)
            egg_y = 20
            egg_catch_sound.play()

        # Draw score
        score_text = font.render("Score: " + str(score), True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        
        # Check if egg missed the basket
        if egg_y >= 800:
            lives -= 1  # Decrease lives if egg missed
            egg_x = random.randint(50, 550)
            egg_y = 20
            egg_miss_sound.play()
            if lives == 0:
                game_over = True
                game_over_sound.play()

        # Draw lives
        draw_lives(lives)

        # Draw level
        draw_level(level)

        # Check if score is a multiple of 50 to increase level
        if score % 50 == 0 and score != 0:
            if level < 5:
                level += 1

    else:
        game_over_screen()

    # Update the display
    pygame.display.update()

    # Limit frame rate
    clock.tick(60)

pygame.quit()
