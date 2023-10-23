# myFile = open('filename', mode='r', 'a', 'w', 'x', encoding='t', 'b')

# myfile = open('/Users/sokebiz/Desktop/Python/Class/letter.txt', 'x')
# myfile = open('/Users/sokebiz/Desktop/Python/Class/letter.txt', 'a')
myfile = open('/Users/sokebiz/Desktop/Python/Class/letter.txt', 'w')
myfile.write("Hello World!\nCyber Se\nDataScience\n")
myfile = open('/Users/sokebiz/Desktop/Python/Class/letter.txt', 'r')
print(myfile.read())

myfile.close()


# myfile = open('/Users/sokebiz/Desktop/Python/Class/letter.txt', 'r')
# print(myfile.read())
# print(myfile.readline())
# for a in myfile:
#     print(a)

# using open function
# with open('/Users/sokebiz/Desktop/Python/Class/letter.txt', 'a') as myfile:
#     myfile.write("\nBlood on the dance floor")
#     myfile.close()
    

# import os.path
# homedir = os.path.expanduser("~")
# print(homedir)
# decision = input("what would you like to do, 1. Read News \n")
# if decision == "1":
#     myfile = open('/Users/sokebiz/Desktop/Python/Class/letter.txt', 'r')
#     print(myfile.read())
# else:
#     print("Nothing for you")

