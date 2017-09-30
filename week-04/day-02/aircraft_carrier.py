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

