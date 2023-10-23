import mysql.connector as connection
import time
import random
operations = [["login", "voting_id", "Password"], ["Register", "first-name", "last-name",  "Year of birth", "password"]]
class db:
    def __init__(self):
        try:
            self.mydb = connection.connect(host="127.0.0.1", user="root", password="", database="coorporative"); 
            self.mycursor = self.mydb.cursor()
        except:
            print("There was an error while connecting to the database\n")
            begin()
    def select(self, table, column, figure, type):
        try:
            if type == 1:
            self.mycursor.execute(f"select * from {table} where {column}={figure}")
            result = self.mycursor.fetchall()
            self.mydb.commit(); return result
        except:
            return False
    def insert(self, table, data):
        try:
            self.mycursor.execute(f"insert into {table}{format} values {tuple(data)}") 
            self.mydb.commit();  return True
        except:
            return False
    def update(self, column, figure, key, keyVal):
        try:
            self.mycursor.execute(f"update users set {column}={figure} where {key}={keyVal}")