from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# draw four different size and color rectangles.

def rectangle (x0, y0, x1, y1, color):
    rectangle = canvas.create_rectangle(x0, y0, x1, y1, fill = color)

rectangle(20, 20, 30, 40, "red")
rectangle(40, 20, 80, 50, "yellow")
rectangle(110, 110, 150, 150, "purple")

root.mainloop()