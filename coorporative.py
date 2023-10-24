#users (id, membeid, fname, lname, accounttype, approved, quota, password, @admin(id, membeid, fname, lname, accounttype, approved, quota, password) 
#finance(id , memberid, borrowed, interest)
import mysql.connector as connection, time, random

DB_HOST, DB_USER, DB_PASSWORD, DB_DATABASE = "127.0.0.1", "root", "", "cooperative"
class DB:
    def __init__(self):
        try:
            self.mydb = connection.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_DATABASE)
            self.mycursor = self.mydb.cursor()
        except: print("Error connecting to the database\n") or self.begin()
    def select(self, table, column, figure):
        try:
            self.mycursor.execute(f"SELECT * FROM {table} WHERE {column} = %s", (figure,))
            return self.mycursor.fetchall()
        except: return False
    def execute_query(self, query, data=None):
        try:
            self.mycursor.execute(query, data)
            self.mydb.commit()
            return True
        except: return False
class Method(DB):
    def __init__(self, idx):
        super().__init__()
        self.idx, result = idx, self.select("finance", "memberid", idx)
        self.id, self.memberid, self.borrowed, self.quota = result[0] if result else [print("No data found for the provided member ID")]
    def borrow(self):
        if self.get(2): print(f"You currently owe {self.get(2)}.\nPlease pay back to receive another loan.\n"); return
        while True:
            amount = abs(int(input("How much would you like to borrow($): "))
            borrow_limit = self.select("users", "accounttype", "admin")[0][6]
            if amount > borrow_limit: print("Borrowing limit exceeded.\nPlease include a lower amount.\n")
            else: break
        if self.update("finance", "borrowed", amount, "memberid", self.memberid): print(f"Borrowed {amount}$ successfully.")
        else: print("Error during transaction.")
    def quota(self):
        current_quota = self.quota
        print(f"Your current quota is: {current_quota}\n")
        if current_quota > 0:
            while True:
                que = input("Would you like to pay your quota (yes/no)\n>>> ").lower()
                if que == "yes":
                    amount = abs(int(input("How much would you like to pay($): "))
                    if isinstance(amount, int):
                        if self.update("users", "quota", self.get("users", "memberid", self.idx)[0][6] - (amount + (amount / 100)), "memberid", self.memberid) and self.update("users", "quota", self.get("users", "memberid", "admin")[0][6] + amount, "memberid", admin):
                            print(f"Paid {amount}$ successfully.")
                        else:
                            print("Error during transaction.")
                    break
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")
    def history(self):
        if not self.result: print("No transaction history found."); return
        print("Transaction History:")
        print(f"Borrowed: {self.result[0][2]}")
    def logout(self):
        print("Logged out successfully.")
        self.start()
def begin():
    print("Welcome to Ski Cooperative")
    ans = []
    try:
        operations = [
            ["Login", "Member_id", "Password"], ["Register", "First name", "Last name", ["Account type", "Member", "Non-member"], "Password"]
        ]
        for i in range(len(operations)): print(f"Enter {i + 1} to {operations[i][0]}")
        for i, j in enumerate(operations[int(input(">>> ")) - 1], 0):
            if i == 0: print(f"\n{j}")
            elif i == 3:
                while True:
                    for x, y in enumerate(j, 0):
                        print(f"{y}:" if x == 0 else f"  {x}. {y}")
                    choice = input(">>> ")
                    if choice in ["1", "2"]:
                        ans.extend([choice, "false", -1000])
                        break
                    print("Invalid account type.\n")
            else: ans.append(input(f"Enter your {j}: "))
    except: return self.start()
    print("\nProcessing..."); time.sleep(2)
    if len(ans) == 2:
        result = DB().select("users", "memberid", ans[1])
        while result:
            if result[0][-1] == ans[-1]: print("Login successful.") or home(result[0])
            else: break
        print("Invalid member_id or password.") or self.start()
    else:
        ans.insert(0, random.randint(11111, 99999))
        while DB().insert("users", tuple(ans)):
            print("Registration successful.\n") or home(ans)
def home(record):
    if record[4] == "false": print("Account awaiting confirmation by admin.")
    else:
        print(f"\nWelcome {record[2]} {record[3]}")
        y = 1; ansi = []
        membership = [
            ["Pay quota", Method(record[1]).quota], ["Borrow money", Method(record[1]).borrow], ["Check all transactions", Method(record[1]).history], ["Logout", Method(record[1]).logout]
        ]
        for x in range(int(record[4]) - 1, len(membership)):
            ansi.append(membership[x])
            print(f"{y}. {membership[x][0]}")
            y += 1
        while True:
            try:
                ans = int(input(">>>")
                if ans <= 0 or ans > len(ansi): print("Invalid input")
                else: ansi[ans - 1][1]()
            except: print("Invalid input") or home(record)
try:
    begin()
except: print("Error connecting to the database\n") or begin()
# home([1, 12345, "duro", "timi", "1", "true", "10", "ski"])
