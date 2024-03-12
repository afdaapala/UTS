
class Car:
    def __init__(self, make, pos):
        self.make = make
        self.pos = pos
    def move(self, pos):
        self.pos =+ pos
    def description(self):
        return f"{self.make} is at position {self.pos}"
        # return '{} and {}'.format(self.make, )

typeCar = Car("BMW", 0)