# https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/inheritance/garden-app/garden-app.md

class Garden:
    def __init__(self, color):
        self.color = color
        self.water_amount = 0
        self.plants = []
        

    def add_plant(self, plant):
        self.plants.append(plant)


    def review_of_garden(self):
        for plant in self.plants:
            if plant.water_amount < plant.water_limit:
                print("The {} {} needs water. Water amount: {}".format(plant.color, plant.__class__.__name__, plant.water_amount))
            else:
                print("The {} {} doesn't need water. Water amount: {}".format(plant.color, plant.__class__.__name__, plant.water_amount))


    def needs_water(self):
        if self.water_amount < self.water_limit:
            return 1
        else:
            return 0


    def plants_to_water(self):
        plants_to_water = []
        for plant in self.plants:
            plants_to_water.append(plant.needs_water())
        return plants_to_water
        

    def water_the_plants(self, water_in_can):
        print("\nWatering with {}".format(water_in_can))
        plants_to_water = self.plants_to_water()
        for plant in self.plants:
            if plant.water_amount < plant.water_limit:
                plant.water_absorb(water_in_can / sum(plants_to_water))


class Flower(Garden):

    def __init__(self, color):
        super().__init__(color)
        self.type = "flower"
        self.water_limit = 5
        self.absortion_efficency = 0.75

    
    def water_absorb(self, water_portion):
        self.water_amount += water_portion * self.absortion_efficency

class Tree(Garden):

    def __init__(self, color):
        super().__init__(color)
        self.type = "tree"
        self.water_limit = 10
        self.absortion_efficency = 0.4


    def water_absorb(self, water_portion):
        self.water_amount += water_portion * self.absortion_efficency

garden = Garden("white")       

plant01 = Flower("yellow")
plant02 = Flower("blue")
plant03 = Tree("purple")
plant04 = Tree("orange")

garden.add_plant(plant01)
garden.add_plant(plant02)
garden.add_plant(plant03)
garden.add_plant(plant04)

garden.review_of_garden()
garden.water_the_plants(40)
garden.review_of_garden()
garden.water_the_plants(70)
garden.review_of_garden()


