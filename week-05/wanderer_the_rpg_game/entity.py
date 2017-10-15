from tkinter import *
from view import Map
from random import randint

class Entity(object):

    def __init__(self):
        self.x = 0
        self.y = 0
        self.level = 1
        self.blood = PhotoImage(file = "blood.png")
        self.map = Map()


    def dice(self):
        return randint(1, 6)


class Hero(Entity):

    def __init__(self, canvas):
        super(Hero, self).__init__()
        self.hero_image = None
        self.x = 0
        self.y = 0
        self.hero_file = {
            "down": PhotoImage(file = "hero-down.png"),
            "up": PhotoImage(file = "hero-up.png"),
            "right": PhotoImage(file = "hero-right.png"),
            "left": PhotoImage(file = "hero-left.png")
        }
        self.canvas = canvas
        self.max_hp = 20 + 3 * self.dice()
        self.hp = self.max_hp
        self.dp = 2 * self.dice()
        self.sp = 5 + self.dice()

   
    def draw(self, x, y):
        self.hero_image = self.canvas.create_image(self.x, self.y, anchor=NW, image=self.hero_file["down"])


    def move(self, dx, dy):
        self.canvas.move(self.hero_image, dx, dy )
        self.x += dx
        self.y += dy


    def configure(self, direction):
        self.canvas.itemconfig(self.hero_image, image=self.hero_file[direction])

class Skeleton(Entity):

    def __init__(self, canvas):
        super(Skeleton, self).__init__()
        self.skeleton_image = None
        self.skeleton_file = PhotoImage(file = "skeleton.png")
        self.canvas = canvas
        self.hp = 2 * self.level * self.dice()
        self.dp = self.level / 2 * self.dice()
        self.sp = self.level * self.dice()
        self.skeleton_marker = ["skeleton_a", "skeleton_b", "skeleton_c", "skeleton_d", "skeleton_e", "skeleton_f"]
        self.key = False


    def draw(self, skeleton_number):
        for i in range(len(skeleton_number)):
            self.skeleton_image = self.canvas.create_image(skeleton_number[i].x, skeleton_number[i].y, anchor=NW, image=self.skeleton_file, tags=self.skeleton_marker[i])


    def delete(self, skeleton_id):
        self.canvas.itemconfig(self.skeleton_marker[skeleton_id], image=self.blood)


class Boss(Entity):

    def __init__(self, canvas):
        super(Boss, self).__init__()
        self.boss_image = None
        self.boss_file = PhotoImage(file = "boss.png")
        self.canvas = canvas
        self.hp = 2 * self.level * self.dice() + self.dice()
        self.dp = self.level / 2 * self.dice() + self.dice() / 2
        self.sp = self.level * self.dice() + self.level


    def draw(self, spot):
        self.boss_image = self.canvas.create_image(spot[0], spot[1], anchor=NW, image=self.boss_file)


    def move_options(self):
        move_options = []
        if self.map.is_wall(self.x + self.map.tile_size, self.y) == False:
            move_options.append([self.map.tile_size, 0])
        if self.map.is_wall(self.x - self.map.tile_size, self.y) == False:
            move_options.append([-self.map.tile_size, 0])
        if self.map.is_wall(self.x, self.y + self.map.tile_size) == False:
            move_options.append([0, self.map.tile_size])
        if self.map.is_wall(self.x, self.y - self.map.tile_size) == False:
            move_options.append([0, -self.map.tile_size])
        return move_options

   
    def move(self):
        move_coords = self.move_options()[randint(0, len(self.move_options()) - 1)]
        self.canvas.move(self.boss_image, move_coords[0], move_coords[1] )
        self.x += move_coords[0]
        self.y += move_coords[1]
        return [self.x, self.y]


    def delete(self):
        self.canvas.itemconfig(self.boss_image, image=self.blood)
