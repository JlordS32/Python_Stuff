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
emp_3 = Employee('Jaylou', 'Rasonabe', 80000)

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())
print(emp_2.fullname())
print("--------------------------")

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
print(emp_1.raise_amt)
print("---------------------------")

# changing the variable via self will only affect the self
# changing the variable via class however will affect the entire "Employee.raise_amount = 1.05"

emp_1.raise_amt = 1.05
Employee.raise_amt = 2
print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)
print("\n" + "Number of Employee:", Employee.num_of_emps)
print("---------------------------")



""" My Function Test """

print("\n")


class Employee_1:
    def type_employee(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

emp1_1 = Employee_1()
emp2_2 = Employee_1()

emp1_1.type_employee('Belva', 'Rachman', 50000)
emp2_2.type_employee('Jaylou', 'Rasonabe', 60000)
print(emp1_1.first, emp1_1.last)
print(emp2_2.first, emp2_2.last)
print(emp1_1.email,  emp2_2.email)

if __name__ == "__main__":
    pass