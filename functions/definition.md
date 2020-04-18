```py
# python function is defined using `def` keyword
# function name follows the same rule of variable defintion (https://www.programiz.com/python-programming/keywords-identifier#rules)

def helloFunction():
    print( "helloFunction() => ", "Hello World" )

helloFunction()

# => helloFunction() =>  Hello World
```

```py
# python function can have optional docstring
def docFunction():
    """
    This is a documentation line for docFunction.
    This can help user understand what the function does.
    """
    print( "docFunction() => ", "I am important!" )

print( docFunction.__doc__ )
# =>    This is a documentation line for docFunction.
# =>    This can help user understand what the function does.
```

```py
# python function can take arguments
def printGreeting( userName ):
    print( "printGreeting() => ", "Hello {}!".format( userName ) )

printGreeting( "John Doe" )
# => printGreeting() =>  Hello John Doe!
```

```py
# python function can return values
# any code after return statement is ignored without warning or error
def sumTwoNumbers( num1, num2 ):
    return num1 + num2

print( "sumTwoNumbers(11, 22) => ", sumTwoNumbers(11, 22) )
# => sumTwoNumbers(11, 22) =>  33
```

```py
# python function can nest another function
def squareOfSum( num1, num2 ):
    def squareNum( input ):
        return input * input

    sumResult = num1 + num2
    squareResult = squareNum( sumResult )
    return squareResult

print( "squareOfSum(2, 3) => ", squareOfSum(2, 3) )
# => squareOfSum(2, 3) =>  25
```

```py
# we can also define function in one line
# you can use multiple statements separated by `;`
def squareMe( num ): return num * num

print( "squareMe(2) => ", squareMe(2) )
# => squareMe(2) =>  4
```

```py
# pass is used as a placeholder for function body
def toDoFunction():
    pass
toDoFunction()
# => 
```