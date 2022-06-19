"""TIC TAC TOE"""

import random
import time
from game.rockpaperscissor import rps_main as who_first


# GLOBAL VAR

winning_tiles = ([0, 1, 2], [3, 4, 5], [6, 7, 8], [2, 4, 6], [0, 4, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8])
tiles = [0, 1, 2, 3, 4, 5, 6, 7, 8]

player_token, opponent_token = "X", "O"


class TicTacToe:

    def __init__(self):

        self.attempts = 0
        self.player_score, self.opponent_score = 0, 0
        self.player, self.opponent = [], []
        self.player_choice, self.opponent_turn = None, None
        self.board = " " * 9
        self.whofirst = None

    def run(self):

        print("\n                TIC-TAC-TOE\n")

        for i in "The layout of this game will be as followed.\n":
            print(i, end="")
            time.sleep(0.05)

        time.sleep(2)
        print("\n{:16s}0 | 1 | 2".format(""))
        time.sleep(0.5)
        print("{:16s}3 | 4 | 5".format(""))
        time.sleep(0.5)
        print("{:16s}6 | 7 | 8".format(""))

        time.sleep(1)
        print("\nPlease only enter numbers to place your move based on the layout.")
        time.sleep(1)

        print("\nLoading", end="")
        for i in "...":
            time.sleep(1)
            print(i, end="")
        print("")

        self.game()

    def print_board(self, player, opponent):
        print("")

        for i, val in enumerate(self.board):
            end = " | "
            if i == 2 or i == 5:
                end = "\n---------\n"
            elif i == 8:
                end = "\n"
            if i in player or opponent:
                if i in player:
                    val = player_token
                elif i in opponent:
                    val = opponent_token
            time.sleep(0.25)
            print(val, end=end)

    def game(self):
        print("----------------------\n"
              "\nRock, Paper, Scissor will be played first to determine who goes first.")

        if self.attempts > 0:
            self.whofirst = None
            self.whofirst = who_first.some_instance.for_imports()
        else:
            self.whofirst = who_first.some_instance.for_imports()

        print("\n---------------------------------\n")
        print("ATTEMPTS: {}".format(self.attempts))
        print("\nYour score: {:3s} Opponent Score: {}".format(str(self.player_score), self.opponent_score))

        if self.whofirst is True:
            self.player_function()
        elif self.whofirst is False:
            self.opponent_function()

    def player_function(self):

        print("\n-----------PLAYER TURN-----------\n")

        self.player_choice = input("Type a number 0-8: ")
        while self.player_choice != int:
            try:
                self.player_choice = int(self.player_choice)
                while self.player_choice not in tiles:
                    if not -1 < self.player_choice < 9:
                        print("\nNumber out of range [0-8].")
                        self.player_choice = int(input("Type a number 0-8: "))
                    else:
                        print("\nSpot is already taken.")
                        self.player_choice = int(input("Type a number 0-8: "))
                break
            except:
                if self.player_choice == "":
                    print("\nError: Missing input."
                          "\nPlease enter an input.")
                    self.player_choice = input("Type a number 0-8: ")
                else:
                    print("\nStrings are not accepted. Please enter a number.")
                    self.player_choice = input("Type a number 0-8: ")
        tiles.remove(self.player_choice)
        self.player.append(self.player_choice)
        time.sleep(1)
        self.print_board(self.player, self.opponent)
        self.who_win()

        # Switch to opponent turn
        self.opponent_function()

    def opponent_function(self):

        print("\n-----------OPPONENT TURN-----------")
        print("\nOpponent taking turn", end="")
        for i in "...":
            time.sleep(1)
            print(i, end="")
        print("")

        while len(tiles) != 0:
            self.opponent_turn = random.choice(tiles)
            tiles.remove(self.opponent_turn)
            self.opponent.append(self.opponent_turn)
            self.print_board(self.player, self.opponent)
            self.who_win()
            break

        # Switch to player turn
        self.player_function()

    def who_win(self):

        for tile in winning_tiles:
            player_win = all(item in self.player for item in tile)
            opponent_win = all(item in self.opponent for item in tile)
            tie = [player_win, opponent_win]
            if player_win is True:
                print("\nYou won!")
                self.player_score += 1
                self.continue_validation()
            elif opponent_win is True:
                print("\nYou lost!")
                self.opponent_score += 1
                self.continue_validation()
            elif len(tiles) == 0 and tie == [False, False]:
                print("\nTie!")
                self.continue_validation()

    def continue_validation(self):
        confirmation = input("\nDO YOU WANT TO TRY AGAIN? [y/n]: ").lower()
        while confirmation != "y" or "n":
            if confirmation == "y":
                self.attempts += 1

                tiles.clear()
                self.player.clear()
                self.opponent.clear()

                for i in range(9):
                    tiles.append(i)
                self.game()
            elif confirmation == "n":
                print("\nExiting Game", end="")
                for i in "...":
                    time.sleep(1)
                    print(i, end="")
                exit()


main = TicTacToe()
main.run()
