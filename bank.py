import time
import random
bank_records = {}
initial_account_balance = float(0)
operations = ["Send money", "Deposit money", "Transactions", "Logout"]

def begin():
   print('''Welcome to NATH bank
      ''')
   
def generate_account_number():
   account_number = ""
   for i in range(10):
      value = random.randint(0,9)
      account_number += str(value)
   return account_number

def registration():
   print("Create an account")
   first_name = input("Firstname: ").upper()
   last_name = input("Lastname: ")
   password = input("password: ")
   confirm = True
   while confirm:
      try:
         year_of_birth = int(input("Year of birth: "))
         if (2023 - year_of_birth) < 18:
            print()
            print("You are too young to create an account")
            confirm = False
         else:
            confirm = False
            print()
            print("Processing...")
            account_number = generate_account_number()
            bank_records[account_number] = [first_name, last_name, password, year_of_birth, account_number, initial_account_balance, []]
            time.sleep(0.6)
            home(bank_records[account_number])
      except:
         print("Invalid year of birth")

def login():
   confirm = True
   print("Login to your account")
   while confirm:
      try:
         account_number = int(input("Account number: "))
         password = int(input("Password: "))
         print()
         print("Processing...")
         time.sleep(0.6)
         if bank_records [account_number][2] == password:
            home(bank_records [account_number])
            confirm = False
         else:
            print("Invalid account number or password")
      except:
         print("Invalid account number or password")

def home(account):
      print()
      print(f"Welcome {account[0]}")
      print()
      print(f"Bal: ${account[5]}")
      for idx,value in enumerate(operations, 1):
         print(f" {idx}. {value}")
      print()
      confirm = True
      while confirm:
         try:
            val = int(input("Which operation will you like to perform: "))    
            print("Processing...")
            time.sleep(0.6)
            print()
            send_money(account)
         except:
            print("Invaid input")
         else:
            confirm = False

def send_money(account):
   print("Send money")
   print()
   x = 0
   for y in range(bank_records.values()):
      x += 1
      if y[4] == account[4]:
         x -= 1
      else:
         print(f"{x}. {y[0]} {y[1]}")
   if x == 0:
      print("Sorry! no user available to send money to")
      home(account)
   nxt = int(input("Who will you like to send money to: "))
   if (nxt > 0) and (nxt <= x):
      nxt = float(input("How much do you want to transfer: "))
      if (account[5] - nxt) < 0:
         print("Sorry! unsufficient balance")
      else:
         print("Processing...")
         print()
         time.sleep(0.6)
   else:
      print("Invalid input")
      time.sleep(0.6)
      home(account)

home(["duro","ski","ad","2000", "123", "0.0"])