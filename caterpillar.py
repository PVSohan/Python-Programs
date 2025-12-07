import pygame
import random
import tkinter as tk
from tkinter import messagebox

# Initialize Pygame
pygame.init()

eating_sound = pygame.mixer.Sound("Sounds_egg_cracked.mp3")  # Replace "eat_sound.wav" with the path to your sound file

# Game settings
GRID_SIZE = 20
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Snake class
class Snake:
    def __init__(self, screen_width, screen_height):
        self.length = 1
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.positions = [(self.screen_width // 2, self.screen_height // 2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = RED

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = ((cur[0] + (x * GRID_SIZE)) % self.screen_width, (cur[1] + (y * GRID_SIZE)) % self.screen_height)
        if len(self.positions) > 2 and new in self.positions[2:]:
            return True  # Collision with itself
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()
            return False

    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, BLACK, r, 1)

    def handle_keys(self, keys):
        for key in keys:
            if key == pygame.K_UP:
                self.turn(UP)
            elif key == pygame.K_DOWN:
                self.turn(DOWN)
            elif key == pygame.K_LEFT:
                self.turn(LEFT)
            elif key == pygame.K_RIGHT:
                self.turn(RIGHT)

# Apple class
class Apple:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.position = (0, 0)
        self.color = (0, 255, 0)
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, self.screen_width // GRID_SIZE - 1) * GRID_SIZE,
                         random.randint(0, self.screen_height // GRID_SIZE - 1) * GRID_SIZE)

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, BLACK, r, 1)

def main():
    # Initialize the screen
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
    pygame.display.set_caption('Snake Game')
    clock = pygame.time.Clock()

    # Initialize the snake and apple
    snake = Snake(screen_width, screen_height)
    apple = Apple(screen_width, screen_height)

    # Game variables
    score = 0
    font = pygame.font.SysFont(None, 36)

    # Main game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                snake.handle_keys([event.key])
            elif event.type == pygame.VIDEORESIZE:
                screen_width, screen_height = event.w, event.h
                screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
                snake.screen_width, snake.screen_height = screen_width, screen_height
                apple.screen_width, apple.screen_height = screen_width, screen_height

        # Move the snake
        collided_with_self = snake.move()

        # If collided with itself, end the game and show score
        if collided_with_self:
            running = False
            show_score(score)

        # Check if the snake eats the apple
        if snake.get_head_position() == apple.position:
            snake.length += 1
            score += 10
            apple.randomize_position()

        # Draw everything
        screen.fill(YELLOW)  # Fill screen with yellow color
        snake.draw(screen)
        apple.draw(screen)

        # Display the score
        score_text = font.render("Score: " + str(score), True, BLACK)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(10)

    pygame.quit()

def show_score(score):
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Game Over", "Your Score: {}".format(score))

if __name__ == '__main__':
    main()
