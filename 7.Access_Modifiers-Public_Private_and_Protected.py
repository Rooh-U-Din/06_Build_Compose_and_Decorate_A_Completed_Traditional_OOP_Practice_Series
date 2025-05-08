# 7. Access Modifiers: Public, Private, and Protected


class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn


e1 = Employee("Kazuya", 100000, 123456789)
print(e1.name)
print(e1._salary)
# print(e1.__ssn)