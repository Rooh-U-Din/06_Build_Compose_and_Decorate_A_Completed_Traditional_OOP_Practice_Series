# 10. Instance Methods

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def bark(self):
        print(f"{self.name} is barking")
        
d1 = Dog("Dogesh", "stray dog")
d1.bark()

