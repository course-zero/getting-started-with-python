#https://riptutorial.com/python/example/14981/destructuring-assignment

# destructring or unpacking


# destructing a list
data = [1,2,3]
a, b, c = data
print('last a, b, c :=>', a, b, c)

# destructing a tuple
data = (1,2)
a, b = data
print('tuple a :=>', a, b)

# destructing a set
data = {1,2,2}
a, b = data
print('set a :=>', a, b)

# destructing a frozenset
data = frozenset([1,2,2])
a, b = data
print('frozenset a :=>', a, b)

# destructing a generator
data = (i*i for i in [1,2,3])
a, b, c = data
print('generator a :=>', a, b,c)

# destructing a range object
data = range(1,4)
a, b, c = data
print('range a :=>', a, b,c)

# must unpack all data
data = [1,2,3]
# a, b = data # ValueError: too many values to unpack (expected 2)
# a,b,c,d = data # ValueError: not enough values to unpack (expected 4, got 3)

# unpack values in a variable
data = [1,2,3,4,5]

a, *b = data # b is only referenced
print('a, *b = [1,2,3,4,5] :=> ', a, b)

a, *b, c = data
print('a, *b, c = [1,2,3,4,5] :=> ', a, b, c)


# ignoring values
# use of _ : https://stackoverflow.com/questions/5893163/what-is-the-purpose-of-the-single-underscore-variable-in-python
data = [1,2]
a, _ = data
print('a, _ = [1,2] :=> ', a)

data = [1,2,3,4,5]
a, *_ = data
print('a, *_ = [1,2,3,4,5] :=> ', a)

data = [1,2,3,4,5,6,7]
a, _, b, *_ = data
print('a, _, b, *_ = [1,2,3,4,5,6,7] :=> ', a, b)

# destructure a dictionary (but unordered)
# https://www.quora.com/Are-Python-dictionaries-unordered
data = {'name': 'John', 'age': 27, 'email': 'john@example.com'}
a, b, _ = data
print('dict: a, b, _ = data :=> ', a, b)

# destructure dict values (but unordered)
a, b, *_ = (data[key] for key in data)
print('destructure dict values :=> ', a, b)
