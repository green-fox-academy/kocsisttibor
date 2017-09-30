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
            filled_ammo = self.max_ammo - self.ammo_store
            self.ammo_store = self.max_ammo
            return ammo_storage - filled_ammo
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


    def fill(self):
        if self.ammo_storage == 0:
            return "No ammo"
        else:
            for aircraft in self.F35_store:
                self.ammo_storage = aircraft.refill(self.ammo_storage)
                if self.ammo_storage == 0:
                    break
            for aircraft in self.F16_store:
                self.ammo_storage = aircraft.refill(self.ammo_storage)
                if self.ammo_storage == 0:
                    break


    def total_damage(self):
        total_damage = 0
        for aircraft in self.F16_store:
            total_damage += aircraft.ammo_store * aircraft.base_damage
        for aircraft in self.F35_store:
            total_damage += aircraft.ammo_store * aircraft.base_damage
        return total_damage


    def get_status(self):
        status = "\nHP: {}, Aircraft count: {}, Ammo: {}, Total damage: {}".format(self.health_point, len(self.F16_store) + len(self.F35_store), self.ammo_storage, self.total_damage())
        status += "\n\nAircrafts:"
        for aircraft in self.F35_store:
            status += "\n" + str(aircraft.get_status())
        for aircraft in self.F16_store:
            status += "\n" + str(aircraft.get_status())
        return status  


    def fight(self, enemy):
        enemy.health_point -= self.total_damage()
        for aircraft in self.F16_store:
            aircraft.ammo_store = 0
        for aircraft in self.F35_store:
            aircraft.ammo_store = 0    
        if enemy.health_point <= 0:
            return "It's dead Jim :("
