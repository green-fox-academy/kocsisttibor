from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# fill the canvas with lines from the edges, every 20 px, to the center.

def line_to_the_center(x, y):
    line = canvas.create_line(x, y, 150, 150)

x = 0
y = 0
distance = 20
canvas_size = 300

while y >= 0:
    while x >= 0:
        while y <= canvas_size:
            while x <= canvas_size:
                line_to_the_center(x, y)
                x += distance
            line_to_the_center(x, y)
            y += distance
        line_to_the_center(x, y)
        x -= distance
    line_to_the_center(x, y)
    y -= distance
    
root.mainloop()