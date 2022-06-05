x = 2


class Animal:

    def __init__(self, animal_type):
        print("The animal type is", animal_type)

    def multiplication(self, a):
        self.e = x * a
        print(self.e)

    def jlordstyle(self):
        pass


class Mammal(Animal):

    def __init__(self, x):
        super().__init__(x)
        print(x)

    def addition(self, x):
        x = 10 + x
        print(x)

    def mult(self, a):
        super().multiplication(6)
        a += self.e
        print(a)

m = Mammal("carabaw")