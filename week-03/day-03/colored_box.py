from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# draw a box that has different colored lines on each edge.
topline = canvas.create_line(50, 50, 150, 50, fill = "purple", width = 5)
rightline = canvas.create_line(150, 50, 150, 150, fill = "red", width = 5)
bottomline = canvas.create_line(150, 150, 50, 150, fill = "orange", width = 5)
leftline = canvas.create_line(50, 150, 50, 50, fill = "yellow", width = 5)

root.mainloop()