phone_book = {
    "tolu": "0803471727",
    "shade": "0813471727",
    "tola": "0903471727",
    "mikey": "0803473727",
    "sodiq": "0703463727"
}
actions = ["See all numbers", "Add a number", "Add multiple numbers", "Delete a name", "Clear the phonebook"]

def show():
    print("Welcome user")
    for i in range(len(actions)):
        print(f'{i+1} {actions[i]}')
    print("")
    answer = input("Which action would you like to peform: ")
    print("")
    if answer == "1":
        k = 1
        for x,y in phone_book.items():
            print(f'{k}: {x} {y}')
            k += 1
    elif answer == "2":
        name = input("Choose name: ")
        number = input("Enter the number: ")
        phone_book[name] = number
        print("")
        print("Successfully completed")
    elif answer == "3":
        arr = {}
        def mult():
            name = input("Enter name or Enter stop to End: ").lower()
            if name == "stop":
                k = 0
                phone_book.update(arr)
                for i in arr.keys():
                    k += 1
                print(f"Successfully added {k} numbers")
            else:
                number = input("Enter the number: ")
                arr[name] = number
                print("")
                mult()
        mult()
    elif answer == "4":
        name = input("Enter name to be deleted: ").lower()
        if name in phone_book.keys():
            phone_book.pop(name)
            print("Successfully deleted")
        else:
            print("Wrong name inputed")
    elif answer == "5":
        phone_book.clear()
        print("Successfully completed")
    print("")
    lastq = input("Would you like to perform another action Y/N: ").lower()
    if lastq == "y":
        show()
