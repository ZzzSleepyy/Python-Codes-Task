import random


number_guess = random.randint(1,100)


while True:
    guess = int(input("Guess your number: "))
    
    
    if number_guess == guess:
        print("Correct")
        raise
    elif guess > number_guess:
        print("Lower")
    elif guess < number_guess:
        print("Higher")
        
    else:
        print("Error")
        break
    
    
#100 seconds code