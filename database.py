import mysql.connector
import sys

class DBhelper:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="student"
            )
            self.mycursor = self.conn.cursor()
        except:
            print("SOME ERROR IS THERE")
            sys.exit(0)
        else:
            print("Successfully connected to the Database")

    def register(self, name, email, password):
        try:
            query = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
            self.mycursor.execute(query, (name, email, password))
            self.conn.commit()
        except Exception as e:
            print("Error during registration:", e)
            return False
        else:
            return True

    def login(self, email, password):
        try:
            query = "SELECT * FROM users WHERE email = %s AND password = %s"
            self.mycursor.execute(query, (email, password))
            data = self.mycursor.fetchone()
            return data is not None
        except Exception as e:
            print("Error during login:", e)
            return False
