```py
# True value
a = True
print(a)
# => True
```

```py
# False value
a = False
print(a)
# => False
```

```py
# convert to boolean
print("bool(0) =", bool(0))
# => bool(0) = False

print("bool(1) =", bool(1))
# => bool(1) = True

print("bool(2) =", bool(2))
# => bool(2) = True

print("bool('') =", bool(''))
# => bool('') = False

print("bool('0') =", bool('0'))
# => bool('0') = True

print("bool('1') =", bool('1'))
# => bool('1') = True

print("bool('abc') =", bool('abc'))
# => bool('abc') = True

print("bool([]) =", bool([]))
# => bool([]) = False

print("bool([0]) =", bool([0]))
# => bool([0]) = True

print("bool(()) =", bool(())) # empty tuple
# => bool(()) = False

print("bool((1,)) =", bool((1,))) # non-empty tuple
# => bool((1,)) = True
```

```py
# add a number and boolean
a = True + 10
b = False + 10
print( a, b )
# => 11 10
```
