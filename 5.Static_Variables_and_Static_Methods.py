# 5. Static Variables and Static Methods

class MathUtils:
    @staticmethod
    def add(a, b):
        print("Sum:")
        return a + b
print(MathUtils.add(2,3))