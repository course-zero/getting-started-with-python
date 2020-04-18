## Comments
```py
# This is a comment.

# python editor
# https://repl.it/languages/python3
```

### Not a comment
```py
'''
This is not a
multi line comment (also tripple double-quotes).
This is still compiled by the interpreter.
But unless assigned to a variable, it is immediately garbage collected.
https://www.codecademy.com/forum_questions/505ba3cfc6addb000200e33c
'''
```

## `print` function

```py
# https://docs.python.org/3/library/functions.html#print
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
```

The `print` function prints the objects received as arguments to a stream (_like STDOUT_). They can be separated by a string (_sep_) and ended with a string (_end_). The `sep`, `end`, `file` and `flush`, if present, must be given as keyword arguments.


```py

# single argument
print(123)
# => 123
print("Hello World!")
# Hello World!

# multiple arguments
print("Hello", "World!")
# => Hello World!

# custom separator
print("Hello", "World!", sep=" - ")
# => Hello - World!

# operations
print(1 == 1)
# => True
print( 1 != 1 )
# => False
print( 4 * 2 )
# => 8

# variables
a, b = 4, 2
print( "a * b =", a * b )
# => a * b = 8
```

### formatting options
https://docs.python.org/3/tutorial/inputoutput.html

#### Old way
```py
print( "%d * %d = %d" %( a, b, (a * b) ) )
# => 4 * 2 = 8
```


#### New way (_using `str.format()`_)
https://docs.python.org/3/library/string.html#format-string-syntax

```
# sequential order
print("{} * {} = {}".format( a, b, a * b ))
# => 4 * 2 = 8

# indexed values
print("{2}, {1} and {0}".format("Italy", "Mercedes", "Pizza"))
# => Pizza, Mercedes and Italy

# named values (all or mixed values)
print("{food}, {1} and {0}".format("Italy", "Mercedes", food="Pizza"))
# => Pizza, Mercedes and Italy

# width and precision
a, b = 4, 2
print( "a * b = {:10.2f}".format( a * b ) )
# => a * b =       8.00
```

> https://pyformat.info/


## Multi-line code
The `\` character is used to put sequential code on the next line.

```py
a, b = 1, 2
c = a + \
    b
print( "c =", c )

# => c = 3
```

