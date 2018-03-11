from module_dir.shape_calc_class import Shapes_calc as SC

class mathcalc (SC):
    def perimeter_circle (self):
        radius = input ("\nEnter your radius: ")
        return self.pi * float(radius)

#print (Shapes_calc.circle(radius))
