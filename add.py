from main import input_verification

def add_cards(db, cursor):
    # Intro message
    print("============================================")
    print("Adding Flashcards")
    print("============================================")
    print("Enter !menu to abort.\n")

    while True:
        print("Enter text for front side:")
        user_input_front = input()
        if user_input_front == "!menu":
            break

        print("Enter text for back side:")
        user_input_back = input()
        if user_input_back == "!menu":
            break
        
        # get confirmation from user
        print("\nPlease review entries. Enter Y to confirm or N to cancel.")
        print("Front of card: ", user_input_front)
        print("Back of card: ", user_input_back)
        confirmation = input_verification("Y","N")

        if confirmation == "N":
            continue
        else:
            # add entry to database
            SQL_insert = "INSERT INTO cards (card_front, card_back) VALUES (%s, %s)"
            insert_values = (user_input_front, user_input_back)
            cursor.execute(SQL_insert, insert_values)
            db.commit()
            print("Flashcard has been added!")

            # offer additional options
            if extra_add_options(db, cursor, user_input_front, user_input_back) == "!main":
                break
           
def extra_add_options(db, cursor, user_input_front, user_input_back):  
        while True:
            options = """
                Enter !add to add another card.
                Enter !undo to undo the last added card.
                Enter !redo to add the last added card again.
                Enter !main to return to the main menu.
                """
            print(options)
            add_command = input_verification("!add", "!undo", "!redo", "!main")

            if add_command == "!add":
                # return to add menu
                break

            elif add_command == "!undo":
                # get id of last entered card
                cursor.execute("SELECT MAX(card_id) FROM cards")
                last_card = cursor.fetchone()
                # delete last entered card
                SQL_undo = "DELETE FROM cards WHERE card_id=" + str(last_card[0])
                cursor.execute(SQL_undo)
                db.commit()
                
                print("Undo successful!")
                # return to add menu to avoid repeated deletion
                break

            
            elif add_command == "!redo":
                SQL_insert = "INSERT INTO cards (card_front, card_back) VALUES (%s, %s)"
                insert_values = (user_input_front, user_input_back)
                cursor.execute(SQL_insert, insert_values)
                db.commit()

                print("Redo successful!")

            elif add_command == "!main":
                return "!main"