import random
import time
import string

print("Welcome to GELOS Enterprise Portal!")

# GLOBAL VARIABLES
no_account = None
glob_option = ""
options = ("a", "b", "c", "d")
acc_val = {}
signup_key = ""

# FUNCTIONS
def login():
    global no_account

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
        print("You do not have an account on the server.")
        sign_up()
        return no_account
    file.close()


def pass_generator():
    global signup_key

    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    user_combination = letters

    number_confirm = input("\nAllow numbers? [y/n]: ")
    while number_confirm != "y" or "n":
        if number_confirm == "y":
            user_combination += digits
            print("Numbers included.")
            break
        elif number_confirm == "n":
            print("Understandable.")
            break
        print("\nInvalid Command.")
        number_confirm = input("Allow numbers? [y/n]: ")

    symbol_confirm = input("\nAllow symbols? [y/n]: ")
    while symbol_confirm != "y" or "n":
        if symbol_confirm == "y":
            user_combination += symbols
            print("Symbols added successfully.")
            break
        elif symbol_confirm == "n":
            print("Alright.")
            break
        print("\nInvalid Command.")
        symbol_confirm = input("Allow symbols? [y/n]: ")

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

    user_exist()
    file = open("accounts.txt", "a")
    file.write("\n{} {}".format(signup_key, generated_pass))


def ext():
    ext_confirm = input("\nDo you wanna exit the program? [y/n]: ")
    while ext_confirm != "y" or "no":
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
            ext_confirm = input("Invalid Command. Please input [y/n]: ")


def sign_up():
    global signup_key
    if no_account is True:
        x = input("\nDo you wanna make an account? [y/n]: ")
        if x == "y":
            print("\n-----------------SIGN IN MENU-----------------")
            signup = input("\nPlease enter your username: ")
            signup_key = signup
            confirm_genpass = input("Do you wanna use generated password? [y/n]: ")
            if confirm_genpass == "y":
                pass_generator()
            else:
                signup_value = input("Enter a secure password: ")
                while len(signup_value) < 8:
                    print("\nPassword must be more than 8 characters.")
                    signup_value = input("Enter a secure password: ")
                user_exist()
                file_in = open("accounts.txt", "a")
                file_in.write("\n{} {}".format(signup_key, signup_value))
                file_in.close()
            login()
        else:
            ext()


def user_exist():
    global signup_key
    file = open("accounts.txt", "r")
    for line in file.readlines():
        acc, pwd = line.split(" ")
        acc_val[acc] = pwd.strip()
    while signup_key in acc_val.keys():
        print("\nAn existing user already exist. Please enter a new one.")
        signup = input("Please enter your username: ")
        signup_key = signup


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


def option_loop():
    global glob_option
    global no_account
    if glob_option == options[0]:
        login()
    elif glob_option == options[1]:
        no_account = True
        sign_up()
    elif glob_option == options[2]:
        ext()
    elif glob_option == options[3]:
        view()


def option_selection():
    global glob_option

    print("\n---------------OPTION SELECTION---------------")
    print("\nOption: [a: login |b: signin |c: exit |d: view ] ")
    option = input("Please input command: [ a | b | c | d ]: ").lower()
    while option not in options:
        print("\nPlease input a proper command. Thank you.")
        option = input("Please input command: [ a | b | c | d ]: ").lower()
    glob_option = option
    option_loop()
    while glob_option not in options:
        print("\nInvalid command.")
        option = input("Option: [ login | signin | exit | view ]: ").lower()
        glob_option = option
        option_loop()


option_selection()