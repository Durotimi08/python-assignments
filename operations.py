operatio = ["Intersection", "isdisjoint", "Union", "Symmetric_difference_update"]
box = []

def begin():
    for i in range(3):
        first = input(f'Input your desired numbers for List {i+1}: ').split()
        box.append(set(first))
    show()

def show():
    print("")
    for i in range(len(operatio)):
        print(f'{i+1}  {operatio[i]}')
    print("")
    answer = input("Which of the following operations do you want to perform: ")
    if answer == "1":
        box4 = box[0].intersection(box[1]).intersection(box[2])
        print(box4) 
    elif answer == "2":
        print(box[0].isdisjoint(box[1]) and box[1].isdisjoint(box[2]))
    elif answer == "3":
        box4 = box[0].union(box[1]).union(box[2])
        print(box4)
    elif answer == "4":
        box4 = box[0]
        box4.symmetric_difference_update(box[1])
        box4.symmetric_difference_update(box[2])
        print(box4)
    print("")
    again = input("Do you want to perform another operation Y/N: ").lower()
    if again == "y":
        show()
begin()      

