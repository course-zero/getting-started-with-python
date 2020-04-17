```py
from decimal import Decimal as D
from fractions import Fraction as F
```

```py
# declare an integer
a = 1
print(a)
# => 1
```

```py
# declare a float (presence of a decimal point)
a = 1.0
print(a)
# => 1.0
```

```py
# convert integer to a float
a = float(1)
print(a)
# => 1.0
```

```py
# convert integer to a float
a = 1 + 0.0
print('1 + 0.0 =>', a)
# => 1 + 0.0 => 1.0
```

```py
# convert float to an integer
a = int(1.0)
print('int(1.0) =>', a)
# => int(1.0) => 1
```

```py
# convert integer from a string
a = int("1") # must not contain decimal point
print(a)
# => 1
```

```py
# convert float from a string
a = float("1.2")
print(a)
# => 1.2
```

```py
# round a float number
a = round( 1.035532, 2 ) # upto 2 decimal points
print(a)
# => 1.04
```

```py
# get absolute of integer (exact distance from 0 origin)
a = abs( -4 )
print(a)
# => 4
```

```py
# get absolute of float
a = abs( -1.035532 )
print(a)
# => 1.035532
```

```py
# hexadecimal number (hex() converts)
a = 0xFF # 0XFF
print('0xFF =', a)
# => 0xFF = 255
```

```py
# octal number ( oct()  converts )
a = 0o11 # same as 0O11
print("038 =", a)
# => 038 = 9
```

```py
# binary number (bin() converts)
a = 0b11 # 0B11
print(a)
# => 3
```

```py
# floats are not accurate
# https://www.programiz.com/python-programming/numbers
a = 3.3
b = 1.1 + 2.2
print('a == b', a == b)
# => a == b False
```

```py
# use decimal package
a = D('3.3')
b = D('1.1') + D('2.2')
print('decimal: a == b', a == b)
# => decimal: a == b True
```

```py
# fraction problem
a = 11/3
b = (5/3) + (6/3)
print('a == b', a == b)
# => a == b False
```

```py
# use fractions package
a = F('11/3')
b = F(5, 3) + F(6, 3)
print('after: a == b', a == b)
# => after: a == b True
```

```py
# get a fraction
a = F('3.5')
print( "F('3.5')", F('3.5') )
# => F('3.5') 7/2
```