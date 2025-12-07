import pygame
from pygame.locals import *
import random

# Initialize pygame
pygame.init()

# Set screen dimensions based on the device's resolution
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Egg Catcher")

# Load images
cloud = pygame.image.load("back_img.jpeg")
cloud = pygame.transform.scale(cloud, (screen_width, screen_height))
basket = pygame.image.load("basket.png")
basket = pygame.transform.scale(basket, (int(screen_width * 0.1), int(screen_height * 0.1)))
egg = pygame.image.load("egg.png")
egg = pygame.transform.scale(egg, (int(screen_width * 0.05), int(screen_height * 0.05)))

# Load sounds
egg_catch_sound = pygame.mixer.Sound("Sounds_egg_catched.wav")
egg_miss_sound = pygame.mixer.Sound("Sounds_egg_cracked.mp3")
game_over_sound = pygame.mixer.Sound("Sounds_game_over.wav")

# Initialize basket position, egg properties, and lives
basket_x = screen_width // 2
basket_y = screen_height - int(screen_height * 0.1)
egg_x = random.randint(0, screen_width - int(screen_width * 0.05))
egg_y = 0
egg_speed = 5
lives = 3

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT = pygame.font.SysFont(None, 30)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move basket based on input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        basket_x -= 5
    if keys[pygame.K_RIGHT]:
        basket_x += 5

    # Update egg position
    egg_y += egg_speed

    # Check collision with basket
    if egg_y + int(screen_height * 0.05) >= basket_y and \
            basket_x <= egg_x <= basket_x + int(screen_width * 0.1):
        egg_x = random.randint(0, screen_width - int(screen_width * 0.05))
        egg_y = 0
        egg_catch_sound.play()

    # Check if egg missed the basket
    if egg_y >= screen_height:
        lives -= 1
        egg_x = random.randint(0, screen_width - int(screen_width * 0.05))
        egg_y = 0
        egg_miss_sound.play()
        if lives == 0:
            game_over_sound.play()
            running = False

    # Draw everything on the screen
    screen.fill(BLACK)
    screen.blit(cloud, (0, 0))
    screen.blit(basket, (basket_x, basket_y))
    screen.blit(egg, (egg_x, egg_y))

    # Draw text
    text = FONT.render(f"Lives: {lives}", True, WHITE)
    screen.blit(text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit pygame
pygame.quit()
