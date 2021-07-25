# literally just rock paper scissors bruh

import random

choices = ["r", "p", "s"]

def playGame():
    print("--------------------------------------") # visual pleasure

    uc = input("Rock (r), Paper (p), or Scissors (s)?\n")
    cc = choices[random.randint(0, 2)]

    print("--------------------------------------") # visual pleasure

    if uc not in choices:
        print("Please provide a valid input!")
        playGame()

    if uc == "r":
        if cc == "r":
            tie("Rock")
        if cc == "p":
            lose("Paper")
        if cc == "s":
            win("Scissors")

    if uc == "p":
        if cc == "p":
            tie("Paper")
        if cc == "s":
            lose("Scissors")
        if cc == "r":
            win("Rock")

    if uc == "s":
        if cc == "s":
            tie("Scissors")
        if cc == "r":
            lose("Rock")
        if cc == "p":
            win("Paper")
    
def win(cc):
    print("Computer chose: %s" % cc)
    print("You Win!")
    uce = input("Play again? (y/n)\n")
    if uce == "y":
        playGame()
    else:
        return

def lose(cc):
    print("Computer chose: %s" % cc)
    print("You Lose!")
    uce = input("Play again? (y/n)\n")
    if uce == "y":
        playGame()
    else:
        return

def tie(cc):
    print("Computer chose: %s" % cc)
    print("Tie!")
    uce = input("Play again? (y/other)\n")

    if uce == "y":
        playGame()
    else:
        return


playGame()