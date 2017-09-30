# https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/oo/sharpie-set/python.md

from sharpies import Sharpie
from random import randint

class SharpieSet(object):

    def __init__(self, number_of_sharpies):
        self.number_of_sharpies = number_of_sharpies
        self.sharpie_set = []
        self.colors = ["orange", "red", "green", "yellow", "blue", "gray", "olive", "black", "purple"]


    def create_set(self):
        for i in range(self.number_of_sharpies):
            color = self.colors[randint(0, len(self.colors) - 1)]
            width = randint(3, 10)
            self.sharpie_set.append(Sharpie(color, width))


    def count_usable(self):
        self.usable = 0
        for i in self.sharpie_set:
            if i.ink_amount > 0:
                self.usable += 1
        return(self.usable)


    def remove_trash(self):
        self.trash = []
        for i in self.sharpie_set:
            if i.ink_amount <= 0:
                self.trash.append(i)
                self.sharpie_set.remove(i)

sharpies = SharpieSet(5)

sharpies.create_set()

for i in sharpies.sharpie_set:
    print(i.color, i.width, i.ink_amount)

print("\n")

for i in range(100):
    sharpies.sharpie_set[2].use()
    sharpies.sharpie_set[4].use()

for i in sharpies.sharpie_set:
    print(i.color, i.width, i.ink_amount)

print(sharpies.count_usable())

print("\n")

sharpies.remove_trash()

for i in sharpies.sharpie_set:
    print(i.color, i.width, i.ink_amount)



