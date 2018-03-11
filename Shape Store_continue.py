#Welcome user

print ("Welcome to my Shape Shop!")
positive_response = ["Yes", "Y"]
response = input ("Do you want to perform a calculation? ")
#Present options
shapes = ["Triangle", "Circle", "Rectangle"]

#Evaluate options, Calculate and throw back result

while response in positive_response:

    selected_shape = input ("\nPlease select a shape of your choice:\t")
    
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

    print ("\n\nFor further enquiries, please call Support on 08030684460")

    response = input ("Do you want to perform a calculation? ")

else:
    print ("We are happy to miss you!")
    exit()

















    
