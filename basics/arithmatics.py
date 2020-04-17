a, b = 4, 2

# addition
c = a + b
print(c)

# substraction
c = a - b
print(c)

# multiplication
c = a * b
print(c)

# division (float)
c = a / b
print(c) 

# division (integer)
c = a // b
print(c)

# power
c = a ** b # a to the power of b (4^2)
print(c)

# reminder
c = a % b
print(c)

# sign change
c = -a
print(c)

# compare values
a = 1
b = 1
print('a == b', a == b)

# compare object ids (memory locations) (same as id(a) == id(b))
a = 1
b = 2
print('a is b', a is b)

# not equal value check
a = 1
b = 2
print( 'a != b', a != b )

# not equal object check
a = 1
b = 1
print( 'a is not b', a is not b ) # a is b

# order of execution
# () => +x => -x => ** => * => / => % => + => -