```py
# we can define an anoymous function in python and assign it to a variable
# this is done using `lambda` keyword
# syntax => lambda arguments: expression
# by default, lambda functions returns the value evaluated from the expression
# use lambda function when they need to be passed anonymously only

myLambdaA = lambda x: x * 2
myLambdaB = lambda name: print( "Hello " + name + "!" )

print( "myLambdaA", myLambdaA( 2 ) )
# => myLambdaA 4
print( "myLambdaB", myLambdaB( "John" ) )
# => Hello John!
# => myLambdaB None
```

```py
# lambda functions can take multiple arguments
myLambdaC = lambda x, y: x * y
print( "myLambdaC", myLambdaC( 3, 5 ) )
# => myLambdaC 15
```

```py
# lambda function can be defined with no arguments
myLambdaD = lambda: "SomeResult"
print( "myLambdaD", myLambdaD() )
# => myLambdaD SomeResult
```

```py
# lambda function arguments syntax is like normal function
myLambdaE = lambda name, *rest, gender="Female" : name + " : " + ( ",".join( rest ) ) + ' : ' + gender
print( "myLambdaE", myLambdaE( "John Doe", "Awesome", "Guy", gender="Male" ) )
# => myLambdaE John Doe : Awesome,Guy : Male
```

```py
# lambda function are useful when they need to be passed as argument to another higher order functions
nums = [1,2,3]
squares = map( lambda n: n * n, nums )
print( "squares", list(squares) )
# => squares [1, 4, 9]
```