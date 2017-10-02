from tkinter import *

# root = Tk()
# canvas_height = 720
# canvas_width = 720
# canvas = Canvas(root, width=canvas_width, height=canvas_height)

class Map(object):

    def __init__(self):
        self.floor_file = PhotoImage(file = "floor.png")
        self.wall_file = PhotoImage(file = "wall.png")
        self.tile_size = 72
        self.x = 0
        self.y = 0
        self.map = [[0, 0, 1, 0, 0, 0, 1, 0, 1, 1],
                    [0, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                    [1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
                    [1, 0, 1, 0, 1, 1, 1, 1, 1, 0],
                    [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
                    [0, 1, 0, 0, 0, 0, 0, 0, 1, 1],
                    [0, 1, 0, 0, 1, 0, 1, 0, 1, 0],
                    [0, 0, 0, 1, 1, 0, 1, 0, 0, 0],
                    [1, 1, 0, 0, 0 ,0, 1, 1, 1, 0],
                    [0, 0, 0, 1, 1, 1, 1, 1, 1, 0]]


    def draw_map(self, canvas):
        for j in range(len(self.map)):
            for i in range(len(self.map[0])):
                if self.map[j][i] == 1:
                    canvas.create_image(self.x, self.y, anchor=NW, image=self.wall_file)
                    self.x += self.tile_size
                else:
                    canvas.create_image(self.x, self.y, anchor=NW, image=self.floor_file)
                    self.x += self.tile_size
            self.x = 0
            self.y += self.tile_size


# mapp_a = Map()
# mapp_a.draw_map()

# canvas.pack()

# canvas.focus_set()
# root.mainloop()



