import mysql.connector
import os
import add
import overview
import history
import quiz

class Main:
    def __init__(self, db, cursor) -> None:
        # create log to track actions
        self.action_log = ActionLog()
        self.db = db
        self.cursor = cursor

    def start(self):
        # Intro message
        while True:
            main_menu = """\nMAIN MENU:
        - Enter one of the commands below:
                !add : ADD new flashcards to use in quizzes (Manual Entry)
                !overview : view all entered flashcards // DELETE and/or UPDATE flashcards
                !quiz : use your flashcards to QUIZ yourself
                !docs : view documentation in a new window
                !helpme : view frequently asked questions
                !history : view last 5 actions made in this session
            """
            print(main_menu)

            options = ["!add", "!overview", "!quiz", "!docs", "!helpme", "!history"]
            main_menu_command = self.input_verification(options)
            self.commands(main_menu_command)

    def commands(self, command):
            if command == "!add":
                add.add_cards(self.db, self.cursor, self.action_log)
            elif command == "!overview":
                self.overview()
            elif command == "!quiz":
                # start perm_server
                os.system('start /min cmd /c python perm_server.py')
                self.quiz()
            elif command == "!docs":
                os.system('start cmd /k python docs.py')
            elif command == "!helpme":
                os.system('start cmd /k python helpme.py')
            elif command == "!history":
                history.check_history(self.action_log)

    def input_verification(self, options):
        while True:
            user_input = input()

            if user_input.isdigit():
                user_input = int(user_input)
            else:
                user_input = user_input.lower()

            if user_input in options:
                return user_input
            else:
                print("Invalid input. Please try again.")
                continue

    def overview(self):
        my_overview = overview.Overview(self.cursor, self.db)
        my_overview.card_overview()

    def quiz(self):
        my_quiz = quiz.Quiz(self.cursor)
        my_quiz.start()

class ActionLog():
    def __init__(self):
        self.log = []
    
    def add(self, action, card_front, card_back):
        # keep max length of action log at 5
        if len(self.log) == 5:
            self.remove()

        action_desc = action + ": " + card_front + " // " + card_back
        self.log.append(action_desc)

    def remove(self):
        self.log.pop(0)
    
    def get(self):
        return self.log
 

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

        main = Main(db, cursor)
        main.start()
    
