import requests
import main
import random

class Quiz:
    def __init__(self, cursor, db) -> None:
        self.cursor = cursor
        self.db = db

    def start(self):
        # Intro message
        print("============================================")
        print("Practice Quiz")
        print("============================================")


        # get total number of cards
        self.cursor.execute("SELECT MAX(card_id) FROM cards")
        max_num = self.cursor.fetchone()[0]
        sequence = self.get_sequence(max_num)

        print("""
        Enter !quiz to start the basic quiz mode (Recommended for general use). 
        Enter !personal to start a more personalized quiz mode (More customized use).
        Enter !main to return to the main menu.""")
        choice = main.Main.input_verification(main.Main, ["!quiz","!personal", "!main"])
        print()

        if choice == "!quiz":
            self.quiz_mode(sequence, max_num)
        if choice == "!personal":
            self.personalized_mode(sequence)
        if choice == "!main":
            return


    def quiz_mode(self, sequence, max_num):
        score = 0

        for num in sequence:
            # fetch card from database
            SQL_query = "SELECT * FROM cards WHERE card_id =" + str(num)
            self.cursor.execute(SQL_query)
            card = self.cursor.fetchone()
            score += self.display_cards(card)
            
            # display answer
            print("The answer is: " + card[2] + "\n")
        print("You got", score, "out of", max_num, "questions correct!")


    def personalized_mode(self, sequence):
        score = 0
        total = 0

        SQL_recur = "SELECT card_id FROM cards WHERE recur = 'Y'"
        self.cursor.execute(SQL_recur)
        recur_cards = self.cursor.fetchall()

        if len(recur_cards) > 0:
            for card in recur_cards:
                # insert card at random position in sequence
                random_position = random.choice(range(len(sequence)))
                sequence.insert(random_position, card[0])

        for num in sequence:
            # fetch card from database
            SQL_query = "SELECT * FROM cards WHERE card_id =" + str(num)
            self.cursor.execute(SQL_query)
            card = self.cursor.fetchone()
            score += self.display_cards(card)
            total += 1
            
            # display answer
            print("The answer is: " + card[2] + "\n")

            # ask user if they want to see card more frequently
            print("Enter Y if you would like to see more of this card. Enter N to see this card a normal amount (starting from the next session). Enter !main to return to the main menu.")
            choice = main.Main.input_verification(main.Main, ["y","n","!main"])

            if choice == "y":
                SQL_update = "UPDATE cards SET recur = %s WHERE card_id = %s"
                values = ("Y", num)
                self.cursor.execute(SQL_update, values)
                self.db.commit()
                sequence.append(num)
                print(sequence)
            
            if choice == "n":
                SQL_update = "UPDATE cards SET recur = NULL WHERE card_id = %s"
                self.cursor.execute(SQL_update, [num])
                self.db.commit()
            
            if choice == "!main":
                return
            print()

        print("You got", score, "out of", total, "questions correct!")



    def get_sequence(self, max_num):
        url = 'http://localhost:8000/perm/?min=1&max=' + str(max_num)
        response = requests.get(url).json()
        
        return response.get("perm")

        
    def display_cards(self, card):
        while True:
        # display card & wait for answer
            print(card[1])
            answer = input("Answer: ")
            if str(answer).lower() == str(card[2]).lower():
                print("Correct!")
                return 1
            else:
                print("Incorrect! Try again? (Y/N):")
                try_again = main.Main.input_verification(main.Main, ["y","n"])

                if try_again == "y":
                    continue
                else:
                    return 0

