# https://github.com/greenfox-academy/teaching-materials/blob/master/project/fractals/sierpinski-carpet.png

from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300', bg="white")
canvas.pack()

def draw_square(x, y, size):
    if size > 1:
        canvas.create_rectangle(x, y, x + size, y + size, fill="black")

        draw_square(x - size * 2 / 3, y - size * 2 / 3, size / 3)
        draw_square(x - size * 2 / 3, y + size * 1 / 3, size / 3)
        draw_square(x - size * 2 / 3, y + size * 4 / 3, size / 3)
        draw_square(x + size * 1 / 3, y + size * 4 / 3, size / 3)
        draw_square(x + size * 4 / 3, y + size * 4 / 3, size / 3)
        draw_square(x + size * 4 / 3, y + size * 1 / 3, size / 3)
        draw_square(x + size * 4 / 3, y - size * 2 / 3, size / 3)
        draw_square(x + size * 1 / 3, y - size * 2 / 3, size / 3)



draw_square(100, 100, 100)

root.mainloop()
