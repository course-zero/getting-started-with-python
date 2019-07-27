
# define a complex number
a = 1 + 2j
print(a)

# coplex number without a real part
a = 2.5j
print('imaginary only complex a', a)

# convert complex number from a string
a = complex('1+2j') # do not add spaces
print(a)

# get real part
print(a.real) # returns float

# get imaginory part
print(a.imag) # return float

# complex numbers arthmetics
c = (1 + 2j) + (2 + 4j) # similar only  -, *, /
print(c)

# absolute value
c = abs(3 + 4j) # same value for (3 - 4j) or (-3 - 4j) or (-3 + 4j)
print(c)