#Craps Roller

import random

first_die = random.randint(1, 6)
second_die = random.randint(1, 6)

print ("\nYou rolled", first_die, "and", second_die)

while first_die == 6 and second_die == 6:
    print ("\nWelldone, you have earned an extra roll!")
    input ("\n\n\Press Enter to roll again...")
    first_die = random.randint(1, 6)
    second_die = random.randint(1, 6)
    print ("\nThis time, you rolled", first_die, "and", second_die)

input ("\n\nThank you for playing our game, press Enter to exit...")   
