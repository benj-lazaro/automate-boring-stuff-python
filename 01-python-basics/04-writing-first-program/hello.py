# This program prints 'Hello World!'
# Then asks for the user's name, prints a response and length of the given name
# Then asks for the user's age
# Computes and prints age the following year

print("Hello World!")           # Display greetings

print("What is your name? ")    # Ask for their name
myName = input()
print("Please to meet you, " + myName)
print("The length of your name is " + str(len(myName)))

print("What is your age? ")     # Ask for their age
myAge = input()
print("You will be " + str(int(myAge) + 1) + " in a year")
