#Guess a Word

import random

word_box = ["Corn", "Egg", "Beef", "Rice", "Pepper", "Salt", "Oil", "Seasoning"]

choice = random.choice(word_box)
print ("The ingredients are", word_box)
guess = input ("\nGuess the ingredient: ")

while choice != guess.title():
    guess = input ("Wrong! Try again...")

else:
    print ("Success! You guessed right. It is", choice)

exit ()
