import turtle as t
import tkinter as tk
import subprocess
import pygame
from PIL import Image, ImageTk
import os

class GameMenu:
    def __init__(self):
        print("Welcome to the Game Menu!")
        self.root = tk.Tk()
        self.root.title("Game Menu")
        
        # Load background image
        image_path = "menu.jpg"
        if os.path.exists(image_path):
            try:
                image = Image.open(image_path)
                self.background_image = ImageTk.PhotoImage(image)
                self.background_label = tk.Label(self.root, image=self.background_image)
                self.background_label.place(relx=0, rely=0, relwidth=1, relheight=1)
            except Exception as e:
                print("Error loading image:", e)
        else:
            print("Image file not found:", image_path)

        # Create a frame with a border around the contents
        self.menu_frame = tk.Frame(self.root, bg="#e6e6e6", bd=2, relief=tk.SOLID)
        self.menu_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        # Access the turtle screen
        self.screen = t.Screen()
        self.screen.setup(width=800, height=600)  # Set up the screen dimensions
        self.screen.tracer(0)  # Turn off screen updates

        # Add background image to the turtle screen
        if os.path.exists(image_path):
            self.screen.bgpic(image_path)

        self.t = t.Turtle(visible=False)  # Make the turtle invisible
        self.t.speed(0)
        self.t.penup()
        self.t.color("red")
        self.t.goto(0, self.screen.window_height() / 2 - 50)
        self.t.write("Select a Game", align="center", font=("Arial", int(self.screen.window_height() * 0.05), "bold"))
        self.t.goto(0, self.screen.window_height() / 2 - 100)
        self.create_buttons()

        # Initialize pygame and load background music
        pygame.init()
        pygame.mixer.init()
        self.background_music = pygame.mixer.music.load("grasshopper.mp3")
        pygame.mixer.music.play(-1)  # Play background music indefinitely

    def create_buttons(self):
        games = [("Balloon Shooter", "#99ccff"), ("Tron Legacy", "#ffcc66"), ("Egg Catcher", "#99ff99"), ("Pacman", "#ff99cc"), ("Snake Game", "#cc99ff")]
        for game, color in games:
            button = tk.Button(self.menu_frame, text=game, command=lambda g=game: self.open_py_file(g), bg=color, fg="white", font=("Arial", int(self.screen.window_height() * 0.03), "bold"))
            button.pack(side=tk.LEFT, padx=10, pady=5, fill=tk.BOTH, expand=True)

    def open_py_file(self, game_choice):
        game_files = {"Balloon Shooter": "balloonshooter.py", "Tron Legacy": "tron.py", "Egg Catcher": "basket.py", "Pacman": "pacman.py", "Snake Game": "snakegame.py"}
        if game_choice in game_files:
            # Stop the background music
            pygame.mixer.music.stop()
            # Run the selected game
            subprocess.call(["python", game_files[game_choice]])
            # Resume the background music after the game exits
            pygame.mixer.music.play(-1)
        else:
            print("Invalid choice. Please select a valid game.")

    def run(self):
        self.root.mainloop()

def main():
    game_menu = GameMenu()
    game_menu.run()

if __name__ == "__main__":
    main()




