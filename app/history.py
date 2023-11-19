def check_history(action_log):
    # Intro message
    print("============================================")
    print("History")
    print("============================================")

    print("Last 5 actions:")

    current_log = action_log.get()
    count = 1
    for action in current_log:
        print(count, ": ", action)
        count += 1