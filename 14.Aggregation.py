# 14. Aggregation

class Department:
    def __init__(self, name, employees):
        self.name = name
        self.employees = employees

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

e1 = Employee("Kazuya", 100000)
d1 = Department("Sales", e1)
print(d1.employees.name)
print(d1.employees.salary)