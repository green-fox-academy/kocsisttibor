# https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/inheritance/garden-app/garden-app.md

class Garden:

    def __init__(self):
        self.plants = []
    
    def add_plant(self, plant):
        self.plants.append(plant)

class Plant:
    
    def __init__(self, color):
        self.color = color
        self.water_amount = 0


class Flower(Plant):
    
    def __init__(self, color):
        super().__init__(color)
        self.water_limit = 5
        self.absorption_efficiency = 0.75


class Tree(Plant):
    
    def __init__(self, color):
        super().__init__(color)
        self.water_limit = 10
        self.absorption_efficiency = 0.4

plant01 = Flower("yellow")
plant02 = Flower("blue")
plant03 = Tree("purple")
plant04 = Tree("orange")

garden = Garden()

garden.add_plant(plant01)
garden.add_plant(plant02)
garden.add_plant(plant03)
garden.add_plant(plant04)
