from import_class import mathcalc
from shape_calc_class import Shapescalculator

new_object = mathcalc()
if isinstance(new_object, mathcalc):
    print ("True")

new_object2 = Shapescalculator()
if isinstance(new_object2, Shapescalculator):
    print ("True")
