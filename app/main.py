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
                !overview : view all entered flashcards // DELETE and/or UPDATE flashcards **NEW!**
                !quiz : use your flashcards to QUIZ yourself **NEW!**
                !docs : view documentation in a new window
                !helpme : view frequently asked questions
                !history : view last 5 actions made in this session
            """
            print(main_menu)

            options = ["!add", "!overview", "!quiz", "!docs", "!helpme", "!history"]
            main_menu_command = self.input_verification(options)
            self.commands(main_menu_command)

    def commands(self, command):
        # start functions depending on command
        if command == "!add":
            self.add()
        elif command == "!overview":
            self.overview()
        elif command == "!quiz":
            # start perm_server
            os.system('start /min cmd /c python perm_server.py')
            self.quiz()
        elif command == "!docs":
            os.system('start cmd /k python docs.py')        # opens new window
        elif command == "!helpme":
            os.system('start cmd /k python helpme.py')
        elif command == "!history":
            history.check_history(self.action_log)

    def input_verification(self, options):
        # check if user input is valid according to available options
        while True:
            user_input = input()

            # for inputs that are digits vs alphabet
            if user_input.isdigit():
                user_input = int(user_input)
            else:
                user_input = user_input.lower()

            if user_input in options:
                return user_input
            else:
                print("Invalid input. Please try again.")
                continue

    def add(self):
        add_new_cards = add.Add(self.cursor, self.db, self.action_log)
        add_new_cards.add_cards()

    def overview(self):
        my_overview = overview.Overview(self.cursor, self.db, self.action_log)
        my_overview.card_overview()

    def quiz(self):
        my_quiz = quiz.Quiz(self.cursor, self.db)
        my_quiz.start()

class ActionLog():
    # action log is a queue
    def __init__(self):
        self.log = []
    
    def add(self, action, items):
        # keep max length of action log at 5
        if len(self.log) == 5:
            self.remove()

        # add actions to log depending on action type
        if action == "Add":
            action_desc = "Added flashcard: " + items[0] + " // " + items[1]
        elif action == "Undo" or action == "Redo":
            action_desc = action + " added flashcard: " + items[0] + " // " + items[1]
        elif action == "Delete":
            action_desc = "Deleted card number " + str(items[0])
        elif action == "Update":
            action_desc = "Updated " + items[0] + " side(s) of card number " + str(items[1]) + " to: " + items[2] + " // " + items[3]
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
        cursor.execute("""CREATE TABLE IF NOT EXISTS Cards (
            card_id int NOT NULL AUTO_INCREMENT PRIMARY KEY, 
            card_front VARCHAR(255), 
            card_back VARCHAR(255),
            recur CHAR(1)
            )""")

        main = Main(db, cursor)
        main.start()
    
