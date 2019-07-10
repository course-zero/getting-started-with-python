# a tuple is like a list but we can not change the elements, it remains frozen
# a tuple length remains constants
a = (1,2,3,4,5)
print('simple tuple a', a)

# tuple is iterable
print('for loop values of a: ')
for val in a:
    print(val, end=" ")
print('')

# tuple can be created without paranthesis
# this is called as tuple packing
a = 1, 2, 3, 4, 5
print('type(a)', type(a), 'and a', a)

# a single element tuble must end with a comma
a = (1,)
b = (1)

print('single element => type(a)', type(a), 'value: ', a)
print('single element => type(b)', type(b), 'value: ', b)

# tuple elements can be of any type
a = (1, "Hello World!", True, [1,2,3], (1,))
print("tuple supports multiple data type", a)

# tuple is similar to a list, hence accesing and checking elements is similar
# tuple also support slicing

# changing tuple element
a = (1,2,3,4,5)
# a[0] = 10 # TypeError: 'tuple' object does not support item assignment

# since tuple length can not be changed, we don't have list methods like append/extend
# but we can check the index of an element and its count
a = (1,2,3,4,5)
print('a.index(3)', a.index(3))
print('a.count(3)', a.count(3))

# even tuple is immutable data type, it can contain a mutable data like a list which can be modified
a = (1,2,[3,4],5)
a[2][0] = 30
print('after mutation a=', a)

# one confusing thing people might say, tuple can be reassigned
# but we are just assigning different value to the label
a = (1,2,3)
a = (4,5,6) # assign `a` to a different value
print('a after reassigned', a)

# create tuple from a list (or iterable)
a = tuple( [1,2,3,4,5] )
print( 'tuple( [1,2,3,4,5] )', tuple( [1,2,3,4,5] ) )

# tuple comprehension
a = (x for x in range(10) if x % 2 == 0) # returns generator object
print('a tuple set comprehension', a)


# benefits of tuple over list : https://www.programiz.com/python-programming/tuple