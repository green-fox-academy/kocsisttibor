# https://github.com/greenfox-academy/teaching-materials/blob/master/project/fractals/tree.png

from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300', bg="#00313F")
canvas.pack()

def branch(x, y, size):
    if size > 10:
        canvas.create_line(x, y, x, y - size, fill="yellow")
        canvas.create_line(x, y - size / 2, x - size / 6, y - size * 9 / 10, fill="yellow")
        canvas.create_line(x, y - size / 2, x + size / 6, y - size * 9 / 10, fill="yellow")

        branch(x - size / 6, y - size * 9 / 10, size * 3 / 4)
        branch(x, y - size, size * 3 / 4)
        branch(x + size / 6, y - size * 9 / 10, size * 3 / 4)




branch(150, 270, 100)


root.mainloop()