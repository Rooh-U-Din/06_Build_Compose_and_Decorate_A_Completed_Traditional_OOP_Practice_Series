# 8. The super() Function

class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

t1 = Teacher("Kazuya", "Martial Arts")
print(t1.name)
print(t1.subject)
