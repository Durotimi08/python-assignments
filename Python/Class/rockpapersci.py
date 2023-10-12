import random
22
def choose():
    play1 = int(input("""Choose rock, paper or scissors
                    1. Rock
                    2. Paper
                    3. Scissors
                 """))
    play2 = random.randint(1,3)
    print(f"Computer chose {play2} \n")
    if play1 == 1 and play2 == 1:
        print("It's a draw")
    elif play1 == 1 and play2 == 2:
        print("You lost, the computer chose Paper")
    elif play1 == 1 and play2 == 3:
        print("You won, the computer chose scissors")
    elif play1 == 2 and play2 == 1:
        print("""You won, the computer chose Rock""")
    elif play1 == 2 and play2 == 2:
        print("It's a draw")
    elif play1 == 2 and play2 == 3:
        print("You lost, the computer chose scissors")
    elif play1 == 3 and play2 == 1:
        print("You lost, the computer chose Rock")
    elif play1 == 3 and play2 == 2:
        print("You won, the computer chose paper")
    elif play1 == 3 and play2 == 3:
        print("It's a draw")
    elif play1 > 3:
        print("Invalid input")
choose()


