import random
import time
import string

print("\nWelcome to GELOS Enterprise Portal!")

# VARIABLES
options = ("a", "b", "c", "d")
acc_val = {}


# FUNCTIONS

# The main function of the program. Contains all the functions to make the loop.
def main():
    print("\n---------------MAIN MENU---------------")
    print("\nOption:"
          "\n"
          "\nA. LOGIN"
          "\nB. SIGN UP"
          "\nC. EXIT"
          "\nD. VIEW")

    # Asks user for option confirmation
    option = input("\nPlease input command: [ A | B | C | D ]: ").lower()
    while option not in options:
        print("\nPlease input a proper command. Thank you.")
        option = input("Please input command: [ A | B | C | D ]: ").lower()
    option_loop(option)


# Intentionally made to make the code shorter for main()
def option_loop(option):
    if option == options[0]:
        login()
    elif option == options[1]:
        sign_up()
    elif option == options[2]:
        ext()
    elif option == options[3]:
        view()


def login():
    print("\n------------------LOG IN MENU------------------")

    # Asks user for username and password for login validation.
    login_key = input("\nPlease enter your username: ")
    login_value = input("Password: ")
    file = open("accounts.txt", "r")

    # Reading accounts.txt to validate if username and password matches the data stored in accounts.txt.
    for line in file.readlines():
        acc, pwd = line.split(" ")
        acc_val[acc] = pwd.strip()
    file.close()
    if (login_key in acc_val.keys()) and (login_value in acc_val[login_key]):
        print("\nWelcome {}!".format(login_key.title()))
        ext()
    # User will be asked if they want to continue logging in case username and password is not validated.
    # this cause a login loop until user is in, otherwise user can also choose options such asa exit or back to main.
    else:
        print("\nYou do not have an account on the server.")
        login_con = input("\nDo you still wanna continue logging in? [y/n]: ").lower()
        while login_con != "y" or "no":
            if login_con == "y":
                login()
            elif login_con == "n":
                confirm_log = input("\nDo you want to:"
                                    "\n"
                                    "\nA. CREATE AN ACCOUNT"
                                    "\nB. BACK TO THE MAIN MENU"
                                    "\nC. EXIT"
                                    "\n"
                                    "\nPlease input the command [ A | B | C ]: ").lower()
                # a loop until user types either 'a', 'b', or 'c'.
                while confirm_log != "a" or "b" or "c":
                    if confirm_log == "a":
                        sign_up()
                    elif confirm_log == "b":
                        main()
                    elif confirm_log == "c":
                        print("\nAlright, commencing exit program...")
                        ext()
                    else:
                        confirm_log = input("\nInvalid command."
                                            "\nPlease enter [ A | B | C ]: ")
            else:
                print("Invalid command.")
                login_con = input("Do you still wanna continue? [y/n]: ").lower()


# Exit function in the case user wants to exit program.
def ext():
    ext_confirm = input("\nDo you wanna exit the program? [y/n]: ").lower()

    while ext_confirm != "y" or "n":
        if ext_confirm == "y":
            for sec in range(2):
                time.sleep(1)
            print("\nExiting program...")
            exit()
        elif ext_confirm == "n":
            for sec in range(2):
                time.sleep(1)
            main()

        else:
            ext_confirm = input("\nInvalid Command. Please input [y/n]: ")


# A special function made for signup, so I don't have to rewrite the code.
# Whenever a user manually creates a password, this function is used to detect any spaces
# if space is detected, a loop will happen until user inputs a password without spaces.
def if_space(if_space_pass):
    # This variable(no_space) is used to contain the password in sign_up to check if there's a space in it.
    # The variable is bool type in which either becomes True or False, depending on if the string sent to it
    # has a space(" ") or not.
    no_space = (" " in if_space_pass)
    # If it's true, that's when the loop takes place.
    while no_space is True:
        if_space_pass = input("\nSpaces are not accepted in passwords."
                              "\nPlease enter a new one without spaces: ")
        no_space = (" " in if_space_pass)
    # The value is returned back after this function ends.
    return if_space_pass


