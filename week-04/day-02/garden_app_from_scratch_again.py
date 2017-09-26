# https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/inheritance/garden-app/garden-app.md

class Plant():
    
    def __init__(self, color):
        self.color = color
        self.water_amount = 0
        self.plants = []


    def add_plant(self, plant):
        self.plants.append(plant)


    def needs_water(self):
        for plant in self.plants:
            if plant.water_amount < plant.water_limit:
                return 1
            else:
                return 0


    def review_of_garden(self):
        for plant in self.plants:
            if plant.water_amount < plant.water_limit:
                print("The {} {} needs water. Water amount: {}".format(plant.color, plant.__class__.__name__, plant.water_amount))
            else:
                print("The {} {} doesn't need water. Water amount: {}".format(plant.color, plant.__class__.__name__, plant.water_amount))


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

plants = Plant("white")

plants.add_plant(plant01)
plants.add_plant(plant02)
plants.add_plant(plant03)
plants.add_plant(plant04)

plants.review_of_garden()
