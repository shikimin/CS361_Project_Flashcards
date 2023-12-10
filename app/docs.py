# Intro message
print("============================================")
print("Documentation")
print("============================================")

topics = """
    1. Requirements
    2. Adding Cards
    3. Redo/Undo Actions
    4. Deleting Cards
    5. Updating Cards
    6. Quizzing
    """
print(topics)

while True:
    print("Enter the number of the topic below to see more information. Enter !topics to bring up the topics again.\n")


    topic_info = {
        1: """To use this program, you must have a MySQL server downloaded onto your computer. 
            You can download MySQL Community Edition for free at https://dev.mysql.com/downloads/. 
            Upon start up, you will be asked to enter your MySQL username and password. 
            This is to establish a connection to the database in which your flashcards are/will be stored. 
            This program assumes that your host name is defaulted to "localhost".""",
        2: """Add cards to your database by entering !add on the main menu. 
            Manually type in the desired information to populate the fronts and backs of each card.""",
        3: """Redo and undo actions are offered immediately after adding a new card. 
            Redo adds the most recently added card again, effectively duplicating the card in the database. 
            Redo action can be done multiple times in a row. The undo action deletes the most recently added card in the database. 
            After a successful undo, the program returns you to the top of the Add menu.""",
        4: """Cards can be deleted via the Overview option. Cards will be displayed in groups of 10.
            You will be given the option to delete any card in the database after each group is displayed 
            (i.e. you don't have to wait for your desired card to be displayed).
            You will, however, need to enter the card number of the card you wish to delete.""",
        5: """Cards can be updated via the Overview option. Cards will be displayed in groups of 10.
            You will be given the option to update any card in the database after each group is displayed 
            (i.e. you don't have to wait for your desired card to be displayed).
            You will, however, need to enter the card number of the card you wish to update.
            You will then be given the option to update the front, back, or both sides of the chosen card.
            The process of updating the card is similar to the process of adding new cards (typing in desired entry).""",
        6: """The Quiz option takes all the cards in your database and displays the front of each card in random order.
            You must type in the contents of the back of the card in order to answer correctly. 
            If you answer incorrectly, you are given the option to try again or move on to the next card.
            The total number of correctly answered cards is shown at the end."""   
        }
    import main
    chosen_topic = main.Main.input_verification(main.Main, [1, 2, 3, 4, 5, 6, "!topics"])

    if chosen_topic == "!topics":
        print(topics)
    else:
        print(topic_info[chosen_topic],"\n")

