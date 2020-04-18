```py
# python for loop is based on "collection based iteration" only
#
# for elem in iterable:
#   <statement>
#

# list
# WARNING: Python's for loop doesn't use indexes, it return values
print('list iteration', end=" :=> ")
for elem in [1,2,3]:
    print( elem * elem, end=" " )
print('')

# => list iteration :=> 1 4 9 
```

```py
# tuple
print('tuple iteration', end=" :=> ")
for elem in (1,2,3):
    print( elem * elem, end=" " )
print('')

# => tuple iteration :=> 1 4 9 
```

```py
# set
print('set iteration', end=" :=> ")
for elem in {1,2,3}:
    print( elem * elem, end=" " )
print('')

# => set iteration :=> 1 4 9
```

```py
# dictionary (key)
print('dictionary iteration', end=" :=> ")
for elem in { 'firstName': 'John', 'lastName': 'doe' }:
    print( elem, end=" " )
print('')

# => dictionary iteration :=> firstName lastName
```

```py
# range
print('range iteration', end=" :=> ")
for elem in range(1, 4):
    print( elem * elem, end=" " )
print('')

# => range iteration :=> 1 4 9
```

```py
# break statement in for loop
print('break when number is 5: range 1-10', end=" :=> ")
for elem in range(1, 10):
    if elem == 5:
        break
    
    print( elem, end=" " )
print('')

# => break when number is 5: range 1-10 :=> 1 2 3 4
```

```py
# continue statement in for loop
# here `pass` won't work
print('continue when number is 5: range 1-10', end=" :=> ")
for elem in range(1, 10):
    if elem == 5:
        continue
    
    print(elem, end=" ")
print('')

# => continue when number is 5: range 1-10 :=> 1 2 3 4 6 7 8 
```

```py
# `continue` skips iteration on inner loop only
print('continue check for parent-child iteration', end=" :=> ")
for i in range(1, 4):
    for j in range(1, 4):
        if i == 2 and j == 2:
            continue
    
        print("j={}".format(j), end=" ")
    print("[i={}]".format(i), end=" / ")
print('')

# => continue check for parent-child iteration :=> j=1 j=2 j=3 [i=1] / j=1 j=3 [i=2] / j=1 j=2 j=3 [i=3] / 
```

```py
# `break` terminates iteration of inner loop only
print('break check for parent-child iteration', end=" :=> ")
for i in range(1, 4):
    for j in range(1, 4):
        if i == 2 and j == 2:
            break
    
        print("j={}".format(j), end=" ")
    print("[i={}]".format(i), end=" / ")
print('')

# => break check for parent-child iteration :=> j=1 j=2 j=3 [i=1] / j=1 [i=2] / j=1 j=2 j=3 [i=3] / 
```

```py
# transform a list to a generator using for loop
print('for loop: transform [1,2,3,4] to square list', end=" :=> ")
squares = (elem * elem for elem in [1,2,3,4])
print(list(squares))

# => for loop: transform [1,2,3,4] to square list :=> [1, 4, 9, 16]
```

```py
# else block in for loop
# else block is invoked when all elements are iterated
# provided no `break` statement in for loop
print('else block in iteration', end=" :=> ")
for elem in range(1, 4):
    print( elem * elem, end=" " )
else:
    print(' :=> finished', end=" ")
print('')

# => else block in iteration :=> 1 4 9  :=> finished 
```