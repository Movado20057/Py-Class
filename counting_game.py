#counting program

def countr (start, end, step):
    for i in range(start, end+1, step):
        print (i, end = " ")
    return

x = int(input("\nYour Starting Point: "))
y = int(input("End point: "))
z = int(input("Step: "))

do_it = countr(x,y,z)

exit ()

