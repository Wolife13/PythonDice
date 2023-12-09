import random

def d6():
    diceRoll6 = random.randint(1,6)
    print(diceRoll6,"\n")


a = 2
while a == 2:
    
    print("Availiable Dice: d2/d4/d6/d8/d12/d20/d100")
    roll = input("What dice would you like to use: ")
    
    if roll == "d6":
        d6()
    else:
        print("")



