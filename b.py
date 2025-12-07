import pygame
import sys
import random
from math import radians, sin, cos

# Initialize Pygame
pygame.init()

# Constants
WIDTH = 2500
HEIGHT = 1200
MARGIN = 100
LOWER_BOUND = 100
WHITE = (230, 230, 230)
LIGHT_BLUE = (174, 214, 241)
RED = (231, 76, 60)
LIGHT_GREEN = (25, 111, 61)
DARK_GRAY = (40, 55, 71)

# Load background image
background_img = pygame.image.load("background.jpg")
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

# Load balloon images
balloon_images = [pygame.image.load(f"balloon_{i}.png") for i in range(1, 7)]

# Initialize display
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Balloon Shooter")
clock = pygame.time.Clock()

# Font
font = pygame.font.Font("Roboto-Bold.ttf", 40)

# Balloon Class
class Balloon:
    def __init__(self, speed):
        self.image = random.choice(balloon_images)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(MARGIN, WIDTH - self.rect.width - MARGIN)
        self.rect.y = HEIGHT - LOWER_BOUND
        self.angle = 90
        self.speed = -speed
        self.probPool = [-1, -1, -1, 0, 0, 0, 0, 1, 1, 1]

    def move(self):
        direct = random.choice(self.probPool)

        if direct == -1:
            self.angle += -10
        elif direct == 1:
            self.angle += 10

        self.rect.y += self.speed * sin(radians(self.angle))
        self.rect.x += self.speed * cos(radians(self.angle))

        if (self.rect.x + self.rect.width > WIDTH) or (self.rect.x < 0):
            if self.rect.y > HEIGHT / 5:
                self.rect.x -= self.speed * cos(radians(self.angle))
            else:
                self.reset()
        if self.rect.y + self.rect.height < 0 or self.rect.y > HEIGHT + 30:
            self.reset()

    def burst(self):
        global score
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            score += 1
            self.reset()

    def reset(self):
        self.rect.x = random.randrange(MARGIN, WIDTH - self.rect.width - MARGIN)
        self.rect.y = HEIGHT - LOWER_BOUND
        self.angle = 90

def draw_lower_platform():
    pygame.draw.rect(display, DARK_GRAY, (0, HEIGHT - LOWER_BOUND, WIDTH, LOWER_BOUND))

def show_score():
    score_text = font.render("Balloons Bursted : " + str(score), True, WHITE)
    display.blit(score_text, (150, HEIGHT - LOWER_BOUND + 50))

def close():
    pygame.quit()
    sys.exit()

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                close()
            if event.key == pygame.K_r:
                global score
                score = 0
                game()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for balloon in balloons:
                balloon.burst()

def draw_pointer():
    pos = pygame.mouse.get_pos()
    r = 25
    l = 20
    color = LIGHT_GREEN
    for balloon in balloons:
        if balloon.rect.collidepoint(pos):
            color = RED
    pygame.draw.ellipse(display, color, (pos[0] - r / 2, pos[1] - r / 2, r, r), 4)
    pygame.draw.line(display, color, (pos[0], pos[1] - l / 2), (pos[0], pos[1] - l), 4)
    pygame.draw.line(display, color, (pos[0] + l / 2, pos[1]), (pos[0] + l, pos[1]), 4)
    pygame.draw.line(display, color, (pos[0], pos[1] + l / 2), (pos[0], pos[1] + l), 4)
    pygame.draw.line(display, color, (pos[0] - l / 2, pos[1]), (pos[0] - l, pos[1]), 4)

def game():
    global score
    score = 0
    balloons = [Balloon(random.choice([1, 1, 2, 2, 2, 2, 3, 3, 3, 4])) for _ in range(10)]

    while True:
        handle_events()
        display.blit(background_img, (0, 0))

        for balloon in balloons:
            display.blit(balloon.image, balloon.rect)
            balloon.move()

        draw_pointer()
        draw_lower_platform()
        show_score()

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    game()
