import random
def begin():
    print("Welcome to rock paper scissors\n")
    cnfirm = True
    while cnfirm:
        try:
            set = ["rock", "paper", "scissors"]
            digit = random.choice(set)
            letter = set.index(input("What wll you like to play: ").lower())
            print(f"Computer played: {digit}")
            if letter == set.index(digit):
                print("Its a draw\n")
            elif (letter+1 == set.index(digit)) or (letter+2 > len(set) and set.index(digit) == 0):
                print("Computer won\n")
            else: 
                print("You won\n")
            nxt = input("Do you want to end this game Y/N: ").lower()
            if nxt == "Y":
                cnfirm = False
        except:
            print("Invalid input\n")
