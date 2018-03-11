def even_numbers(startpoint, endpoint = 101, step = 5):
    even_numbers = []
    for number in range(startpoint, endpoint, step):
        if number%2 == 0:
            even_numbers.append (number)


    return even_numbers

print (even_numbers (0))


def generatenumber():
    start = input("Enter a start point: ")
    endpoint = input ("Enter an end point: ")
    while not start.isdigit():
        start = input("Enter a start point in digits: ")
    while not endpoint.isdigit():
        endpoint = input ("Enter an end point in digits: ")

    return(even_numbers (int(start), int(endpoint)))

num_list = generatenumber()


def summation (num_list):
    summ = 0
    for number in num_list:
        summ += number

    return summ * len(num_list)

print (summation (num_list))
