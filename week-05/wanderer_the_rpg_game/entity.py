from tkinter import *

class Entity(object):

    def __init__(self):
        self.x = x
        self.y = y


class Hero(Entity):

    def __init__(self, canvas):
        self.hero_image = None
        self.x = 0
        self.y = 0
        self.hero_file_down = PhotoImage(file = "hero-down.png")
        self.hero_file_up = PhotoImage(file = "hero-up.png")
        self.hero_file_right = PhotoImage(file = "hero-right.png")
        self.hero_file_left = PhotoImage(file = "hero-left.png")
        self.canvas = canvas

   
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
