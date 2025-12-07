import turtle as t
import tkinter as tk
from tkinter import messagebox
import subprocess

class GameDialog(tk.Toplevel):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.title("Choose a Game")
        self.configure(bg="#e6e6e6")  # Set background color

        # Create a frame with a border around the contents
        self.dialog_frame = tk.Frame(self, bg="#e6e6e6", bd=2, relief=tk.SOLID)
        self.dialog_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        self.label = tk.Label(self.dialog_frame, text="Select a game to play:", fg="red", bg="#e6e6e6", font=("Arial", 14, "bold"))
        self.label.pack(pady=10)
        self.buttons_frame = tk.Frame(self.dialog_frame, bg="#e6e6e6")
        self.buttons_frame.pack(fill=tk.BOTH, expand=True)
        self.create_buttons()
        self.game_info_label = tk.Label(self.dialog_frame, text="", wraplength=380, bg="#e6e6e6", font=("Arial", 12))
        self.game_info_label.pack(pady=10)

    def create_buttons(self):
        games = [("Game 1", "#99ccff"), ("Game 2", "#ffcc66"), ("Game 3", "#99ff99"), ("Game 4", "#ff99cc"), ("Game 5", "#cc99ff")]
        for game, color in games:
            button = tk.Button(self.buttons_frame, text=game, command=lambda g=game: self.choose_game(g), bg=color, fg="white", font=("Arial", 12, "bold"))
            button.pack(side=tk.LEFT, padx=10, pady=5, fill=tk.BOTH, expand=True)

    def choose_game(self, game_choice):
        self.parent.open_py_file(game_choice)
        self.destroy()

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
        self.t = t.RawTurtle(self.screen)
        self.t.speed(0)
        self.t.hideturtle()
        self.t.penup()
        self.t.goto(0, self.screen.window_height() / 2 - 50)
        self.t.write("Select a Game", align="center", font=("Arial", int(self.screen.window_height() * 0.05), "bold"), move=False)
        self.t.color("red")
        self.t.penup()
        self.t.goto(0, self.screen.window_height() / 2 - 100)
        self.t.pendown()
        self.create_buttons()

    def create_buttons(self):
        games = [("Game 1", "#99ccff"), ("Game 2", "#ffcc66"), ("Game 3", "#99ff99"), ("Game 4", "#ff99cc"), ("Game 5", "#cc99ff")]
        for game, color in games:
            button = tk.Button(self.menu_frame, text=game, command=lambda g=game: self.open_py_file(g), bg=color, fg="white", font=("Arial", int(self.screen.window_height() * 0.03), "bold"))
            button.pack(side=tk.LEFT, padx=10, pady=5, fill=tk.BOTH, expand=True)

    def open_py_file(self, game_choice):
        game_files = {"Game 1": "game1.py", "Game 2": "game2.py", "Game 3": "game3.py", "Game 4": "game4.py", "Game 5": "game5.py"}
        if game_choice in game_files:
            # Run the selected game
            subprocess.call(["python", game_files[game_choice]])
        else:
            print("Invalid choice. Please select a valid game.")

    def show_dialog(self):
        dialog = GameDialog(self)

def main():
    game_menu = GameMenu()
    game_menu.show_dialog()
    game_menu.root.mainloop()

if __name__ == "__main__":
    main()



