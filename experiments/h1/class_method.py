class Employee:
    raise_amt = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.firstName = first
        self.lastName = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.num_of_emps += 1

    def fullname(self):
        return "{} {}".format(self.firstName, self.lastName)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

emp_1 = Employee('Belva', 'Rachman', 50000)
emp_2 = Employee('John', 'Olfindo', 60000)



