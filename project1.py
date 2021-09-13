import random

ask = input("Do you want to play (Y/N)?\n")
a = str(ask)
while a!="Y" and a!="y" and a!="N" and a!="n":
    ask = input("Please enter Yes or No (Y/N).")
    a = str(ask)
while a=="Y" or a=="y":
    dice = random.randint(1,6)
    print("Here's your result :")
    print(dice)
    ask = input("Do you want to play again (Y/N)?\n")
    a = str(ask)
