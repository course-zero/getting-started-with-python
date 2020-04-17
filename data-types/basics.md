```py
# in python, everything is an object
a, b, c = 1, 1.0, 'Hello World!'
print( type(a), type(b), isinstance( c, str ) )
# => <class 'int'> <class 'float'> True
```

#---------------------------------------#

```py
'''
https://medium.com/@larmalade/python-everything-is-an-object-and-some-objects-are-mutable-4f55eb2b468b
# https://stackoverflow.com/a/27460468
# https://stackoverflow.com/a/38189759
Python has mutable and immutable data types.
We can not modify the value of immutable data type.
For example, string even being a slice, can not be modified using value assignment of an index.

class           immutable
int                 Yes
float               Yes
bool                Yes
tuble               Yes
frozenset           Yes
set                  No
list                 No
dictionary           No
'''
```

```py
# id() returns the unique identifier of an object
# id doesn't necessarily returns memory address of an object => https://stackoverflow.com/questions/27460234/two-variables-with-the-same-list-have-different-ids-why-is-that/27460468#27460468
a = 1
print( 'id of a', id(a) )
# => id of a 4509404064
```

```py
# in python, a variable is like a label assigned to a given value (obecj)
# for optimization, python can assign multiple labels to the same immutable data types
a, b = 1, 1
c, d = 'Hi', 'Hi'

print( "id(a) - id(b)", id(a), ' - ' , id(b) )
# => id(a) - id(b) 4509404064  -  4509404064
print( "id(c) - id(d)", id(c), ' - ' , id(d) )
# => id(c) - id(d) 4511513328  -  4511513328
```

```py
# use `is` keyword, to check if object in memory represented two labels are the same
a, b = 1, 1
print( 'a is b', a is b )
# => a is b True
```

```py
# this does not work with mutable data types, python will always create new object for it
a, b = [1], [1]
print( "id(a) - id(b)", id(a), ' - ' , id(b) )
# => id(a) - id(b) 4510559200  -  4512671936
print( 'a is b', a is b )
# => a is b False
```

```py
# when it comes to storing large data, python will also create distinct object
a, b = 1000, 1000
print( "id(a) - id(b)", id(a), ' - ' , id(b) )
# => id(a) - id(b) 4512678768  -  4512678896
print( 'a is b', a is b )
# => a is b False
```

```py
# python will automatically create new value when a label points to same object in memory
a, b = 1, 1
print( "before: id(a) - id(b)", id(a), ' - ' , id(b) )
# => before: id(a) - id(b) 4509404064  -  4509404064
print( 'before: a is b', a is b )
# => before: a is b True
b = 2
print( "after: id(a) - id(b)", id(a), ' - ' , id(b) )
# => after: id(a) - id(b) 4509404064  -  4509404096
print( 'after: a is b', a is b )
# => after: a is b False
```

```py
# python will throw error when an immutable data type is forcefully tried to change
a = 'Hello World!' # immutable # same for a tuple
print('before: id(a)', id(a))
# => before: id(a) 4512977264
# a[0] = 'B' # change the value
a = 'How are you?' # create new object and assign this label, recycle old value
print('after: id(a)', id(a))
# => after: id(a) 4512977392
```

```py
# for both mutable and immutable data type, new value is created
a = b = 1 # same as a = 1 and b = a
c = d = [1]
print('before: a is b / c is d', a is b, '/', c is d)
# => before: a is b / c is d True / True

b = 2
d = [2]
print('after: a is b / c is d', a is b, '/', c is d)
# => after: a is b / c is d False / False
```

```py
# mutable data type persist changes
a = [1,2,3]
b = a # points to the same value

b[0] = 10
print('a - b', a, b)
# => a - b [10, 2, 3] [10, 2, 3]
```

```py
# a immutable data type can contain immutable data type
# hence a true immutibity is with individual element reference, not their values
a = (1, [2, 20], 3)
# a[0] = 10 # fails, trying to change the immutable data type
# a[1] = [2, 20, 200] also fails
a[1][1] = 200 # works
print('a', a)
# => a (1, [2, 200], 3)
```

```py
# immutable data type is referenced
a = [2, 20]
b = (1, a, 3)
b[1][1] = 200 # works
print('b', b)
# => b (1, [2, 200], 
```

```py
# mutable data type are copied by value
a = 2
b = (1, a, 3)

print('before: a is b[1] => ', a is b[1])
# => before: a is b[1] =>  True
print( 'before: a, b => ', a, ',', b )
# => before: a, b =>  2 , (1, 2, 3)
```

```py
a = 3 # a points to different object now
print('after: a is b[1] => ', a is b[1])
# => after: a is b[1] =>  False
print( 'after: a, b => ', a, ',', b )
# => after: a, b =>  3 , (1, 2, 3)
```

```py
# None in python
# None is a global singleton object in python that signifies empty object
# A variable can point to None just to say that it holds null value
# https://stackoverflow.com/questions/19473185/what-is-a-none-value
a = 1
print('before a =>', a)
# => before a => 1
a = None # this does not delete the variable
print('after a =>', a) # used for statement 'a is not None'
# => after a => None
```

