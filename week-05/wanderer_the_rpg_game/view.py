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
            if self.map[y][x] == 0 and [x * self.tile_size, y * self.tile_size] not in spots and [x, y] != [0, 0]:
                spots.append([x * self.tile_size, y * self.tile_size])
        print(spots)
        return spots

class Hud(object):

    def __init__(self):
        self.x = 0
        self.y = 0
        self.key_file = PhotoImage(file = "key.png")
        self.hud1 = None
        self.hud2 = None
        self.hud3 = None
        self.hud4 = None


    def draw_hud(self, canvas, x, y, level, hp, dp, sp):
        canvas.create_text(x, y, font=(12), anchor=NW, text=" Hero")
        self.hud1 = canvas.create_text(x, y + 20, font=(12), anchor=NW, text=" Level "+str(level))
        self.hud2 = canvas.create_text(x, y + 40, font=(12), anchor=NW, text=" HP: "+str(hp))
        self.hud3 = canvas.create_text(x, y + 60, font=(12), anchor=NW, text=" DP: "+str(dp))
        self.hud4 = canvas.create_text(x, y + 80, font=(12), anchor=NW, text=" SP: "+str(sp))


    def print_key(self, canvas, x, y):
        self.hud5 = canvas.create_image(x, y + 100, anchor=NW, image=self.key_file)


    def next_level(self, canvas, x, y):
        self.next_level_bckgr = canvas.create_rectangle(x, y, x + 350, y + 150, fill="tomato")
        self.next_level = canvas.create_text(x, y, font=(55), anchor=NW, text="Congrats! Press space for next level.")
