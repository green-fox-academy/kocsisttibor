from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# draw 3 lines with that function.

def line_to_the_center(x, y):
    line = canvas.create_line(x, y, 150, 150)

line_to_the_center(20, 20)
line_to_the_center(180, 40)
line_to_the_center(50, 200)

root.mainloop()