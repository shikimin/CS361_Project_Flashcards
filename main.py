import mysql.connector
import os
from add import *

def main(db, cursor):
    # Intro message
    while True:
        main_menu = """\nMAIN MENU:
    - Enter one of the commands below:
            !add : add new flashcards to use in quizzes (Manual Entry)
            !overview : view all entered flashcards
            !docs : view documentation in a new window
            !helpme : view frequently asked questions
            !history : view last 5 actions made in this session
        """
        print(main_menu)
        main_menu_command = input_verification("!add", "!overview", "!docs", "!helpme", "!history")
        if main_menu_command == "!add":
            add_cards(db, cursor)
            continue
        elif main_menu_command == "!overview":
            overview()
        elif main_menu_command == "!docs":
            docs()
        elif main_menu_command == "!helpme":
            helpme()
        elif main_menu_command == "!history":
            history()

def input_verification(*args):
    while True:
        user_input = input()
        if user_input in args:
            return user_input
        else:
            print("Invalid input. Please try again.")
            continue

def overview():
    pass
def docs():
    pass
def helpme():
    pass
def history():
    pass


if __name__ == '__main__':
    # print welcome message
    print("============================================")
    print("Welcome to FLASHCARDS!")
    print("============================================")

    # establish connection to MySQL database
    while True:
        sql_username = input("Please enter your username: ")
        sql_password = input("Please enter your password: ")

        # check if username/password combo is valid
        try:
            db = mysql.connector.connect(
                host="localhost",
                user=sql_username,
                password=sql_password
            )
        except:
            print("Cannot connect to MYSQL with entered username/password. Please try again.")
            continue

        # create flashcard database if doesn't exist
        cursor = db.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS my_flashcards")

        db = mysql.connector.connect(
            host="localhost",
            user=sql_username,
            password=sql_password,
            database="my_flashcards"
        )
        cursor = db.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS Cards (card_id int NOT NULL AUTO_INCREMENT PRIMARY KEY, card_front VARCHAR(255), card_back VARCHAR(255))")

        main(db, cursor)
    
