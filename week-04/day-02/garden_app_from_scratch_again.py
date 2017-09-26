# https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/inheritance/garden-app/garden-app.md

class Garden:
    pass


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
