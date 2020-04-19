## Variables and Arguments scope
- All variables declared inside the function body have scope of that function.
- They do not pollute outside scope.
- Arguments also live in function's scope.

```py
def myFuncA( num ):
    result = num ** num
    return result

print( "myFuncA(3) => ", myFuncA( 3 ) )
# => myFuncA(3) =>  27
# print( num ) # NameError: name 'num' is not defined
# print( result ) # NameError: name 'result' is not defined
```

## Lexical scope
```py
firstName = "John"
def myFuncB( lastName ):
    print("myFuncB: firstName, lastName => ", firstName, lastName )
    
    age = 26
    def myInnerFuncB( gender ):
        email = "john@email.net"
        print("myInnerFuncB: firstName, lastName, age, gender, email => ", firstName, lastName, age, gender, email )
    
    myInnerFuncB( "Male" )

myFuncB( "Doe" )

# => myFuncB: firstName, lastName =>  John Doe
# => myInnerFuncB: firstName, lastName, age, gender, email =>  John Doe 26 Male john@email.net
```

## Overriding variables
- You can not override variable from the outer scope.
- It always create new variable in the function scope.

```py
firstName = "John"
def myFuncC( lastName ):
    firstName = "Mike"
    
    gender = "Male"
    age = 26
    def myInnerFuncC( gender ):
        age = 27
        print("myInnerFuncC-scope: gender => ", gender )
        print("myInnerFuncC-scope: age => ", age )
    
    myInnerFuncC( "Female" )
    print( "myFuncC-scope: firstName => ", firstName )
    print( "myFuncC-scope: lastName => ", lastName )
    print( "myFuncC-scope: gender => ", gender )
    print( "myFuncC-scope: age => ", age )

myFuncC( "Doe" )
print( "global-scope: firstName => ", firstName )

# => myInnerFuncC-scope: gender =>  Female
# => myInnerFuncC-scope: age =>  27
# => myFuncC-scope: firstName =>  Mike
# => myFuncC-scope: lastName =>  Doe
# => myFuncC-scope: gender =>  Male
# => myFuncC-scope: age =>  26
# => global-scope: firstName =>  John
```

## Use of the `global` keyword
- Variables defined on file level scope are called as **global** variables.
- variables defined inside the function body are called as **local** variables.
- To override a global variable, we need to tell Python it is a global variable using `global` keyword.
```py
fruit = "Mango"
drink = "Vanilla Shake"
def myFuncD():
    global fruit # define fruit as global
    
    fruit = "Apple" # change its value
    drink = "Virgin Mojito" # creates a local variable

    print("myFuncD-scope: fruit => ", fruit)
    print("myFuncD-scope: drink => ", drink)

myFuncD()
print("global-scope: fruit => ", fruit)
print("global-scope: drink => ", drink)


# => myFuncD-scope: fruit =>  Apple
# => myFuncD-scope: drink =>  Virgin Mojito
# => global-scope: fruit =>  Apple
# => global-scope: fruit =>  Vanilla Shake


# If a global variable is not defined, using `global` variable, it can be created.
def myFuncE():
    global car # define fruit as global, but doesn't create one
    
    car = "Mercedes" # create global variable if not present and assign a value

    print("myFuncE-scope: car => ", car)

myFuncE()
print("global-scope: car => ", car)

# => myFuncE-scope: car =>  Mercedes
# => global-scope: car =>  Mercedes

# Inner python function can also use `global` keyword
def myFuncF():
    country = "India" # creates a local variable

    def myInnerFuncF():
        global country # define country as global variable

        country = 'Denmark' # assign a value to global variable

        print("myInnerFuncF-scope: country => ", country)

    myInnerFuncF()
    print("myFuncF-scope: country => ", country)

myFuncF()
print("global-scope: country => ", country)

# => myInnerFuncF-scope: country =>  Denmark
# => myFuncF-scope: country =>  India
# => global-scope: country =>  Denmark
```

## Use of `nolocal` keyword
- A new variable is always created inside an inner function if we assign a value to a variable even if the same variable is passed to the inner fuction lexically.
- The `global` keyword is only useful to use variables from global scope.
- To override variable from lexical scope, we need to use `nolocal` keyword.
- However, unlike `global` keyword, `nolocal` does not create a variable in any of the outer scopes.
- The `nonlocal` does not work for variables coming from global scope, have to use `global` keyword.

```py
def myFuncG():
    color = 'red'
    taste = 'sweet'
    mood = 'happy'

    def myInnerFuncG():
        nonlocal color # comes from myFuncG-scope

        color = 'green'
        taste = 'sour'

        def myNestedInnerFuncG():
            nonlocal mood # comes from myFuncG-scope

            mood = 'sad'

            # color comes from myFuncG-scope as well
            print("myNestedInnerFuncG-scope: color, taste, mood => {}, {}, {}".format( color, taste, mood ))

        myNestedInnerFuncG()
        print("myInnerFuncG-scope: color, taste, mood => {}, {}, {}".format( color, taste, mood ))

    myInnerFuncG()
    print("myFuncG-scope: color, taste, mood => => {}, {}, {}".format( color, taste, mood ))

myFuncG()

# => myNestedInnerFuncG-scope: color, taste, mood => green, sour, sad
# => myInnerFuncG-scope: color, taste, mood => green, sour, sad
# => myFuncG-scope: color, taste, mood => => green, sweet, sad
```

## Hoisting
```py
# Like JavaScript, functions and variables are hoisted in Python.
# However, hoisted variable are not assigned with an initial value.
originalValue = 2
def myFuncH():
    originalValue = originalValue * 2 # multiply global value by 2 and create local variable
    print( "myFuncH-scope: originalValue => ", originalValue )

myFuncH() # UnboundLocalError: local variable 'originalValue' referenced before assignment
```
