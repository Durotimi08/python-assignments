import mysql.connector as connection

mydb = connection.connect(host="127.0.0.1", user="root", password="", database="mydatabase")
mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")
# mycursor.execute("DROP DATABASE IF EXISTS mydatabase")
# sql = 'INSERT INTO customers (name, address) VALUES (%s, %s)'
# name = "owolabi"
# address = "dugbe"
# info = (name, address)
# mycursor.execute(sql, info)
# querry = "SELECT * FROM customers"
# mycursor.execute(querry)
# result = mycursor.fetchall()
# print(result)
query = "DELETE FROM customers WHERE id = 3"
mycursor.execute(query)
mydb.commit()