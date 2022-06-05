import random

x = bool(random.getrandbits(1))
attempt = 0


def quiz(attempt):
    attempt = attempt

    validation = input("\nTrue or False? ").lower()
    while validation != "true" or "false":
        if validation == "true":
            validation = True
            if validation == x:
                print("\nYou got it right boy.")
                return attempt
            elif validation != x:
                print("\nYou got it wrong.")
                confirm = input("\nWanna go again? [y/n]: ")
                while confirm == "y" or "n":
                    if confirm == "y":
                        attempt += 1
                        return quiz(attempt)
                    elif confirm == "n":
                        print("Exiting.")
                        break
            break
        elif validation == "false":
            validation = False
            if validation == x:
                print("\nYou got it right boy.")
                return attempt
            elif validation != x:
                print("\nYou got it wrong.")
                confirm = input("\nWanna go again? [y/n]: ")
                while confirm == "y" or "n":
                    if confirm == "y":
                        attempt += 1
                        return quiz(attempt)
                    elif confirm == "n":
                        print("\nExiting.")
                        break
            break
        else:
            print("\nWrong command.")
            validation = input("True or False? ").lower()


attempt = quiz(attempt)
print("\nThanks for using the program.")
print("Here are your no. of attempts:", attempt)