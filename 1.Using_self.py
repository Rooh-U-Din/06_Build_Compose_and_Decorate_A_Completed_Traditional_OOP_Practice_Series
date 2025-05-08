# 1. Using self

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print("Student Details:")
        print(self.name)
        print(self.marks)

s1 = Student("Kazuya",100)
s2 = Student("Mishima",80)
s1.display()
s2.display()