# A sign-up function so user can create account.
def sign_up():
    print("\n-----------------SIGN UP MENU-----------------")
    x = input("\nDo you wanna make an account? [y/n]: ").lower()

    # While loop was used to keep everything in loop until user either inputs 'y' or 'n'.
    while x != "y" or "n":
        if x == "y":
            signup_name = input("\nPlease enter your username: ")
            signup_name = signup_name.replace(" ", "")
            while len(signup_name) < 6:
                signup_name = input("\nUsername cannot be less than 6 characters."
                                    "\nPlease type another one: ")
                signup_name = signup_name.replace(" ", "")
            confirm_genpass = input("Do you wanna use generated password? [y/n]: ").lower()
            while confirm_genpass != "y" or "n":
                if confirm_genpass == "y":
                    pass_generator(signup_name)
                    break
                elif confirm_genpass == "n":

                    signup_value = input("Enter a secure password: ")
                    signup_value = if_space(signup_value)
                    # a loop intentionally made to check if user has put less than 8 or more than 20 characters
                    # otherwise, it'll loop.
                    while (len(signup_value) < 8) or (len(signup_value) > 20):
                        if len(signup_value) < 8:
                            print("\nPassword must be more than 8 characters.")
                            signup_value = input("Enter a secure password: ")
                            # used for validating if space exist as it can cause errors.
                            signup_value = if_space(signup_value)
                        elif len(signup_value) > 20:
                            print("\nPassword must be less than 20 characters.")
                            signup_value = input("Enter a secure password: ")
                            signup_value = if_space(signup_value)
                    # The function user_exist was used here to validate is user has input a username that is currently
                    # existing in the database 'accounts.txt'.
                    signup_name = user_exist(signup_name)
                    with open("accounts.txt", "a") as file_in:
                        file_in.write("\n{} {}".format(signup_name, signup_value))
                        file_in.close()
                    break
                else:
                    print("\nInvalid command.")
                    confirm_genpass = input("Do you wanna use generated password? [y/n]: ").lower()
            login()

        if x == "n":
            whatever = input("\nDo you still wanna continue? [y/n]: ").lower()
            while whatever != "y" or "n":
                if whatever == "y":
                    main()
                elif whatever == "n":
                    print("Understandable.")
                    ext()
                else:
                    whatever = input("\nDo you still wanna continue? [y/n]: ").lower()

        else:
            print("\nInvalid Command.")
            x = input("Type [y/n]: ").lower()


# A function for password generator was created as it'll make signup function longer.
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
    # This code is a bit long, but it's mostly just copy and pasting.
    while length != int:
        try:
            int(length)
            # Basically the same as sign_up. The same validation stuff.
            while int(length) not in range(8, 20):
                if int(length) < 8:
                    print("\nPassword cannot be more than 8 characters.")
                    try:
                        length = int(input("\nHow many characters do you want for your password? "))
                    except (ValueError, TypeError):
                        print("\nError: Enter a number.")
                        length = int(input("How many characters do you want for your password? "))
                elif int(length) > 20:
                    print("\nPassword must be less than 20 characters.")
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
    # Function user_exist has been used here as well just like in sign_up.
    key = user_exist(key)
    file = open("accounts.txt", "a")
    file.write("\n{} {}".format(key, generated_pass))
    file.close()


# A validating function to check if username exists in the database 'accounts.txt'.
def user_exist(username):
    file = open("accounts.txt", "r")

    # for reading purposes to validate if username input by the user in sign_up exist in accounts.txt
    for line in file.readlines():
        acc, pwd = line.split(" ")
        acc_val[acc] = pwd.strip()
    file.close()
    while username in acc_val.keys():
        # if the username doesn't pass the validation, while loop will be set up to keep asking the user until
        # a new username has been input.
        print("\nAn existing user already exist. Please enter a new one.")
        username = input("Please enter a new one: ")
        if username not in acc_val.keys():
            return username
        # if the new username is no longer in 'accounts.txt' username will be returned back to variable in sign_up
        # responsible for the username creation.
    else:
        # in the case user passes the while loop validation, the value is just automatically sent back to sign_up.
        return username


# A separate function so user can view all password listed in the .txt file assuming they had admin access.
# username: admin, password: admin
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
        file.close()
        print("\nHere's the list of users with their password:")
        print("\n{:15s} {}".format("Username", "Password"))
        print("--------------------------")
        for a in acc_val.keys():
            time.sleep(0.5)
            print("{:15s} {}".format(a, acc_val[a]))
        # Made this input statement to keep the loop going.
        view_selection = input("\nDo you still wanna continue? [y/n]: ")
        while view_selection != "y" or "n":
            if view_selection == "y":
                main()
            elif view_selection == "n":
                ext()
            else:
                view_selection = input("\nInvalid Command."
                                       "\nPlease input [y/n]")
    # As it was stated in the print function, the program is automatically terminated if user inputs the
    # wrong admin username and password.
    else:
        print("\nACCESS DENIED!")
        for i in range(1):
            time.sleep(2)
        print("TERMINATING PROGRAM...")
        exit()


# CALLING OUT THE FUNCTIONS

main()
