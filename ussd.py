import time

first = ["Buy Data Plan", "Share Data Plan", "Check Data Balance", "Borrow Airtime", "Exit"]
second = [["Daily Plan", "Weekly Plan", "Monthly Plan", "Social Bundles"]]
third = [[["25mb for 25N", "50mb for 50N", "100mb for 100N"], ["1gb for 300N", "2gb for 500N"]]]

def display_menu(options):
    for idx, option in enumerate(options, 1):
        print(f"{idx}. {option}")
    print()

def select_option(options):
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if 1 <= choice <= len(options):
                return choice
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def buy_data_plan():
    print("Choose a Data Plan:")
    display_menu(second[0])

    second_choice = select_option(second[0])
    print(f"You have selected: {second[0][second_choice - 1]}")

    print("Available Data Plans:")
    display_menu(third[0][second_choice - 1])

    third_choice = select_option(third[0][second_choice - 1])
    print(f"You have selected: {third[0][second_choice - 1][third_choice - 1]}")
    print("Processing...")

    print("Data plan purchase successful!")

def share_data_plan():
    print("Share Data Plan functionality is not implemented yet.")
    print("Processing...")
    time.sleep(2)

def check_data_balance():
    print("Check Data Balance functionality is not implemented yet.")
    print("Processing...")
    time.sleep(2)

def borrow_airtime():
    print("Borrow Airtime functionality is not implemented yet.")
    print("Processing...")
    time.sleep(2)

while True:
    print('''
Welcome to our USSD Service''')
    display_menu(first)

    main_choice = select_option(first)

    if main_choice == 1:
        buy_data_plan()
    elif main_choice == 2:
        share_data_plan()
    elif main_choice == 3:
        check_data_balance()
    elif main_choice == 4:
        borrow_airtime()
    elif main_choice == 5:
        print("Thank you for using USSD Service. Goodbye!")
        break
