import random
import string
import time

phonebook = {}
no_account = None
def pass_gen():

    letters = string.ascii_letters
    symbol = string.punctuation
    digits = string.digits

    user_combination = letters

    allow_digits = input("Allow numbers? y/n: ").lower()
    allow_symbol = input("Allow symbols? y/n: ").lower()

    if allow_digits == "y":
        user_combination += digits
    elif allow_digits == "n":
        print("Okay.")
    if allow_symbol == "y":
        user_combination += symbol
    elif allow_symbol == "n":
        print("Understandable.")

    length = int(input("How many characters for the password? "))

    gen_password = "".join(random.sample(user_combination, length))
    print("Here's the generated password: ", gen_password)

    file_in = open("data.txt", "a")
    file_in.write(signup_key + "." + gen_password + "\n")
    file_in.close()


def login():
    global no_account

    file_in = open("data.txt", "r")
    for line in file_in:
        key, value = line.split(".")
        phonebook[key] = value.strip()

    login_key = input("Please enter your username: ")
    login_value = input("Password: ")

    if (login_key in phonebook.keys()) and (login_value in phonebook[login_key]):
        no_account = False
        print("Welcome {}".format(login_key.title()))
        return no_account
    else:
        no_account = True
        print("You do have an account.")
        return no_account

login()

if no_account is True:
    x = input("Do you wanna make an account? [y/n]: ")
    if x == "y":
        signup_key = input("Please enter your username: ")
        confirm_genpass = input("Do you wanna use generated password? [y/n]: ")
        if confirm_genpass == "y":
            pass_gen()
        else:
            signup_value = input("Enter a secure password: ")
            file_in = open("data.txt", "a")
            file_in.write(signup_key + "." + signup_value + "\n")
            file_in.close()
        print("-----LOG IN MENU-----")
        login()
    else:
        print("Thanks for visiting us.")
elif no_account is False:
    ext = input("Do you wanna exit the program? [y/n]: ")
    if ext == "y":
        for i in range(2):
            time.sleep(1)
            second = 2 - i
            print("{} seconds".format(second))
        print("Exiting Program....")
