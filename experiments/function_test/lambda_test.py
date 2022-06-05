def command():

    n = input("Name: ")
    s = input("Surname: ")

    fullname = lambda n, s: n.title() + " " + s.title()

    print(fullname(n, s))

command()

lambda:command()