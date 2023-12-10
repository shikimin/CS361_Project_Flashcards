import requests
import main

class Quiz:
    def __init__(self, cursor) -> None:
        self.cursor = cursor

    def start(self):
        # Intro message
        print("============================================")
        print("Practice Quiz")
        print("============================================")

        # get total number of cards
        self.cursor.execute("SELECT MAX(card_id) FROM cards")
        max_num = self.cursor.fetchone()[0]

        sequence = self.get_sequence(max_num)
        print(sequence)
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

