# 6. Constructors and Destructors

class Logger:
    def __init__(self):
        
        print("A fight is about who`s left standing nothing else...")
    def __del__(self):
        
        print("A fight is about who`s alive...")

print("constructor")
l1 = Logger()
print("destructor")
del l1
