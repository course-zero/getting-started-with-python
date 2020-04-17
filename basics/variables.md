```py
# declare a variable
a = 1
print(a)
# => 1
```

```py
# override a value
a = 10
print(a)
# => 10
```

```py
# declare multiple variable in a single line
b, c = 2, 3
print( b, c )
# => 2 3
```

```py
# assign same variable
a = b = c = 1
print('a = b = c = 1 => ', a, b, c)
# => a = b = c = 1 =>  1 1 1
```

```py
# delete a variable
# (del removes the binding from the variable and it will be garbage collected: https://stackoverflow.com/questions/21053380/what-does-del-do-exactly)
b = 1
del b
print(b)
# => NameError: name 'b' is not defined
```

#### convention
- You can use camelCase for a variable.
- Do not start a variable with a digit.
