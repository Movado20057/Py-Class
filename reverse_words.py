#Backward Program

reversed_string  = " "
message = input("\nEnter your message: ")
reversed_string = message[::-1]
print (reversed_string.lower())


reversed_string  = " "
message = input("\nEnter your message: ")
for i in range(len(message)-1, -1, -1):
    reversed_string  += message[i]

print (reversed_string.lower())

reversed_string  = " "
message = input("\nEnter your message: ")
for i in reversed(message):
    reversed_string  += i

print (reversed_string.lower())

exit()
    
