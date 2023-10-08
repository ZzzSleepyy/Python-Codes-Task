import random
import os


play = False

yes_no = ["y","n"]

money = int()

i = input("Want to play?(y, n): ")

l = int(input("How much money do you have?: "))

if l < 0:
    print("Balance exceeds up to 0")
    play = False
elif l < 501:
    print("moneu")
    money += l
else:
    print("Money only exceeds to 500P")

if i == "y":
    play = True

elif i not in yes_no:
    print("Error!")

else:
    print("Exit!")
    
# ________________________________
while 1 == 1:
    roll_dice = random.randint(1,6)

    bot_dice = random.randint(1,6)
    
    if play is True:

        print(f"Bet game! \n 1.Roll \n 2.Pay \n 3. Withdraw \n Money: {money}")
        n = input("Choices(1/2/3): ")
        if n == "1":
            print("1. Get the same number(150P), 2. Not get the same number(10P), 3. Tie it up(30): ")
            q = input("Your choice(1/2/3): ")
            if q == "1":
                print(roll_dice)
                m = int(input("Your number: "))
                if m == roll_dice:
                    print(f"You won the bet!\n Number: {roll_dice}")
                    money += 150
                    print(f"Money: {money}")
                elif m == roll_dice and m == bot_dice:
                    a = input(f"Tie!\n Play again?(y, n): ")
                    money -= 30
                    print(f"Money: {money}")
                if m != roll_dice:
                    print(f"You didn't get the number! \n Number: {roll_dice}\n")
                    money -= 30
                    print(f"Money: {money}")
            

                
        elif n == "2":
            pass
        
        elif n == "3":
            pass
