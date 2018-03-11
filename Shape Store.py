#Welcome user

print ("Welcome to my Shape Shop!")

#Present options
shapes = ["Triangle", "Circle", "Rectangle"]
print ("\nThe Shapes on offer today are", shapes)
selected_shape = input ("\n\nPlease select a shape of your choice:\t")

#Evaluate options, Calculate and throw back result
while selected_shape.title() not in shapes:
    selected_shape = input ("\nPlease select either 'Triangle', 'Circle' or 'Rectangle'")

if selected_shape.title() == "Circle":
    radius = input ("Kindly enter your specification for Radius: ")
    while not radius.isdigit():
        radius = input ("Please enter the Radius in digits: ")
    print ("The Area for the Circle you chose is", 3.16*float(radius)**2)

elif selected_shape.title() == "Triangle":
    base = input ("Kindly enter your specification for Base: ")
    while not base.isdigit():
        base = input ("Please enter the Base in digits: ")
    height = input ("Kindly enter your specification for Height: ")
    while not height.isdigit():
        height = input ("Please enter the Height in digits: ")
    print ("The Area for the Triangle you chose is", 0.5*float(base)*float(height))

elif selected_shape.title() == "Rectangle":
    length = input ("Kindly enter your specification for Length: ")
    while not length.isdigit():
        length = input ("Please enter the length in digits: ")
    height = input ("Kindly enter your specification for Height: ")
    while not height.isdigit():
        height = input ("Please enter the Height in digits: ")
    print ("The Area for the Rectangle you chose is", float(length)*float(height))

#Continue
gfinish = input("\nDo you want to try another product? Yes or No)")
if finish.title() == "Yes":
    goto (7)
else:
    real_finish = input("\nDo you want to checkout now? Yes or No)")
    if real_finish.title() == "Yes":
        print ("\nThank you for your time!")
    else:
        goto (39)

print ("For further enquiries, please call Support on 08030684460")

input ("\n\n")
