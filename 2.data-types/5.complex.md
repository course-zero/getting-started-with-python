```py
# define a complex number
a = 1 + 2j
print(a)
# => (1+2j)
```

```py
# coplex number without a real part
a = 2.5j
print('imaginary only complex a', a)
# => imaginary only complex a 2.5j
```

```py
# convert complex number from a string
a = complex('1+2j') # do not add spaces
print(a)
# => (1+2j)
```

```py
# get real part
print(a.real) # returns float
# => 1.0
```

```py
# get imaginory part
print(a.imag) # return float
# => 2.0
```

```py
# complex numbers arthmetics
c = (1 + 2j) + (2 + 4j) # similar only  -, *, /
print(c)
# => (3+6j)
```

```py
# absolute value
c = abs(3 + 4j) # same value for (3 - 4j) or (-3 - 4j) or (-3 + 4j)
print(c)
# => 5.0
```