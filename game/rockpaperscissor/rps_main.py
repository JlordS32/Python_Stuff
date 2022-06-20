import time
import random


class RockPaperScissor:

    def __init__(self):

        self.player = None
        self.items = ["rock", "paper", "scissor"]
        self.opponent_score = 0
        self.player_score = 0
        self.attempts = 0
        self.truefalse = None
        self.confirmation = []
        self.yes_no = ["y", "n"]

    def game_run(self):

        print("\n      ", end="")
        for_text = self.items

        for i in for_text:
            time.sleep(1)
            print(i.upper(), end=" ")
        time.sleep(1)
        print("\n------------------------------")

        time.sleep(1)

        self.main_menu()

    def main_menu(self):

        print("\nMAIN MENU:"
              "\n------------\n"
              "\na. PLAY"
              "\nb. EXIT\n")

        time.sleep(0.25)
        option = input("Select your option [a/b]: ").lower()
        while option != "a" or "b":
            if option == "a":
                self.play()
                break
            elif option == "b":
                self.ext()
            else:
                option = input("\nInvalid Command."
                               "\nPlease enter [a/b]: ").lower()

    def ext(self):
        print("\nEXIT MENU:"
              "\n------------\n")

        confirm_exit = input("Do you wanna exit the game? [y/n]: ").lower()
        while confirm_exit != "y" or "n":
            if confirm_exit == "y":
                print("\nThanks for playing ^-^!\n"
                      "\nExiting", end="")
                for i in "...":
                    time.sleep(0.5)
                    print(i, end="")
                exit()
            elif confirm_exit == "n":
                self.main_menu()
            else:
                confirm_exit = input("\nInvalid Command."
                                     "\nPlease enter [y/n]; ").lower()

    def play(self):
        # Just to print the game instructions for imports.
        if self.attempts == 0:
            if __name__ != "__main__":
                print("\nInstructions: Whoever wins goes first!")

        print("\nSCORE DASHBOARD:"
              "\n-----------------\n"
              "\nPlayer: {} Opponent: {}".format(self.player_score, self.opponent_score))
        print("Attempts: {}".format(self.attempts))

        print("\n------------"
              "\n    GAME"
              "\n------------\n")

        options = ["a", "b", "c"]
        print("OPTION:\n"
              "\na. Rock"
              "\nb. Paper"
              "\nc. Scissor")

        player_choice = input("\nPlease type your option: ").lower()
        while player_choice not in options:
            if player_choice in options:
                break
            else:
                player_choice = input("\nInvalid command."
                                      "\nPlease input the options: ").lower()

        if player_choice == options[0]:
            self.player = self.items[0]
        elif player_choice == options[1]:
            self.player = self.items[1]
        elif player_choice == options[2]:
            self.player = self.items[2]

        opponent = random.choice(self.items)

        self.who_win(self.player, opponent)
        time.sleep(1)

        if __name__ == "__main__":
            self.game_continue()

    def who_win(self, player, opponent):

        if player == self.items[0] and opponent == self.items[1]:
            self.print_lose()
        elif player == self.items[1] and opponent == self.items[2]:
            self.print_lose()
        elif player == self.items[2] and opponent == self.items[0]:
            self.print_lose()

        elif player == self.items[1] and opponent == self.items[0]:
            self.print_win()
        elif player == self.items[2] and opponent == self.items[1]:
            self.print_win()
        elif player == self.items[0] and opponent == self.items[2]:
            self.print_win()
        elif player == opponent:
            print("\nTie!")
            self.attempts += 1

    def print_win(self):

        print("\nYou won!")
        self.player_score += 1
        self.attempts += 1

    def print_lose(self):

        print("\nYou lose!")
        self.opponent_score += 1
        self.attempts += 1

    def game_continue(self):
        self.confirmation.clear()
        confirm = input("\nDo you wanna continue? [y/n]: ").lower()
        self.confirmation.append(confirm)

        while self.confirmation not in self.yes_no:
            if self.confirmation[0] == self.yes_no[0]:
                self.play()
            elif self.confirmation[0] == self.yes_no[1]:
                self.ext()
            else:
                print("\nInvalid command.")
                self.confirmation = input("Do you wanna continue? [y/n]:").lower()

    def for_imports(self):
        if self.opponent_score == 1:
            return False
        elif self.player_score == 1:
            return True
        else:
            self.play()


if __name__ == "__main__":
    game = RockPaperScissor()
    game.game_run()