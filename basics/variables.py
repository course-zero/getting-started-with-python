# declare a variable
a = 1
print(a)

# override a value
a = 10
print(a)

# declare multiple variable in a single line
b, c = 2, 3
print( b, c )

# assign same variable
a = b = c = 1
print('a = b = c = 1 => ', a, b, c)

# delete a variable (del removes the binding from the variable and it will be garbage collected: https://stackoverflow.com/questions/21053380/what-does-del-do-exactly)
b = 1
del b
print(b)

# convention
# you can use camelCase for a variable
# do not start a variable with a digit
