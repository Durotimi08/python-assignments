import random
tests = [["1. Math ", []]]
scores = {}
def opera():
    print(""); test()
def test():
    testss = ""  
    global username
    username = input("Please enter your username: ")
    for i in range(len(tests)):
        testss += tests[i][0]
    print(testss); first = input("Please select the subject: ")
    if first == "1":
        genmath(int(num)); print(""); score = 0
        for i in range(len(tests[0][1])):
            if tests[0][1][i][2] == 0:
                print(f"solve {tests[0][1][i][0]} * {tests[0][1][i][1]}")
                k = 1; arry = []
                for o in tests[0][1][i][3]:
                    print(f"{k}. {o}")
                    j = tests[0][1][i][0] * tests[0][1][i][1]
                    if o == j:
                        arry.append(k)
                    k += 1
                print("")
                anss = input("Choose an answer: ")
                if anss == str(arry[0]):
                    arry.clear()
                    score += 1
                print("")
            elif tests[0][1][i][2] == 1:
                print(f"solve {tests[0][1][i][0]} + {tests[0][1][i][1]}")
                k = 1; arry = []
                for o in tests[0][1][i][3]:
                    print(f"{k}. {o}")
                    j = tests[0][1][i][0] + tests[0][1][i][1]
                    if o == j:
                        arry.append(k)
                    k += 1
                print(""); anss = input("Choose an answer: ")
                if anss == str(arry[0]):
                    arry.clear()
                    score += 1
                print("")
            elif tests[0][1][i][2] == 2:
                print(f"solve {tests[0][1][i][0]} - {tests[0][1][i][1]}")
                k = 1; arry = []
                for o in tests[0][1][i][3]:
                    print(f"{k}. {o}")
                    j = tests[0][1][i][0] - tests[0][1][i][1]
                    if o == j:
                        arry.append(k)
                    k += 1
                print("")
                anss = input("Choose an answer: ")
                if anss == str(arry[0]):
                    arry.clear()
                    score += 1
                print("")
        try:
            total = round((score*100)/int(num))
        except:
            total = 0
        print(f"Your Percentage is {total}%")
        if total >= 75:
            print("You got an A 👍")
        elif total >= 65:
            print("You got a B")
        elif total >= 50:
            print("You got a C")
        elif total >= 30:
            print("You got a D")
        else:
            print("You Failed, Better luck next time")
        scores[username] = score
def genmath(num):
    tests[0][1].clear()
    for i in range(num):
        f = random.randint(0, 2)
        if f == 0:
            x = random.randint(1, 20); y = random.randint(1, 20); ans = x*y
            other_opt1 = ans+x; other_opt2 = ans/x; other_opt3 = ans/-y-x
            tests[0][1].extend([[x, y, f, set((round(other_opt1), round(other_opt2), round(other_opt3), ans))]])
        elif f == 1:
            x = random.randint(1, 20); y = random.randint(1, 20); ans = x+y
            other_opt1 = ans+x; other_opt2 = ans+x+y; other_opt3 = ans-x-y
            tests[0][1].extend([[x, y, f, set((round(other_opt1), round(other_opt2), round(other_opt3), ans))]])  
        elif f == 2:
            x = random.randint(1, 20); y = random.randint(1, 20); ans = x-y
            other_opt1 = ans-x; other_opt2 = ans/x-y; other_opt3 = ans-x-y
            tests[0][1].extend([[x, y, f, set((round(other_opt1), round(other_opt2), round(other_opt3), ans))]])

def begin():
    print("Welcome to our cbt app"); print()
    global num
    stu = int(input("How many students will be taking this test: "))
    num = input("How many questions will they be answering: ")
    for i in range(stu):
        opera()
    print()
    print("The scores are as follows")
    for x,y in scores.items():
        print(f"{x}: {y}/{num}")
