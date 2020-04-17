```py
# list is a collection of any data type.
# list literal
a = [1, 2, 3, 4, 5]
print(a)
# => [1, 2, 3, 4, 5]
```

```py
# using list function
a = list({1, 2, 3, 4, 5})
print(a)
# => [1, 2, 3, 4, 5]
```

```py
# list of different data types
a = [ 1, 3.14, "string", True, [1,2,3] ]
print("different data types =", a)
# => different data types = [1, 3.14, 'string', True, [1, 2, 3]]
```

```py
# length of a slice
a = [1, 2, 3, 4, 5]
b = len(a)
print( 'len(a) =', len(a) )
# => len(a) = 5
```

```py
# access an element at index
a = [1, 2, 3, 4, 5]
b = a[0]
print('a[0] =', b)
# => a[0] = 1
```

```py
# access element at index from the end
a = [1, 2, 3, 4, 5]
b = a[-1]
print('a[-1] =', b) # -0 is same as 0, hence index from the end starts at -1
# => a[-1] = 5
```

```py
# nested lists
a = [ [1,2], [3,4], [5] ]
print( "nested list =", a, "and a[1][0] =", a[1][0] )
# => nested list = [[1, 2], [3, 4], [5]] and a[1][0] = 3
```

```py
# lists are mutable
a = [1, 2, 3, 4, 5]
a[-1] = 50
print("a after (a[-1] = 50) =", a)
# => a after (a[-1] = 50) = [1, 2, 3, 4, 50]
```

```py
# concat two lists
a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]
print( 'a + b =', a + b )
# => a + b = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]
```

```py
# append new item
a = [1, 2, 3, 4, 5]
a.append( 6 ) # no return value
print("a after (a.append( 6 )) =", a)
# => a after (a.append( 6 )) = [1, 2, 3, 4, 5, 6]
```

```py
# repeat a list
a = [1, 2, 3]
b = a * 3
print("a*3 =", b)
# => a*3 = [1, 2, 3, 1, 2, 3, 1, 2, 3]
```

```py
# delete an item (use del keyword)
a = [1, 2, 3, 4, 5]
del a[0]
print("a after (del( a[0] )) =", a)
# => a after (del( a[0] )) = [2, 3, 4, 5]
```

```py
# return index of an element (throws ValueError exception if value not found)
a = [1, 2, 3, 4, 5]
b = a.index(3)
print("a after (a.index(3))) =", a.index(3))
# => a after (a.index(3))) = 2
```

```py
# extend a list with another
a = [1, 2, 3]
b = [4, 5]
a.extend( b ) # extend a with b, no return value
print('a after (a.extend( list )) =', a)
# => a after (a.extend( list )) = [1, 2, 3, 4, 5]
```

```py
# extend a list with tuple
a = [1, 2, 3]
b = (3, 4)
a.extend(b) # no return value
print('a after (a.extend( tuple )) =', a)
# => a after (a.extend( tuple )) = [1, 2, 3, 3, 4]
```

```py
# merge two lists using + operator
a = [1,2,3]
b = [3,4,5]
c = a + b
print('a + b lists', c)
# => a + b lists [1, 2, 3, 3, 4, 5
```

```py
# insert a value at an index and pushes remaining value to the right
# if index is greater than list length, adds new value at the end
a = [1, 2, 4, 5]
a.insert(2, 3) # insert 3 at 2nd index, no return value
print('a after (a.insert(2, 3)) =', a)
# => a after (a.insert(2, 3)) = [1, 2, 3, 4, 5]
```

```py
# remove an element from the list
# throws ValueError exceptionn if element doesn't exist
# only removes first occurance of the value if duplicate value exist
a = [1, 2, 3, 4, 5]
a.remove(3) # no return value
print('a after (a.remove(3)) =', a)
# => a after (a.remove(3)) = [1, 2, 4, 5]
```

```py
# count number of occurances of a value in alist
# here value can be anything, event a list or tuple
a = [ 1, 2, 2, 3, 1, 2, 4, 5 ]
count = a.count(2)
print( 'count of 2 in a =', count )
# => count of 2 in a = 3
```

```py
# pop (remove and return) element from a list
# takes an optional index to pop value at, default is -1
# throws IndexError when index is not present
a = [1, 2, 3, 4, 5]
value = a.pop( 2 ) # 2nd index
print('a after (a.pop( 2 )) =', a, 'and value =', value)
# => a after (a.pop( 2 )) = [1, 2, 4, 5] and value = 3
```

```py
# reverse a list
a = [1, 2, 3, 4, 5]
a.reverse() # returns nothing
print('a after (a.reverse()) =', a)
# => a after (a.reverse()) = [5, 4, 3, 2, 1]
```

```py
# sort a list
a = [ 4, 2, 3, 1, 5 ]
b = [ 'a', 'c', 'd', 'e', 'b' ]
a.sort()
b.sort(reverse=True)
print('sorted a ASC, b DESC =', a, b)
# => sorted a ASC, b DESC = [1, 2, 3, 4, 5] ['e', 'd', 'c', 'b', 'a']
```

