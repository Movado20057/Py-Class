# The Guess

import random
num = random.randint(1,10)
chance = int(1)
print ("\t\tWelcome to the game, 'Guess My Number'!")
print ("\nMy name is FAVORITO and I will be picking a number between 1 and 10")
print ("\nTry to guess what number I picked in three attempts, you set?")
input ("\nReady? Press Enter to Continue...")

guess = int(input ("Take a guess: "))

if guess == num:
    print ("\n\nWowza! Are you a psychic medium?! You picked my number", num)

else:
    while guess != num:
        if chance < 3:
            if guess < num:
                guess = int(input ("Nice try, go higher this time..."))
                chance += 1
            elif guess > num:
                guess = int(input ("Nice try, go lower this time..."))
                chance += 1
            continue
        else:
            print ("\n\nGame Over!")
            print ("\nYou should have picked", num)
            break

    else:
        print ("\n\nNot bad! You picked my number", num, "in", chance, "tries")

input ("\n\n")
