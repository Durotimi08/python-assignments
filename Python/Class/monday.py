



















# questions = ["What is today's date", "Who is sodeeq"]
# options = ["A: Tuesday... B: Monday", "A. Money man... B. Python Student"]
# answers = ["b", "a"]
# score = 0
# for i in questions:
#     index = questions.index(i)
#     print(questions[index])
#     print(options[index])
#     user_ans = input("choose the correct answer ")
#     answer = answers[index]
#     if user_ans == answer:
#         print("Correct")
#         score += 10
#     else:
#         print("Wrong")
#         score -= 5
# print(f"Your score is {score}")



import random
import time
mycursor = mydb.cursor()

class Exam:
    def __init__(self):
        self.questions = ["What is today's date", "Who is sodeeq", "president of naija", "Head of SQI", "Who is Loki"]
        self.options = ["A: Tuesday B: Monday", "A: Man B: Python Student", "A: Peter Obi B: Tinubu", "A: Aderinto B: Wunmi", "A: Thor's brother B: He who remains"]
        self.answers = ["b", "b", "b", "a", "a"]
        self.score = 0
        self.cbt()
        mydb.commit()

    def cbt(self):
        action = input("""
              Welcome to the SCHOOL
              ENTER 1 to login
              ENTER 2 to register 
              """)
        if action == "1": 
            self.login()
        elif action == "2":
            self.register()
        else: 
            print("Wrong Input, try again")
            time.sleep(3)
            Exam()
        

    def test(self): 
        for i in self.questions:
            index = self.questions.index(i)
            print(self.questions[index])
            print(self.options[index])
            user_ans = input("choose the correct answer ")
            answer = self.answers[index]
            if user_ans == answer:
                # print("Correct")
                self.score += 20
            else:
                print("Wrong")
                self.score += 0
        print(f"Your score is {self.score}")
        upd = f"update student set score = {self.score} where matric = {self.mat}"
        dex = f"update student set exam_done = 'YES' where matric = {self.mat}"
        mycursor.execute(upd)
        mycursor.execute(dex)
        self.grade()

        
    def register(self):
        query = "insert into student(fname, lname, matric, password, address, gender, score, state_of_origin, course, duration, admission_status, exam_done) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        gen = random.randint(11111,55555)
        fname = input("What is the first name \n")
        lname = input("what is the last name \n")
        matric = gen
        password = input("What is your password \n")
        address = input("what is your address \n")
        gender = input("what is your gender \n")
        score = 0
        origin = input("what is your state of origin \n")
        course = input("what course would you like to study \n")
        info = (fname, lname, matric, password, address, gender, score, origin, course, '4years', 'NO', 'NO')
        mycursor.execute(query, info) 
        mydb.commit()
        print(f"Welcome {fname} {lname}, you have successfully registered & your matric number is {matric}.")
        time.sleep(2)
        self.login()

    def login(self):
        self.mat = input("Enter your matric number? \n")
        acts = f"select * from student where matric = {self.mat}"
        mycursor.execute(acts)
        self.user = mycursor.fetchone()
        if self.user == None:
            print("Invalid Matric Number, try again")
            self.login()
        password = input("Enter your password \n")
        if password in self.user[4]:
            print("Login Successful")
            self.checkTest()
        else:
            print("Incorrect Password, please try again")

    def checkTest(self):
        if self.user[12] == 'NO':
            self.test()
        elif self.user[12] == "YES":
            print("\nYou have taken the test, this is your letter")
            time.sleep(2)
            self.letter()

    def grade(self):
        if self.score >= 60:
            print("Good job, you are admitted. Hold on for your admission letter")
            drp = f"update student set admission_status = 'YES' where matric = {self.mat}"
            mycursor.execute(drp)
            time.sleep(3)
            self.letter()
        elif self.score < 60:
            print("U no sabi o, Hold on for your rejection letter")
            time.sleep(3)
            self.letter()

    def letter(self):
        if self.user[7] >= 60:
            myfile = open('/Users/sokebiz/Desktop/Python/Class/letter.txt', 'w')
            myfile.write(f"""
                        
                Dear Mr/Mrs {self.user[1]} {self.user[2]}

                                ADMISSION LETTER
                Wow! Your performance blew us away. We're over the moon to offer you admission. 
                Your dedication and talent shone throughout the test. 
                We're excited to see you grow and achieve even more in our community. 
                Welcome aboard! This is just the beginning of your amazing journey.

                The details of your admission is as follows:
                Name is {self.user[1]} {self.user[2]}, you live at {self.user[5]} and you are from {self.user[8]}.
                Your course of study is {self.user[9]} which would span for {self.user[10]} and your matric number is {self.user[3]}.


                                                                                        Yours Sincerely,
                                                                                        Ogunmepon Razaq.
                                                                                        Registrar, UI.
                """)
            myfile = open('/Users/sokebiz/Desktop/Python/Class/letter.txt', 'r')
            print(myfile.read())
            myfile.close()
        elif self.user[7] < 60:
            myfile = open('/Users/sokebiz/Desktop/Python/Class/letter.txt', 'w')
            myfile.write(f"""
                        
                Dear Mr/Mrs {self.user[1]} {self.user[2]}

                                ADMISSION LETTER
                Wow! Your performance blew us away. We're over the moon to see you fail. 
                Your dedication and talent did not show throughout the test. 
                We're excited not to see you grow and not achieve even more in our community. 
                Bye bye! This is just the beginning of your PREDICAMENT.

                The details of your REJECTED admission is as follows:
                Name is {self.user[1]} {self.user[2]}, you live at {self.user[5]} and you are from {self.user[8]}.


                                                                                        Yours Sincerely,
                                                                                        Ogunmepon Razaq.
                                                                                        Registrar, UI.
                """)
            myfile = open('/Users/sokebiz/Desktop/Python/Class/letter.txt', 'r')
            print(myfile.read())
            myfile.close()