```py
# sort a list with custom function
a = [ [1, 2], [1, 2, 3], [1], [1, 3] ]
a.sort(key=len, reverse=True) # len is built in function
print('a after a.sort(key=len, reverse=True)', a)
# => a after a.sort(key=len, reverse=True) [[1, 2, 3], [1, 2], [1, 3], [1]]
```

```py
# shallow copy (as a=b only references)
a = [1, 2, 3, 4, 5]
b = [1, [2, 4], 4, 5]
c = a.copy() # returns shallow copy
d = b.copy() # returns shallow copy

c[1] = 20
d[1][1] = 40

print( "copy-op: a and c =", a, c)
# => copy-op: a and c = [1, 2, 3, 4, 5] [1, 20, 3, 4, 5]

print( "copy-op: b and d =", b, d ) # shallow-copy
# => copy-op: b and d = [1, [2, 40], 4, 5] [1, [2, 40], 4, 5]
```

```py
# clear/empty a list
a = [1, 2, 3, 4, 5]
a.clear()
print('a after a.clear() =', a)
# => a after a.clear() = []
```

```py
# check if an element exists in a list
a = [1,2,3,4,5]
exists_1_in_a = 1 in a
does_not_exist_10_in_a = 10 not in a
print('exists_1_in_a', exists_1_in_a)
# => exists_1_in_a True
print('does_not_exist_10_in_a', does_not_exist_10_in_a)
# => does_not_exist_10_in_a True
```

```py
# slice operator
# it returns a new slice
a = [1, 2, 3, 4, 5]
print('a[0:2] =', a[0:2] ) # end index excluded
# => a[0:2] = [1, 2]
print('a[0:] =', a[0:]) # default end index is length of a list
# => a[0:] = [1, 2, 3, 4, 5]
print('a[:len(a)] =', a[:len(a)]) # default start index is 0
# => a[:len(a)] = [1, 2, 3, 4, 5]
print('a[:] =', a[:]) # use all defaults, shallow copy
# => a[:] = [1, 2, 3, 4, 5]
print('a[-3:] =', a[-3:]) # can use index from the end
# => a[-3:] = [3, 4, 5]
```

```py
# assign multiple items
a = [1, 2, 3, 4, 5]
a[0:2] = [10,20]
print('a after (a[0:2] = [10,20]) =', a)
# => a after (a[0:2] = [10,20]) = [10, 20, 3, 4, 5]
```

```py
# delete multiple values
a = [1, 2, 3, 4, 5]
a[0:2] = []
print('a after (a[0:2] = []) =', a)
# => a after (a[0:2] = []) = [3, 4, 5]
```

```py
# clear list
a = [1, 2, 3, 4, 5]
a[:] = []
print('a after (a[:] = []) =', a)
# => a after (a[:] = []) = []
```

```py
# clear a list using del
a = [1, 2, 3, 4, 5]
del a[:]
print('a after (del a[:]) =', a)
# => a after (del a[:]) = []
```

```py
# list comprehension
# syntax => [ expression for x in range() ] / expression => x * 2
a = [ x * 2 for x in range(5) ]
print('list comprehension : a =>', a)
# => list comprehension : a => [0, 2, 4, 6, 8]
```

```py
# list comprehension filter
# syntax => [ expression for x in range() if condition ] / expression => x * 2 / condition => x % 2 != 0
a = [ x * 2 for x in range(10) if x % 2 != 0 ]
print( 'list comprehension filter : a =>', a )
# => list comprehension filter : a => [2, 6, 10, 14, 18]
```

```py
# list comprehension nested for loops
a = [ ( x + " " + y ) for x in [ "Good", "Have a good" ] for y in [ "Morning", "Evening", "Night" ] ]
print('Nested list compregensions : a =>', a)
# => Nested list compregensions : a => ['Good Morning', 'Good Evening', 'Good Night', 'Have a good Morning', 'Have a good Evening', 'Have a good Night']
```

```py
# list comprehension nested for loops with filter
a = [ ( x + " " + y ) for x in [ "Good", "Have a good" ] for y in [ "Morning", "Evening", "Night" ] if x == 'Good' ]
# same => a = [ ( x + " " + y ) for x in [ "Good", "Have a good" ] if x == 'Good' for y in [ "Morning", "Evening", "Night" ] ]
print('Nested list compregensions with filter : a =>', a)
# => Nested list compregensions with filter : a => ['Good Morning', 'Good Evening', 'Good Night']
```

```py
# convert range to a list
a = range(1,5)
print( 'list(range(1,5))', list(a) )
# => list(range(1,5)) [1, 2, 3, 4]
```

```py
# list iteration
a = [1,2,3,4,5]
for val in a:
    print(val, end=" ")
# => 1 2 3 4 5 
```