# Print "Hello World!"
# Asks for the user's name then prints a response & length of the given name
# Asks for the user's age then computes & prints the age the following year

print("Hello World!")           # Display greetings

print("What is your name? ")    # Ask for their name
myName = input()
print("Please to meet you, " + myName)
print("The length of your name is " + str(len(myName)))

print("What is your age? ")     # Ask for their age
myAge = input()
print("You will be " + str(int(myAge) + 1) + " in a year")
