import time; import random
list = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
games = [0, 0, 0]; k = [0]; lastmove = []; move = [True]

def check_draw():
    for i in range(len(list)):
        for j in range(len(list[i])):
            if list[i][j] == " ":
                return False
            elif ((i == 2) and (j == 2)) and (list[i][j] != " "):
                return True

def checker(letter):
    if ((list[0][0] == letter) and (list[0][1] == letter)) and (list[0][2] == letter):
        return True
    elif ((list[0][0] == letter) and (list[0][2] == letter)) and (list[0][1] == letter):
        return True
    elif ((list[0][0] == letter) and (list[1][0] == letter)) and (list[2][0] == letter):
        return True
    elif ((list[0][0] == letter) and (list[2][0] == letter)) and (list[1][0] == letter):
        return True
    elif ((list[0][1] == letter) and (list[0][2] == letter)) and (list[0][0] == letter):
        return True
    elif ((list[1][0] == letter) and (list[2][0] == letter)) and (list[0][0] == letter):
        return True
    elif ((list[0][0] == letter) and (list[1][1] == letter)) and (list[2][2] == letter):
        return True
    elif ((list[0][0] == letter) and (list[2][2] == letter)) and (list[1][1] == letter):
        return True
    elif ((list[1][1] == letter) and (list[2][2] == letter)) and (list[0][0] == letter):
        return True
    elif ((list[0][2] == letter) and (list[1][1] == letter)) and (list[2][0] == letter):
        return True
    elif ((list[0][2] == letter) and (list[2][0] == letter)) and (list[1][1] == letter):
        return True
    elif ((list[1][1] == letter) and (list[2][0] == letter)) and (list[0][2] == letter):
        return True
    elif ((list[1][0] == letter) and (list[1][1] == letter)) and (list[1][2] == letter):
        return True
    elif ((list[1][0] == letter) and (list[1][2] == letter)) and (list[1][1] == letter):
        return True
    elif ((list[1][2] == letter) and (list[1][1] == letter)) and (list[1][0] == letter):
        return True
    elif ((list[2][0] == letter) and (list[2][1] == letter)) and (list[2][2] == letter):
        return True
    elif ((list[2][0] == letter) and (list[2][2] == letter)) and (list[2][1] == letter):
        return True
    elif ((list[2][2] == letter) and (list[2][1] == letter)) and (list[2][0] == letter):
        return True
    elif ((list[0][2] == letter) and (list[1][2] == letter)) and (list[2][2] == letter):
        return True
    elif ((list[0][2] == letter) and (list[2][2] == letter)) and (list[1][2] == letter):
        return True
    elif ((list[2][2] == letter) and (list[1][2] == letter)) and (list[0][2] == letter):
        return True
    elif ((list[0][1] == letter) and (list[1][1] == letter)) and (list[2][1] == letter):
        return True
    elif ((list[0][1] == letter) and (list[2][1] == letter)) and (list[1][1] == letter):
        return True
    elif ((list[2][1] == letter) and (list[1][1] == letter)) and (list[0][1] == letter):
        return True
    else:
        return False

def pri(x,y,lastmove):
    if ((x > 0 and x < 4) and (y > 0 and y < 4)) and (list[x-1][y-1] == " "):
        if list[x-1][y-1] != comp_letter:
            list[x-1][y-1] = letter
            lastmove = [x-1, y-1]
            game()
            gengame(lastmove)
            start(lastmove)

        else:
            print("Oops! The space has been occupied")
    else:
        print("Oops! invalid input. Please enter a valid move (e.g., A1, B2, C3)")
        start(lastmove)
def game():
    print("")
    print("    1   2   3")
    print("---------------")
    print(f"A | {list[0][0]} | {list[0][1]} | {list[0][2]} |")
    print("  -------------")
    print(f"B | {list[1][0]} | {list[1][1]} | {list[1][2]} |")
    print("  -------------")
    print(f"C | {list[2][0]} | {list[2][1]} | {list[2][2]} |")
    print("")

