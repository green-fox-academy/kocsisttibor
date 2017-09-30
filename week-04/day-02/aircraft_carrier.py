# https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/inheritance/aircraft-carrier/aircraft-carrier.md

class Aircraft(object):

    def __init__(self):
        self.ammo_store = 0


    def fight(self):
        self.damage = self.ammo_store * self.base_damage
        self.ammo_store = 0
        return self.damage


    def refill(self, ammo_storage):
        if self.max_ammo - self.ammo_store <= ammo_storage:
            self.ammo_store = self.max_ammo
            return ammo_storage - (self.max_ammo - self.ammo_store)
        else:
            self.ammo_store += ammo_storage
            return 0


    def get_type(self):
        return self.__class__.__name__


    def get_status(self):
        return "Type {}, Ammo: {}, Base damage: {}, All damage: {}".format(self.__class__.__name__, self.ammo_store, self.base_damage, self.ammo_store * self.base_damage)

class F16(Aircraft):

    def __init__(self):
        super(F16, self).__init__()
        self.max_ammo = 8
        self.base_damage = 30

class F35(Aircraft):

    def __init__(self):
        super(F35, self).__init__()
        self.max_ammo = 12
        self.base_damage = 50

class Carrier(object):

    def __init__(self, ammo_storage, health_point):
        self.ammo_storage = ammo_storage
        self.health_point = health_point
        self.F16_store = []
        self.F35_store = []


    def add_aircraft(self, aircraft):
        if aircraft.__class__.__name__ == "F16":
            self.F16_store.append(aircraft)
        elif aircraft.__class__.__name__ == "F35":
            self.F35_store.append(aircraft)

f15 = F16()
carrier = Carrier(300, 5000)

carrier.add_aircraft(f15)
print(carrier.F16_store)
