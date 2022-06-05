def x():
    print("Hello {}".format(__name__))

print("I like you", __name__)

if __name__ == "__main__":
    x()