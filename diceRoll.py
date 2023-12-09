import random


def d2():
    diceRoll2 = random.randint(1,2)
    print(diceRoll2,"\n")

def d4():
    diceRoll4 = random.randint(1,4)
    print(diceRoll4,"\n")

def d6():
    diceRoll6 = random.randint(1,6)
    print(diceRoll6,"\n")

def d8():
    diceRoll8 = random.randint(1,8)
    print(diceRoll8,"\n")

def d12():
    diceRoll12 = random.randint(1,12)
    print(diceRoll12,"\n")

def d20():
    diceRoll20 = random.randint(1,20)
    print(diceRoll20,"\n")

def d100():
    diceRoll100 = random.randint(1,100)
    print(diceRoll100,"\n")

def main():
    a = 2
    while a == 2:
        
        print("Availiable Dice: d2/d4/d6/d8/d12/d20/d100")
        roll = input("What dice would you like to use: ")
        
        if roll == "d2":
            d2()
        elif roll == "d4":
            d4()
        elif roll == "d6":
            d6()
        elif roll == "d8":
            d8()
        elif roll == "d12":
            d12()
        elif roll == "d20":
            d20()
        elif roll == "d100":
            d100()
        else:
            print("Thanks for using")
            a+=1
main()
