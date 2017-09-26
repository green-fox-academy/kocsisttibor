# https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/inheritance/garden-app/garden-app.md

class Plant():
    
    def __init__(self, color):
        self.color = color
        self.water_amount = 0
        self.plants = []


    def add_plant(self, plant):
        self.plants.append(plant)


    def needs_water(self):
        plants_in_need = 0
        for plant in self.plants:
            if plant.water_amount < plant.water_limit:
                plants_in_need +=1
        return plants_in_need


    def review_of_garden(self):
        for plant in self.plants:
            if plant.water_amount < plant.water_limit:
                print("The {} {} needs water. Water amount: {}".format(plant.color, plant.__class__.__name__, plant.water_amount))
            else:
                print("The {} {} doesn't need water. Water amount: {}".format(plant.color, plant.__class__.__name__, plant.water_amount))


    def water_to_plants(self, water_in_can):
        print("\nWatering with {}".format(water_in_can))
        plants_in_need = self.needs_water()
        if plants_in_need == 0:
            print("No need of water.")
        else:
            for plant in self.plants:
                if plant.water_amount < plant.water_limit:
                    plant.water_amount += (water_in_can / plants_in_need) * plant.absorption_efficiency


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
plants.water_to_plants(40)
plants.review_of_garden()
plants.water_to_plants(70)
plants.review_of_garden()
plants.water_to_plants(70)
plants.review_of_garden()
