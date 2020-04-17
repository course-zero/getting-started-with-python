```py
# what is hashable: https://www.quora.com/What-are-hashable-types-in-Python
# hashable: https://www.pythonforthelab.com/blog/what-are-hashable-objects/

# unordered mutable key:value pair
a = {'firstName': "John", 'lastName': "Doe"}
print('type of a', type(a))
# => type of a <class 'dict'>
print('simple dict a', a)
# => simple dict a {'firstName': 'John', 'lastName': 'Doe'}
```

```py
# key can be any immutable (hashable) data type with immutable elements
# value can be anything
key_string = "123"
key_number = 123
key_tuple = (1,2,3)
key_frozenset = frozenset([1,2,3])
a = {key_number: 1, key_number: 2, key_tuple: 3, key_frozenset: 4}

print('complex dict a', a)
# => complex dict a {123: 2, (1, 2, 3): 3, frozenset({1, 2, 3}): 4}
```

```py
# problem with immutable key but mutable elements
key_tuple = (1,2,[3,4]) # contains mutable element
# a = {key_tuple: 1} # TypeError: unhashable type: 'list'

# accesing a value
# use a key which provides a unique hash
key_tuple = (1,2,3)
a = {'firstName': "John", key_tuple: "Doe", } # last comma is accepted
print("a['firstName']", a['firstName'], 'and a[key_tuple]', a[key_tuple])
# => a['firstName'] John and a[key_tuple] Doe
```

```py
# when key does not exist
# b = a['unknown_key'] # KeyError: 'unknown_key'
b = a.get('unknown_key') # no error, return None
c = a.get('unknown_key', 'unknown_value') # use default value
print('unknown key using get() b', b)
# => unknown key using get() b None
print('unknown key using get() c', c)
# => unknown key using get() c unknown_value
```

```py
# dictionary using dict()
a = dict({1: "one", 2: "two"})
print("using dict() a", a)
# => using dict() a {1: 'one', 2: 'two'}
```

```py
# dictionary from a list of tuples
a = dict([(1, "one"),(2, "two")]) # if more than 2 elements or less in tuple, ValueError: dictionary update sequence element #1 has length 3; 2 is required
print("dict using list of tuples a", a)
# => dict using list of tuples a {1: 'one', 2: 'two'}
```

```py
# empty dictionaty
a = {}
b = dict()
print('empty dictionaty {}', a, ' and type', type(a))
# => empty dictionaty {} {}  and type <class 'dict'>
print('empty dictionaty dict()', b, ' and type', type(b))
# => empty dictionaty dict() {}  and type <class 'dict'>
```

```py
# change element in dictionary
a = {1: 'On', 2: 'Two'}
a[1] = 'One'
print('a after change', a)
# => a after change {1: 'One', 2: 'Two'}
```

```py
# add new element
a = {1: 'One', 2: 'Two'}
a[3] = 'Three'
print('adding new element a', a)
# => adding new element a {1: 'One', 2: 'Two', 3: 'Three'}
```

```py
# remove an element
a = {1: 'One', 2: 'Two', 3: 'three', 4: 'Four'}
del a[1] # KeyError if key is missing
popped = a.pop(2) # returns value, KeyError if key is missing

print('after pop(2) a', a, ' and popped', popped)
# => after pop(2) a {3: 'three', 4: 'Four'}  and popped Two
```

```py
# pop a random element
a = {1: 'One', 2: 'Two', 3: 'three', 4: 'Four'}
popped_item = a.popitem()
print('after popitem a', a, ' and popped_item', popped_item)
# => after popitem a {1: 'One', 2: 'Two', 3: 'three'}  and popped_item (4, 'Four')
```

```py
# clear dict
a = {1: 'One', 2: 'Two', 3: 'three', 4: 'Four'}
a.clear()

print('after clear a', a)
# => after clear a {}
```

