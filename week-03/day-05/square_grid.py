# https://github.com/greenfox-academy/teaching-materials/blob/master/project/fractals/square-grid.png

from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300', bg="white")
canvas.pack()


def draw_grid(x, y, size, border, color):
    rainbow = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
    if size > 3:
        canvas.create_rectangle(x, y, x + size, y + size, width=border, outline=rainbow[color])

        draw_grid(x - size / 4, y - size / 4, size / 2, border / 2, color + 1)
        draw_grid(x + size * 3 / 4, y - size / 4, size / 2, border / 2, color + 1)
        draw_grid(x + size * 3 / 4, y + size * 3 / 4, size / 2, border / 2, color + 1)
        draw_grid(x - size / 4, y + size * 3 / 4, size / 2, border / 2, color + 1)

draw_grid(75, 75, 150, 15, 0)

root.mainloop()