import turtle as t
import tkinter as tk
import subprocess
import pygame

class GameMenu:
    def __init__(self):
        print("Welcome to the Game Menu!")
        self.root = tk.Tk()
        self.root.title("Game Menu")
        self.root.configure(bg="#e6e6e6")  # Set background color

        # Create a frame with a border around the contents
        self.menu_frame = tk.Frame(self.root, bg="#e6e6e6", bd=2, relief=tk.SOLID)
        self.menu_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        self.canvas = t.ScrolledCanvas(self.menu_frame)
        self.canvas.pack(fill="both", expand=True)
        self.screen = t.TurtleScreen(self.canvas)
        self.screen.bgcolor("#6407f0")  # Set background color

        # Add background image
        self.screen.bgpic("ground.png")
        self.resize_bg_image()

        self.t = t.RawTurtle(self.screen)
        self.t.hideturtle()
        self.create_buttons()

        # Initialize pygame and load background music
        pygame.init()
        pygame.mixer.init()
        self.background_music = pygame.mixer.music.load("grasshopper.mp3")
        pygame.mixer.music.play(-1)  # Play background music indefinitely

    def resize_bg_image(self):
        width, height = self.screen.window_width(), self.screen.window_height()
        self.screen.bgpic("ground.png")
        self.screen.bgpic().stretch_width(width)
        self.screen.bgpic().stretch_height(height)

    def create_buttons(self):
        games = [("Balloon Shooter", "#99ccff"), ("Tron Legacy", "#ffcc66"), ("Egg Catcher", "#99ff99"), ("Pacman", "#ff99cc"), ("Snake Game", "#cc99ff")]
        for game, color in games:
            button = tk.Button(self.menu_frame, text=game, command=lambda g=game: self.open_py_file(g), bg=color, fg="white", font=("Arial", int(self.screen.window_height() * 0.05), "bold"))
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
