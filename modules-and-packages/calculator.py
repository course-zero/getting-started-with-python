print("caculator.py __name__ => ", __name__)
print("caculator.py __package__ => ", __package__)

# export a variable
version = 'v1.0.1'

# export a function
def add( num1, num2 ):
    return num1 + num2

# export a class
class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def multiply(self):
        return self.num1 * self.num2