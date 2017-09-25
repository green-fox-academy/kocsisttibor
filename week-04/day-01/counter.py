# https://github.com/greenfox-academy/teaching-materials/tree/master/workshop/oo/counter/python

class Counter(object):

    def __init__(self, value=0):
        self.value = value
        self.initial = value


    def add(self, number=1):
        self.value += number


    # def add_one(self):
    #     self.value += 1


    def get(self):
        return self.value


    def reset(self):
        self.value = 0
        

