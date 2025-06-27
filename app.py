import sys
from dbhelper import DBhelper

class Students:
    def __init__(self):
        self.db = DBhelper()
        self.menu()

    def menu(self):
        user_input = input("""
        1. Enter 1 to Register
        2. Enter 2 to Login
        3. Enter anything else to leave: """)

        if user_input == "1":
            self.register()
        elif user_input == "2":
            self.login()
        else:
            sys.exit(404)

    def register(self):
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        response = self.db.register(name, email, password)
        if response:
            print("REGISTRATION SUCCESSFUL")
        else:
            print("REGISTRATION FAILED")

    def login(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        response = self.db.login(email, password)
        if response:
            print("LOGIN SUCCESSFUL")
        else:
            print("LOGIN FAILED")


obj = Students()
