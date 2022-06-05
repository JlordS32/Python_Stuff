class Fruits:

    def __init__(self, fruit, colour, price, amt):
        self.fruit = fruit
        self.colour = colour
        self.price = price
        self.amount = amt

    def sentence(self):
        print("This fruit is", self.fruit)
        print("The colour is", self.colour)
        print("It cost about", self.price)
        print("I wanna buy", self.amount, "of them." + "\n")

f1 = Fruits("Apple", "Red", 2.5, 5)
f2 = Fruits("Orange", "Orange", 9, 2)
f3 = Fruits("Mandarin", "Orange", 1, 10)

f1.sentence()
f2.sentence()
f3.sentence()