import random
import time
import os

JHC = 0
LM = 0
IA = 0
AH = 0
TBM = 0
JLP = 0
SAG = 0
VRAA = 0
joker = 0
var = True

names = ["Jhun Harvey Cueto", "Lawrence Marasigan", "Ian Angelo", "Aron Holgado", "Timoteo Bien Mendoza", "Jericho Louise Panganiban", "Sean Angelo Gumba", "Vincent Romar Angelo Aala", "Joker"]
while var:
    names1 = [random.choice(names)]
    for each in names1:
        if each == "Jhun Harvey Cueto":
            JHC += 2
        elif each == "Lawrence Marasigan":
            LM += 2
        elif each == "Ian Angelo":
            IA += 2
        elif each == "Aron Holgado":
            AH += 2
        elif each == "Timoteo Bien Mendoza":
            TBM += 2
        elif each == "Jericho Louise Panganiban":
            JLP += 2
        elif each == "Sean Angelo Gumba":
            SAG += 2
        elif each == "Vincent Romar Angelo Aala":
            VRAA += 2
        elif each == "Joker":
            joker += 0.5
        namesint = [JHC, LM, IA, AH, TBM, JLP, SAG, VRAA]
        varnames = random.choice(namesint)
        if varnames >= 20:
                JHC -= random.randint(1,2)
                LM -= random.randint(1,2)
                IA -= random.randint(1,2)
                AH -= random.randint(1,2)
                TBM -= random.randint(1,2)
                JLP -= random.randint(1,2)
                SAG -= random.randint(1,2)
                VRAA -= random.randint(1,2)
        os.system('cls')
        print("| Jhun Harvey Cueto: ", JHC
              ,"| Lawrence Marasigan: ", LM
              ,"| Ian Angelo: ", IA
              ,"| Aron Holgado: ", AH
              ,"| Timoteo Bien Mendoza: ", TBM
              ,"| Jericho Louise Panganiban: ", JLP
              ,"| Sean Angelo Gumba: ", SAG
              ,"| Vincent Romar Angelo Aala: ", VRAA
              ,"| Joker: ", joker)
    if joker == 50:
        break
    for eachvar in namesint:
        if eachvar == 30:
                       print("Winner: ", names1)
                       var = False
                       