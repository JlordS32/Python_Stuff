num = int(input("Type a number: "))

while num < 8 or num > 16:
    if num < 8:
        print("Number is too little. Must be more than 8.")
        num = int(input("Type a number: "))
    elif num > 16:
        print("It's over 16.")
        num = int(input("Type a number: "))
print("You pass.")