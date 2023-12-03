# Intro message
print("============================================")
print("Frequently Asked Questions")
print("============================================")

faq = """
    1. Where can I find my username and password?
    2. Where can I find my stored cards?
    3. How can I delete my cards?
    4. My question isn't listed here. Where can I get help?
    """
print(faq)

while True:
    print("Enter the number of the topic below to see more information. Enter !topics to bring up the topics again.\n")


    faq_answers = {
        "1": """MySQL will have asked for a username and password upon installation. The default username provided is typically "root" while the password is one you choose yourself. To create a new user/password, please see https://dev.mysql.com/doc/refman/8.0/en/account-management-statements.html.""",
        "2": """Stored cards can be viewed by entering !overview at the main menu. In MySQL, they are stored in the database named "my_flashcards".""",
        "3": """Cards that were just added can be immediately deleted through the !undo function. A more general delete function will be coming soon.""",
        "4": """For any further questions, please contact shinminy@oregonstate.edu."""    
        }
    import main
    chosen_q = main.Main.input_verification(["1", "2", "3", "4", "!helpme"])

    if chosen_q == "!helpme":
        print(faq)
    else:
        print(faq_answers[chosen_q],"\n")
