#Shape Calculator

pi = 3.142

class Shapescalculator():
    def __init__(self):
        pass

    def triangle(self, base, height):
        return 0.5*base*height

    def rectangle(self, length, height):
        return length*height

    def circle(self, radius):
        return pi*(radius**2)

    def square(self, length):
        return length**2

    def cylinder(self, radius, height):
        return pi*(radius**2)*height

