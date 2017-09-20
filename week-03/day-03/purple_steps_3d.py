from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/purple-steps-3d/r4.png]

x = 10
size = 10

def purple_square(x):
    square = canvas.create_rectangle(x, x, x + size, x + size, fill = "#B146F4")

for i in range(1, 6):
    purple_square(x)
    x = x + (i * 10)
    size += 10
    
root.mainloop()