from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/purple-steps/r3.png]

x = 10

def purple_square(x):
    square = canvas.create_rectangle(x, x, x + 10, x + 10, fill = "#6D388F")

for i in range(19):
    purple_square(x)
    x += 10

root.mainloop()