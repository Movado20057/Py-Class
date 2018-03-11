import random
word = input ("Input your string of choice: ")
print ("You've inputted,", word, "\n")

low = -len (word)
high = len (word)

for i in range(len(word)):
    print (word[i])


for i in range(20):
    position = random.randrange(low, high)
    print ("Your string [", position, "]\t", word[position])


input ("\n\nPress the enter key to exit")    
