import random
operations = [["Welcome to our betting app", "Login", "Ceate account"],["username", "password"],{}, ["Deposit money", "Place a bet"], {"blue", "orange","red", "white", "black", "green", "pink"}]
def begin():
    for idx,val in enumerate(operations[0], 0):
        print(f"{idx}.{val}" if idx != 0 else f"{val}\n")
    nxt = input(""); login() if nxt == "1" else register()
def register():
    for x,y in enumerate(operations[1], 1):
        x = input(f"Enter your {y}: ")
    operations[2][x] = [y, 0.0]; home(x)
def login():
    for x,y in enumerate(operations[1], 1):
        x = input(f"Enter your {y}: ")
    home(x) if x in operations[2].keys() and operations[2][x][0] == y else print("Invalid username or password\n"); begin()
def home(x):
    print(f"Welcome {x} ({operations[2][x][1]})\n")
    for i,j in enumerate(operations[3], 1):
        print(f"{i}. {j}")
    while True:
        nxt = input("")
        if nxt == "1":
            deposit(x)
        elif nxt == "2":
            bet(x)
def deposit(x):
    while True:
        try:
            nxt = float(input("Amount to deposit: ")); operations[2][x][1] += nxt
        except:
            print("Invalid input")
        else:
            home(x)
def bet(x):
    for i in operations[4]:
        print(i)
    nxt = set(input("From the list above type any Three color of your choice: ").lower().split())
    while True:
        try:
            amount = float(input("How much do you wanna stake: "))
            if ((operations[2][x][1] - amount) < 0):
                print("Insufficient balance, please deposit"); deposit(x)
        except:
            print("Invalid input")
        else:
            operations[2][x][1] -= amount
            break
    comp = ""; u = 0
    for i in range(3):
        comp += random.choice(list(operations[4]))+" "
    for i in nxt:
        if i in comp.split():
            u += 1
    print(comp, set(comp).intersection(nxt))      
    if u == 0:
        print("You lost")
    else:
        print(f"You won {amount*u}"); y = amount*(u+1); operations[2][x][1] += y
    nnx = input("\nDo you want to play again Y/N: ").lower()
    bet(x) if nnx == "y" else home(x)
begin()