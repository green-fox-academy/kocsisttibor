
from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# divide the canvas into 4 equal parts
# and repeat this pattern in each quarter:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/line-play/r1.png]

def line_from_top_to_right(x, vertical, horizontal):
    line = canvas.create_line(x, vertical, horizontal, x, fill = "purple")


def line_from_bottom_to_left(y, vertical, horizontal):
    line = canvas.create_line(vertical, y, y, horizontal, fill = "green")

start = 20
distance = 10
vertical = 0
horizontal = 150

def seed_drawer(start, distance, vertical, horizontal):
    for i in range(int((horizontal - start) / distance)):
        line_from_top_to_right(start, vertical, horizontal)
        start += distance

    for j in range(int((start - vertical) / distance)):
        line_from_bottom_to_left(start - distance, vertical, horizontal)
        start -= distance

seed_drawer( start, distance, vertical, horizontal)
start = 170
vertical = 150
horizontal = 300
seed_drawer( start, distance, vertical, horizontal)


root.mainloop()