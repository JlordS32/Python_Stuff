
import time
import random
import string

user_account = {}

print("Welcome to GELOS Enterprise!"
      "\n")

print("Would you like to:"
      "\n"
      "\nA) Login"
      "\nB) Create an account"
      "\nc) View account"
      "\nD) Quit")

option = input("\nChoose [a/b/c/d]: ").lower()

if option == "a":
    print("\nLOGIN:"
          "\n-----------------------------------------")
    username = input("\nEnter Username: ")
    password = input("Enter Password: ")
    file = open("accounts.txt", "r")
    for i in file:
        data = i.strip()
        usr, pwd = data.split(" ")
        user_account[usr] = pwd.strip()
    if username in user_account.keys() and password in user_account[username]:
        print("Welcome", username)
    else:
        print("Access denied.")
    file.close()

elif option == "b":
    print("\nCREATE NEW ACCOUNT:"
          "\n-------------------------------------------")
    signup_name = input("Enter Username:")
    print("\nWould you like to:"
          "\n"
          "\na) Create your won password" 
          "\nb) Randomly generate a password")
    option = input("\nChoose [a/b]:").lower()

if option == "a":
    password = input("enter password:")
    print("Your password has been created")
    print("you can now login")
    file = open("accounts.txt", "a")
    file.write("\n" + signup_name + " " + password)
    file.close()

if option == "b":
    print("\nLets create a unique password for you...")

    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    combination = letters + digits + symbols

    user_combination = letters
    allow_digits = input("Would you like to include numbers? [y/n]: ").lower()
    allow_symbols = input("What about symbols? [y/n]: ").lower()

    password_length = int(input(" Length of the password (default 10): "))

    if allow_digits == "y":
        user_combination += digits
    if allow_symbols == "y":
     user_combination += symbols

    password = ""
    for i in range(password_length):
     random_character = random.choice(user_combination)
     password += random_character
    print("Your new generated password is:", password)
    print("\nYour account has been created")
    print("You can now log in")
    file = open("accounts.txt", "a")
    file.write("\n" + signup_name + " " + password)
    file.close()

if option == "C":
    file = open("accounts.txt", "r")
    for line in file:
        print(line)
if option == "D":
    time.sleep(2)
    print("Exiting program.")

