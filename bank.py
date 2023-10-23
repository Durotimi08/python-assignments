import time
import json
import random

class bank:
   def __init__(self):
      #dictionary for storing data
      f = open("db.json", "r")
      x = json.loads(f.read())
      self.bank_records = x
      #setting the initial account balance on register
      self.initial_account_balance = float(0)

      #operations that can be performed with the bank app
      self.operations = ["Send money", "Deposit money", "Donate to charity", "Logout"]

   def update(self):
      x = json.dumps(self.bank_records)
      f = open("db.json", "w")
      f.write(x)
      f.close()
            
   #generating account number for new users  
   def generate_account_number(self):
      account_number = ""
      for i in range(10):
         value = random.randint(0,9)
         account_number += str(value)
      return account_number

   #registration for bank app
   def registration(self):
      print("\nCreate an account")
      first_name = input("Input your Firstname: ").upper()
      last_name = input("Input your Lastname: ")
      password = input("Create a password: ")
      while True:
         try:
            year_of_birth = int(input("Year of birth: "))
            if (2023 - year_of_birth) < 18:
                  print("\nYou are too young to create an account")
                  return
            break
         except ValueError:
            print("Invalid year of birth")
      while True:
         pin = input("Set-up your 4-digit pin: ")
         if len(pin) != 4:
            print("Invalid input")
         else:
            account_number = self.generate_account_number()
            self.bank_records[account_number] = [first_name, last_name, password, year_of_birth, account_number, self.initial_account_balance, [], pin]
            self.update()
            print("\nProcessing...")
            time.sleep(0.6)
            return self.bank_records[account_number]

   #login for bank app
   def login(self):
      print("\nLogin to your account")
      while True:
         account_number = input("Account number: ")
         password = input("Password: ")
         print("\nProcessing...")
         time.sleep(0.6)
         if account_number in self.bank_records and self.bank_records[account_number][2] == password:
            return self.bank_records[account_number]
            break
         else:
            print("Invalid account number or password")
            nxt = input("Do you want to create an account Y/N: ").lower()
            if nxt == "y":
               self.registration()
            print()

   #send money operation
   def send_money(self, account):
      print("\nSend money to:")
      recipients = []
      for acc_num, details in self.bank_records.items():
         if acc_num != account[4]:
            recipients.append(acc_num)
            print(f"{len(recipients)}. {details[0]} {details[1]}")
      if not recipients:
         print("Sorry! no user available to send money to")
         return self.home(account)
      
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
                        self.bank_records[recipient_acc_num][5] += amount
                        account[5] -= amount
                        self.bank_records[recipient_acc_num][6].append(f"Received ${amount} from {account[0]} {account[1]}")
                        self.update()
                        print("Transfer successful")
                     else:
                        print("Invalid pin")
                  return self.home(account)
            else:
                  print("Invalid choice. Please select a valid recipient.")
         except ValueError:
            print("Invalid input. Please enter a valid number.")

   #deposit money operation
   def deposit_money(self, account):
      nxt = float(input("How much do you want to add: "))
      account[5] += nxt
      self.update()
      print()
      print("Processing...")
      time.sleep(0.6)
      print("Deposit completed successfully ✔")
      self.home(account)

   #donate money operation
   def donate(self, account):
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
            self.update()
            print("Thanks for donating to those in need ❤")
         else:
            print("Invalid pin")
            time.sleep(0.6)
      self.home(account)

class user(bank):
   def __init__(self):
      self.home(self.begin())
   #first function to be initialized
   def begin(self):
      print("Welcome to NATH bank\n")
      print("1. Create an account")
      print("2. Sign in to your account")
      
      while True:
         try:
            choice = int(input("Which operation will you like to perform: "))
            if choice == 1:
                  self.registration()
            elif choice == 2:
                  self.login()
            else:
                  print("Invalid choice. Please select 1 or 2.")
         except ValueError:
            print("Invalid input. Please enter a valid number.")
   
   #home page for bank app
   def home(self, account):
         print()
         print(f"Welcome {account[0]}({account[4]})")
         for i in account[6]:
            print(f"{i}")
         account[6].clear()
         self.update()
         print()
         print(f"Bal: ${account[5]}")
         for idx,value in enumerate(self.operations, 1):
            print(f" {idx}. {value}")
         print()
         while True:
            try:
                  choice = int(input("Which operation will you like to perform: "))
                  if choice == 1:
                     self.send_money(account)
                  elif choice == 2:
                     self.deposit_money(account)
                  elif choice == 3:
                     self.donate(account)
                  elif choice == 4:
                     print("Thanks for banking with us 😊")
                     return self.begin()
                  else:
                     print("Invalid choice. Please select 1, 2, 3, or 4.")
            except ValueError:
                  print("Invalid input. Please enter a valid number.")
user()