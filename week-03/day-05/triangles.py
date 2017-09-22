# https://github.com/greenfox-academy/teaching-materials/blob/master/project/fractals/triangles.jpg

from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300', bg="gray")
canvas.pack()

def big_triangle(x, y, size):
    canvas.create_polygon(x, y, x + size, y, x + size / 2, y + 0.75 ** 0.5 * size, fill="white", outline="black")


def small_triangle(x, y, size):
    if size > 2:
        canvas.create_polygon(x, y, x - size / 2, y + 0.75 ** 0.5 * size, x + size / 2, y + 0.75 ** 0.5 * size, fill="", outline="black")
        small_triangle(x - size / 2, y, size / 2)
        small_triangle(x + size / 2, y, size / 2)
        small_triangle(x, y + 0.75 ** 0.5 * size, size / 2)

big_triangle(0, 20, 300)
small_triangle(150, 20, 150)


root.mainloop()