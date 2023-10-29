import sqlite3
db = sqlite3.connect('voting_app.db')
cursor = db.cursor()
cursor.executescript('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    );
    
    CREATE TABLE IF NOT EXISTS votes (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        candidate TEXT NOT NULL
    );
''')
def execute_query(query, params):
    cursor.execute(query, params)
    db.commit()
def register():
    username, password = input("Enter your username: "), input("Enter your password: ")
    execute_query("INSERT INTO users (username, password) VALUES (?, ?)", username, password)
    print("Registration successful!")
def login():
    username, password = input("Enter your username: "), input("Enter your password: ")
    cursor.execute("SELECT id FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    if user:
        print("Login successful!")
        return user[0]
    else:
        print("Invalid username or password.")
        return None
def vote(user_id):
    candidates = ["Atiku", "Tinubu", "Obi"]
    for i, candidate in enumerate(candidates, 1):
        print(f"{i}. {candidate}")
    
    choice = int(input("\nEnter the number of your chosen candidate: "))
    if 1 <= choice <= len(candidates):
        execute_query("INSERT INTO votes (user_id, candidate) VALUES (?, ?)", user_id, candidates[choice - 1])
        print("Vote submitted successfully!")
    else:
        print("Invalid choice.")
def check_votes(user_id):
    cursor.execute("SELECT candidate FROM votes WHERE user_id = ?", (user_id,))
    user_votes = cursor.fetchall()
    if user_votes:
        print("\nYour votes:")
        for vote in user_votes:
            print(f"- {vote[0]}")
    else:
        print("You have not voted yet.")
while True:
    print("\nWelcome to the Voting Application")
    print('1. Register\n2. Login\n3. Exit')
    choice = input("Enter your choice: ")
    if choice == "1":
        register()
    elif choice == "2":
        user_id = login()
        if user_id is not None:
            while True:
                print("\n1. Vote\n2. Check Votes\n3. Logout")
                inner_choice = input("Enter your choice: ")
                if inner_choice == "1":
                    vote(user_id)
                elif inner_choice == "2":
                    check_votes(user_id)
                elif inner_choice == "3":
                    print("Logged out.")
                    break
                else:
                    print("Invalid choice.")
    elif choice == "3":
        print("Goodbye!")
        cursor.close()
        db.close()
        break
    else:
        print("Invalid choice.")
