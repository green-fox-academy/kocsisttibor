# https://github.com/greenfox-academy/teaching-materials/blob/master/project/fractals/square-grid.png

from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300', bg="white")
canvas.pack()

def draw_grid(x, y, size, border):
    if size > 5:
        canvas.create_rectangle(x, y, x + size, y + size, width=border)

        draw_grid(x - size / 4, y - size / 4, size / 2, border / 2)
        draw_grid(x + size * 3 / 4, y - size / 4, size / 2, border / 2)
        draw_grid(x + size * 3 / 4, y + size * 3 / 4, size / 2, border / 2)
        draw_grid(x - size / 4, y + size * 3 / 4, size / 2, border / 2)

draw_grid(75, 75, 150, 15)

root.mainloop()