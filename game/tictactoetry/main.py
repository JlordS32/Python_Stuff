"""TIC TAC TOE"""
import random

winning_tiles = ([1, 2, 3], [4, 5, 6], [7, 8, 9], [3, 5, 7], [1, 5, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9])
tiles = [1, 2, 3, 4, 5, 6, 7, 8, 9]


class TicTacToe:

    @staticmethod
    def game():

        player = []
        opponent = []

        while player or opponent not in winning_tiles:
            player_choice = int(input("Type a number 1-9: "))
            while player_choice not in tiles:
                player_choice = int(input("\nSpot taken."
                                          "\nType a number 1-9: "))
            tiles.remove(player_choice)
            player.append(player_choice)
            player = sorted(player)

            opponent_choice = random.randint(1, 9)
            while opponent_choice not in tiles:
                opponent_choice = random.randint(1, 9)
            tiles.remove(opponent_choice)
            opponent.append(opponent_choice)
            opponent = sorted(opponent)

            if player in winning_tiles:
                break
        print("Congrats")


main = TicTacToe

main.game()
