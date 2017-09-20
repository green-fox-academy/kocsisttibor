from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a square drawing function that takes 2 parameters:
# the x and y coordinates of the square's top left corner
# and draws a 50x50 square from that point.
# draw 3 squares with that function.

def rectangle (x0, y0):
    rectangle = canvas.create_rectangle(x0, y0, x0 + 50, y0 + 50)

rectangle(20, 20)
rectangle(40, 20)
rectangle(110, 110)

root.mainloop()