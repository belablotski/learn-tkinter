import tkinter as tk
from tkinter.constants import *
from functools import partial

x1 = 100
y1 = 100

anim_target_x = 0
anim_target_y = 0
anim_interval_ms = 30

background = None

def draw_ptr(x, y, outline, fill, width):
    points = [x, y, x+20, y, x+20, y+20, x, y+20]
    canvas.create_polygon(points, outline=outline, fill=fill, width=width)

def draw_new(new_x, new_y):
    global x1, y1
    draw_ptr(x1, y1, background, background, 3)
    draw_ptr(new_x, new_y, 'green', 'yellow', 3)
    x1, y1 = new_x, new_y

def draw_anim(frame):
    def delta(cur, target):
        if cur < target:
            return 1
        elif cur > target:
            return -1
        else:
            return 0
    
    global x1, y1, anim_target_x, anim_target_y
    if x1 != anim_target_x or y1 != anim_target_y:
        draw_new(x1 + delta(x1, anim_target_x), y1 + delta(y1, anim_target_y))
        frame.after(anim_interval_ms, partial(draw_anim, frame))

def draw(event):
    print(type(event))
    print(dir(event))
    print(event)
    print(event.widget['background'])

    global x1, y1, anim_target_x, anim_target_y
    new_x = x1
    new_y = y1
    if event.keysym != '??':
        if event.keysym == 'Right':
            new_x += 1
        elif event.keysym == 'Left':
            new_x -= 1
        elif event.keysym == 'Up':
            new_y -= 1
        elif event.keysym == 'Down':
            new_y += 1
        else:
            raise Exception(f'Unexpected event.keysym = {event.keysym}')
        draw_new(new_x, new_y)
    else:
        anim_target_x = event.x
        anim_target_y = event.y
        event.widget.master.after(anim_interval_ms, partial(draw_anim, event.widget.master))

canvas_width, canvas_height = 300, 300

root = tk.Tk()
root.title = "Move"

canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

canvas.bind("<ButtonPress>", draw)
canvas.master.bind("<Right>", draw)
canvas.master.bind("<Left>", draw)
canvas.master.bind("<Up>", draw)
canvas.master.bind("<Down>", draw)

background = canvas['background']

root.mainloop()
