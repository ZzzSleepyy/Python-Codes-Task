import random
import os

attempts = 0
print("Choices:\n 1. Name 2. Random")
choice = ["1", "2"]

your_choice = input("|1| or |2?|: ")
your_pass = input("Password: ")

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","0","1","2","3","4","5","6","7","8","9","0"]

if your_choice == "1":
    with open('first-names1.txt') as f:
        contents = f.read().splitlines()
elif your_choice == "2":
    contents = None

while True:
    if your_choice == "1":
        attempts += 1
        guess = random.choice(contents)
        print(f"Cracking password: {guess}\n{'-'*13}\nAttempts: {attempts}")
        os.system("cls")  
        if guess == your_pass:
            print(f"Your password is {guess}")
            break
    elif your_choice == "2":
        attempts += 1
        guess = ''.join(random.choices(letters, k=len(your_pass)))
        print(f"Cracking password: {guess}\n{'-'*13}\nAttempts: {attempts}")
        os.system("cls")  
        if guess == your_pass:
            print(f"Your password is {guess}")
            break