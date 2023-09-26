import time
import random
bank_records = {}
initial_account_balance = float(0)
operations = ["Send money", "Deposit money", "Donate to charity", "Logout"]

def begin():
   print('''Welcome to NATH bank
      ''')
   print("1. Create an account")
   print("2. Sign in to your account")
   confirm = True
   while confirm:
      try:
         nxt = int(input("Which operation will you like to perform: "))
         print()
         if nxt == 1:
            registration()
         elif nxt == 2:
            login()
      except:
         print("Invalid input")
      finally:
         begin()
         
   
def generate_account_number():
   account_number = ""
   for i in range(10):
      value = random.randint(0,9)
      account_number += str(value)
   return account_number

def registration():
   print("Create an account")
   first_name = input("Input your Firstname: ").upper()
   last_name = input("Input your Lastname: ")
   password = input("Create a password: ")
   confirm = True
   while confirm:
      try:
         year_of_birth = int(input("Year of birth: "))
         if (2023 - year_of_birth) < 18:
            print()
            print("You are too young to create an account")
            begin()
            confirm = False
         else:
            confirm = False
      except:
         print("Invalid year of birth")
   confirm = True
   while confirm:
      try:
         pin = input("Set-up your 4-digit pin: ")
         if len(pin) != 4:
            print("Invalid input")
         else:
            account_number = generate_account_number()
            bank_records[account_number] = [first_name, last_name, password, year_of_birth, account_number, initial_account_balance, [], str(pin)]
            print()
            print("Processing...")
            time.sleep(0.6)
            home(bank_records[account_number])
      except:
         print("Invalid input")

def login():
   confirm = True
   print("Login to your account")
   while confirm:
      try:
         account_number = input("Account number: ")
         password = input("Password: ")
         print()
         print("Processing...")
         time.sleep(0.6)
         if bank_records[account_number][2] == password:
            home(bank_records[account_number])
            confirm = False
         else:
            print("Invalid account number or password")
      except:
         print("Invalid account number or password")

def home(account):
      print()
      print(f"Welcome {account[0]}({account[4]})")
      for i in account[6]:
         print(f"{i}")
      account[6].clear()
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
            if val == 1:
               send_money(account)
            elif val == 2:
               deposit_money(account)
            elif val == 3:
               donate(account)
            elif val == 4:
               print("Thanks for banking with us 😊")
               begin()
         except:
            print("Invaid input")
         else:
            confirm = False

def send_money(account):
   print("Send money to:")
   x = 0
   z = []
   for i,y in bank_records.items():
      x += 1
      if y[4] == account[4]:
         x -= 1
      else:
         print(f"{x}. {y[0]} {y[1]}")
         z.append(i)
   if x == 0:
      print("Sorry! no user available to send money to")
      home(account)
   nxt = int(input("Who will you like to send money to: "))
   if (nxt > 0) and (nxt <= x):
      nxt2 = float(input("How much do you want to transfer: "))
      if (account[5] - nxt) < 0:
         print("Sorry! unsufficient balance")
      else:
         password = int(input("Enter 4-digit pin: "))
         if password == account[7]:
            print("Processing...")
            print()
            time.sleep(0.6)
            bank_records[z[nxt-1]][5] += nxt2
            account[5] -= nxt2
            bank_records[z[nxt-1]][6].append(f"Recieved {nxt2} from {account[0]} {account[1]}")
            print("Transfer succesful")
            home(account)
         else:
            print("Invalid input")
            time.sleep(0.6)
            home(account)
   else:
      print("Invalid input")
      time.sleep(0.6)
      home(account)

def deposit_money(account):
   nxt = int(input("How much do you want to add: "))
   account[5] += nxt
   print()
   print("Processing...")
   time.sleep(0.6)
   print("Deposit completed successfully ✔")
   home(account)

def donate(account):
   nxt = int(input("How much do you want to donate: "))
   if (account[5] - nxt) < 0:
      print("Sorry! unsufficient balance")
      time.sleep(0.6)
      home(account)
   else:
      password = input("Enter 4-digit pin: ")
      if (password == account[7]):
         print("Processing...")
         print()
         time.sleep(0.6)
         account[5] -= nxt
         print("Thanks for donating to those in need ❤")
         home(account)
      else:
         print("Invalid input")
         time.sleep(0.6)
         home(account)

begin()