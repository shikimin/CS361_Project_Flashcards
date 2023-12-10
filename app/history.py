import main

def check_history(action_log):
    while True:
        # Intro message
        print("============================================")
        print("History")
        print("============================================")

        print("Last 5 actions:")

        current_log = action_log.get()
        
        if len(current_log) == 0:
            print("                There are no actions.")
        else:
            count = 1
            for action in current_log:
                print(count, ": ", action)
                count += 1

        print()
        print("Enter !main to return to main menu.")
        confirmation = main.Main.input_verification(main.Main, ["!main"])

        if confirmation == "!main":
            break