fruit = ["mango", "orange", "pineapple", "apple", "banana", "grape"]

#print (fruit[2])
#print (fruit[2:])
#print (fruit[:2])
#print (fruit[:])
#print (fruit[-3])
#fruit[4] = "Ice Cream"
#print (fruit[4])
#print (fruit[2:3])
#print (fruit)
#print (len(fruit))

for item in fruit:
    print (item)

items = ["clothes", ["bags", "shoes", "pen"], "Dogs", "House"]

print (items[1][1])

print (items[1])


for num in range(100):
    excludes = [0,1]
    if num % 2 == 0 and num not in excludes:
        print (num)
exit ()
