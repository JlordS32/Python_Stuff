import random

player, computer = "X", "O"

winning_tiles = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                 (1, 4, 7,), (2, 5, 8), (0, 4, 8), (2, 4, 6))


class TicTacToe:

    def __init__(self, y):
        self.board = y*9

    def print_board(self):
        for i, val in enumerate(self.board):
            end = " | "
            if i == 2 or i == 5:
                end = "\n---------\n"
            elif i == 8:
                end = "\n"
            print(val, end=end)

x = TicTacToe([" "])
x.print_board()