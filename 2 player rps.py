import random
import os

def title():
    print("="*30)
    print("ROCK PAPER SCISSORS GAME\n   2 PLAYERS EDITION")
    print("="*30)

def clear():
    os.system("cls")

ran = random.randint(1,2)



name1 = []
name2 = [] # I WOULD'VE JUST PUT NAME1 & 2 IN ONE SINGLE LIST BUT IDK WHY I DIDNT XD

title()

player_name1 = input("Name: ")
name1.append(player_name1)
player_name2 = input("Name: ")
name2.append(player_name2)



if ran == 1:
    print("1. Rock \n 2. Paper\n 3. Scissors")
    player2 = input(f"{name2}\n What is your choice?(1/2/3): ")
    clear()
    print("1. Rock \n 2. Paper\n 3. Scissors")
    player1 = input(f"{name1}\n What is your choice?(1/2/3): ")
    clear()
    #ROCK
    if player2 == "1" and player1 =="1":
        print("Tie!")
    elif player2 == "1" and player1 == "2":
        print(f"{name1} lose!")
    elif player2 == "1" and player1 == "3":
        print(f"{name2} win!")
    #PAPER
    elif player2 == "2" and player1 =="1":
        print(f"{name1} lose!")
    elif player2 == "2" and player1 == "2":
        print(f"tie!")
    elif player2 == "2" and player1 == "3":
        print(f"{name2} win!")
    #SCISSORS
    elif player2 == "3" and player1 =="1":
        print(f"{name2} lose!")
    elif player2 == "3" and player1 == "2":
        print(f"{name1} win!")
    elif player2 == "3" and player1 == "3":
        print(f"tie!")
if ran == 2:
    print("1. Rock \n 2. Paper\n 3. Scissors")
    player1 = input(f"{name1}\n What is your choice?(1/2/3): ")
    clear()
    print("1. Rock \n 2. Paper\n 3. Scissors")
    player2 = input(f"{name2} \nWhat is your choice(1/2/3: ")
    clear()
    #ROCK
    if player2 == "1" and player1 =="1":
        print("Tie!")
    elif player2 == "1" and player1 == "2":
        print(f"{name1} lose!")
    elif player2 == "1" and player1 == "3":
        print(f"{name2} win!")
    #PAPER
    elif player2 == "2" and player1 =="1":
        print(f"{name1} lose!")
    elif player2 == "2" and player1 == "2":
        print(f"tie!")
    elif player2 == "2" and player1 == "3":
        print(f"{name2} win!")
    #SCISSORS
    elif player2 == "3" and player1 =="1":
        print(f"{name2} lose!")
    elif player2 == "3" and player1 == "2":
        print(f"{name1} win!")
    elif player2 == "3" and player1 == "3":
        print(f"tie!")
