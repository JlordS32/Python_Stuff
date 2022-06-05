class Employee:
    raise_amt = 1.04
    num_of_emp = 0

    def __init__(self, first, last, pay):
        self.firstName = first
        self.lastName = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.num_of_emp += 1

    def fullname(self):
        return "{} {}".format(self.firstName, self.lastName)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.firstName, self.lastName, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __mul__(self, other):
        return self.pay * other.pay

    def __sub__(self, other):
        return self.pay - other.pay


emp_1 = Employee('Belva', 'Rachman', 50000)
emp_2 = Employee('John', 'Olfindo', 60000)

print(repr(emp_1))
print(str(emp_2))

print(emp_1 + emp_2)
print(emp_1 - emp_2)
print(emp_1 * emp_2)