from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/envelope-star/r2.png]

def top_right(left, right, top, bottom, step):
    line = canvas.create_line(left, step + top, step + left, bottom, fill = "green")


def top_left(left, right, top, bottom, step):
    line = canvas.create_line(left + step, bottom, right, bottom - step, fill ="green")


def bottom_left(left, right, top, bottom, step):
    line = canvas.create_line(left + step, top, right, top + step, fill = "green")


def bottom_right(left, right, top, bottom, step):
    line = canvas.create_line(left, top + step, right - step, top)

canvas_size = 300
step = 0
stepper = 10

for i in range(int(canvas_size / 2 / stepper) + 1):
    top_right(150, 300, 0, 150, step)
    top_left(0, 150, 0, 150, step)
    bottom_left(0, 150, 150, 300, step)
    bottom_right(150, 300, 150, 300, step)
    step += stepper

root.mainloop()