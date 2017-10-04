from tkinter import *
from random import randint

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

    
    def is_wall(self, x, y):
        cell_x = int(x / self.tile_size)
        cell_y = int(y / self.tile_size)
        if cell_x >= 0 and cell_x < len(self.map[0]) and cell_y >= 0 and cell_y < len(self.map):
            return self.map[cell_y][cell_x] == 1
        else:
            return True


    def create_enemy_spots(self, skeleton_number):
        spots = []
        while len(spots) != skeleton_number:
            y = randint(0, len(self.map) - 1)
            x = randint(0, len(self.map[0]) - 1)
            if self.map[y][x] == 0 and [x, y] not in spots and [x, y] != [0, 0]:
                spots.append([x * self.tile_size, y * self.tile_size])
        return spots
