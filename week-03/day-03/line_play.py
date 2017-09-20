from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/line-play/r1.png]

def line_from_top_to_right(x, canvas_size):
    line = canvas.create_line(x, 0, canvas_size, x, fill = "purple")


def line_from_bottom_to_left(y, canvas_size):
    line = canvas.create_line(0, y, y, canvas_size, fill = "green")

start = 40
distance = 20
canvas_size = 300

for i in range(int((canvas_size - start) / distance)):
    line_from_top_to_right(start, canvas_size)
    start += distance

for j in range(int(start / distance)):
    line_from_bottom_to_left(start - distance, canvas_size)
    start -= distance

root.mainloop()