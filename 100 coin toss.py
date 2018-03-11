## The 100 Coin Flip

import random

count = 1
head = 0
tail = 0

while count <= 100:
    coin_box = random.randint(0,1)
    if coin_box == 0:
        head += 1
        print ("Head")
    else:
        tail += 1
        print ("Tail")
    count += 1

else:
    print ("\nAfter tossing the coin randomly, we recorded ", head, "Heads &", tail, "Tails")
    print ("\nThe probabilities are", head/100, "and", tail/100, "respectively")

input ("\nPress Enter to exit")
