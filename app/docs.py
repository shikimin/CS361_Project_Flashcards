# Intro message
print("============================================")
print("Documentation")
print("============================================")

topics = """
    1. Requirements
    2. Adding Cards
    3. Redo/Undo Actions
    """
print(topics)

while True:
    print("Enter the number of the topic below to see more information. Enter !topics to bring up the topics again.\n")


    topic_info = {
        "1": """To use this program, you must have a MySQL server downloaded onto your computer. You can download MySQL Community Edition for free at https://dev.mysql.com/downloads/. Upon start up, you will be asked to enter your MySQL username and password. This is to establish a connection to the database in which your flashcards are/will be stored. This program assumes that your host name is defaulted to "localhost".""",
        "2": """Add cards to your database by entering !add on the main menu. Manually type in the desired information to populate the fronts and backs of each card.""",
        "3": """Redo and undo actions are offered immediately after adding a new card. Redo adds the most recently added card again, effectively duplicating the card in the database. Redo action can be done multiple times in a row. The undo action deletes the most recently added card in the database. After a successful undo, the program returns you to the top of the Add menu."""    
        }
    import main
    chosen_topic = main.input_verification("1", "2", "3", "!topics")

    if chosen_topic == "!topics":
        print(topics)
    else:
        print(topic_info[chosen_topic],"\n")

