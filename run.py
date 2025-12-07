
from itertools import cycle
from random import randrange
from tkinter import Canvas, Tk, font, messagebox, Button

class EggCatcherGame:
    def __init__(self, root):
        self.root = root
        self.canvas_width = root.winfo_screenwidth() // 2
        self.canvas_height = root.winfo_screenheight() // 2
        self.c = Canvas(root, width=self.canvas_width, height=self.canvas_height, background='deep sky blue')
        self.c.create_rectangle(-5, self.canvas_height - 100, self.canvas_width + 5, self.canvas_height + 5, fill='sea green', width=0)
        self.c.create_oval(-80, -80, 120, 120, fill='orange', width=0)
        self.c.pack()

        self.color_cycle = cycle(['light blue', 'light green', 'light pink', 'light yellow', 'light cyan'])

        self.egg_width = 45
        self.egg_height = 55
        self.egg_score = 10
        self.egg_speed = 500
        self.egg_interval = 4000
        self.difficulty_factor = 0.75  

        self.catcher_color = 'blue'
        self.catcher_width = 100
        self.catcher_height = 100
        self.catcher_start_x = self.canvas_width / 2 - self.catcher_width / 2
        self.catcher_start_y = self.canvas_height - self.catcher_height - 20
        self.catcher_start_x2 = self.catcher_start_x + self.catcher_width
        self.catcher_start_y2 = self.catcher_start_y + self.catcher_height

        self.catcher = self.c.create_arc(self.catcher_start_x, self.catcher_start_y, \
                                        self.catcher_start_x2, self.catcher_start_y2, start=200, extent=140, \
                                        style='arc', outline=self.catcher_color, width=3)

        self.game_font = font.nametofont('TkFixedFont')
        self.game_font.config(size=18)

        self.score = 0
        self.score_text = self.c.create_text(10, 10, anchor='nw', font=self.game_font, fill='darkblue', \
                                                text='Score: ' + str(self.score))

        self.lives_remaining = 3
        self.lives_text = self.c.create_text(self.canvas_width - 10, 10, anchor='ne', font=self.game_font, fill='darkblue', \
                                                text='Lives: ' + str(self.lives_remaining))

        self.level_text = self.c.create_text(10, 30, anchor='nw', font=self.game_font, fill='darkblue', \
                                                text='Level 1')

        self.eggs = []

        self.is_paused = False
        self.pause_button = Button(self.root, text="Pause", command=self.pause_resume)
        self.pause_button.pack()

        self.c.bind('<Left>', self.move_left)
        self.c.bind('<Right>', self.move_right)
        self.c.focus_set()

        self.create_egg()
        self.move_eggs()
        self.check_catch()

    def create_egg(self):
        if not self.is_paused:
            x = randrange(10, 740)
            y = 40
            new_egg = self.c.create_oval(x, y, x + self.egg_width, y + self.egg_height, fill=next(self.color_cycle), width=0)
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
        level = (self.score // 50) + 1
        self.c.itemconfigure(self.level_text, text='Level ' + str(level))

    def move_left(self, event):
        (x1, y1, x2, y2) = self.c.coords(self.catcher)
        if x1 > 0:
            self.c.move(self.catcher, -20, 0)

    def move_right(self, event):
        (x1, y1, x2, y2) = self.c.coords(self.catcher)
        if x2 < self.canvas_width:
            self.c.move(self.catcher, 20, 0)

    def pause_resume(self):
        self.is_paused = not self.is_paused
        if self.is_paused:
            self.pause_button.config(text='Resume')
        else:
            self.pause_button.config(text='Pause')
            self.create_egg()
            self.move_eggs()
            self.check_catch()

root = Tk()
game = EggCatcherGame(root)
root.mainloop()