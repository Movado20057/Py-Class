#hardcoding

num = {"key" : "person", "preference" : ["basis", "movies", "pizza", ("fun", "games", "football")]}

print (type(num))
print ("The values of the dictionary are:\n")
for i in num:
    print (num.get(i))
    num_new = num.get(i)

print (type (num_new))
print ("The values of the lists are\n")
for j in num_new:
    print (j)
    num_latest = num_new[3:4]
    

print (type (num_latest))
print ("The values of the tuples are\n")
for k in num_latest:
    print (k)
    

van_dict = {"name":"James", "color":"white","race":"black"}
for i in van_dict:
    print (van_dict[i], "\n")


exit ()
