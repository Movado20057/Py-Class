class Vehicle ():
    def __init__ (self, kind, year_manufactured, cost, speed, no_of_wheels):
        self.kind = kind
        self.year_manufactured = year_manufactured
        self.cost = cost
        self.speed = speed
        self.no_of_wheels = no_of_wheels

    def can_fly(self):
        return self.kind == "Aeroplane"

    def accelerate (self, value):
        self.speed += value
        return self.speed

    def can_sail (self):
        return self.kind == "Ship"


class Car (Vehicle):
    pass



    
