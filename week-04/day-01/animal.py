# https://github.com/greenfox-academy/teaching-materials/tree/master/workshop/oo/animal

class Animal:

    def __init__(self, hunger=50, thirst=50):
        self.hunger = hunger
        self.thirst= thirst


    def eat(self):
        self.hunger -= 1

    
    def drink(self):
        self.thirst -= 1


    def play(self):
        self.hunger += 1
        self.thirst += 1

dog = Animal()
cat = Animal()

dog.eat()
dog.eat()
cat.play()

print(cat.hunger)
print(dog.hunger)
