## Function Definiton
- Python function is defined using `def` keyword.
- function name follows the same rule of variable defintion (https://www.programiz.com/python-programming/keywords-identifier#rules)


```py
def helloFunction():
    print( "helloFunction() => ", "Hello World" )

helloFunction()

# => helloFunction() =>  Hello World
```

## Python functions can have optional **docstring**
```py
def docFunction():
    """
    This is a documentation line for the docFunction.
    This can help user understand what the function does.
    """
    print( "docFunction() => ", "I am important!" )

print( docFunction.__doc__ )
# =>    This is a documentation line for the docFunction.
# =>    This can help user understand what the function does.
```

## Python function can take arguments
```py
def printGreeting( userName ):
    print( "printGreeting() => ", "Hello {}!".format( userName ) )

printGreeting( "John Doe" )
# => printGreeting() =>  Hello John Doe!
```

## Python function can return values
```py
# any code after return statement is ignored without warning or an error
def sumTwoNumbers( num1, num2 ):
    return num1 + num2

print( "sumTwoNumbers(11, 22) => ", sumTwoNumbers(11, 22) )
# => sumTwoNumbers(11, 22) =>  33
```

## Nesting functions
```py
def squareOfSum( num1, num2 ):
    def squareNum( input ):
        return input * input

    sumResult = num1 + num2
    squareResult = squareNum( sumResult )
    return squareResult

print( "squareOfSum(2, 3) => ", squareOfSum(2, 3) )
# => squareOfSum(2, 3) =>  25
```

## Defining function in one line
```py
# you can use multiple statements separated by `;`
def squareMe( num ): return num * num

print( "squareMe(2) => ", squareMe(2) )
# => squareMe(2) =>  4
```

## Use of `pass` keyword
```py
def toDoFunction():
    pass
toDoFunction()
# => 
```
