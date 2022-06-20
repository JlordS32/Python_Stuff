def x():
    print("Hello {}".format(__name__))

print("I like you", __name__)

if __name__ == "__main__":
    x()

if __name__ == "__main.py__":
    print("This is the import")