# https://github.com/greenfox-academy/teaching-materials/blob/master/project/fractals/circles.gif

from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300', bg="white")
canvas.pack()

def big_circle(x, y, size):
    canvas.create_oval(x - size / 2, y, x + size / 2, y + size)


def small_circles (x, y, size):
    canvas.create_oval(x - size / 2, y, x + size / 2, y + size)

    

big_circle(150, 0, 300)
small_circles(150, 0, 150)

root.mainloop()
