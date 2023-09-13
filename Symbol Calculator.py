#Here's a Python task that involves using the repetition operator (*) to generate a pattern of characters:

#Task: Generate a Repeated Pattern

#Write a Python program that takes a character and a number n as input from the user and prints a pattern of the character repeated n times on each row, forming a rectangular pattern.

symbol_choice =  input("Choose a symbol: ")

number_choice = int(input("Choose a number: "))

combine =  symbol_choice * number_choice

print("PATTERN:")

for i in range(number_choice):
    print(combine)



