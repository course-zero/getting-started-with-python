```py
# a package is collection of modules that can be imported under one name. A package is a directory containing module files. This directory should also contain `__init__.py` which is usually empty to make this directory as python package
# python package name should be all lowercase letters although the use of underscores is discouraged. (https://www.python.org/dev/peps/pep-0008/#package-and-module-names)

import basicmath
# => basicmath/__init__.py: __name__ =>  basicmath
# => basicmath/__init__.py: __package__ =>  basicmath
# => basicmath/utils.py: __name__ =>  basicmath.utils
# => basicmath/utils.py: __package__ =>  basicmath

# like modules, python load package only once. It also compiles the package inside __pycache__ directory inside the package directory itself. This directory should not be commited as bytecode is tailored to the OS.
import basicmath

# like __name__ variable inside a file tells if the file is imported as a module or executed as main. Likewise, __package__ tells how a module is accessed. If a file is executed as main, __package__ is `None`. If a file is accessed as module but does not contains inside a package, __package__ is empty. If a file is accessed as a module from within a package, __package__ is the name of the package it contains inside of access as. For __init__.py, __name__ and __package__ is the same, which is name of the package.

# python package can also be reloaded using `importlib` package
import importlib
importlib.reload(basicmath)
# => basicmath/__init__.py: __name__ =>  basicmath
# => basicmath/__init__.py: __package__ =>  basicmath

# to see all exported members, we need to use `dir` function
print( "dir(basicmath) => ", dir(basicmath) )
# => dir(basicmath) =>  ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'info', 'utility', 'utils', 'version']

# `__init__.py` file can also contain export members which will be accessible on package name
print( "basicmath.info() => ", basicmath.info() )
# => basicmath.info() =>  Yes, init can also contain functions.

# import `calculator` module from a package
import basicmath.calculator
# => basicmath/calculator.py: __name__ =>  basicmath.calculator
# => basicmath/calculator.py: __package__ =>  basicmath
# => basicmath/numbers/power.py: __name__ =>  basicmath.numbers.power
# => basicmath/numbers/power.py: __package__ =>  basicmath.numbers

print( 'basicmath.calculator.add(1, 2) => ', basicmath.calculator.add(1, 2) )
# => basicmath.calculator.add(1, 2) =>  3

# another module import style
from  basicmath import calculator
print( 'calculator.add(1, 2) => ', calculator.add(1, 2) )
# => calculator.add(1, 2) =>  3

# python packages can have nested subppackages. A subpackage is directory inside package directory containing __init__.py file.

# from basicmath.numbers package, import power module
from basicmath.numbers import power
print( 'power.square(2) => ', power.square(2) )
# => power.square(2) =>  4


# python package can also be conditionally loaded
if True:
    # from basicmath.numbers.power module, import square function
    from basicmath.numbers.power import square
    print( 'square(2) => ', square(2) )
# => square(2) =>  4

# similar to module search pyth, python looks for packages in same order.

# intra-package reference using absolute name is valid. Check basicmath/calculator.py
# but importing anything inside a module also exports it (like `power` is available on calculator)
print( 'calculator.square(3)', calculator.square(3) )
# => calculator.square(3) 9

# we can use relative imports as well (https://docs.python.org/3/tutorial/modules.html#intra-package-references)

# inside a package, if a script is executed as package, where `__name__` is `packagename`, `.` also represent as a package. Hence, we imported everything from `.utils`modules (same as basicmath.calculator but empty package name) and dumped inside package namespace to export them. We also renamed it to utility and exported it.
print( "basicmath.utility.version() => ", basicmath.utility.version() )
# => basicmath.utility.version() =>  1.0.0
print( "basicmath.version() => ", basicmath.version() )
# => basicmath.version() =>  1.0.0
```