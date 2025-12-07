from itertools import cycle
from random import randrange
from tkinter import Canvas, Tk, messagebox, font,PhotoImage

canvas_width = 2000
canvas_height = 800

root = Tk()
root.title("Egg Catcher")

c = Canvas(root, width=canvas_width, height=canvas_height, background="cyan")
c.create_rectangle(-5, canvas_height-100, canvas_width+5, canvas_height+5, fill="sea green", width=0)
c.create_oval(-80, -80, 120, 120, fill='light yellow', width=0)
c.pack()

color_cycle = cycle(["orange", "pink", "light green", "blue", "red"])
egg_width = 45
egg_height = 55
egg_score = 10
egg_speed = 100
egg_interval = 3800
difficulty = 0.95
catcher_color = "brown"
catcher_width = 100
catcher_height = 150
catcher_startx = canvas_width / 2 - catcher_width / 2
catcher_starty = canvas_height - catcher_height - 25
catcher_startx2 = catcher_startx + catcher_width
catcher_starty2 = catcher_starty + catcher_height
catcher = c.create_arc(catcher_startx, catcher_starty, catcher_startx2, catcher_starty2, start=200, extent=140, style="arc", outline=catcher_color, width=10)

game_font = font.nametofont("TkFixedFont")
game_font.config(size=18)

score = 0
score_text = c.create_text(10, 10, anchor="nw", font=game_font, fill="darkblue", text="Score: "+ str(score))

lives_remaining = 3
lives_text = c.create_text(canvas_width-10, 10, anchor="ne", font=game_font, fill="darkblue", text="Lives: "+ str(lives_remaining))

eggs = []

def create_egg():
    x = randrange(20, 740)
    y = 40
    new_egg = c.create_oval(x, y, x+egg_width, y+egg_height, fill=next(color_cycle), width=0)
    eggs.append(new_egg)
    root.after(egg_interval, create_egg)

def move_eggs():
    for egg in eggs:
        (eggx, eggy, eggx2, eggy2) = c.coords(egg)
        c.move(egg, 0, 10)
        if eggy2 > canvas_height:
            egg_dropped(egg)
    root.after(egg_speed, move_eggs)

def egg_dropped(egg):
    global lives_remaining
    eggs.remove(egg)
    c.delete(egg)
    lose_a_life()
    if lives_remaining == 0:
        messagebox.showinfo("Game Over!", "Final Score: "+ str(score))
        root.destroy()

def lose_a_life():
    global lives_remaining
    lives_remaining -= 1
    c.itemconfigure(lives_text, text="Lives: "+ str(lives_remaining))

def check_catch():
    global score
    (catcherx, catchery, catcherx2, catchery2) = c.coords(catcher)
    for egg in eggs:
        (eggx, eggy, eggx2, eggy2) = c.coords(egg)
        if catcherx < eggx and eggx2 < catcherx2 and catchery2 - eggy2 < 40:
            eggs.remove(egg)
            c.delete(egg)
            score += egg_score
            c.itemconfigure(score_text, text="Score: "+ str(score))
    root.after(100, check_catch)

root.bind("<Left>", lambda event: c.move(catcher, -20, 0) if c.coords(catcher)[0] > 0 else None)
root.bind("<Right>", lambda event: c.move(catcher, 20, 0) if c.coords(catcher)[2] < canvas_width else None)

c.focus_set()

root.after(1000, create_egg)
root.after(1000, move_eggs)
root.after(1000, check_catch)
root.mainloop()
