import time
import json
import random

#dictionary for storing data
f = open("db.json", "r")
x = json.loads(f.read())
bank_records = x

#setting the initial account balance on register
initial_account_balance = float(0)

#operations that can be performed with the bank app
operations = ["Send money", "Deposit money", "Donate to charity", "Logout"]

#first function to be initialized
def begin():
   print("Welcome to NATH bank\n")
   print("1. Create an account")
   print("2. Sign in to your account")
   
   while True:
      try:
         choice = int(input("Which operation will you like to perform: "))
         if choice == 1:
               registration()
         elif choice == 2:
               login()
         else:
               print("Invalid choice. Please select 1 or 2.")
      except ValueError:
         print("Invalid input. Please enter a valid number.")

def update():
    x = json.dumps(bank_records)
    f = open("db.json", "w")
    f.write(x)
    f.close()
          
#generating account number for new users  
def generate_account_number():
   account_number = ""
   for i in range(10):
      value = random.randint(0,9)
      account_number += str(value)
   return account_number

#registration for bank app
def registration():
   print("\nCreate an account")
   first_name = input("Input your Firstname: ").upper()
   last_name = input("Input your Lastname: ")
   password = input("Create a password: ")
   while True:
      try:
         year_of_birth = int(input("Year of birth: "))
         if (2023 - year_of_birth) < 18:
               print("\nYou are too young to create an account")
               return begin()
         break
      except ValueError:
         print("Invalid year of birth")
   while True:
      pin = input("Set-up your 4-digit pin: ")
      if len(pin) != 4:
         print("Invalid input")
      else:
         account_number = generate_account_number()
         bank_records[account_number] = [first_name, last_name, password, year_of_birth, account_number, initial_account_balance, [], pin]
         update()
         print("\nProcessing...")
         time.sleep(0.6)
         home(bank_records[account_number])

#login for bank app
def login():
   print("\nLogin to your account")
   while True:
      account_number = input("Account number: ")
      password = input("Password: ")
      print("\nProcessing...")
      time.sleep(0.6)
      if account_number in bank_records and bank_records[account_number][2] == password:
         home(bank_records[account_number])
         break
      else:
         print("Invalid account number or password")
         nxt = input("Do you want to create an account Y/N: ").lower()
         if nxt == "y":
            registration()
         print()

#home page for bank app
def home(account):
      print()
      print(f"Welcome {account[0]}({account[4]})")
      for i in account[6]:
         print(f"{i}")
      account[6].clear()
      update()
      print()
      print(f"Bal: ${account[5]}")
      for idx,value in enumerate(operations, 1):
         print(f" {idx}. {value}")
      print()
      while True:
         try:
               choice = int(input("Which operation will you like to perform: "))
               if choice == 1:
                  send_money(account)
               elif choice == 2:
                  deposit_money(account)
               elif choice == 3:
                  donate(account)
               elif choice == 4:
                  print("Thanks for banking with us 😊")
                  return begin()
               else:
                  print("Invalid choice. Please select 1, 2, 3, or 4.")
         except ValueError:
               print("Invalid input. Please enter a valid number.")

#send money operation
def send_money(account):
   print("\nSend money to:")
   recipients = []
   for acc_num, details in bank_records.items():
      if acc_num != account[4]:
         recipients.append(acc_num)
         print(f"{len(recipients)}. {details[0]} {details[1]}")
   if not recipients:
      print("Sorry! no user available to send money to")
      return home(account)
   
   while True:
      try:
         choice = int(input("Who will you like to send money to: "))
         if 1 <= choice <= len(recipients):
               recipient_acc_num = recipients[choice - 1]
               amount = float(input("How much do you want to transfer: "))
               
               if account[5] - amount < 0:
                  print("Sorry! insufficient balance")
               else:
                  pin = input("Enter 4-digit pin: ")
                  if pin == account[7]:
                     print("Processing...")
                     time.sleep(0.6)
                     bank_records[recipient_acc_num][5] += amount
                     account[5] -= amount
                     bank_records[recipient_acc_num][6].append(f"Received ${amount} from {account[0]} {account[1]}")
                     update()
                     print("Transfer successful")
                  else:
                     print("Invalid pin")
               return home(account)
         else:
               print("Invalid choice. Please select a valid recipient.")
      except ValueError:
         print("Invalid input. Please enter a valid number.")

#deposit money operation
def deposit_money(account):
   nxt = float(input("How much do you want to add: "))
   account[5] += nxt
   update()
   print()
   print("Processing...")
   time.sleep(0.6)
   print("Deposit completed successfully ✔")
   home(account)

#donate money operation
def donate(account):
   nxt = float(input("How much do you want to donate: "))
   if (account[5] - nxt) < 0:
      print("Sorry! unsufficient balance")
      time.sleep(0.6)
   else:
      password = input("Enter 4-digit pin: ")
      if (password == account[7]):
         print("Processing...")
         print()
         time.sleep(0.6)
         account[5] -= nxt
         update()
         print("Thanks for donating to those in need ❤")
      else:
         print("Invalid pin")
         time.sleep(0.6)
   home(account)

begin()