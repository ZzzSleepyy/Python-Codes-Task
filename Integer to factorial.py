#Positive integer to factorial

#Python task for you:

#Task: Create a program that calculates the factorial of a given positive integer.

#Requirements: The program should prompt the user to enter a positive integer.
#Handle invalid input (negative numbers or non-integer input) gracefully.
#Calculate the factorial of the input integer using a loop or recursion.
#Display the calculated factorial as output.
#Feel free to give it a try and let me know if you need any assistance!

import math
for i in range(3):
    try:    
        while True:
            detect_integer = int(input("Enter a positive integer: "))
            factorial = math.factorial(detect_integer)
            print(factorial)
    except ValueError:
        if i < 3:
            print(f"You have 3 tries : Your tries {i + 1}." )
            continue
        else:
            print(ValueError)
    break

