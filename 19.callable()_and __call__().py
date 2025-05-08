# 19. callable() and __call__()

class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    def __call__(self, num):
        return num * self.factor
    
multiplier = Multiplier(3)
print(multiplier(3))
print(callable(multiplier))
    