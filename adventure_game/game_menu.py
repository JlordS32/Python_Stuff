import sys
import time

run = None


def startup(game_run):
    confirm_run = input("\nDo you wanna run the game? [y/n]: ").lower()
    while confirm_run != "y" or "n":

        if confirm_run == "y":
            game_run = True
            print("\nRunning the game...")
            time.sleep(3)
            return game_run

        elif confirm_run == "n":
            confirm_exit = input("\nDo you wanna exit? [y/n]: ")
            while confirm_exit != "y" or "n":
                if confirm_exit == "y":
                    print("\nExiting program...")
                    time.sleep(3)
                    sys.exit()
                elif confirm_exit == "n":
                    print("\nInitiating program...")
                    time.sleep(3)
                    startup(run)

        else:
            print("\nInvalid Command.")
            confirm_run = input("\nDo you wanna run the game? [y/n]: ").lower()


class App:

    def __init__(self):
        pass

    def function(self):
        pass


if __name__ == "__main__":

    startup(run)