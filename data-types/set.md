```py
# a set is an unordered collection of unique elements
a = {1,2,3}
print('set a', a)
# => set a {1, 2, 3}
```

```py
# check type
print('type of a', type(a))
# => type of a <class 'set'>
```

```py
# mixed elements
a = {1,2,True,"Hello World"}
print('mixed set a', a)
# => mixed set a {1, 2, 'Hello World'}
```

```py
# a set will filter duplicate elements
a = {1,2,3,4,4,5}
print('duplicate elements set', a)
# => duplicate elements set {1, 2, 3, 4, 5}
```

```py
# a set, unlike tuple, must not contain mutable elements
# a = {1,2,[3,4]} # TypeError: unhashable type: 'list' ==> https://stackoverflow.com/questions/14535730/what-does-hashable-mean-in-python
# a = {1,2,(1,2,[3,4])} # error if tuple contains nested mutable elements
# a = {1,2,{3,3,4}} # error as a set is mutable

# create set from a iterable
a = set([1,2,3,3,4])
print('set([1,2,3,3,4])', a)
# => set([1,2,3,3,4]) {1, 2, 3, 4}
```

```py
# empty set
print('type(set()), type({}) => ', type(set()), type({})) 
# => type(set()), type({}) =>  <class 'set'> <class 'dict'>
```

```py
# since set is unordered, we can not access the elements
a = {1,2,3}
b = a[0] # => TypeError: 'set' object is not subscriptable

# to add new element, use add method
a = {1,2,3}
a.add(4)
print('after add() a =>', a)
# => after add() a => {1, 2, 3, 4}
```

```py
# set is mutable, hence use copy() to clone a set
a = {1,2,3}
b = a
c = a.copy()

b.add(4)
c.add(5)

print('set a after add operations on b & c', a)
# => set a after add operations on b & c {1, 2, 3, 4}
```

```py
# to add elements from a iterable, use update method
a = {1,2,3}
a.update([4,5],(6,7,7),{8,9},"GAMMA") # single level only
print('after update() =>', a)
# => after update() => {1, 2, 3, 4, 5, 6, 7, 8, 9, 'M', 'G', 'A'}
```

```py
# merge two dictionaries using + operator does not work
a = {1,2,3}
b = {3,4,5}
# c = a + b # => TypeError: unsupported operand type(s) for +: 'set' and 'set'

# remove element from a set
a = {1,2,3,4,5}
a.discard(1) # one argument, non iterable
# a.remove(20) # same as discard but raise value KeyError if element doesn't exist
print('after removal a =>', a)
# => after removal a => {2, 3, 4, 5}
```

```py
# pop an element
# for empty set, raises KeyError
a = {1,2,3,4,5}
b = a.pop() # remove arbitary element as set is unordered
print(a, b)
# => {2, 3, 4, 5} 1
```

```py
# empty a set
a = {1,2,3,4,5}
a.clear()
print('after clear() a =>', a)
# => after clear() a => set()
```

```py
# set operations #
a = {4,5,6,7,8,9}
b = {1,20,3,40,5,6,70,8,90}

# union of the set (all elements combined without duplicates)
union = a | b # same as a.union(b) or b.union(a)
print('union', union)
# => union {1, 3, 4, 5, 6, 7, 8, 9, 70, 40, 20, 90}
```

```py
# intersection of set (all common elements)
# a.intersection_update(b): to update set a with results
intersection = a & b # same as a.intersection(b) and b.intersection(a)
print('intersection', intersection)
# => intersection {8, 5, 6}
```

```py
# difference:  A - B yields all elements of A without matching elements of B
# a.difference_update(b) :to update set a with results
difference_a_min_b = a - b # a.difference(b) # elements of a, which are not in b
difference_b_min_a = b - a # b.difference(a) # elements of b, which are not in a

print('difference_a_min_b', difference_a_min_b)
# => difference_a_min_b {9, 4, 7}
print('difference_b_min_a', difference_b_min_a)
# => difference_b_min_a {1, 3, 70, 40, 20, 90}
```

```py
# symmetric difference (common elements)
# a.symmetric_difference_update(b) : to update set a with results
sym_diff = a ^ b # same as a.symmetric_diiference(b) or b.symmetic_difference(a)
print('sym_diff', sym_diff)
# => sym_diff {1, 3, 4, 70, 40, 9, 7, 20, 90}
```

```py
# isdisjoint: two sets are disjoint if they have no common elements
a = {1,2,3}
b = {4,5,6}
a_b_is_disjoint = a.isdisjoint(b) # same as b.disjoint(a)
print('a_b_is_disjoint', a_b_is_disjoint)
# => a_b_is_disjoint True
```

```py
# issubset: if elements of one set exits in another
a = {1,2,3}
b = {1,2,3,4,5,6,7,8,9}

is_a_subset_of_b = a.issubset(b) # yes, all elements of a in b
is_b_subset_of_a = b.issubset(a) # no, all elements of b does not comtain in a

print('is_a_subset_of_b', is_a_subset_of_b)
# => is_a_subset_of_b True
print('is_b_subset_of_a', is_b_subset_of_a)
# => is_b_subset_of_a False
```

```py
# superset: when one set contains elements of another
a = {1,2,3}
b = {1,2,3,4,5,6,7,8,9}

is_a_superset_of_b = a.issuperset(b) # no, as a does not contain all elements of b
is_b_superset_of_a = b.issuperset(a) # yes, as b contains all elements of a

print('is_a_superset_of_b', is_a_superset_of_b)
# => is_a_superset_of_b False
print('is_b_superset_of_a', is_b_superset_of_a)
# => is_b_superset_of_a True
```

#####################################################

```py
# python set implements iterable interface
a = {1,2,3,4,5}
print("for loop on set a =>", end=" ")
for val in a:
    print(val, end=" ")
print("")
# => for loop on set a => 1 2 3 4 5 
```

```py
# check if item exists in a set
a  = {1,2,3}
print('2 in a', 2 in a)
# => 2 in a True
print('4 not in a', 4 not in a)
# => 4 not in a True
```

```py
# set comprehension
a = {x for x in range(10) if x % 2 == 0}
print('a from set comprehension', a)
# => a from set comprehension {0, 2, 4, 6, 8}
```

```py
# a fronzenset is immutable set. Like tuple is immutable list, a frozenset is immutable set.
# but a frozenset provides API to interate theough its elements
a = frozenset([1,2,4,3,4,1]) # from a list
b = frozenset({5,66,5,8,66}) # from a set # any iterable works
print('frozenset a and b', a, b)
# => frozenset a and b frozenset({1, 2, 3, 4}) frozenset({8, 66, 5})
```

```py
# methods
# all methods except add or update as they will try to change the set

# other built-in important methods
# https://www.programiz.com/python-programming/methods/set
```