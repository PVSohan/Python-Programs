from itertools import cycle
from random import randrange
from tkinter import Canvas, Tk, font, messagebox, Button

class EggCatcherGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Egg Catcher Game")
        self.canvas_width = root.winfo_screenwidth() // 2
        self.canvas_height = root.winfo_screenheight() // 2
        self.c = Canvas(root, width=self.canvas_width, height=self.canvas_height, background='deep sky blue')
        self.c.pack(expand=True, fill='both')

        # Background elements
        self.create_background()

        # Game variables
        self.color_cycle = cycle(['light blue', 'light green', 'light pink', 'light yellow', 'light cyan'])
        self.egg_width = 45
        self.egg_height = 55
        self.egg_score = 10
        self.egg_speed = 500
        self.egg_interval = 4000
        self.difficulty_factor = 0.75
        self.catcher_color = 'blue'
        self.catcher_width = self.canvas_width // 8
        self.catcher_height = self.catcher_width
        self.catcher_start_x = self.canvas_width / 2 - self.catcher_width / 2
        self.catcher_start_y = self.canvas_height - self.catcher_height - 20
        self.catcher_start_x2 = self.catcher_start_x + self.catcher_width
        self.catcher_start_y2 = self.catcher_start_y + self.catcher_height
        self.game_font = font.Font(family="Helvetica", size=self.canvas_width // 30)

        # Game elements
        self.score = 0
        self.lives_remaining = 3
        self.level = 1
        self.is_paused = False
        self.eggs = []
        self.create_game_elements()
        self.bind_keys()
        self.start_game()

    def create_background(self):
        # Additional background elements (if any)
        pass

    def create_game_elements(self):
        # Create game elements like catcher, text, etc.
        self.create_catcher()
        self.create_text_elements()

    def create_catcher(self):
        self.catcher = self.c.create_arc(self.catcher_start_x, self.catcher_start_y,
                                         self.catcher_start_x2, self.catcher_start_y2,
                                         start=200, extent=140,
                                         style='arc', outline=self.catcher_color, width=3)

    def create_text_elements(self):
        self.score_text = self.c.create_text(10, 10, anchor='nw', font=self.game_font, fill='darkblue',
                                              text='Score: ' + str(self.score))
        self.lives_text = self.c.create_text(self.canvas_width - 10, 10, anchor='ne', font=self.game_font,
                                              fill='darkblue',
                                              text='Lives: ' + str(self.lives_remaining))
        self.level_text = self.c.create_text(10, 30, anchor='nw', font=self.game_font, fill='darkblue',
                                              text='Level ' + str(self.level))

    def bind_keys(self):
        self.c.bind('<Left>', self.move_left)
        self.c.bind('<Right>', self.move_right)
        self.c.bind('<space>', self.pause_resume)
        self.c.focus_set()

    def start_game(self):
        self.create_egg()
        self.move_eggs()
        self.check_catch()

    def create_egg(self):
        if not self.is_paused:
            x = randrange(10, self.canvas_width - self.egg_width - 10)
            y = 40
            new_egg = self.c.create_oval(x, y, x + self.egg_width, y + self.egg_height,
                                          fill=next(self.color_cycle), width=0)
            self.eggs.append(new_egg)
            self.root.after(self.egg_interval, self.create_egg)

    def move_eggs(self):
        if not self.is_paused:
            for egg in self.eggs:
                (egg_x, egg_y, egg_x2, egg_y2) = self.c.coords(egg)
                self.c.move(egg, 0, 10)
                if egg_y2 > self.canvas_height:
                    self.egg_dropped(egg)
            self.root.after(self.egg_speed, self.move_eggs)

    def egg_dropped(self, egg):
        self.eggs.remove(egg)
        self.c.delete(egg)
        self.lose_a_life()
        if self.lives_remaining == 0:
            messagebox.showinfo('Game Over', 'Final Score: ' + str(self.score))
            self.root.destroy()

    def lose_a_life(self):
        self.lives_remaining -= 1
        self.c.itemconfigure(self.lives_text, text='Lives: ' + str(self.lives_remaining))

    def check_catch(self):
        if not self.is_paused:
            (catcher_x, catcher_y, catcher_x2, catcher_y2) = self.c.coords(self.catcher)
            for egg in self.eggs:
                (egg_x, egg_y, egg_x2, egg_y2) = self.c.coords(egg)
                if catcher_x < egg_x and egg_x2 < catcher_x2 and catcher_y2 - egg_y2 < 40:
                    self.eggs.remove(egg)
                    self.c.delete(egg)
                    self.increase_score(self.egg_score)
            self.root.after(100, self.check_catch)

    def increase_score(self, points):
        self.score += points
        self.c.itemconfigure(self.score_text, text='Score: ' + str(self.score))
        if self.score >= 50:
            self.promote_level()

    def promote_level(self):
        self.level += 1
        self.c.itemconfigure(self.level_text, text='Level ' + str(self.level))
        # Adjust game difficulty here if needed

    def move_left(self, event):
        (x1, y1, x2, y2) = self.c.coords(self.catcher)
        if x1 > 0:
            self.c.move(self.catcher, -20, 0)

    def move_right(self, event):
        (x1, y1, x2, y2) = self.c.coords(self.catcher)
        if x2 < self.canvas_width:
            self.c.move(self.catcher, 20, 0)

    def pause_resume(self, event=None):
        self.is_paused = not self.is_paused
        if self.is_paused:
            self.root.after_cancel(self.create_egg)
            self.root.after_cancel(self.move_eggs)
            self.pause_button.config(text='Resume')
        else:
            self.create_egg()
            self.move_eggs()
            self.pause_button.config(text='Pause')

root = Tk()
game = EggCatcherGame(root)
root.mainloop()
