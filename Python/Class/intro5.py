multiple = ("ade", "femi")
#Tuple cannot be changed or reassigned

#Dictionary

myNames = {"Name1": "Emma", "Name2": "Nath"}
# print(myNames["Name1"])

stu_record = {"Isaac": ['Male', 24, "Married"],"Ope": ['Female', 34, "Single"]}

print(stu_record["Isaac"][0])
# print(stu_record.keys())
# print(stu_record.values())
# print(stu_record.items())

product = {
    "producer" : "Toyota",
    "model" : "Corolla",
    "year" : "2024",
    "color" : "black",
    "gear" : 4
}

product["passenger"] = 3
# print(product)
product["tyres"] = 4
# print(product)
product["model"] = "Supra"
# print(product)

# product.pop("color")
# product.popitem()
del product["model"]
# product.clear()
# print(product)

student_details = {"Tony Johnson": {'name': 'Tony Johnson', 'level': 400, "location": 'Takie', 'dept': 'math'},
                "Micheal Chan": {'name':"Micheal Chan", 'level':200, 'location': 'General','dept': 'computer'},
                "Timi Joy": {'level' :400, 'location': 'Apake' , 'dept': 'english'}
}
# print(student details.keys ())
std1 = {'name': 'Tony Johnson', 'level': 400, "location": 'Takie', 'dept': 'math'}
std2 = {'name':"Micheal Chan", 'level':200, 'location': 'General','dept': 'computer'}
student_details2 = {
    'FIRST_PERSON' :std1,
    'SECOND_PERSON':std2
}
# print(student_details2['FIRST_PERSON'])
# print(student_details["Tony Johnson"])



#   IF STATEMENTS

a = "Ade"
b = "Ola"
c = "Ade"
d = "Ola"

# if a == c:
#     if b == d: 
#         print("A and C are similar, B and D are also similar")
#     else: 
#         print("Onky B and D are similar")
# else: 
#     print("I cannot evaluate the block of code")


import time
print("good afternoon")
time.sleep (5) # sleep for five seconds before printing this line again
instruction = input("are u a student \n")





