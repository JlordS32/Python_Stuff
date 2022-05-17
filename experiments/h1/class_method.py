class Employee:
    raise_amt = 1.04
    num_of_emp = 0

    def __init__(self, first, last, pay):
        self.firstName = first
        self.lastName = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.num_of_emp += 1
        print(self.firstName, self.lastName, self.pay)

    def fullname(self):
        return "{} {}".format(self.firstName, self.lastName)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

emp_1 = Employee('Belva', 'Rachman', 50000)
emp_2 = Employee('John', 'Olfindo', 60000)

Employee.set_raise_amt(1.05)

emp_str_1 = 'Joe-Doe-70000'
emp_str_2 = 'Steve-Smith-80000'
emp_str_3 = 'Jane-Will-60000'

Employee.from_string(emp_str_1)
Employee.from_string(emp_str_2)
Employee.from_string(emp_str_3)

print(emp_1.raise_amt)
print(emp_2.raise_amt)
print("class", Employee.raise_amt)



