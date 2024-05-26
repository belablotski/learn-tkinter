from turtle import Turtle
from random import random
from math import *

def random_walk(t: Turtle) -> None:
    for i in range(100):
        steps = int(random() * 100)
        angle = int(random() * 360)
        t.right(angle)
        t.fd(steps)

def circle_walk(t: Turtle) -> None:
    for i in range(100000):
        steps = 0.4
        angle = sin(i/100) - cos(i/100) * cos(i/100)
        t.right(angle)
        t.fd(steps)

t = Turtle()
t.screen.setup(500, 500)
t.screen.tracer(4, 25)

# random_walk(t)
circle_walk(t)

t.screen.update()
t.screen.mainloop()