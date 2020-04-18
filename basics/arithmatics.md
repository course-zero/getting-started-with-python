## Addition

```py
a, b = 4, 2
c = a + b
print(c)
# => 6
```


## Substraction
```py
a, b = 4, 2
c = a - b
print(c)
# => 2
```


## Multiplication
```py
a, b = 4, 2
c = a * b
print(c)
# => 8
```


## Division

#### Get float result
```py
a, b = 4, 2
c = a / b
print(c) 
# => 2.0
```

#### Get integer result
```py
a, b = 4, 2
c = a // b
print(c)
# => 2
```


## Power
```py
a, b = 4, 2
c = a ** b # a to the power of b (4^2)
print(c)
# => 16
```


## Reminder
```py
a, b = 4, 2
c = a % b
print(c)
# => 0
```


## Sign change
```py
a, b = 4, 2
c = -a
print(c)
# => -4
```


## Compare values

#### Check if two values are the same
```py
a, b = 4, 2
a = 1
b = 1
print('a == b', a == b)
# => a == b True
```

#### Check if two values are not the same
```py
a = 1
b = 2
print( 'a != b', a != b )
# => a != b True
```


## Compare object ids (_memory locations_)

#### If two variables point to the same value
```py
a = 1
b = c = 2
print('a is b', a is b)
# => a is b False
print('b is c', b is c)
# => b is c True
```
> This operation is same as `id(a) == id(b)` (https://docs.python.org/3/library/functions.html#id)

#### If two variables point to the different values
```py
a = 1
b = 1
print( 'a is not b', a is not b ) # a is b
# => a is not b False
```

## :bulb: Unsupported operations in Python
- `x++` and `x--`
- `++x` and `--x`
- `x += 1` or `x <operator>= <value>` 


## :bulb: Order of the execution
`()` => `+x` => `-x` => `**` => `*` => `/` => `%` => `+` => `-`
