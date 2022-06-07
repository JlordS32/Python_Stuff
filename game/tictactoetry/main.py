"""TIC TAC TOE"""

import random
import time

# GLOBAL VAR

winning_tiles = ([0, 1, 2], [3, 4, 5], [6, 7, 8], [2, 4, 6], [0, 4, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8])
tiles = [0, 1, 2, 3, 4, 5, 6, 7, 8]

player_token, opponent_token = "X", "O"


class TicTacToe:

    def __init__(self):

        self.attempts = 0
        self.player_choice = None
        self.opponent_turn = None
        self.board = " "*9

    def run(self):
        print("\n                TIC-TAC-TOE\n"
              "\nThe layout of this game will be as followed.\n"
              "\n {:16s}0 | 1 | 2"
              "\n {:16s}3 | 4 | 5"
              "\n {:16s}6 | 7 | 8".format("", "", ""))

        time.sleep(1)
        print("\nPlease only enter numbers to place your move based on the layout.")
        time.sleep(1)
        print("\nLoading...")
        time.sleep(3)
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
            print(val, end=end)

    def game(self):
        player = []
        opponent = []

        while True:
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
                except (ValueError, TypeError):
                    print("\nStrings are not accepted. Please enter a number.")
                    self.player_choice = input("Type a number 0-8: ")
            tiles.remove(self.player_choice)
            player.append(self.player_choice)
            time.sleep(1)
            self.print_board(player, opponent)
            self.can_win(player, opponent)

            print("\n-----------OPPONENT TURN-----------")
            print("\nOpponent taking turn...")
            time.sleep(2)

            while len(tiles) != 0:
                self.opponent_turn = random.choice(tiles)
                tiles.remove(self.opponent_turn)
                opponent.append(self.opponent_turn)
                time.sleep(1)
                self.print_board(player, opponent)
                self.can_win(player, opponent)
                break

    def can_win(self, player, opponent):

        for tile in winning_tiles:
            player_win = all(item in player for item in tile)
            opponent_win = all(item in opponent for item in tile)
            if player_win is True:
                print("\nYou won!")
                self.continue_validation()
            if opponent_win is True:
                print("\nYou lost!")
                self.continue_validation()
            if player_win and opponent_win is False and len(tiles) == 0:
                print("\nTie!")
                self.continue_validation()

    def continue_validation(self):
        confirmation = input("\nDO YOU STILL WANT TO CONTINUE? [y/n]: ").lower()
        while confirmation != "y" or "n":
            if confirmation == "y":
                self.attempts += 1
                self.game()
            elif confirmation == "n":
                print("Exiting Game.")
                exit()


main = TicTacToe()
main.run()
