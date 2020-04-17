```py
a, b = 4, 2

# addition
c = a + b
print(c)
# => 6
```

```py
# substraction
c = a - b
print(c)
# => 2
```

```py
# multiplication
c = a * b
print(c)
# => 8
```

```py
# division (float)
c = a / b
print(c) 
# => 2.0
```

```py
# division (integer)
c = a // b
print(c)
# => 2
```

```py
# power
c = a ** b # a to the power of b (4^2)
print(c)
# => 16
```

```py
# reminder
c = a % b
print(c)
# => 0
```

```py
# sign change
c = -a
print(c)
# => -4
```

```py
# compare values
a = 1
b = 1
print('a == b', a == b)
# => a == b True
```

```py
# compare object ids (memory locations) (same as id(a) == id(b))
a = 1
b = 2
print('a is b', a is b)
# => a is b False
```

```py
# not equal value check
a = 1
b = 2
print( 'a != b', a != b )
# => a != b True
```

```py
# not equal object check
a = 1
b = 1
print( 'a is not b', a is not b ) # a is b
# => a is not b False
```

#### order of execution
() => +x => -x => ** => * => / => % => + => -