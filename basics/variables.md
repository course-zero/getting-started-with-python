- In Python, a variable is just a **label** assigned to a memory that contains a value.
- A variable can point to the value of any data type.
- A value not assigned to a variable (_label_) is garbage collected.

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

## Delete a variable
- The `del` keyword removes the binding between variable name and the value by removing the variable (_label_).
- The value will be garbage collected unless pointed by another vaiable.

> https://stackoverflow.com/questions/21053380/what-does-del-do-exactly)

```py
a = b = 1
del b
print(b)
# => NameError: name 'b' is not defined
print(a)
# => 1
```

## :bulb: convention
- Generally use lowercase ASCII letters.
- You can use **camelCase** or **snake_case** syntax.
- Use `ALL_UPPERCASE` letters for global constants (_fixed values_).
  - Constants do not exist in Python -> https://stackoverflow.com/a/2682752/2790983
- Use `_` prefix for `_private` or `_INTERNAL` variables and constants.
- Do not start a variable with a digit.
