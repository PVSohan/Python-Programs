import pygame
import sys
import random
import tkinter as tk
from tkinter import messagebox
from math import radians, sin, cos

pygame.init()

# Get the screen dimensions
screen_info = pygame.display.Info()
base_width = screen_info.current_w
base_height = screen_info.current_h

# Set a scale factor for screen resizing
scale_factor = 0.8  # Adjust this factor as needed to fit the game comfortably on most screens

# Set screen dimensions
width = int(base_width * scale_factor)
height = int(base_height * scale_factor)

# Calculate responsive dimensions
margin = width // 8
lowerBound = height // 8

display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Balloon Shooter")
clock = pygame.time.Clock()

score = 0

# Colors
white = (230, 230, 230)
lightBlue = (174, 214, 241)
red = (231, 76, 60)
lightGreen = (25, 111, 61)
darkGray = (40, 55, 71)
darkBlue = (21, 67, 96)
green = (35, 155, 86)
yellow = (244, 208, 63)
blue = (46, 134, 193)
purple = (155, 89, 182)
orange = (243, 156, 18)

font_size = int(width // 40)  # Adjust font size based on screen width

font = pygame.font.SysFont("Snap ITC", font_size)

# Balloon Class
class Balloon:
    def __init__(self, speed):
        self.a = random.randint(width // 30, width // 20)
        self.b = self.a + random.randint(0, width // 40)
        self.x = random.randrange(margin, width - self.a - margin)
        self.y = height - lowerBound
        self.angle = 90
        self.speed = -speed
        self.probPool = [-1, -1, -1, 0, 0, 0, 0, 1, 1, 1]
        self.length = random.randint(width // 25, width // 12)
        self.color = random.choice([red, green, purple, orange, yellow, blue])

    # Move balloon around the Screen
    def move(self):
        direct = random.choice(self.probPool)

        if direct == -1:
            self.angle += -10
        elif direct == 0:
            self.angle += 0
        else:
            self.angle += 10

        self.y += self.speed * sin(radians(self.angle))
        self.x += self.speed * cos(radians(self.angle))

        if (self.x + self.a > width) or (self.x < 0):
            if self.y > height / 5:
                self.x -= self.speed * cos(radians(self.angle)) 
            else:
                self.reset()
        if self.y + self.b < 0 or self.y > height + width // 80:
            self.reset()

    # Show/Draw the balloon  
    def show(self):
        pygame.draw.line(display, darkBlue, (self.x + self.a / 2, self.y + self.b), (self.x + self.a / 2, self.y + self.b + self.length))
        pygame.draw.ellipse(display, self.color, (self.x, self.y, self.a, self.b))
        pygame.draw.ellipse(display, self.color, (self.x + self.a / 2 - width // 80, self.y + self.b - 3, width // 40, width // 40))

    # Check if Balloon is bursted
    def burst(self):
        global score
        pos = pygame.mouse.get_pos()

        if onBalloon(self.x, self.y, self.a, self.b, pos):
            score += 10
            self.reset()

    # Reset the Balloon
    def reset(self):
        self.a = random.randint(width // 30, width // 20)
        self.b = self.a + random.randint(0, width // 40)
        self.x = random.randrange(margin, width - self.a - margin)
        self.y = height - lowerBound 
        self.angle = 90
        self.speed -= 0.002
        self.probPool = [-1, -1, -1, 0, 0, 0, 0, 1, 1, 1]
        self.length = random.randint(width // 25, width // 12)
        self.color = random.choice([red, green, purple, orange, yellow, blue])

balloons = []
noBalloon = 10
for i in range(noBalloon):
    obj = Balloon(random.choice([1, 1, 2, 2, 2, 2, 3, 3, 3, 4]))
    balloons.append(obj)

def onBalloon(x, y, a, b, pos):
    if (x < pos[0] < x + a) and (y < pos[1] < y + b):
        return True
    else:
        return False

# Show the location of Mouse
def pointer():
    pos = pygame.mouse.get_pos()
    r = width // 26  # Reduced the pointer size by 0.75
    l = width // 20  # Reduced the pointer size by 0.75
    color = lightGreen
    for i in range(noBalloon):
        if onBalloon(balloons[i].x, balloons[i].y, balloons[i].a, balloons[i].b, pos):
            color = red
    pygame.draw.ellipse(display, color, (pos[0] - r / 2, pos[1] - r / 2, r, r), width // 160)  # Reduced the pointer size by 0.75
    pygame.draw.line(display, color, (pos[0], pos[1] - l / 2), (pos[0], pos[1] - l), width // 160)  # Reduced the pointer size by 0.75
    pygame.draw.line(display, color, (pos[0] + l / 2, pos[1]), (pos[0] + l, pos[1]), width // 160)  # Reduced the pointer size by 0.75
    pygame.draw.line(display, color, (pos[0], pos[1] + l / 2), (pos[0], pos[1] + l), width // 160)  # Reduced the pointer size by 0.75
    pygame.draw.line(display, color, (pos[0] - l / 2, pos[1]), (pos[0] - l, pos[1]), width // 160)  # Reduced the pointer size by 0.75

def lowerPlatform():
    pygame.draw.rect(display, darkGray, (0, height - lowerBound, width, lowerBound))

def showScore():
    scoreText = font.render("Score: " + str(score), True, white)
    scoreRect = scoreText.get_rect()
    scoreRect.topright = (width - width // 40, width // 40)
    display.blit(scoreText, scoreRect)

def showFinalScore(score):
    finalScoreText = font.render("Final Score: " + str(score), True, white)
    finalScoreRect = finalScoreText.get_rect(center=(width // 2, height // 2))
    display.blit(finalScoreText, finalScoreRect)
    pygame.display.update()
    pygame.time.delay(2000)  # Display message for 2 seconds

    # Display final score in a dialog box
    tk.Tk().withdraw()
    messagebox.showinfo("Game Over", f"Your Final Score: {score}")
    close()

def close():
    pygame.quit()
    sys.exit()

def game():
    global score
    loop = True
    start_time = pygame.time.get_ticks()

    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    close()
                if event.key == pygame.K_r:
                    score = 0
                    game()
                if event.key == pygame.K_ESCAPE:  # Quit if the player presses the "Esc" key
                    close()

            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(noBalloon):
                    balloons[i].burst()

        display.fill(lightBlue)
        
        for i in range(noBalloon):
            balloons[i].show()

        pointer()
        
        for i in range(noBalloon):
            balloons[i].move()

        lowerPlatform()
        showScore()  # Display the score

        # Show final score if 2 minutes have passed
        if pygame.time.get_ticks() - start_time >= 120000:
            loop = False
            display.fill(lightBlue)
            showFinalScore(score)

        pygame.display.update()
        clock.tick(60)


game()
