# list is a collection of any data type.

# list literal
a = [1, 2, 3, 4, 5]
print(a)

# using list function
a = list({1, 2, 3, 4, 5})
print(a)

# list of different data types
a = [ 1, 3.14, "string", True, [1,2,3] ]
print("different data types =", a)

# length of a slice
a = [1, 2, 3, 4, 5]
b = len(a)
print( 'len(a) =', len(a) )

# access an element at index
a = [1, 2, 3, 4, 5]
b = a[0]
print('a[0] =', b)

# access element at index from the end
a = [1, 2, 3, 4, 5]
b = a[-1]
print('a[-1] =', b) # -0 is same as 0, hence index from the end starts at -1

# nested lists
a = [ [1,2], [3,4], [5] ]
print( "nested list =", a, "and a[1][0] =", a[1][0] )

# lists are mutable
a = [1, 2, 3, 4, 5]
a[-1] = 50
print("a after (a[-1] = 50) =", a)

# concat two lists
a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]
print( 'a + b =', a + b )

# append new item
a = [1, 2, 3, 4, 5]
a.append( 6 ) # no return value
print("a after (a.append( 6 )) =", a)

# repeat a list
a = [1, 2, 3]
b = a * 3
print("a*3 =", b)

# delete an item (use del keyword)
a = [1, 2, 3, 4, 5]
del a[0]
print("a after (del( a[0] )) =", a)

# return index of an element (throws ValueError exception if value not found)
a = [1, 2, 3, 4, 5]
b = a.index(3)
print("a after (a.index(3))) =", a.index(3))

# extend a list with another
a = [1, 2, 3]
b = [4, 5]
a.extend( b ) # extend a with b, no return value
print('a after (a.extend( list )) =', a)

# extend a list with tuple
a = [1, 2, 3]
b = (3, 4)
a.extend(b) # no return value
print('a after (a.extend( tuple )) =', a)

# merge two lists using + operator
a = [1,2,3]
b = [3,4,5]
c = a + b
print('a + b lists', c)

# insert a value at an index and pushes remaining value to the right
# if index is greater than list length, adds new value at the end
a = [1, 2, 4, 5]
a.insert(2, 3) # insert 3 at 2nd index, no return value
print('a after (a.insert(2, 3)) =', a)

# remove an element from the list
# throws ValueError exceptionn if element doesn't exist
# only removes first occurance of the value if duplicate value exist
a = [1, 2, 3, 4, 5]
a.remove(3) # no return value
print('a after (a.remove(3)) =', a)

# count number of occurances of a value in alist
# here value can be anything, event a list or tuple
a = [ 1, 2, 2, 3, 1, 2, 4, 5 ]
count = a.count(2)
print( 'count of 2 in a =', count )

# pop (remove and return) element from a list
# takes an optional index to pop value at, default is -1
# throws IndexError when index is not present
a = [1, 2, 3, 4, 5]
value = a.pop( 2 ) # 2nd index
print('a after (a.pop( 2 )) =', a, 'and value =', value)

# reverse a list
a = [1, 2, 3, 4, 5]
a.reverse() # returns nothing
print('a after (a.reverse()) =', a)

# sort a list
a = [ 4, 2, 3, 1, 5 ]
b = [ 'a', 'c', 'd', 'e', 'b' ]
a.sort()
b.sort(reverse=True)
print('sorted a ASC, b DESC =', a, b)

# sort a list with custom function
a = [ [1, 2], [1, 2, 3], [1], [1, 3] ]
a.sort(key=len, reverse=True) # len is built in function
print('a after a.sort(key=len, reverse=True)', a)

# shallow copy (as a=b only references)
a = [1, 2, 3, 4, 5]
b = [1, [2, 4], 4, 5]
c = a.copy() # returns shallow copy
d = b.copy() # returns shallow copy

c[1] = 20
d[1][1] = 40

print( "copy-op: a and c =", a, c)
print( "copy-op: b and d =", b, d ) # shallow-copy

# clear/empty a list
a = [1, 2, 3, 4, 5]
a.clear()
print('a after a.clear() =', a)

# check if an element exists in a list
a = [1,2,3,4,5]
exists_1_in_a = 1 in a
does_not_exist_10_in_a = 10 not in a
print('exists_1_in_a', exists_1_in_a)
print('does_not_exist_10_in_a', does_not_exist_10_in_a)

# slice operator
# it returns a new slice
a = [1, 2, 3, 4, 5]
print('a[0:2] =', a[0:2] ) # end index excluded
print('a[0:] =', a[0:]) # default end index is length of a list
print('a[:len(a)] =', a[:len(a)]) # default start index is 0
print('a[:] =', a[:]) # use all defaults, shallow copy
print('a[-3:] =', a[-3:]) # can use index from the end

# assign multiple items
a = [1, 2, 3, 4, 5]
a[0:2] = [10,20]
print('a after (a[0:2] = [10,20]) =', a)

# delete multiple values
a = [1, 2, 3, 4, 5]
a[0:2] = []
print('a after (a[0:2] = []) =', a)

# clear list
a = [1, 2, 3, 4, 5]
a[:] = []
print('a after (a[:] = []) =', a)

# clear a list using del
a = [1, 2, 3, 4, 5]
del a[:]
print('a after (del a[:]) =', a)

# list comprehension
# syntax => [ expression for x in range() ] / expression => x * 2
a = [ x * 2 for x in range(5) ]
print('list comprehension : a =>', a)

# list comprehension filter
# syntax => [ expression for x in range() if condition ] / expression => x * 2 / condition => x % 2 != 0
a = [ x * 2 for x in range(10) if x % 2 != 0 ]
print( 'list comprehension filter : a =>', a )

# list comprehension nested for loops
a = [ ( x + " " + y ) for x in [ "Good", "Have a good" ] for y in [ "Morning", "Evening", "Night" ] ]
print('Nested list compregensions : a =>', a)

# list comprehension nested for loops with filter
a = [ ( x + " " + y ) for x in [ "Good", "Have a good" ] for y in [ "Morning", "Evening", "Night" ] if x == 'Good' ]
# same => a = [ ( x + " " + y ) for x in [ "Good", "Have a good" ] if x == 'Good' for y in [ "Morning", "Evening", "Night" ] ]
print('Nested list compregensions with filter : a =>', a)

# convert range to a list
a = range(1,5)
print( 'list(range(1,5))', list(a) )

# list iteration
a = [1,2,3,4,5]
for val in a:
    print(val, end=" ")