from tkinter import *
from view import Map, Hud
from entity import Hero, Skeleton, Boss
from random import randint

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
        self.hud_x = 720
        self.hud_y = 0
        self.canvas = Canvas(root, width=canvas_width, height=canvas_height)
        self.map = Map()
        self.map.draw_map(self.canvas)
        self.hero = Hero(self.canvas)
        self.hero.draw(0, 0)
        self.hero_has_key = False
        self.skeleton_number = 3
        self.spots = self.map.create_enemy_spots(self.skeleton_number + 1)
        self.skeletons = []
        self.create_skeletons()
        self.add_skeleton_coordinates()
        self.add_key_to_skeleton()
        self.skeletons[0].draw(self.skeletons)
        self.boss = Boss(self.canvas)
        self.boss.draw(self.spots[-1])
        self.boss_is_dead = False
        self.enemies = []
        self.enlist_enemies()
        self.hud = Hud()
        self.hud.draw_hud(self.canvas, self.hud_x, self.hud_y, self.hero.level, self.hero.hp, self.hero.dp, self.hero.sp)


        root.bind("<KeyPress>", self.on_key_press)
        self.canvas.pack()
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
        elif( e.keysym == 'space'):
            if [self.hero.x, self.hero.y] in self.spots:
                self.fight(self.hero, self.enemies[self.spots.index([self.hero.x, self.hero.y])])


    def create_skeletons(self):
        for i in range(self.skeleton_number):
            self.skeletons.append(Skeleton(self.canvas))


    def add_key_to_skeleton(self):
        self.skeletons[randint(0, self.skeleton_number - 1)].key = True


    def add_skeleton_coordinates(self):
        for i, skeleton in zip(self.spots, self.skeletons):
            skeleton.x = i[0]
            skeleton.y = i[1]

    
    def enlist_enemies(self):
        for skeleton in self.skeletons:
            self.enemies.append(skeleton)
        self.enemies.append(self.boss)


    def is_strike(self, attacker, defender):
        return attacker.sp + 2 * attacker.dice() > defender.dp


    def strike(self, attacker, defender):
        print("attacker.hp: ", attacker.hp, "defender.hp: ", defender.hp)
        if self.is_strike(attacker, defender):
            defender.hp -= (attacker.sp + 2 * attacker.dice()) - defender.dp
            print("attacker.hp: ", attacker.hp, "defender.hp: ", defender.hp)


    def fight(self, fighter_1, fighter_2):      #fight will be called always wiht hero as fighter_1
        while fighter_1.hp > 0 and fighter_2.hp > 0:
            self.strike(fighter_1, fighter_2)
            if fighter_1.hp > 0 and fighter_2.hp > 0:
                fighter_1, fighter_2 = fighter_2, fighter_1
            print(fighter_1.hp, fighter_2.hp)
        if fighter_1.hp > 0:
            self.level_up()
            if fighter_2 == self.boss:
                self.boss.delete()
                self.boss_is_dead = True
                print("boss_is_dead")
                self.enter_next_area()
            for i in self.skeletons:
                if fighter_2 == i:
                    if i.key == True:
                        self.hero_has_key = True
                        print("hero_has_key")
                        self.hud.print_key(self.canvas, self.hud_x, self.hud_y)
                    i.delete(self.spots.index([self.hero.x, self.hero.y]))
                    self.enter_next_area()
        else:
            print("Game over")


    def level_up(self):
        self.hero.max_hp += self.hero.dice()
        self.hero.dp += self.hero.dice()
        self.hero.sp += self.hero.dice()
        self.hero.level += 1
        self.canvas.delete(self.hud.hud1)
        self.canvas.delete(self.hud.hud2)
        self.canvas.delete(self.hud.hud3)
        self.canvas.delete(self.hud.hud4)
        self.hud.draw_hud(self.canvas, 720, 0, self.hero.level, self.hero.hp, self.hero.dp, self.hero.sp)
        

    def enter_next_area(self):
        if self.hero_has_key == True and self.boss_is_dead == True:
            self.hud.next_level(self.canvas, 50, 150)

game = Game()

