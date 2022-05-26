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


class Developer(Employee):
    raise_amt = 1.1

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def rev_emp(self, emp):
        if emp not in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.firstName, self.lastName, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)


emp_1 = Employee('Belva', 'Rachman', 50000)
emp_2 = Employee('John', 'Olfindo', 60000)

dev_1 = Developer('Elon', 'Musk', 60000, 'Python')
dev_2 = Developer('Jeff', 'Bezos', 70000, 'Java')

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

print("\n{}".format(dev_1.email))
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)
print(dev_1.prog_lang)

print("\n{}".format(dev_2.email))

mgr_1 = Manager('\nSue', 'Smith', 100000, [dev_1])
mgr_1.add_emp(dev_2)
mgr_1.print_emps()

print(emp_1)