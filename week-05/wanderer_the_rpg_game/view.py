from tkinter import *

root = Tk()
canvas_height = 720
canvas_width = 720
canvas = Canvas(root, width=canvas_width, height=canvas_height)

floor_file = PhotoImage(file = "floor.png")
wall_file = PhotoImage(file = "wall.png")
tile_size = 72
tiles_in_row = canvas_width / tile_size
tiles_in_coloumn = canvas_height = tile_size
x = 0
y = 0
map = [[0, 0, 1, 0, 0, 0, 1, 0, 1, 1],
       [0, 0, 1, 0, 1, 0, 1, 0, 1, 0],
       [1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
       [1, 0, 1, 0, 1, 1, 1, 1, 1, 0],
       [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
       [0, 1, 0, 0, 0, 0, 0, 0, 1, 1],
       [0, 1, 0, 0, 1, 0, 1, 0, 1, 0],
       [0, 0, 0, 1, 1, 0, 1, 0, 0, 0],
       [1, 1, 0, 0, 0 ,0, 1, 1, 1, 0],
       [0, 0, 0, 1, 1, 1, 1, 1, 1, 0]]

for j in range(len(map)):
    for i in range(len(map[0])):
        if map[j][i] == 1:
            canvas.create_image(x, y, anchor=NW, image=wall_file)
            x += tile_size
        else:
            canvas.create_image(x, y, anchor=NW, image=floor_file)
            x += tile_size
    x = 0
    y += tile_size



canvas.pack()

root.mainloop()