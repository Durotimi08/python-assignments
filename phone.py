import phonebook
import tic_tac
import ussd
import operations
import bank
import cbt
import rockpaperscssors
import time
operation = ["Phone Directory", "Ussd service", "Games", "Calculator", "Take a test", "Bank app"]

print("Loading...\n")
time.sleep(0.6)

while True:
    print("Here are a list of operations you can perform")
    for i,val in enumerate(operation, 1):
        print(f"{i}. {val}")
    print()
    nxt = int(input("Which operation will you like to perform: "))
    if nxt == 1:
        phonebook.show()
    elif nxt == 2:
        ussd.begin()
    elif nxt == 3:
        print()
        print("1. Tic_Tac_Toe")
        print("2. Rock-Paper_scissors\n")
        nxxt = input("Which game will you like to play: ").lower()
        if int(nxxt) == 1:
            tic_tac.new()
        elif int(nxxt) == 2:
            rockpaperscssors.begin()
        else:
            print("Invalid input")
    elif nxt == 4:
        operations.begin()
    elif nxt == 5:
        cbt.begin()
    elif nxt == 6:
        bank.begin()
    else: 
        print("Invalid input")
