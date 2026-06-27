def back(message):

    while True:
        answer = input(message).lower().strip()

        if answer == "y":
            return True
        elif answer == "n":
            return False
        
        print("\nlotfan dorst vared kon ---> (Y/N)")

    