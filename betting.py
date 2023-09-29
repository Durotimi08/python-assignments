import random; import time

def begin():
    print("----------------------------------")
    print("|   Welcome to our Betting app   |")
    print("----------------------------------")
    print("|                                |")
    print("| 1. Create account   2. Sign in |")
    print("----------------------------------\n")
    nxt = input("")
    if nxt == "1":
        register()
    elif nxt == "2":
        login()
    else:
        begin()

def register():

print1()