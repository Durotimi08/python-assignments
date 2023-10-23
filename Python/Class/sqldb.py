












mycursor = mydb.cursor()
import random
    # CREATE A DATABASE IF IT DOESNT EXIST
# mycursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")

    # DROP DATABASE IF IT EXISTS 
# mycursor.execute("DROP DATABASE IF EXISTS mydatabase")

    # CREATE A TABLE
# mycursor.execute("create table customer(ID int primary key auto_increment,fname char(20), lname char(20), address varchar(255), gender char(10))")
# mycursor.execute("create table student(ID int primary key auto_increment, fname char(20), lname char(20), matric int(5), password varchar(20), address varchar(255), gender char(10), score int(3), state_of_origin char(15), course char(20), duration char(10), admission_status char(5), exam_done char(5))")

    # INSERTING CUSTOMERS BY COLLECTING INPUTS
generate = random.randint(11111,55555)
# details=f"insert into student(fname, lname, matric, password, address, gender, score, state_of_origin, course, duration, admission_status, exam_done) values('Sodeeq', 'Oladimeji', {generate}, 'soso1', 'Ibadan', 'Male', 0, 'Oyo', 'Cyb', '4 years', 'NO', 'NO')"
# query = "insert into student(fname, lname, matric, password, address, gender, score, state_of_origin, course, duration, admission_status, exam_done) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
# fname = input("What is the first name \n")
# lname = input("what is the last name \n")
# gen = random.randint(11111,55555)
# matric = gen
# password = input("What is your password \n")
# address = input("what is your address \n")
# gender = input("what is your gender \n")
# score = 0
# origin = input("what is your state of origin \n")
# course = input("what course would you like to study \n")
# duration = input("How many months will it take \n")
drp = f"update student set admission_status = 'YES' where matric = 54894"
mycursor.execute(drp)
# info = (fname, lname, matric, password, address, gender, score, origin, course, duration)

# def register: 
# mycursor.execute('drop table student')

# mycursor.execute(details)
# mycursor.execute(query, info)

# drp = f"update student set admission_status = 'YES' where matric = 28149"
# mycursor.execute(drp)


# act = "select * from customer"
# acts = "select * from customer where id = 200"
# mycursor.execute(act)
# mycursor.execute(acts)
# result = mycursor.fetchall()
# result = mycursor.fetchone()
# print(result)
# for r in result:
#     print(f"The address is {r[3]}")

# upd = "update customer set gender = 'female' where id = 200"
# dele = "delete from student where id = 3"
# mycursor.execute(upd)
# mycursor.execute(dele)

    # DELETE A ROW FROM A TABLE
mydb.commit()