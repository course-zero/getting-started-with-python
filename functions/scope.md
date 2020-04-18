```py
# all variables declared inside has scope of that function
# it does not pollute outside scope
# arguments are also live in function's scope
def myFuncA( num ):
    result = num ** num
    return result

print( "myFuncA(3) => ", myFuncA( 3 ) )
# => myFuncA(3) =>  27
# print( num ) # NameError: name 'num' is not defined
# print( result ) # NameError: name 'result' is not defined
```

```py
# variables in python are lexically scoped
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

```py
# python can not override variable from the outer scope
# it always create new variable in function scope
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

```py
# variables defined on file level scope are called as `global` variables
# variables defined inside a function are called as `local` variables
# to override a global variable, we need to tell python, it is a global variable using `global` keyword
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

# => myFuncD-scope: fruit =>  Apple
# => myFuncD-scope: drink =>  Virgin Mojito
# => global-scope: fruit =>  Apple
```

```py
# if a global variable is not defined, using `global` variable, it can be created
def myFuncE():
    global car # define fruit as global, but doesn't create one
    
    car = "Mercedes" # create global variable if not present and assign a value

    print("myFuncE-scope: car => ", car)

myFuncE()
print("global-scope: car => ", car)

# => myFuncE-scope: car =>  Mercedes
# => global-scope: car =>  Mercedes
```

```py
# inner python function can also use `global` keyword
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

```py
# since a new variable is always created inside an inner function
# when we assign a value to a variable if it is coming from lexical scope
# `global` is useful to use variables from global scope
# to use variable from lexical scope, we need to use `nolocal` keyword
# warning: unline `global` keyword, `nolocal` does not create a variable in any of the outer scopes
# warning: nonlocal does not work for variables coming from global scope, have to use `global`
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

```py
# like JavaScript, python hoists variables in a function scope without assiging any alue
# hence below example would fail
originalValue = 2
def myFuncH():
    originalValue = originalValue * 2 # multiply global value by 2 and create local variable
    print( "myFuncH-scope: originalValue => ", originalValue )

myFuncH() # UnboundLocalError: local variable 'originalValue' referenced before assignment
```