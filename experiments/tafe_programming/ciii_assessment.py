import random
import time
import string

print("Welcome to GELOS Enterprise Portal!")

# VARIABLES
options = ("a", "b", "c", "d")
acc_val = {}

# FUNCTIONS


def option_selection():
    print("\n---------------OPTION SELECTION---------------")
    print("\nOption:"
          "\n"
          "\nA. LOGIN"
          "\nB. SIGN IN"
          "\nC. EXIT"
          "\nD. VIEW")
    option = input("\nPlease input command: [ A | B | C | D ]: ").lower()
    while option not in options:
        print("\nPlease input a proper command. Thank you.")
        option = input("Please input command: [ A | B | C | D ]: ").lower()
    option_loop(option)


def option_loop(option):
    if option == options[0]:
        login(None)
    elif option == options[1]:
        sign_up(True)
    elif option == options[2]:
        ext()
    elif option == options[3]:
        view()


def login(no_account):
    print("\n------------------LOG IN MENU------------------")
    login_key = input("\nPlease enter your username: ")
    login_value = input("Password: ")
    file = open("accounts.txt", "r")
    for line in file.readlines():
        acc, pwd = line.split(" ")
        acc_val[acc] = pwd.strip()
    if (login_key in acc_val.keys()) and (login_value in acc_val[login_key]):
        print("\nWelcome {}!".format(login_key.title()))
        no_account = False
        ext()
    else:
        no_account = True
        print("\nYou do not have an account on the server.")
        login_con = input("\nDo you still wanna continue? [y/n]: ").lower()
        while login_con != "y" or "no":
            if login_con == "y":
                login(None)
            elif login_con == "n":
                confirm_log = input("Do you still wanna use the program? [y/n]: ")
                while confirm_log != "y" or "n":
                    if confirm_log == "y":
                        option_selection()
                    elif confirm_log == "n":
                        print("\nAlright, commencing exit program...")
                        ext()
                    else:
                        confirm_log = input("Invalid command."
                                            "\nPlease enter [y/n]: ")
            else:
                print("Invalid command.")
                login_con = input("Do you still wanna continue? [y/n]: ").lower()
        sign_up(True)
    file.close()


def ext():
    ext_confirm = input("\nDo you wanna exit the program? [y/n]: ").lower()
    while ext_confirm != "y" or "n":
        if ext_confirm == "y":
            for sec in range(2):
                time.sleep(1)
            print("\nExiting program...")
            exit()
        elif ext_confirm == "n":
            for sec in range(1):
                time.sleep(1)
            option_selection()
        else:
            ext_confirm = input("\nInvalid Command. Please input [y/n]: ")


def sign_up(no_account):
    if no_account is True:
        x = input("\nDo you wanna make an account? [y/n]: ").lower()
        while x != "y" or "n":
            if x == "y":
                print("\n-----------------SIGN IN MENU-----------------")
                signup_name = input("\nPlease enter your username: ")
                confirm_genpass = input("Do you wanna use generated password? [y/n]: ").lower()
                while confirm_genpass != "y" or "n":
                    if confirm_genpass == "y":
                        pass_generator(signup_name)
                        break
                    else:
                        print("\nInvalid command.")
                        confirm_genpass = input("Do you wanna use generated password? [y/n]: ").lower()
                else:
                    signup_value = input("Enter a secure password: ")
                    while len(signup_value) < 8:
                        print("\nPassword must be more than 8 characters.")
                        signup_value = input("Enter a secure password: ")
                    signup_name = user_exist(signup_name)
                    file_in = open("accounts.txt", "a")
                    file_in.write("\n{} {}".format(signup_name, signup_value))
                    file_in.close()
                login(False)
            if x == "n":
                whatever = input("\nDo you still wanna continue? [y/n]: ").lower()
                while whatever != "y" or "n":
                    if whatever == "y":
                        option_selection()
                    elif whatever == "n":
                        print("Understandable.")
                        ext()
                    else:
                        whatever = input("\nDo you still wanna continue? [y/n]: ").lower()
            else:
                print("\nInvalid Command.")
                x = input("Type [y/n]: ").lower()


def pass_generator(key):
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    user_combination = letters
    number_confirm = input("\nAllow numbers? [y/n]: ").lower()
    while number_confirm != "y" or "n":
        if number_confirm == "y":
            user_combination += digits
            print("Numbers included.")
            break
        elif number_confirm == "n":
            print("Understandable.")
            break
        print("\nInvalid Command.")
        number_confirm = input("Allow numbers? [y/n]: ").lower()
    symbol_confirm = input("\nAllow symbols? [y/n]: ").lower()
    while symbol_confirm != "y" or "n":
        if symbol_confirm == "y":
            user_combination += symbols
            print("Symbols added successfully.")
            break
        elif symbol_confirm == "n":
            print("Alright.")
            break
        print("\nInvalid Command.")
        symbol_confirm = input("Allow symbols? [y/n]: ").lower()
    length = input("\nHow many characters do you want for your password? ")
    while length != int:
        try:
            int(length)
            while int(length) < 8:
                print("\nPassword must be more than 8 characters.")
                try:
                    length = int(input("\nHow many characters do you want for your password? "))
                except (ValueError, TypeError):
                    print("\nError: Enter a number.")
                    length = int(input("How many characters do you want for your password? "))
            break
        except (ValueError, TypeError):
            print("\nError: Enter a number.")
            length = input("How many characters do you want for your password? ")
    generated_pass = ""
    for i in range(int(length)):
        i = random.choice(user_combination)
        generated_pass += i
    print("\n.......")
    for sec in range(5):
        time.sleep(1)
        seconds = 5 - sec
        print("Generating password in", seconds, "seconds...")
    print("\nHere's the generated password:", generated_pass)
    key = user_exist(key)
    file = open("accounts.txt", "a")
    file.write("\n{} {}".format(key, generated_pass))


def user_exist(username):
    file = open("accounts.txt", "r")
    for line in file.readlines():
        acc, pwd = line.split(" ")
        acc_val[acc] = pwd.strip()
    while username in acc_val.keys():
        print("\nAn existing user already exist. Please enter a new one.")
        username = input("Please enter a new one: ")
        if username not in acc_val.keys():
            return username
    else:
        return username


def view():
    print("\nINITIATING...")
    for i in range(2):
        time.sleep(1)
    print("\n------------------ADMIN VIEW------------------")
    print("\nWARNING! AUTHORISATION IS REQUIRED FOR ACCESS.")
    print("PROGRAM MAY BE TERMINATED IF ACCOUNT IS INVALID")
    admin_username = input("\nPlease input admin username: ")
    admin_pwd = input("Password: ")
    if admin_username and admin_pwd == "admin":
        file = open("accounts.txt", "r")
        for i in file:
            user, pwd = i.split(" ")
            acc_val[user] = pwd.strip()
        print("\nHere's the list of users with their password:")
        print("\n{:15s} {}".format("Username", "Password"))
        print("--------------------------")
        for a in acc_val.keys():
            print("{:15s} {}".format(a, acc_val[a]))
    else:
        print("\nACCESS DENIED!")
        for i in range(2):
            time.sleep(2)
        print("TERMINATING PROGRAM...")
        exit()


option_selection()