#Classwork

list_of_numbers = []
response = input ("Do you want to add another number? (Yes/No)")

while response.title() in ["Yes", "Y"]:
    xyz = input ("Enter a number: ")
    list_of_numbers.append(xyz)
    response = input ("Do you want to add another number? (Yes/No)")
     

#list_of_numbers = [5, 10, 35, 25]

def summation (num_list):
    summ = 0
    for number in num_list:
        summ += number

    return summ * len(num_list)
elif:
    print (summation (list_of_numbers))

