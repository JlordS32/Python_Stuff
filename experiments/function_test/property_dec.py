class Employee:

    def __init__(self, first, last, pay):
        self.firstName = first
        self.lastName = last
        self.pay = pay

    @property
    def fullname(self):
        return "{} {}".format(self.firstName, self.lastName).title()

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.firstName = first
        self.lastName = last

    @fullname.deleter
    def fullname(self):
        self.firstName = None
        self.lastName = None
        print("Name deleted.")

    @property
    def email(self):
        return "{}.{}@email.com".format(self.firstName, self.lastName).lower()


emp_1 = Employee('Belva', 'Rachman', 50000)
emp_2 = Employee('Meme', 'Rasonabe', 15000)

emp_1.firstName = "Jaylou"
print(emp_1.fullname)
print(emp_1.email)

emp_1.fullname = "Belva Rasonabe"
print(emp_1.fullname)

print(emp_2.email)
print(emp_2.fullname)

del emp_1.fullname

print(emp_1.fullname)