Exam()




        
    















# Loop means repeating something over and over until a particular condition is satisfied.
# Types of Loop:
# for loop
# while loop

# A for loop is used for iterating over a sequence.


# for victor in range(2):
#     print(questions[victor])
#     print(options[victor])
#     user_ans = input("Enter your answer ").lower()
#     right_answer = answers[victor]
#     if user_ans == right_answer:
#         print("Correct")
#         score += 10
#     else:
#         print("Wwrong")
#         score -= 5
# print(f'Your score is {score}')



# A set is a collection which is unordered and unindexed
# It is written using curly bracket
# i.e {} or set()

name = {"Shade", "energy", "Shade", "Charse", "Charse", "energy"}
name2 = set((12, 14, "Sunday", "Charse", True, False, 5.08))
# print(name)

# for top in name:
#     print(top)

# print("charse" not in name)

# name.add("Tope")

# name.update(name2)

# myList = []
# for i in range(5):
#     nam = input("Enter your name ")
#     myList.append(nam)
# print(myList)

# result = []

# for i in range(3):
#     inp = input("enter any numbeer ")
#     result.append(inp)
#     print(result)

set1 = {"Ade", "Charse", "Bade"}
# list1 = ["Mango", "Energy", "Ade"]

# set1.update(list1)
# print(set1)

# set1 = {"fay", "jay"}
# list2 = ["ade", "ayo"]
# set1.update(list2)
# print(set1)

# set1.discard("Ade")
# print(set1)

# comment = "commented that this is a python class. It was started last week"
# new = comment.split()
# print(type(new))
# print(new)

# print(set(new))
# new_input = set(input("Enter here ").split())
# print(new_input)

yes = {6, 1, 2, 3, 4, 5}
s = {1, 4, 5}
# it = s.intersection(yes)

# set1 = {2, 8, 6, 4}
# set2 = {2, 4, 5, 50, 5, 7, 8, 12}
# set3 = {20, 50, 60}

# set4 = set1.union(set2).union(set3)
# set4 = set1.intersection(set2).intersection(set3)
# print(set4)

# set2 = {2, 4, 50, 5, 7, 8, 12, 13}
# set1 = {10, 50, 3, 4}
# set3 = {10, 3, 4, 20, 50, 60}

# set4 = set1.symmetric_difference(set2)
# print(set4)

# set2.symmetric_difference_update(set1)
# print(set2)

# set1 = {4, 5, 6}
# set2 = {5, 7, 8}
# set3 = {4, 8, 20, 54}
# set1.symmetric_difference_update(set2)
# print(set1)
# print(set2)

# print(set1.symmetric_difference(set2))
# print(set1)
# print(set1)

# print(set1.intersection(set3))

# print(set1.isdisjoint(set2))

# print(set2.issubset(set1))
# print(set2.issuperset(set1))





