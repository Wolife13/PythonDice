from tkinter import *
import random

root = Tk()
root.title('Dice Roller')
root.configure(background="white")
root.minsize(300, 150)


def d2():
    diceRoll2 = random.randint(1,2)
    print("D2 Rolled a", diceRoll2)

    diceOutput.config(text=diceRoll2)
    
def d4():
    diceRoll4 = random.randint(1,4)
    print("D4 Rolled a",diceRoll4)

    diceOutput.config(text=diceRoll4)

def d6():
    diceRoll6 = random.randint(1,6)
    print("D6 Rolled a",diceRoll6)

    diceOutput.config(text=diceRoll6)

def d8():
    diceRoll8 = random.randint(1,8)
    print("D8 Rolled a",diceRoll8)

    diceOutput.config(text=diceRoll8)

def d12():
    diceRoll12 = random.randint(1,12)
    print("D12 Rolled a",diceRoll12)

    diceOutput.config(text=diceRoll12)

def d20():
    diceRoll20 = random.randint(1,20)
    print("D20 Rolled a",diceRoll20)

    diceOutput.config(text=diceRoll20)

def d100():
    diceRoll100 = random.randint(1,100)
    print("D100 Rolled a",diceRoll100)

    diceOutput.config(text=diceRoll100)

bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )

info = Label(root, text="What dice would you like to use", bg="#BB85AB", font=("Comic Sans", 20))
info.pack(side="top", ipady="20", fill="both", expand=True)

dice2 = Button(root, text="D2", command=d2, height=5, width=10)
dice2.pack(side="left", expand=True, ipady="10")

dice4 = Button(root, text="D4", command=d4, height=5, width=10)
dice4.pack(side="left", expand=True, ipady="10")

dice6 = Button(root, text="D6", command=d6, height=5, width=10)
dice6.pack(side="left", expand=True, ipady="10")

dice8 = Button(root, text="D8", command=d8, height=5, width=10)
dice8.pack(side="left", expand=True, ipady="10")

dice12 = Button(root, text="D12", command=d12, height=5, width=10)
dice12.pack(side="left", expand=True, ipady="10")

dice20 = Button(root, text="D20", command=d20, height=5, width=10)
dice20.pack(side="left", expand=True, ipady="10")

dice100 = Button(root, text="D100", command=d100, height=5, width=10)
dice100.pack(side="left", expand=True, ipady="10")

diceOutput = Label(bottomframe, text="Output", bg="white", height=5, width=10, font=("Arial", 25))
diceOutput.pack(side="top", expand="True")


root.mainloop()
