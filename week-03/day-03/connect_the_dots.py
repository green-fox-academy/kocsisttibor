from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a function that takes 1 parameter:
# a list of [x, y] points
# and connects them with green lines.
# connect these to get a box: [[10, 10], [290,  10], [290, 290], [10, 290]]
# connect these: [[50, 100], [70, 70], [80, 90], [90, 90], [100, 70],
# [120, 100], [85, 130], [50, 100]]

box = [[10, 10], [290,  10], [290, 290], [10, 290]]
fox =  [[50, 100], [70, 70], [80, 90], [90, 90], [100, 70],
[120, 100], [85, 130], [50, 100]]

def drawer(dots_list):
    for i in range(len(dots_list)):
        if i + 1 != len(dots_list):
            line = canvas.create_line(dots_list[i][0], dots_list[i][1], 
            dots_list[i + 1][0], dots_list[i + 1][1])
        else: 
            line = canvas.create_line(dots_list[i][0], dots_list[i][1], 
            dots_list[0][0], dots_list[0][1])

drawer(box)
drawer(fox)

root.mainloop()