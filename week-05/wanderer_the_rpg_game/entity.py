class Entity(object):

    def __init__(self):
        self.x = x
        self.y = y


class Hero(Entity):

    def move(self, dx, dy):
        canvas.move(self.rect, dx, dy )