#Miles Converter

def miles_conv (miles):
    km = 1.6 * float(miles)
    return km

int_input = 6.0

int_output = miles_conv(float(int_input))

print ("The equivalent in kilometres is", int_output)


#Compute all multiples of 3,5
#that are less than 100

total = 0
for i in range (1,100):
    if i % 3 == 0 or i % 5 == 0:
        total += i

print (total)

total2 = 0
j = 1
while j < 100:
    if j % 3 == 0 or j % 5 == 0:
        total2 += j

    j += 1

print (total2)        

total3 = 0
given_list = [5, 4, 4, 3, 1, -2, -3, -5]
for i in given_list:
    if i > 0:
        total3 += i

print (total3)


total4 = 0
i = 0
while i < len(given_list) and given_list[i] > 0:
    total4 += given_list[i]
    i += 1
    
print (total4)


total5 = 0
i = 0
while True:
    total5 += given_list[i]
    i += 1
    if given_list[i] <= 0:
        break

print (total5)

given_list4 = []
total6 = 0
for i in range(7, -8, -2):
    given_list4.append(i)
    total6 += i

print (given_list4)
print (total6)
















exit()


