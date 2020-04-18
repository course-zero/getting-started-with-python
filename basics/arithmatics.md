## addition

```py
a, b = 4, 2
c = a + b
print(c)
# => 6
```

## substraction
```py
a, b = 4, 2
c = a - b
print(c)
# => 2
```

## multiplication
```py
a, b = 4, 2
c = a * b
print(c)
# => 8
```

## division (float)
```py
a, b = 4, 2
c = a / b
print(c) 
# => 2.0
```

## division (integer)
```py
a, b = 4, 2
c = a // b
print(c)
# => 2
```

## power
```py
a, b = 4, 2
c = a ** b # a to the power of b (4^2)
print(c)
# => 16
```

## reminder
```py
a, b = 4, 2
c = a % b
print(c)
# => 0
```

## sign change
```py
a, b = 4, 2
c = -a
print(c)
# => -4
```

## compare values
```py
a, b = 4, 2
a = 1
b = 1
print('a == b', a == b)
# => a == b True
```

## compare object ids (memory locations) (same as id(a) == id(b))
```py
a = 1
b = 2
print('a is b', a is b)
# => a is b False
```

## not equal value check
```py
a = 1
b = 2
print( 'a != b', a != b )
# => a != b True
```

## not equal object check
```py
a = 1
b = 1
print( 'a is not b', a is not b ) # a is b
# => a is not b False
```

## :bulb: order of execution
() => +x => -x => ** => * => / => % => + => -