def gengame(lastmove):
    def check():
        if ((list[0][0] == letter) and (list[0][1] == letter)) and (list[0][2] == " "):
            list[0][2] = comp_letter
            return True
        elif ((list[0][0] == letter) and (list[0][2] == letter)) and (list[0][1] == " "):
            list[0][1] = comp_letter
            return True
        elif ((list[0][0] == letter) and (list[1][0] == letter)) and (list[2][0] == " "):
            list[2][0] = comp_letter
            return True
        elif ((list[0][0] == letter) and (list[2][0] == letter)) and (list[1][0] == " "):
            list[1][0] = comp_letter
            return True
        elif ((list[0][1] == letter) and (list[0][2] == letter)) and (list[0][0] == " "):
            list[0][0] = comp_letter
            return True
        elif ((list[1][0] == letter) and (list[2][0] == letter)) and (list[0][0] == " "):
            list[0][0] = comp_letter
            return True
        elif ((list[0][0] == letter) and (list[1][1] == letter)) and (list[2][2] == " "):
            list[0][1] = comp_letter
            return True
        elif ((list[0][0] == letter) and (list[2][2] == letter)) and (list[1][1] == " "):
            list[2][0] = comp_letter
            return True
        elif ((list[1][1] == letter) and (list[2][2] == letter)) and (list[0][0] == " "):
            list[0][0] = comp_letter
            return True
        elif ((list[0][2] == letter) and (list[1][1] == letter)) and (list[2][0] == " "):
            list[2][0] = comp_letter
            return True
        elif ((list[0][2] == letter) and (list[2][0] == letter)) and (list[1][1] == " "):
            list[1][1] = comp_letter
            return True
        elif ((list[1][1] == letter) and (list[2][0] == letter)) and (list[0][2] == " "):
            list[0][2] = comp_letter
            return True
        elif ((list[1][0] == letter) and (list[1][1] == letter)) and (list[1][2] == " "):
            list[1][2] = comp_letter
            return True
        elif ((list[1][0] == letter) and (list[1][2] == letter)) and (list[1][1] == " "):
            list[1][1] = comp_letter
            return True
        elif ((list[1][2] == letter) and (list[1][1] == letter)) and (list[1][0] == " "):
            list[1][0] = comp_letter
            return True
        elif ((list[2][0] == letter) and (list[2][1] == letter)) and (list[2][2] == " "):
            list[2][2] = comp_letter
            return True
        elif ((list[2][0] == letter) and (list[2][2] == letter)) and (list[2][1] == " "):
            list[2][1] = comp_letter
            return True
        elif ((list[2][2] == letter) and (list[2][1] == letter)) and (list[2][0] == " "):
            list[2][0] = comp_letter
            return True
        elif ((list[0][2] == letter) and (list[1][2] == letter)) and (list[2][2] == " "):
            list[2][2] = comp_letter
            return True
        elif ((list[0][2] == letter) and (list[2][2] == letter)) and (list[1][2] == " "):
            list[1][2] = comp_letter
            return True
        elif ((list[2][2] == letter) and (list[1][2] == letter)) and (list[0][2] == " "):
            list[0][2] = comp_letter
            return True
        elif ((list[0][1] == letter) and (list[1][1] == letter)) and (list[2][1] == " "):
            list[2][1] = comp_letter
            return True
        elif ((list[0][1] == letter) and (list[2][1] == letter)) and (list[1][1] == " "):
            list[1][1] = comp_letter
            return True
        elif ((list[2][1] == letter) and (list[1][1] == letter)) and (list[0][1] == " "):
            list[0][1] = comp_letter
            return True
        else:
            return False
    def tacturn(num,k):
        if k == 1:
            if num == 0:
                list[2][2] = comp_letter
            elif num == 1:
                list[2][0] = comp_letter
            elif num == 2:
                list[0][0] = comp_letter
            elif num == 3:
                list[0][2] = comp_letter
        elif k == 2:
            check()

    def unstoppable(num,k):
        if k == 1:
            if num == 0:
                list[2][2] = comp_letter
            elif num == 1:
                list[0][2] = comp_letter


    def sideway(num,k):
        if k == 1:
            if num == 0:
                list[0][2] = comp_letter
            elif num == 1:
                list[2][0] = comp_letter
    def finish():
        if ((list[0][0] == comp_letter) and (list[0][1] == comp_letter)) and (list[0][2] == " "):
            list[0][2] = comp_letter
            return True
        elif ((list[0][0] == comp_letter) and (list[0][2] == comp_letter)) and (list[0][1] == " "):
            list[0][1] = comp_letter
        elif ((list[0][0] == comp_letter) and (list[1][0] == comp_letter)) and (list[2][0] == " "):
            list[2][0] = comp_letter
            return True
        elif ((list[0][0] == comp_letter) and (list[2][0] == comp_letter)) and (list[1][0] == " "):
            list[1][0] = comp_letter
        elif ((list[0][1] == comp_letter) and (list[0][2] == comp_letter)) and (list[0][0] == " "):
            list[0][0] = comp_letter
            return True
        elif ((list[1][0] == comp_letter) and (list[2][0] == comp_letter)) and (list[0][0] == " "):
            list[0][0] = comp_letter
            return True
        elif ((list[0][0] == comp_letter) and (list[1][1] == comp_letter)) and (list[2][2] == " "):
            list[0][1] = comp_letter
            return True
        elif ((list[0][0] == comp_letter) and (list[2][2] == comp_letter)) and (list[1][1] == " "):
            list[2][0] = comp_letter
        elif ((list[1][1] == comp_letter) and (list[2][2] == comp_letter)) and (list[0][0] == " "):
            list[0][0] = comp_letter
        elif ((list[0][2] == comp_letter) and (list[1][1] == comp_letter)) and (list[2][0] == " "):
            list[2][0] = comp_letter
            return True
        elif ((list[0][2] == comp_letter) and (list[2][0] == comp_letter)) and (list[1][1] == " "):
            list[1][1] = comp_letter
        elif ((list[1][1] == comp_letter) and (list[2][0] == comp_letter)) and (list[0][2] == " "):
            list[0][2] =comp_letter
            return True
        elif ((list[1][0] == comp_letter) and (list[1][1] == comp_letter)) and (list[1][2] == " "):
            list[1][2] = comp_letter
        elif ((list[1][0] == comp_letter) and (list[1][2] == comp_letter)) and (list[1][1] == " "):
            list[1][1] = comp_letter
            return True
        elif ((list[1][2] == comp_letter) and (list[1][1] == comp_letter)) and (list[1][0] == " "):
            list[1][0] = comp_letter
        elif ((list[2][0] == comp_letter) and (list[2][1] == comp_letter)) and (list[2][2] == " "):
            list[2][2] = comp_letter
            return True
        elif ((list[2][0] == comp_letter) and (list[2][2] == comp_letter)) and (list[2][1] == " "):
            list[2][1] = comp_letter
            return True
        elif ((list[2][2] == comp_letter) and (list[2][1] == comp_letter)) and (list[2][0] == " "):
            list[2][0] = comp_letter
            return True
        elif ((list[0][2] == comp_letter) and (list[1][2] == comp_letter)) and (list[2][2] == " "):
            list[2][2] = comp_letter
            return True
        elif ((list[0][2] == comp_letter) and (list[2][2] == comp_letter)) and (list[1][2] == " "):
            list[1][2] = comp_letter
            return True
        elif ((list[2][2] == comp_letter) and (list[1][2] == comp_letter)) and (list[0][2] == " "):
            list[0][2] = comp_letter
            return True
        elif ((list[0][1] == comp_letter) and (list[1][1] == comp_letter)) and (list[2][1] == " "):
            list[2][1] = comp_letter
            return True
        elif ((list[0][1] == comp_letter) and (list[2][1] == comp_letter)) and (list[1][1] == " "):
            list[1][1] = comp_letter
            return True
        elif ((list[2][1] == comp_letter) and (list[1][1] == comp_letter)) and (list[0][1] == " "):
            list[0][1] = comp_letter
            return True
        else:
            return False

    def tacticmid2(lastmove, k):
        if k[0] == 0:
            if list[1][1] != letter:
                list[1][1] = comp_letter
                k.append("mid")
            elif list[1][1] == letter:
                x = random.randint(0, 3)
                print(x)
                if x == 1:
                    list[0][0] = comp_letter
                elif x == 2:
                    list[0][2] = comp_letter
                elif x == 3:
                    list[2][0] = comp_letter
                elif x == 0:
                    list[2][2] = comp_letter
                k.append("edge")
           
        elif k[0] == 1:
            if not check():
                if k[1] == "edge":
                    if not check():
                        if list[1][0] == " ":
                            list[1][0] = comp_letter
                        else:
                            list[1][2] = comp_letter

                elif k[1] == "mid":
                    if (list[0][1] == letter) and (list[1][0] == letter):
                        list[0][0] = comp_letter
                    elif (list[0][1] == letter) and (list[1][2] == letter):
                        list[0][2] = comp_letter
                    elif (list[1][0] == letter) and (list[2][1] == letter):
                        list[2][0] = comp_letter
                    elif (list[2][1] == letter) and (list[1][2] == letter):
                        list[2][2] = comp_letter
                    else:
                        if (list[1][0] == letter) and (list[1][2] == letter):
                            list[0][2] = comp_letter
                        elif list[1][0] == " ":
                            list[1][0] = comp_letter
                        else:
                            list[1][2] = comp_letter

        elif k[0] == 2:
            if k[1] == "edge":
                finish()
                check()
            elif k[1] == "mid":
                finish()
                if not check():
                    if list[1][0] == " ":
                        list[1][0] = comp_letter
                    else:
                        list[1][2] = comp_letter
  

        elif k[0] == 3:
            if k[1] == "edge":
                finish()
                check()
            elif k[1] == "mid":
                finish()
                check()
                    
        

    def tacticmid(lastmove,k):
        if k[0] == 0:
            list[1][1] = comp_letter
        elif k[0] == 1:
            if lastmove[0] == 0:
                if lastmove[1] == 0:
                    tacturn(0,k[0])
                    k.append("turn")
                elif lastmove[1] == 1:
                    unstoppable(0,k[0])
                    k.append("unstop")
                elif lastmove[1] == 2:
                    tacturn(1,k[0])
                    k.append("turn")
            elif lastmove[0] == 1:
                if lastmove[1] == 0:
                    sideway(0,k[0])
                    k.append("side")
                elif lastmove[1] == 2:
                    sideway(1, k[0])
                    k.append("side")
            elif lastmove[0] == 2:
                if lastmove[1] == 0:
                    tacturn(3, k[0])
                    k.append("turn")
                elif lastmove[1] == 1:
                    unstoppable(1,k[0])
                    k.append("unstop")
                elif lastmove[1] == 2:
                    tacturn(2,k[0])
                    k.append("turn")
        elif k[0] == 2:
            if "turn" in k:
                if not check():
                    if ((list[0][0] == letter) and (list[2][0] == letter)) and (list[1][2] == " "):
                        list[1][2] = comp_letter
                    elif ((list[0][0] == letter) and (list[1][2] == letter)) and (list[2][1] == " "):
                        list[2][1] = comp_letter
                    elif ((list[0][2] == letter) and (list[2][1] == letter)) and (list[1][0] == " "):
                        list[1][0] = comp_letter
                    elif ((list[0][2] == letter) and (list[1][0] == letter)) and (list[2][1] == " "):
                        list[2][1] = comp_letter
                    elif ((list[2][2] == letter) and (list[1][0] == letter)) and (list[0][1] == " "):
                        list[0][1] = comp_letter
                    elif ((list[2][2] == letter) and (list[0][1] == letter)) and (list[1][0] == " "):
                        list[1][0] = comp_letter
                    elif ((list[2][0] == letter) and (list[0][1] == letter)) and (list[1][2] == " "):
                        list[1][2] = comp_letter
                    elif ((list[2][0] == letter) and (list[1][2] == letter)) and (list[0][1] == " "):
                        list[0][1] = comp_letter

            elif "side" in k:
                if not check():
                    if list[1][2] == letter:
                        list[2][2] = comp_letter
                    elif list[1][0] == letter:
                        list[0][0] = comp_letter
            
            elif "unstop" in k:
                finish()
                check()

        elif k[0] == 3:
            if "turn" in k:
                if not finish():
                    if ((list[0][0] == letter) and (list[0][2] == letter)) and (list[2][1] == letter):
                        ra = random.randint(0,1)
                        if ra == 0:
                            list[1][0] = comp_letter
                        elif ra == 1:
                            list[1][2] = comp_letter

                    elif ((list[2][2] == letter) and (list[0][1] == letter)) and (list[2][2] == letter):
                        ra = random.randint(0,1)
                        if ra == 0:
                            list[1][0] = comp_letter
                        elif ra == 1:
                            list[1][2] = comp_letter

                    elif ((list[0][0] == letter) and (list[1][2] == letter)) and (list[2][0] == letter):
                        ra = random.randint(0,1)
                        if ra == 0:
                            list[0][1] = comp_letter
                        elif ra == 1:
                            list[2][1] = comp_letter

                    elif ((list[0][2] == letter) and (list[2][2] == letter)) and (list[1][0] == letter):
                        ra = random.randint(0,1)
                        if ra == 0:
                            list[0][1] = comp_letter
                        elif ra == 1:
                            list[2][1] = comp_letter
            elif "side" in k:
                finish()
            
            elif "unstop" in k:
                finish()

        elif k[0] == 4:
            if "turn" in k:
                if not finish():
                    for i in range(len(list)):
                        for j in range(len(list[i])):
                            if  list[i][j] == " ":
                                list[i][j] = comp_letter               

    if ((list[1][1] == " ") or (list[1][1] == comp_letter)) and (move[0]):
        tacticmid(lastmove, k)
    elif (not move[0]):
        tacticmid2(lastmove, k)
    k[0] += 1
    print("Computer's turn...")
    time.sleep(0.5)


