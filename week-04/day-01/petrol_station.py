# Petrol Station

# Create Station and Car classes
# Station
# gas_amount
# refill(car) -> decreases the gasAmount by the capacity of the car and increases the cars gas_amount
# Car
# gas_amount
# capacity
# create constructor for Car where:
# initialize gas_amount -> 0
# initialize capacity -> 100

class Station:

    def __init__(self, gas_amount):
        self.gas_amount = gas_amount


    def refill(self, car):
        self.gas_amount -= car.capacity
        car.gas_amount += car.capacity

class Car:

    def __init__(self):
        self.gas_amount = 0
        self.capacity = 100

trabant = Car()
mol = Station(10000)

mol.refill(trabant)

print(trabant.gas_amount)
print(mol.gas_amount)

