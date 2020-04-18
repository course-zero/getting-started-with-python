```py
# when calling a function, you must provide all the arguments and in correct order
def myFuncA( firstName, lastName, gender ):
    print( "myFuncA: fullName, gender :=> {} {}, {} ".format( firstName, lastName, gender ) )

myFuncA( "John", "Doe", "Male" )
# => myFuncA: fullName, gender :=> John Doe, Male
# myFuncA( "John", "Doe" ) # TypeError: myFuncA() missing 1 required positional argument: 'gender'
```

```py
# you can change the order of arguments by specifying parameter names
# when an argument is provided using its position in function definition, it is called as positional argument
# when an argument is provided using parameter name, it is called as keyword argument
# positional arguments must come before keyword arguments in a function call
def myFuncB( firstName, lastName, gender ):
    print( "myFuncB: fullName, gender :=> {} {}, {} ".format( firstName, lastName, gender ) )

myFuncB( "John", gender = "Male", lastName = "Doe" )
# => myFuncB: fullName, gender :=> John Doe, Male 
# OR => myFuncB( gender = "Male", lastName = "Doe", firstName = "John" )
# myFuncB( gender = "Male", lastName = "Doe", "John" ) # SyntaxError: positional argument follows keyword argument
```

```py
# python function arguments can have default value
# by providing default value, they become optional
# a default argument be come after all non-default arguments, else "SyntaxError: non-default argument follows default argument" error is thrown
def myFuncC( firstName, lastName, gender = 'Male' ):
    print( "myFuncC: fullName, gender :=> {} {}, {} ".format( firstName, lastName, gender ) )

myFuncC( "John", "Doe" )
# => myFuncC: fullName, gender :=> John Doe, Male
```

```py
# python function can accept arbitrary length of arguments
# Python packs all arguments in a tuple
def myFuncD( *args ):
    result = 0

    for num in args:
        result += num
    
    print( "myFuncD() args, type => ", args, type( args ) )
    print( "myFuncD() result => ", result )

myFuncD( 1, 2, 3, 4, 5 )
# => myFuncD() args, type =>  (1, 2, 3, 4, 5) <class 'tuple'>
# => myFuncD() result =>  15
```

```py
# arbitrary arguments can be mixed with other named arguments
# since arbitrary arguments are position-only arguments as they lack parameter name, if function has arbitrary arguments as last parameter, function can not be called with keyword argument
def myFuncE( name, gender = 'Female', *score ):
    print( "myFuncE() name, gender, totalScore => ", name, gender, sum(score) )

myFuncE( 'John Doe', "Male", 60, 80 )
# => myFuncE() name, gender, totalScore =>  John Doe Male 140
# OK: myFuncE( 'John Doe' ) # John Doe Female 0
# OK: myFuncE( 'John Doe', "Male" ) # John Doe Male 0
# OK: myFuncE( 'John Doe', gender = "Male" ) # John Doe Male 0
# myFuncE( 'John Doe', gender="Male", 60, 80 ) SyntaxError: positional argument follows keyword argument
```

```py
# arbitrary arguments can be placed anywhere in the function definition
# but arguments coming after it must be called with parameter name AKA keyword-only argument
def myFuncF( name, *score, gender ):
    print( "myFuncF() name, gender, totalScore => ", name, gender, sum(score) )

# myFuncF( 'John Doe', 60, 80, gender ) TypeError: myFuncF() missing 1 required keyword-only argument: 'gender'
myFuncF( 'John Doe', 60, 80, gender = "Male" )
# => myFuncF() name, gender, totalScore =>  John Doe Male 140
```

```py
# to make a function only accept keyword arguments, use arbitrary arguments as first parameter without a parameter name
def myFuncG( *, firstName, lastName ):
    print( "myFuncG() fullName => ", firstName + lastName )

myFuncG( firstName = 'John', lastName = 'Doe' )
# => myFuncG() fullName =>  JohnDoe
# OR: myFuncG( lastName = 'Doe', firstName = 'John' )
# myFuncG( 'John', 'Doe' ) # TypeError: myFuncG() takes 0 positional arguments but 2 were given
```

```py
# python can also accept arbitrary keyword arguments
# all keyword arguments are stored in a dictionary
def myFuncH( **kwargs ):
    print( 'myFuncH() kwargs, type => ', kwargs, type( kwargs ) )

myFuncH( firstName = 'John', lastName = 'Doe', gender = 'Male' )
# => myFuncH() kwargs, type =>  {'firstName': 'John', 'lastName': 'Doe', 'gender': 'Male'} <class 'dict'>
```

```py
# arbitrary keyword arguments can be mixed with non-keyword arguments
# no arguments are allowed after arbitrary keyword arguments
# def myFuncI( fistName, lastName, **kwargs, rank = 0 ): pass # SyntaxError: invalid syntax
def myFuncI( fistName, lastName, **kwargs ): pass
```

```py
# arbitrary keyword arguments can be mixed with arbitrary arguments
# arbitrary arguments must come before arbitrary keyword arguments
def myFuncI( fistName, *args, **kwargs ): pass
```

```py
# in Python, arguments are passed by reference
uuid = 1
distances = [60, 80]
speeds = [ 20, 50 ]

def myFuncJ( _uuid, _distances, _speeds ):
    print( 'before: myFuncJ() uuid is _uuid',  uuid is _uuid )
    print( 'before: myFuncJ() distances is _distances',  distances is _distances )
    print( 'before: myFuncJ() speeds is _speeds',  speeds is _speeds )

    _uuid = 2 # override should assign new value
    _distances = [ 70, 90 ] # override should assign new value
    _speeds[ 0 ] = 30 # mutating the original list

    print( 'after: myFuncJ() uuid is _uuid',  uuid is _uuid )
    print( 'after: myFuncJ() distances is _distances',  distances is _distances )
    print( 'after: myFuncJ() speeds is _speeds',  speeds is _speeds )

myFuncJ( uuid, distances, speeds )
print( 'global-score :  uuid, distances, speeds =>  ',  uuid, distances, speeds )
# => before: myFuncJ() uuid is _uuid True
# => before: myFuncJ() distances is _distances True
# => before: myFuncJ() speeds is _speeds True
# => after: myFuncJ() uuid is _uuid False
# => after: myFuncJ() distances is _distances False
# => after: myFuncJ() speeds is _speeds True
# => global-score :  uuid, distances, speeds =>   1 [60, 80] [30, 50]
```