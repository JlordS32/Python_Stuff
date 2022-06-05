print("Hello welcome to Jlord's Cafe")

class pizza:

    def __init__(self, topping, price, crust):
        self.topping = topping
        self.price = price
        self.crust = crust

    def sentence(self):
        print("You ordered a",self.crust, self.topping, "pizza and it cost", self.price, "dollars.")

pizza1 = pizza("meat", 10, "thin")

pizza1.sentence()