import mysql.connector
#cursor.execute('''
#    CREATE TABLE IF NOT EXISTS users (
#        id INTEGER PRIMARY KEY AUTOINCREMENT,
#        username TEXT UNIQUE NOT NULL,
#       password TEXT NOT NULL
#    )
#''')
#cursor.execute('''
 #   CREATE TABLE IF NOT EXISTS votes (
#        id INTEGER PRIMARY KEY AUTOINCREMENT,
#       user_id INTEGER,
#        candidate TEXT NOT NULL
#    )
#''')
# Connect to the MySQL database
db = mysql.connector.connect(
    host="your_host",
    user="your_user",
    password="your_password",
    database="voting_app"
)
cursor = db.cursor()

def register():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
    db.commit()
    print("Registration successful!")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    cursor.execute("SELECT id FROM users WHERE username = %s AND password = %s", (username, password))
    user = cursor.fetchone()
    if user:
        print("Login successful!")
        return user[0]
    else:
        print("Invalid username or password.")
        return None

def vote(user_id):
    print("Available candidates:")
    candidates = ["Candidate 1", "Candidate 2", "Candidate 3"]

    for i, candidate in enumerate(candidates, 1):
        print(f"{i}. {candidate}")

    choice = int(input("Enter the number of your chosen candidate: "))
    if 1 <= choice <= len(candidates):
        cursor.execute("INSERT INTO votes (user_id, candidate) VALUES (%s, %s)", (user_id, candidates[choice - 1]))
        db.commit()
        print("Vote submitted successfully!")
    else:
        print("Invalid choice.")

def check_votes(user_id):
    cursor.execute("SELECT candidate FROM votes WHERE user_id = %s", (user_id,))
    user_votes = cursor.fetchall()
    if user_votes:
        print("Your votes:")
        for vote in user_votes:
            print(f"- {vote[0]}")
    else:
        print("You have not voted yet.")

while True:
    print("\nWelcome to the Voting Application")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        register()
    elif choice == "2":
        user_id = login()
        if user_id is not None:
            while True:
                print("\n1. Vote")
                print("2. Check Votes")
                print("3. Logout")
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
