# 13. Composition

class Engine:
    def start(slef):
        print("Engine started")

class Car:
    def __init__(self, engine):
        self.engine = engine
    
    def start(self):
        self.engine.start()

e1 = Engine()
c1 = Car(e1)
c1.start()