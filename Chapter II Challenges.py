# The Food Chain App

print ("Welcome to the world's foremost food chain app")

first_food = str(input("\nPlease enter the name of your most favourable food: "))
alt_food = str(input ("\nOkay, what's your second choice: "))

print ("\n\nOh wow! You should try", first_food, "and", alt_food, "together")

input("\n\n")
print ("Or better yet,", first_food + alt_food + "!")


input("\n\n")

# Tipper Program

print ("This is the Tipper Program")

bill = int(input("Please enter the total bill (in Naira): "))
#while not bill.isdigit():
    #bill = float(input("Please enter the total bill (in Naira): "))
print ("\nThanks")
print ("\nYou can either give a 15% tip which is", .15*bill, "or go large @ 20%,", .20*bill)

input("\n\n")


# Car Salesman program
import random
tax = float(random.randrange(45))
license_fee = float(random.randint(12, 15))
dealer_prep = float(random.randint(17000, 25000))
destination_charge = float(random.randrange(50000))

print ("Welcome to the best online car mart!")
base_price = float(input ("Please enter the Base Price of the car you selected (in Naira): "))
total_price = (tax*base_price/100) + (license_fee*base_price/100) + dealer_prep + destination_charge
print ("\n\nAfter adding the charges below:\n1. Tax\t\t\t", tax, "\n2. License registration\t", license_fee, "\n3. Dealership Charges\t",
       dealer_prep, "\n4. Delivery Charge\t", destination_charge, "\n\nYour total bill is\t", total_price)

input ("\n\n")

