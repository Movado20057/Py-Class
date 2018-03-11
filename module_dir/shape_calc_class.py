#Shape Calculator


class Shapes_calc():
    pi = 3.142    
    def __init__(self):
        pass

    def triangle(self, base, height):
        print ("The area of the triangle is:", 0.5*base*height)
        return

    def rectangle(self, length, height):
        print ("The area of the rectangle is: ", length*height)
        return

    def circle(self, radius):
        print ("The area of the circle is: ", self.pi*(radius**2))
        return

    def square(self, length):
        print ("The area of the square is: ", length**2)
        return

    def cylinder(self, radius, height):
        print ("The area of the cylinder is: ", self.pi*(radius**2)*height)
        return

