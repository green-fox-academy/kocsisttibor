# https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/oo/sharpie/python.md

class Sharpie:

    def __init__(self, color, width):
        self.color = color
        self.width = width
        self.ink_amount = 100


    def use(self):
        self.ink_amount -= 1

yellow_sharpie = Sharpie("yellow", 4)

yellow_sharpie.use()

print(yellow_sharpie.ink_amount)