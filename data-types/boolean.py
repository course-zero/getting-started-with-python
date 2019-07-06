# True value
a = True
print(a)

# False value
a = False
print(a)

# conver to boolean
print("bool(0) =", bool(0))
print("bool(1) =", bool(1))
print("bool(2) =", bool(2))
print("bool('') =", bool(''))
print("bool('0') =", bool('0'))
print("bool('1') =", bool('1'))
print("bool('abc') =", bool('abc'))
print("bool([]) =", bool([]))
print("bool([0]) =", bool([0]))
print("bool(()) =", bool(())) # empty tuple
print("bool((1,)) =", bool((1,))) # non-empty tuple

# add a number and boolean
a = True + 10
b = False + 10
print( a, b )
