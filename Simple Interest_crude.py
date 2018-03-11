#Simple Interest Calculator

#Collect User Data
principal = input ("Enter the Principal:\t")
rate = input ("Enter the Rate (in %):\t")
time = input ("Time (in years)?:\t")


#Evaluate Input Type
if principal.isdigit() and rate.isdigit() and time.isdigit():
    simple_interest = (float(principal)*float(rate)*float(time))/100
    print ("\nThe Simple Interest is\t", simple_interest)
#Convert datatype to Float
else:
    #print ("\nPlease enter digits ONLY\t")
    
    if not principal.isdigit():
        principal = input ("\nPlease enter digits ONLY for Principal:\t")
        simple_interest = (float(principal)*float(rate)*float(time))/100
        print ("\nThe Simple Interest is\t", simple_interest)

    if principal.isdigit() and rate.isdigit():
        rate = input ("\nPlease enter digits ONLY for Rate:\t")
        simple_interest = (float(principal)*float(rate)*float(time))/100
        print ("\nThe Simple Interest is\t", simple_interest)

    if principal.isdigit() and rate.isdigit() and time.isdigit():
        time = input ("\nPlease enter digits ONLY for time:\t")
        simple_interest = (float(principal)*float(rate)*float(time))/100
        print ("\nThe Simple Interest is\t", simple_interest)


#print ("\nThe Simple Interest is\t", simple_interest)

input ("\nPress Enter to Quit...")
