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
        self.hero_file = PhotoImage(file = "hero-down.png")
        self.canvas = canvas

   
    def draw(self, x, y):
        self.hero_image = self.canvas.create_image(self.x, self.y, anchor=NW, image=self.hero_file)


    def move(self, dx, dy):
        self.canvas.move(self.hero_image, dx, dy )
        self.x += dx
        self.y += dy
