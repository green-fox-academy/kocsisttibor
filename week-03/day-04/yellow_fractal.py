
from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300', bg="yellow")
canvas.pack()

canvas_size = 300

def squares(canvas_size, x_point, y_point):
    size = canvas_size / 3
    square = canvas.create_rectangle(x_point + size, y_point, x_point + 2 * size, y_point + size)
    square = canvas.create_rectangle(x_point, y_point + size, x_point + size, y_point + 2 * size)
    square = canvas.create_rectangle(x_point + size, y_point + 2 * size, x_point + 2 * size, y_point + 3 * size)
    square = canvas.create_rectangle(x_point + 2 * size, y_point + size, x_point + 3 * size, y_point + 2 * size)
    
    if canvas_size > 10:
        squares(canvas_size / 3, x_point + canvas_size / 3, y_point)
        squares(canvas_size / 3, x_point, y_point + canvas_size /3)
        squares(canvas_size / 3, x_point + canvas_size * 2 / 3, y_point + canvas_size / 3)
        squares(canvas_size / 3, x_point + canvas_size / 3, y_point + canvas_size * 2 / 3)

squares(canvas_size, 0, 0)

root.mainloop()