def start(lastmove):
    game()
    if checker(letter):
        print("Congratulations you won 🎉")
        list[0][0] = " "
        list[0][1] = " "
        list[0][2] = " "
        list[1][0] = " "
        list[1][1] = " "
        list[1][2] = " "
        list[2][0] = " "
        list[2][1] = " "
        list[2][2] = " "
        lastmove = []
        games[0] += 1
        print(f'Wins: {games[0]}  draws: {games[1]}  loss: {games[2]}')
        print("")
        quest = input("Would you like to play another game Y/N: ").lower()
        if quest == "y":
            bhh()
    elif checker(comp_letter):
        time.sleep(0.2)
        print("Computer won")
        list[0][0] = " "
        list[0][1] = " "
        list[0][2] = " "
        list[1][0] = " "
        list[1][1] = " "
        list[1][2] = " "
        list[2][0] = " "
        list[2][1] = " "
        list[2][2] = " "
        lastmove = []
        games[2] += 1
        print(f'Wins: {games[0]}  draws: {games[1]}  loss: {games[2]}')
        print("")
        quest = input("Would you like to play another game Y/N: ").lower()
        if quest == "y":
            bhh()
    elif check_draw():
        print("It's a draw")
        list[0][0] = " "
        list[0][1] = " "
        list[0][2] = " "
        list[1][0] = " "
        list[1][1] = " "
        list[1][2] = " "
        list[2][0] = " "
        list[2][1] = " "
        list[2][2] = " "
        lastmove = []
        games[1] += 1
        print(f'Wins: {games[0]}  draws: {games[1]}  loss: {games[2]}')
        print("")
        quest = input("Would you like to play another game Y/N: ").lower()
        if quest == "y":
                bhh()
    else:
        print("")
        try:
            splitted = input("Enter your move (e.g., A1): ").lower()
            y = int(splitted[1])
            x = splitted[0]
            if x == "a":
                x = 1
                pri(x,y,lastmove)
            elif x == "b":
                x = 2
                pri(x,y,lastmove)
            elif x == "c":
                x = 3
                pri(x,y,lastmove)
            elif len(splitted) > 2:
                print("Oops! invalid input. Please enter a valid move (e.g., A1, B2, C3)")
                start(lastmove)
            else:
                print("Oops! invalid input. Please enter a valid move (e.g., A1, B2, C3)")
                start(lastmove)
        except:
            print("Oops! invalid input. Please enter a valid move (e.g., A1, B2, C3)")
            start(lastmove)

def bhh():
    global k
    k = [0]
    move[0] = not move[0]
    if move[0]:
        gengame(lastmove)
        start(lastmove)
    else:
        start(lastmove)

def new():
    print('''Welcome to Tic-Tac-Toe
        ''')
    global comp_letter
    global letter
    letter = input("Choose 'X' or Any letter to play with: ").upper()
    if letter != "O":
        comp_letter = "O"
    else:
        comp_letter = "X"
    print()
    print(f"Computer will play as '{comp_letter}'")
    first = input("Should Computer play first Y/N: ").lower()
    print()
    if first == "y":
        move[0] = False
        bhh()
    elif first == "n":
        move[0] = True
        bhh()
