import mysql.connector as connection
import time; import random
<<<<<<< HEAD
mydb =  
=======
mydb = connection.connect(host="127.0.0.1", user="root", password="", database="project1"); mycursor = mydb.cursor()
>>>>>>> 591e483a3d774fd997061e673ac5abe155bf5e9e
operations = [["Matric_no", "Password"], ["First-name", "Last-name", "gender", "course", "address", "password"], [], [["Who killed Mohbad", 2, "Sorry but no evidence",["Sam larry", "Naira marley", " Sucide", "Zinoleesky"]], ["is '4' > '18'", 3, "You cant perform arithmetric operation on strings", ["yes", "no", "error", "no idea"]], ["What is our tutor name", 1, "😁",["Nath", "ola", " sodiq", "fola"]], ["What is my name", 2, "My name is durotimi", ["Duro", "Durotimi", " Money man", "Senior dev"]], ["explain python", 1, "python is actually a snake", ["A snake", "A programming language", "Nath`s girlfriend", "No idea"]]]]
def begin():
   ans = input("Welcome to our cbt portal \n Enter 1 to login \n Enter 2 to regiser \n >>> ")
   sign(int(ans)-1) if  ans  == "1" or ans == "2" else begin()
def sign(val):
   operations[2] = []
   for i in operations[val]:
      val = "ans"+str(i); val = input(f"Enter your {i}: "); operations[2].append(val)
   x = query()
   home(x) if x else print("Invalid input\n"); begin()
def query():
   print("Processing..."); time.sleep(2)
   if len(operations[2]) == 6:
      operations[2].insert(0, random.randint(11111, 99999))
      mycursor.execute('insert into users(matric_number, first_name, last_name, gender, course, address, password, score) values(%s, %s, %s, %s, %s, %s, %s, 0)', tuple(operations[2]))
   mycursor.execute(f"select * from users where matric_number={operations[2][0]}")
   result = mycursor.fetchone(); mydb.commit()
   if result:
      if result[4] == operations[2][-1]:
         return result[1]
      else:
         return False
   else:
      return False
def home(matric):
   mycursor.execute(f"select * from users where matric_number={matric}"); result = mycursor.fetchone()
   while True:
<<<<<<< HEAD
      ans = input(f"\nWelcome, your matric number is ({matric}) \n Enter 1 to Take a test \n Enter 2 to print admission letter \n Enter 3 to Logout \n >>> ")
=======
      ans = input(f"\nWelcome {result[2]} {result[3]}, your matric number is ({matric}) \n Enter 1 to Take a test \n Enter 2 to print admission letter \n Enter 3 to Logout \n >>> ")
>>>>>>> 591e483a3d774fd997061e673ac5abe155bf5e9e
      if ans == "1":
         if result[-1] > 60:
            print("You have already been offered admission\n"); time.sleep(2)
         else:
            scor = test()
            if scor < 60:
               print("Sorry! your admission has been rejected\n"); time.sleep(2)
            else:
               print("Congratulations Your admission has been accepted\n"); time.sleep(2)
               mycursor.execute(f"update users set score ={scor} where matric_number = {result[1]}")
      elif ans == "2":
         if result[8] > 60:
            with open("admission.txt", mode="x") as f:
               f.write(letter(result[2])); f.close(); print("Successfully saved to this folder\n"); time.sleep(2)
         else:
            print("Sorry! no admission letter available for you\n"); time.sleep(2)
      elif ans == "3":
         begin()
      mydb.commit()   
def letter(name):
   with open("letter.txt", "r") as f:
      x = f.read(); f.close()
   y = x.replace("nameee", name)
   return y
def test():
   score = 0
<<<<<<< HEAD
=======
   print("\nThere are a total of 5 questions, 20 marks each, be sure to read and answer them carefully, Good luck\n")
>>>>>>> 591e483a3d774fd997061e673ac5abe155bf5e9e
   for i in range(len(operations[3])):
      print(operations[3][i][0])
      for j,x in enumerate(operations[3][i][3], 1):
         print(f"  {j}. {x}")
      ans = input(">>> ")
      print(f"Wrong ({operations[3][i][2]})\n") if ans != str(operations[3][i][1]) else print("correct\n"); score += 20
   print(f"Your score is {score}"); time.sleep(2)
   return score
begin()