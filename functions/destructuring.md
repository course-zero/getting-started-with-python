```py
# python provides a way to store selected elements from an iterator into variables with easy syntax
a, b, c = [ 1, 2, 3 ]
print( "a, b, c = [ 1, 2, 3 ] => ", a, b, c )
# => a, b, c = [ 1, 2, 3 ] =>  1 2 3

a, b, c = (1, 2, 3)
print( "a, b, c = (1, 2, 3) => ", a, b, c )
# => a, b, c = (1, 2, 3) =>  1 2 3
```

```py
# we can not provide less or more destruting variable than actual length of the iterator
# a, b = [ 1, 2, 3 ] # ValueError: too many values to unpack (expected 2)
# a, b, c, d = (1, 2, 3) # ValueError: not enough values to unpack (expected 4, got 3)

# but we can store rest arguments in a list using * notation
a, *rest = [ 1, 2, 3 ]
print( "a, *rest = [ 1, 2, 3 ] => ", a, rest )
# => a, *rest = [ 1, 2, 3 ] =>  1 [2, 3]

a, *rest, b = ( 1, 2, 3, 4 )
print( "a, *rest, b = ( 1, 2, 3, 4 ) => ", a, rest, b )
# => a, *rest, b = ( 1, 2, 3, 4 ) =>  1 [2, 3] 4
```

```py
# we can  use underscore to ignore values while destructuring
# use of _ : https://stackoverflow.com/a/5893946
a, _, b = [ 1, 2, 3 ]
print( "a, _, b = [ 1, 2, 3 ] => ", a, b )
# => a, _, b = [ 1, 2, 3 ] =>  1 3

a, *_, b = ( 1, 2, 3, 4 )
print( "a, *_, b = ( 1, 2, 3, 4 ) => ", a, b )
# => a, *_, b = ( 1, 2, 3, 4 ) =>  1 4
```

```py
# destructuring is useful in function with arbitrary arguments
myArgs = [1, 2, 3, 4]
def myFuncA( *args ):
    print( "myFuncA(*args) : args => ", args )

myFuncA(*myArgs)
# => myFuncA(*args) : args =>  (1, 2, 3, 4)
```

```py
# we can also destructure dictionary and pass to a function which only expect arbitrary keyword arguments
# but dictionary must have string keys
myKwArgs = { 'name': 'John', 'lastName': 'Doe', 'age': 26 }
def myFuncB( **kwargs ):
    print( "myFuncB(**kwargs) : kwargs => ", kwargs )

myFuncB(**myKwArgs)
# => myFuncB(**kwargs) : kwargs =>  {'name': 'John', 'lastName': 'Doe', 'age': 26}
```

