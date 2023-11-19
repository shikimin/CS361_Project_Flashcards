import main

def card_overview(cursor):
    # Intro message
    print("============================================")
    print("Overview")
    print("============================================")

    # retrieve all cards from database
    cursor.execute("SELECT * FROM cards")
    all_cards = cursor.fetchall()

    while True:
        count = 0
        for card in all_cards:
            count += 1
            print(count, ". ", card[1], " // ", card[2])
            if count % 10 == 0:
                print("\nEnter Y to see the next 10 flashcards. Enter N to return to main menu.")
                view_more = main.input_verification("Y","N")
                if view_more == "Y":
                    continue
                else:
                    break

        print("\nThere are no more cards to view. Enter Y to see the flashcards from the beginning again. Enter N to return to main menu.")
        view_more = main.input_verification("Y","N")
        if view_more == "Y":
                    continue
        else:
            break