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
        canvas.create_text(x, y + 10, font=("Helvetica", 14, "bold"), anchor=NW, text=" Hero")
        canvas.create_line(x, y + 35, x + 100, y + 35, fill="#343D4A")
        self.hud1 = canvas.create_text(x, y + 40, font=("Helvetica", 11, "italic"), anchor=NW, text=" Level "+str(level))
        self.hud2 = canvas.create_text(x, y + 60, font=("Helvetica", 11, "italic"), anchor=NW, text=" HP: "+str(hp))
        self.hud3 = canvas.create_text(x, y + 80, font=("Helvetica", 11, "italic"), anchor=NW, text=" DP: "+str(dp))
        self.hud4 = canvas.create_text(x, y + 100, font=("Helvetica", 11, "italic"), anchor=NW, text=" SP: "+str(sp))


    def update_hud(self):
        pass


    def draw_inventory(self, canvas, x, y):
        self.inventory = canvas.create_text(x, y + 150, font=("Helvetica", 14, "bold"), anchor=NW, text=" Inventory")
        self.inventory_image = canvas.create_image(x, y + 175, anchor=NW, image=self.key_file)


    def draw_enemy_stat(self, canvas, x, y, enemy):
        self.enemy_stat1 = canvas.create_text(x, y + 250, font=("Helvetica", 14, "bold"), anchor=NW, text=" "+enemy.__class__.__name__)
        self.enemy_statline= canvas.create_line(x, y + 275, x + 100, y + 275, fill="#343D4A")
        self.enemy_stat2 = canvas.create_text(x, y + 280, font=("Helvetica", 11, "italic"), anchor=NW, text=" Level "+str(enemy.level))
        self.enemy_stat3 = canvas.create_text(x, y + 300, font=("Helvetica", 11, "italic"), anchor=NW, text=" HP: "+str(enemy.hp))
        self.enemy_stat4 = canvas.create_text(x, y + 320, font=("Helvetica", 11, "italic"), anchor=NW, text=" DP: "+str(enemy.dp))
        self.enemy_stat5 = canvas.create_text(x, y + 340, font=("Helvetica", 11, "italic"), anchor=NW, text=" SP: "+str(enemy.dp))


    def update_enemy_stat(self):
        pass


    def clear_enemy_stat(self, canvas):
        canvas.delete(self.enemy_stat1)
        canvas.delete(self.enemy_statline)
        canvas.delete(self.enemy_stat2)
        canvas.delete(self.enemy_stat3)
        canvas.delete(self.enemy_stat4)
        canvas.delete(self.enemy_stat5)


    def next_level(self, canvas, x, y):
        self.next_level_bckgr = canvas.create_rectangle(x, y, x + 450, y + 150, fill="#957740")
        self.next_level = canvas.create_text(x, y + 10, font=("Helvetica", 45, "italic bold"), anchor=NW, text="     Congrats!")
        self.next_level = canvas.create_text(x, y + 100, font=("Helvetica", 25, "italic"), anchor=NW, text="    Press space for next level.")
