from tkinter import *
from view import Map
from random import randint

class Entity(object):

    def __init__(self):
        self.x = 0
        self.y = 0
        self.level = 1


    def dice(self):
        return randint(1, 6)


class Hero(Entity):

    def __init__(self, canvas):
        super(Hero, self).__init__()
        self.hero_image = None
        self.x = 0
        self.y = 0
        self.hero_file_down = PhotoImage(file = "hero-down.png")
        self.hero_file_up = PhotoImage(file = "hero-up.png")
        self.hero_file_right = PhotoImage(file = "hero-right.png")
        self.hero_file_left = PhotoImage(file = "hero-left.png")
        self.canvas = canvas
        self.hp = 20 + 3 * self.dice()
        self.dp = 2 * self.dice()
        self.sp = 5 + 6 * self.dice()

   
    def draw(self, x, y):
        self.hero_image = self.canvas.create_image(self.x, self.y, anchor=NW, image=self.hero_file_down)


    def move(self, dx, dy):
        self.canvas.move(self.hero_image, dx, dy )
        self.x += dx
        self.y += dy


    def configure(self, direction):
        if direction == "up":
            self.canvas.itemconfig(self.hero_image, image=self.hero_file_up)
        elif direction == "down":
            self.canvas.itemconfig(self.hero_image, image=self.hero_file_down)
        elif direction == "right":
            self.canvas.itemconfig(self.hero_image, image=self.hero_file_right)
        elif direction == "left":
            self.canvas.itemconfig(self.hero_image, image=self.hero_file_left)

class Skeleton(Entity):

    def __init__(self, canvas):
        super(Skeleton, self).__init__()
        self.skeleton_image = None
        self.skeleton_file = PhotoImage(file = "skeleton.png")
        self.canvas = canvas
        self.hp = 2 * self.level * self.dice()
        self.dp = self.level / 2 * self.dice()
        self.sp = self.level * self.dice()


    def draw(self, skeleton_number):
        for i in range(len(skeleton_number)):
            self.skeleton_image = self.canvas.create_image(skeleton_number[i].x, skeleton_number[i].y, anchor=NW, image=self.skeleton_file)


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