
from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# divide the canvas into 4 equal parts
# and repeat this pattern in each quarter:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/line-play/r1.png]

def top_to_right_line(left, right, top, bottom, actual):
    line = canvas.create_line(actual + left, top, right, actual + top, fill = "purple")


def bottom_to_left_line(left, right, top, bottom, actual):
    line = canvas.create_line(left, actual + top, actual + left, bottom, fill = "green")

canvas_size = 300
starting_position = 20
step = 10

quarters = [[0, canvas_size / 2, 0, canvas_size / 2, starting_position], 
            [canvas_size / 2, canvas_size, 0, canvas_size / 2, starting_position],
            [0, canvas_size / 2, canvas_size / 2, canvas_size, starting_position],
            [canvas_size / 2, canvas_size, canvas_size / 2, canvas_size, starting_position]]

for i in range(4):
    for j in range(int(canvas_size / 2 / step) - 2):
        top_to_right_line(*quarters[i])
        bottom_to_left_line(*quarters[i])
        quarters[i][4] += step
    i += 1
    
root.mainloop()