```py
# dict is mutable
a = {1: 'One', 2: 'Two', 3: 'three', 4: 'Four'}
b = a
b[1] = 'Ten'
print('a after mutation of b', a)
# => a after mutation of b {1: 'Ten', 2: 'Two', 3: 'three', 4: 'Four'
```

```py
# use copy() to deep clone
a = {1: 'One', 2: 'Two', 3: 'three', 4: 'Four'}
b = a.copy()
b[1] = 'Ten'
print('cop() : a after mutation of b', a)
# => cop() : a after mutation of b {1: 'One', 2: 'Two', 3: 'three', 4: 'Four'}
```

```py
# merge two dictionaries
a = {1: 'Ten', 2: 'Two'}
b = {1: 'One', 4: 'Four'}

a.update(b) # update a with b, override keys
print('after update() a', a, 'and b', b)
# => after update() a {1: 'One', 2: 'Two', 4: 'Four'} and b {1: 'One', 4: 'Four'}
```

```py
# merge two dictionies using + does not work
a = {1: 'Ten', 2: 'Two'}
b = {1: 'One', 4: 'Four'}
# c = a + b

# create a dictionary from keys, static method
interable = {1,2,3} # a set
a = dict.fromkeys(interable, 'default') # None if default is missing
print('a after fromKeys()', a)
# => a after fromKeys() {1: 'default', 2: 'default', 3: 'default'}
```

```py
# get tuples, returns list like object of type of dict_items
a = {1: 'One', 2: 'Two', 3: 'three', 4: 'Four'}
a_items = a.items()
print('items of a', a_items, 'type', type(a_items))
# => items of a dict_items([(1, 'One'), (2, 'Two'), (3, 'three'), (4, 'Four')]) type <class 'dict_items'>
```

```py
print('items of a_items')
for t in a_items:
    print(t, end=" ")
print('')
# => items of a_items
# => (1, 'One') (2, 'Two') (3, 'three') (4, 'Four')
```

```py
# get keys, returns list like object of type of dict_keys
a = {1: 'One', 2: 'Two', 3: 'three', 4: 'Four'}
a_keys = a.keys()
print('keys of a', a_keys, 'type', type(a_keys))
# => keys of a dict_keys([1, 2, 3, 4]) type <class 'dict_keys'>
```

```py
# get values, returns list like object of type of dict_values
a = {1: 'One', 2: 'Two', 3: 'three', 4: 'Four'}
a_values = a.values()
print('value of a', a_values, 'type', type(a_values))
# => value of a dict_values(['One', 'Two', 'three', 'Four']) type <class 'dict_values'>
```

```py
# upsert operation
a = {1: 'One', 2: 'Two'}
return_1 = a.setdefault(1) # sets None if 1 key is missing
return_3 = a.setdefault(3, 'Three') # None if default value is not provided
print('a after setdefault', a, 'return_1', return_1, 'return_3', return_3)
# => a after setdefault {1: 'One', 2: 'Two', 3: 'Three'} return_1 One return_3 Three
```

```py
# dictionary comprehnsion
a = {v: str(v) for v in range(5)} # you can use if statement
print('a as dict comprehension', a)
# => a as dict comprehension {0: '0', 1: '1', 2: '2', 3: '3', 4: '4'}
```

```py
# check if key exist
a = {1: 'One', 2: 'Two', 3: 'three', 4: 'Four'}
print('1 in a', 1 in a)
# => 1 in a True
print('5 in a', 5 not in a)
# => 5 in a True
```

```py
# nested dictionary
user = {'id_1': { 'name': 'Mike' }, 'id_2': { 'name': 'John', 'email': 'john@x.com' }}
mike = user['id_1']
mike_name = user['id_1']['name'] # same as mike['name']
del user['id_2']['email'] # delete nested key
print('mested dictionary user', user, 'mike_name', mike_name)
# => mested dictionary user {'id_1': {'name': 'Mike'}, 'id_2': {'name': 'John'}} mike_name Mike
```