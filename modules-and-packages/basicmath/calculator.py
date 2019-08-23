# calculator module
print( 'basicmath/calculator.py: __name__ => ', __name__ )
print( 'basicmath/calculator.py: __package__ => ', __package__ )

# export a function
def add( num1, num2 ):
    return num1 + num2

# import numbers subpackage using absolute intra-package referennce
from basicmath.numbers import power
def square(num):
    return power.square(num)
