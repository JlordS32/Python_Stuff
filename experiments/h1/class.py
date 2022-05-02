# This is the classification

class Fruits:
    def type_fruit(self, name, colour):
        self.fruit = name
        self.colour = colour

a = Fruits()
a.type_fruit("Apple", "Red")
print("The fruit is", a.fruit)
print("The colour is", a.colour)


# the self has been used as an argument for the new function order()
class Food:
    def order(self):
        print("This food is", self.food_kind)
        print("It cost about", self.food_price, "\n")

f1 = Food()
f1.food_kind = "Chips"
f1.food_price = 8

f1.order()

class Tweet:
    def __init__(self, message):
        self.x = message

a = Tweet("Something about this is wrong.")
print(a.x)

class epic:
    def __init__(self, message):
        self.message = message
    def print_epic(self):
        print(self.message)

z = epic("Something about this is epic.")

z.print_epic()

epic.print_epic(z)