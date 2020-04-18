```py
# A module is a python file containing variables, functions and classes which can be used by other python scripts.

# using this import style, all exported veriables are stored inside `calculator` name from `calculator.py` file in the current directory
# python module name should be all lowercase letters with optional underscore (https://www.python.org/dev/peps/pep-0008/#package-and-module-names)
import calculator

# => caculator.py __name__ =>  calculator
# => caculator.py __package__ =>  

# When we import a module, python sets `__name__` variable to the module name which is name of the python script file, in this case, `calculator`. If the module file is executed as main file, it will be `__main__`. Using this, we can take some action.

# We can check variables exported by a module using `dir()` function
print( 'dir(calculator) => ', dir(calculator))
# => dir(calculator) =>  ['Calculator', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'add', 'version']

# we need to use `.` operator to access variables
print( 'calculator.add(1, 2) => ', calculator.add(1, 2))
# => alculator.add(1, 2) =>  3


# module running in single python thread is initialized only once and cached inside `__pycache__` directory in the directory where module file is present. This directory contains `.pyc` files which are compiled bytecode of the modules you are importing. This will increase the performance as modules are not subjected to change frequently.  This directory should not be commited as bytecode is tailored to the OS.

# we can rename a module to avoid collision with other modules or names
import calculator as calc
print( 'calc.version => ', calc.version)
# => calc.version =>  v1.0.1

# we can import specific members from a module
# this make sense for classes but not recommended
from calculator import Calculator
myCalc = Calculator(2, 3)
print( 'myCalc.multiply() => ', myCalc.multiply())
# => myCalc.multiply() =>  6

# we can also import everything exported by the module in the current namespace (score)
# but this is a bad practice
from calculator import *
print( 'add(2, 5) => ', add(2, 5))
# => add(2, 5) =>  7

# when we import a module, python first searches for the python files with that name in
# 1. local directory
# 2. Directory defined by PYTHONPATH environment variable (multiple: https://stackoverflow.com/a/39682723)
# 3. Python standard installation directory
# we see list of resolution directory from `sys.path` name
import sys
print("sys.path => ", sys.path)
# => sys.path =>  ['/Users/Uday.Hiwarale/uday-gh/getting-started-with-python/modules-and-packages', '/usr/local/Cellar/python/3.7.7/Frameworks/Python.framework/Versions/3.7/lib/python37.zip', '/usr/local/Cellar/python/3.7.7/Frameworks/Python.framework/Versions/3.7/lib/python3.7', '/usr/local/Cellar/python/3.7.7/Frameworks/Python.framework/Versions/3.7/lib/python3.7/lib-dynload', '/usr/local/lib/python3.7/site-packages']

# as python caches a module, it can reloaded using `importlib` package.
# this can be necessary if module is changed during course of the program execution
import importlib
importlib.reload(calculator)

# => caculator.py __name__ =>  calculator
# => caculator.py __package__ => 

# conditional importing of module
if True:
    import sample
    sample.info()


# => sample.py __name__ =>  sample
# => I am sample module
```