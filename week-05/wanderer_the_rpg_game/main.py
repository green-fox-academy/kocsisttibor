from tkinter import *
from view import Map, Hud
from entity import Hero, Skeleton, Boss

# Game class

    # init
    # - create tkinter base objects
    # - map instance
    # - hero instance

    # call keyboard listener

class Game(object):

    def __init__(self):
        root = Tk()
        canvas_height = 720
        canvas_width = 780
        canvas = Canvas(root, width=canvas_width, height=canvas_height)
        self.map = Map()
        self.map.draw_map(canvas)
        self.hero = Hero(canvas)
        self.hero.draw(0, 0)
        self.skeleton = Skeleton(canvas)
        self.boss = Boss(canvas)
        self.skeleton_number = 3
        self.spots = self.map.create_enemy_spots(self.skeleton_number + 1)
        self.skeleton.draw(self.spots[:-1])
        self.boss.draw(self.spots[-1])
        self.hud = Hud()
        self.hud.draw_hud(canvas, 720, 0, self.hero.level, self.hero.hp, self.hero.dp, self.hero.sp)


        root.bind("<KeyPress>", self.on_key_press)
        canvas.pack()
        root.mainloop()


    def on_key_press(self, e):
        if ( e.keysym == 'Up' ):
            self.hero.configure("up")
            if self.map.is_wall(self.hero.x, self.hero.y - self.map.tile_size) == False:
                self.hero.move(0,-self.map.tile_size)
        elif( e.keysym == 'Down' ):
            self.hero.configure("down")
            if self.map.is_wall(self.hero.x, self.hero.y + self.map.tile_size) == False:
                self.hero.move(0,self.map.tile_size)
        elif( e.keysym == 'Right' ):
            self.hero.configure("right")
            if self.map.is_wall(self.hero.x + self.map.tile_size, self.hero.y) == False:
                self.hero.move(self.map.tile_size,0)
        elif( e.keysym == 'Left' ):
            self.hero.configure("left")
            if self.map.is_wall(self.hero.x - self.map.tile_size, self.hero.y) == False:
                self.hero.move(-self.map.tile_size,0)

game = Game()

