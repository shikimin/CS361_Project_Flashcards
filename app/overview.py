import main

class Overview:
    def __init__(self, cursor, db) -> None:
        self.cursor = cursor
        self.db = db

    def card_overview(self):
        # Intro message
        print("============================================")
        print("Overview")
        print("============================================")

        while True:
            print("Below are all the cards currently in your collection:")
            # retrieve all cards from database
            self.cursor.execute("SELECT * FROM cards")
            all_cards = self.cursor.fetchall()
            count = 0
            for card in all_cards:
                count += 1
                print(count, ". ", card[1], " // ", card[2])
                if count % 10 == 0:
                    print("""\nEnter !delete to delete a card. Enter !update to update a card.
                    Enter Y to see the next 10 flashcards. Enter N to return to main menu. """)
                    result = self.verification()
                    if result == "N":
                        break

            print("""\nThere are no more cards to view. 
            Enter !delete to delete a card. Enter !update to update a card.
            Enter Y to see the flashcards from the beginning again. Enter N to return to main menu. """)
            result = self.verification()
            if result == "N":
                break

    def verification(self):
        view_more = main.Main.input_verification(main.Main, ["Y", "N", "!delete", "!update"])
        if view_more == "Y":
            return
        elif view_more == "N":
            return "N"
        elif view_more == "!delete":
            self.delete_card()
        elif view_more == "!update":
            self.update_card()

    def delete_card(self):
        print("Enter the number of the card you want to delete: ")
        self.cursor.execute("SELECT MAX(card_id) FROM cards")
        max_num = self.cursor.fetchone()[0]
        card_num = main.Main.input_verification(main.Main, range(1, max_num+1))

        SQL_delete = "DELETE FROM cards WHERE card_id=" + str(card_num)
        self.cursor.execute(SQL_delete)
        self.db.commit()

        print("Card has been deleted!\n")

    def update_card(self):
        print("Enter the number of the card you want to update: ")
        self.cursor.execute("SELECT MAX(card_id) FROM cards")
        max_num = self.cursor.fetchone()[0]
        card_num = main.Main.input_verification(main.Main, range(1, max_num+1))

        print("Would you like to update the front, back, or both sides of the card?")
        side = main.Main.input_verification(main.Main, ["front", "back", "both"])
        print()

        if side == "front":
            # populate front of card
            print("Enter text for front side:")
            user_input_front = input()
            insert_values = (user_input_front, card_num)
            print()

        elif side == "back":
            # populate back of card
            print("Enter text for back side:")
            user_input_back = input()
            insert_values = (user_input_back, card_num)
            print()

        else:
            print("Enter text for front side:")
            user_input_front = input()
            print()
            print("Enter text for back side:")
            user_input_back = input()
            print()
            insert_values = (user_input_front, user_input_back, card_num)

        # update card in database
        SQL_update = """UPDATE cards 
        SET card_front = %s, card_back = %s
        WHERE card_id = %s"""
        self.cursor.execute(SQL_update, insert_values)    
        self.db.commit()

        print("Card has been updated!\n")
