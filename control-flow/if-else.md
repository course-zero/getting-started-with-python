```py
# simple if condition
condition = True

if condition:
    print('if: condition is True')

# => if: condition is True
```

```py
# if-else condition
condition = False

if condition:
    print('if-else: condition is True')
else:
    print('if-else: condition is False')

# => if-else: condition is False
```

```py
# if-elif-else: evaluate a condition
value = 2

if value < 0:
    print('if-elif-else: Value is negative.')
elif value == 0:
    print('if-elif-else: Value is zero.')
else:
    print('if-elif-else: Value is positive.') 

# => if-elif-else: Value is positive.
```

```py
# false values: check boolean data-type lesson
value = []

if value:
    print('false value: list is non empty.')
else:
    print('false value: list is empty.')

# => false value: list is empty.
```

```py
# nested if-else condition
value = 0

if value >= 0:
    print('nested: value is positive.')

    if value == 0:
        print('nested: value is 0.')
    else:
        print('nested: value is greater than 0.')
else:
    print('nested: value is negative.')

# => nested: value is positive.
# => nested: value is 0.
```

```py
# and conditions
value = 5

if value >= 0 and value <= 9 :
    print('and condition: value is between 0-9')

# => and condition: value is between 0-9
```

```py
# or condition
value = 3

if value == 3 or value == 6:
    print('or condition: it is either 3 or 6.')

# => or condition: it is either 3 or 6.
```

```py
# if a word exist in a string
if 'am' in 'I am a wonderful person':
    print('word test: "am" exists in the sentense.')

# => word test: "am" exists in the sentense.
```

```py
# if an element exist in a list
if 2 in [1,2,3,4,5]:
    print('list test: 2 exists in the list.')

# => list test: 2 exists in the list.
```

```py
# if an element exists in a tuple
if 2 in (1,2,3,4,5):
    print('tuple test: 2 exists in the tuple.')

# => tuple test: 2 exists in the tuple.
```

```py
# if an element exists in a set
if 2 in {1,2,2,3,4,4,5}:
    print('set test: 2 exists in the set.')

# => set test: 2 exists in the set.
```

```py
# if an element exists in a frozenset
if 2 in frozenset( [ 1,2,2,3,4,4,5 ] ):
    print('frozenset test: 2 exists in the frozenset.')

# => frozenset test: 2 exists in the frozenset.
```

```py
# object comparison
list_one = [1,2,3]
list_two = [1,2,3]

if list_one == list_two:
    print('list comparison: two lists have same value.')

if list_one is list_two:
    print('list comparison: two lists are the same.')

# => list comparison: two lists have same value.
```

```py
# if-else on single line
value = 3
if value == 3: print('single line: value is 3')

# if-else on single line and other statements
value = 4
if value == 3: print('single line: 3'); print('later...')

# => single line: value is 3
```

```py
# ternary operator
# true-expression> if condition else <false-expression>
value = 1
print('ternary: value is 1') if value == 1 else print('ternary: value is not 1')

# => ternary: value is 1
```

```py
# ternary return value
value = 2
name = 'mina' if value == 1 else 'other'
print('ternary return value: ' + name)

# => ternary return value: other
```

```py
# pass statement: represents a null statement, as placeholder
# https://www.programiz.com/python-programming/pass-statement
value = 0
if value == 0:
    pass
else:
    print('pass: doing something with the value.')

# => 
```