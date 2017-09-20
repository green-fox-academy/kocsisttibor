from tkinter import *

root = Tk()

canvas = Canvas(root, width='320', height='320')
canvas.pack()

# fill the canvas with a checkerboard pattern.

def square(x, y, color):
    square = canvas.create_rectangle(x, y, x + 40, y + 40, fill = color)

x = 0
y = 0

for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            color = "black"
        else:
            color = "white"
        square(x, y, color)
        x += 40
    x = 0
    y += 40



root.mainloop()