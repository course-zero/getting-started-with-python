# a set is an unordered collection of unique elements
a = {1,2,3}
print('set a', a)

# check type
print('type of a', type(a))

# mixed elements
a = {1,2,True,"Hello World"}
print('mixed set a', a)

# a set will filter duplicate elements
a = {1,2,3,4,4,5}
print('duplicate elements set', a)

# a set, unlike tuple, must not contain mutable elements
# a = {1,2,[3,4]} # TypeError: unhashable type: 'list'
# a = {1,2,(1,2,[3,4])} # error if tuple contains nested mutable elements
# a = {1,2,{3,3,4}} # error as a set is mutable

# create set from a iterable
a = set([1,2,3,3,4])
print('set([1,2,3,3,4])', a)

# empty set
print('type(set()), type({}) => ', type(set()), type({})) 

# since set is unordered, we can not access the elements
a = {1,2,3}
# b = a[0] #TypeError: 'set' object is not subscriptable

# to add new element, use add method
a = {1,2,3}
a.add(4)
print('after add() a =>', a)

# set is mutable, hence use copy() to clone a set
a = {1,2,3}
b = a
c = a.copy()

b.add(4)
c.add(5)

print('set a after add operations on b & c', a)

# to add elements from a iterable, use update method
a = {1,2,3}
a.update([4,5],(6,7,7),{8,9},"GAMMA") # single level only
print('after update() =>', a)

# remove element from a set
a = {1,2,3,4,5}
a.discard(1) # one argument, non iterable
# a.remove(20) # same as discard but raise value KeyError if element doesn't exist
print('after removal a =>', a)

# pop an element
# for empty set, raises KeyError
a = {1,2,3,4,5}
b = a.pop() # remove arbitary element as set is unordered
print(a, b)

# empty a set
a = {1,2,3,4,5}
a.clear()
print('after clear() a =>', a)

#######################################

# set operations #
a = {4,5,6,7,8,9}
b = {1,20,3,40,5,6,70,8,90}

# union of the set (all elements combined without duplicates)
union = a | b # same as a.union(b) or b.union(a)
print('union', union)

# intersection of set (all common elements)
# a.intersection_update(b): to update set a with results
intersection = a & b # same as a.intersection(b) and b.intersection(a)
print('intersection', intersection)

# difference:  A - B yields all elements of A without matching elements of B
# a.difference_update(b) :to update set a with results
difference_a_min_b = a - b # a.difference(b) # elements of a, which are not in b
difference_b_min_a = b - a # b.difference(a) # elements of b, which are not in a

print('difference_a_min_b', difference_a_min_b)
print('difference_b_min_a', difference_b_min_a)

# symmetric difference (common elements)
# a.symmetric_difference_update(b) : to update set a with results
sym_diff = a ^ b # same as a.symmetric_diiference(b) or b.symmetic_difference(a)
print('sym_diff', sym_diff)

# isdisjoint: two sets are disjoint if they have no common elements
a = {1,2,3}
b = {4,5,6}
a_b_is_disjoint = a.isdisjoint(b) # same as b.disjoint(a)
print('a_b_is_disjoint', a_b_is_disjoint)

# issubset: if elements of one set exits in another
a = {1,2,3}
b = {1,2,3,4,5,6,7,8,9}

is_a_subset_of_b = a.issubset(b) # yes, all elements of a in b
is_b_subset_of_a = b.issubset(a) # no, all elements of b does not comtain in a

print('is_a_subset_of_b', is_a_subset_of_b)
print('is_b_subset_of_a', is_b_subset_of_a)

# superset: when one set contains elements of another
a = {1,2,3}
b = {1,2,3,4,5,6,7,8,9}

is_a_superset_of_b = a.issuperset(b) # no, as a does not contain all elements of b
is_b_superset_of_a = b.issuperset(a) # yes, as b contains all elements of a

print('is_a_superset_of_b', is_a_superset_of_b)
print('is_b_superset_of_a', is_b_superset_of_a)

#####################################################

# other important methods
# https://www.programiz.com/python-programming/methods/set