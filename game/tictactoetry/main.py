"""TIC TAC TOE"""
import random

winning_tiles = ([1, 2, 3], [4, 5, 6], [7, 8, 9], [3, 5, 7], [1, 5, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9])
tiles = [1, 2, 3, 4, 5, 6, 7, 8, 9]


class TicTacToe:

    def __init__(self):

        player = []
        opponent = []
        winner = None

        while winner is None:
            player_choice = int(input("Type a number 1-9: "))
            while player_choice not in tiles:
                if not 0 < player_choice < 10:
                    print("Number out of range [1-9].")
                    player_choice = int(input("Type a number 1-9: "))
                else:
                    print("Spot is already taken.")
                    player_choice = int(input("Type a number 1-9: "))
            tiles.remove(player_choice)
            player.append(player_choice)
            print(player)

            while len(tiles) != 0:
                opponent_turn = random.choice(tiles)
                tiles.remove(opponent_turn)
                opponent.append(opponent_turn)
                break
            print(opponent)

            winner = self.can_win(player, opponent)

    @staticmethod
    def can_win(player, opponent):

        for tile in winning_tiles:
            player_win = all(item in player for item in tile)
            opponent_win = all(item in opponent for item in tile)
            if player_win is True:
                print("You won!")
                return True
            if opponent_win is True:
                print("You lost!")
                return True
            if player_win and opponent_win is False and len(tiles) == 0:
                print("Tie!")
                return False


main = TicTacToe()
