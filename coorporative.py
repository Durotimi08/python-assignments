#users (id, membeid, fname, lname, accounttype, approved, quota, password, @admin(id, membeid, fname, lname, accounttype, approved, quota, password) 
#finance(id , memberid, borrowed, contributed)
import mysql.connector as connection
import time
import random

def begin():
    print("Welcome to Ski Cooperative")
    ans = []

    try:
        for i in range(len(operations)):
            print(f"Enter {i+1} to {operations[i][0]}")

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
                    print("Invalid account type\n")
            else:
                ans.append(input(f"Enter your {j}: "))
    except:
        start()
    else:
        print("\nProcessing...")
        time.sleep(2)

        if len(ans) == 2:
            result = DB().select("users", "member_id", ans[1])

            while result:
                if result[0][-1] == ans[-1]:
                    print("Login successful")
                    home(result[0])
                else:
                    break

            print("Invalid member_id or password")
            start()
        else:
            ans.insert(0, random.randint(11111, 99999))
            while DB().insert("users", tuple(ans)):
                print("Registration successful\n")
                home(ans)

def home(record):
    if record[5] == "false":
        print("Account awaiting confirmation by admin")
    else:
        print(f"\nWelcome {record[2]} {record[3]}")
        y = 1
        ansi = []
        membership = [
            ["Pay quota", method(ans[1]).quota],
            ["Borrow money", method(ans[1]).borrow],
            ["Check all transactions", method(ans[1]).history],
            ["Logout", method(ans[1]).logout]
        ]
        for x in range(int(record[4]) - 1, len(membership)):
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

            except:
                print("Invalid input")
                home(record)

class DB:
    def __init__(self):
        try:
            self.mydb = connection.connect(host="127.0.0.1", user="root", password="", database="cooperative")
            self.mycursor = self.mydb.cursor()
            self.idx = 21123
        except:
            print("Error connecting to the database\n")
            begin()

    def select(self, table, column, figure):
        try:
            self.mycursor.execute(f"SELECT * FROM {table} WHERE {column} = {figure}")
            result = self.mycursor.fetchall()
            self.mydb.commit()
            return result
        except:
            return False

    def insert(self, table, data):
        format = (
            ("member_id", "fname", "lname", "member_type", "approved", "password")
            if table == "users"
            else ("member_id", "borrowed", "quota")
        )
        try:
            self.mycursor.execute(f"INSERT INTO {table}{format} VALUES {data}")
            self.mydb.commit()
            return True
        except:
            return False

    def update(self, column, figure, key, keyVal):
        try:
            self.mycursor.execute(f"UPDATE users SET {column} = {figure} WHERE {key} = {keyVal}")
            self.mydb.commit()
            return True
        except:
            return False
# Account operations
class method(DB, idx):
    def __init__(self):
        self.result = self.select("finance", "member_id", self.idx)
        self.id, self.memberid, self.borrowed, self.quota = self.result[0]
    def get(self, position):
        score = 0
        for i in range(len(self.result)):
            score += self.result[i][position]
        return score
    def borrow(self):
        current_borrowed = self.get(2)
        if current_borrowed:
            print(f"You curently owe {current_borrowed},\nPlease pay back to recieve another loan\n")
            return
        while True:
            amount = int(input("How much would you like to borrow($): "))
            Borrow_limit = self.select("users", "accounttype", "admin")[0][6]
            if amount > Borrow_limit:
                print("Borrowing limit exceeded\nPlease include a lower amount\n")
            else:
                break
        # Update the user's borrowed amount
        if self.update("users", "borrowed", amount, "member_id", self.memberid):
            print(f"Borrowed {amount} successfully")
        else:
            print("Error updating borrowed amount")

    def quota(self):
        current_quota = self.quota
        print(f"Your current quota is: {current_quota}\n")
        if current_quota > 0:
            while True:
                que = input("Would you like to pay your quota (yes/no)\n>>>")

    def history(self):
        if not transactions:
            print("No transaction history found")
            return
        print("Transaction History:")
        for transaction in transactions:
            print(f"Transaction ID: {transaction[0]}, Borrowed: {transaction[2]}, Contributed: {transaction[3]}")

    def logout():
        print("Logged out successfully")
        start()

operations = [
    ["Login", "Member_id", "Password"],
    ["Register", "First name", "Last name", ["Account type", "Member", "Non-member"], "Password"]
]


# def start():
#     try:
#         begin()
#     except:
#         print("Error connecting to the database\n")
#         start()
# start()
home([1, 12345, "duro", "timi", "1", "true", "10", "ski"])
