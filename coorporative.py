import sqlite3
import time
import random

class DB:
    def __init__(self):
        try:
            self.mydb = sqlite3.connect("cooperative.db")
            self.mycursor = self.mydb.cursor()
            self.mycursor.executescript('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    memberid INTEGER NOT NULL,
                    fname TEXT NOT NULL,
                    lname TEXT NOT NULL,
                    accounttype TEXT NOT NULL,
                    approved TEXT NOT NULL,
                    quota REAL NOT NULL,
                    password TEXT NOT NULL
                );

                CREATE TABLE IF NOT EXISTS finance (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    memberid INTEGER NOT NULL,
                    borrowed REAL NOT NULL,
                    interest REAL NOT NULL
                );
                INSERT INTO users (memberid, fname, lname, accounttype, approved, quota, password) VALUES (123456, 'duro', 'timi', 'admin', 'true', 50000, 'durotimi1#');
            ''')
        except Exception as e:
            print(f"Error connecting to the database: {e}")
            self.begin()

    def select(self, table, column, figure):
        try:
            self.mycursor.execute(f"SELECT * FROM {table} WHERE {column} = ?", (figure,))
            return self.mycursor.fetchall()
        except Exception as e:
            return []

    def execute_query(self, query, data=None):
        try:
            self.mycursor.execute(query, data)
            self.mydb.commit()
            return True
        except Exception as e:
            return False

class Method(DB):
    def __init__(self, idx):
        self.result = self.select("finance", "memberid", idx)
        if self.result:
            self.id, self.memberid, self.borrowed, self.borrowed_interest = self.result[0]
        user_info = self.select("users", "memberid", idx)
        if user_info:
            user_info = user_info[0]
            self.accounttype, self.quota = user_info[4], user_info[6]

    def calculate_interest(self, amount):
        interest_rate = 0.07
        if self.accounttype == "Non-member":
            interest_rate = 0.10
        return amount + (amount * interest_rate)

    def borrow(self):
        if self.result:
            print(f"You currently owe {self.borrowed_interest}. Please pay back to receive another loan.")
            return

        while True:
            amount = abs(int(input("How much would you like to borrow($): ")))
            amount_with_interest = self.calculate_interest(amount)
            borrow_limit = self.select("users", "accounttype", "admin")
            if borrow_limit:
                borrow_limit = borrow_limit[0][6]
                if amount_with_interest > borrow_limit:
                    print("Borrowing limit exceeded. Please include a lower amount.")
                else:
                    break
            else:
                print("Admin information not found. Please check the database.")
                return

            if self.execute_query("INSERT INTO finance (memberid, borrowed, interest) VALUES (?, ?, ?)", (self.memberid, amount_with_interest - amount, amount_with_interest)):
                print(f"Borrowed {amount_with_interest}$ successfully.")
                admin_memberid = 12345
                new_quota_value = self.select("users", "memberid", admin_memberid)
                if new_quota_value:
                    new_quota_value = new_quota_value[0][6] + amount
                    self.execute_query('UPDATE users SET quota = ? WHERE memberid = ?', (new_quota_value, admin_memberid))
                else:
                    print("Admin information not found. Please check the database.")
            else:
                print("Error during the transaction.")

    def quota(self):
        current_quota = self.quota
        print(f"Your current quota is: {current_quota}\n")
        if current_quota > 0:
            while True:
                que = input("Would you like to pay your quota (yes/no)\n>>> ").lower()
                if que == "yes":
                    amount = abs(int(input("How much would you like to pay($): ")))
                    if isinstance(amount, int):
                        user_quota = self.quota - (amount + (amount / 100))
                        admin_memberid = 123456
                        admin_quota = self.select("users", "memberid", admin_memberid)
                        if admin_quota:
                            admin_quota = admin_quota[0][6] + amount
                            if self.execute_query('UPDATE users SET quota = ? WHERE memberid = ?', (user_quota, self.memberid)) and self.execute_query('UPDATE users SET quota = ? WHERE memberid = ?', (admin_quota, admin_memberid)):
                                print(f"Paid {amount}$ successfully.")
                            else:
                                print("Error during the transaction.")
                        else:
                            print("Admin information not found. Please check the database.")
                    break
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")

    def history(self):
        if not self.result:
            print("No transaction history found.")
        else:
            print("Transaction History:")
            print(f"Borrowed: {self.result[0][2]}")

    def logout(self):
        print("Logged out successfully.")
        begin()

def begin():
    print("Welcome to Ski Cooperative")
    ans = []
    try:
        operations = [
            ["Login", "Member_id", "Password"],
            ["Register", "First name", "Last name", ["Account type", "Member", "Non-member"], "Password"]
        ]
        for i in range(len(operations)):
            print(f"Enter {i + 1} to {operations[i][0]}")
        for i, j in enumerate(operations[int(input(">>> ")) - 1], 0):
            if i == 0:
                print(f"\n{j}")
            elif i == 3:
                while True:
                    for x, y in enumerate(j, 0):
                        print(f"{y}:" if x == 0 else f"  {x}. {y}")
                    choice = input(">>> ")
                    if choice in ["1", "2"]:
                        ans.extend([choice, "false", -1000])
                        break
                    print("Invalid account type.\n")
            else:
                ans.append(input(f"Enter your {j}: "))
    except Exception as e:
        return begin()
    print("\nProcessing...")
    time.sleep(2)
    if len(ans) == 2:
        result = DB().select("users", "memberid", ans[0])
        if result and len(result) > 0 and result[0][7] == ans[1]:
            print("Login successful.")
            home(result[0])
        else:
            print("Invalid member_id or password.")
            begin()
    else:
        ans.insert(0, random.randint(11111, 99999))
        if DB().execute_query("INSERT INTO users (memberid, fname, lname, accounttype, approved, quota, password) VALUES (?, ?, ?, ?, ?, ?, ?)", tuple(ans)):
            print("Registration successful.\n")
            user_info = DB().select("users", "memberid", ans[0])
            if user_info and len(user_info) > 0:
                home(user_info[0])
            else:
                print("User information not found. Please check the database.")

def home(record):
    print(f"\nWelcome {record[2]} {record[3]}({record[1]})")
    y = 1
    ansi = []
    membership = [
        ["Pay quota", Method(record[1]).quota],
        ["Borrow money", Method(record[1]).borrow],
        ["Check all transactions", Method(record[1]).history],
        ["Logout", Method(record[1]).logout]
    ]
    for x in range(len(membership)):
        ansi.append(membership[x])
        print(f"{y}. {membership[x][0]}")
        y += 1
    while True:
        try:
            ans = int(input(">>>"))
            if ans <= 0 or ans > len(ansi):
                print("Invalid input")
            else:
                ansi[ans - 1][1]()
        except Exception as e:
            print("Invalid input")
            home(record)

try:
    begin()
except Exception as e:
    print(f"Error connecting to the database: {e}")
    begin()
