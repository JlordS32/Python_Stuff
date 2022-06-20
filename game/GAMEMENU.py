from game.rockpaperscissor import rps_main
from game.tictactoetry import main
import time

print("---------------------\n")
time.sleep(1)

print("{:5s} UWU GAME\n".format(""))


def ext():
    confirm_exit = input("\nAre you sure you want to exit? [y/n]: ")
    while confirm_exit != "y" or "n":
        if confirm_exit == "y":
            time.sleep(1)
            print("\nExiting", end="")
            for x, y in enumerate("..."):
                time.sleep(1)
                print(y, end="")
                # Nothing too special for this if statement, it only prints a new line after the for loop finishes.
                if x == 2:
                    print(y, end="\n")
            exit()
        elif confirm_exit == "n":
            print("")
            menu()
        else:
            confirm_exit = input("\nInvalid Command.\n"
                                 "Please input [y/n]: ")


def menu():

    time.sleep(1)
    print("{:6s} MENU ".format(""))
    print("-----------------\n")

    print("a. SELECT GAME"
          "\nb. EXIT\n")

    # Used a while function, so it would loop until the condition is meet.
    menu_option = input("Please select your option: ").lower()
    while menu_option != "a" or "b":
        if menu_option == "a":
            game_selection()
        elif menu_option == "b":
            ext()
        else:
            menu_option = input("\nInvalid Command.\n"
                                "Please input the proper command [a/b]: ")


def game_selection():
    print("\n{:6s} GAME SELECTION ".format(""))
    print("-"*28, end="\n")

    print("\na. ROCK, PAPER, SCISSOR\n"
          "b. TICTACTOE\n")

    select_game = input("Please select your game: ").lower()
    while select_game != "a" or "b":
        if select_game == "a":
            print("\n"*20)
            time.sleep(3)
            rps = rps_main.RockPaperScissor()
            rps.game_run()
            rps.game_continue()
        elif select_game == "b":
            print("\n"*20)
            time.sleep(3)
            tictactoe = main.TicTacToe()
            tictactoe.run()
        else:
            select_game = input("\nInvalid command.\n"
                                "Please input the proper command: ")


menu()