- In Python, a variable is just a label assigned to a memory that contains a value.
- A variable points to the value of any data type.
- A value not pointed by a variable is garbage collected.

## Declare a variable
```py
a = 1
print(a)
# => 1
```

## Override a value
Variable (_label_) points to the new value and old value unless pointed by another variable is garbage collected.

```py
a = 1
a = 10
print(a)
# => 10
```

## Declare multiple variable on a single line
```py
b, c = 2, 3
print( b, c )
# => 2 3
```

## Assign same variable
These ariables (_labels_) point to the same value.

```py
a = b = c = 1
print('a = b = c = 1 => ', a, b, c)
# => a = b = c = 1 =>  1 1 1
```

## delete a variable
- The `del` keyword removes the binding between variable name and the value by removing the variable (_label_).
- The value will be garbage collected.

> https://stackoverflow.com/questions/21053380/what-does-del-do-exactly)

```py
b = 1
del b
print(b)
# => NameError: name 'b' is not defined
```

## :bulb: convention
- You can use camelCase for a variable.
- Do not start a variable with a digit.
