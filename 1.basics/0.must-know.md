## Comments
```py
# This is a comment.

# python editor
# https://repl.it/languages/python3
```

```py
'''
This is not a
multi line comment (also tripple double-quotes).
This is still compiled by the interpreter
but does nothing.
https://www.python.org/dev/peps/pep-0257/#multi-line-docstrings
'''
```

## `print` function

```py
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
```

Print objects to the text stream file, separated by sep and followed by end. `sep`, `end`, `file` and `flush`, if present, must be given as keyword arguments.

https://docs.python.org/3/library/functions.html#print


```py
print(123)
# => 123

print("Hello World!")
# Hello World!

print("Hello", "World!")
# => Hello World!

print("Hello", "World!", sep=" - ")
# => Hello - World!

print( 4 * 2 )
# => 8

a, b = 4, 2
print( "a * b =", a * b )
# => a * b = 8

# https://docs.python.org/3/tutorial/inputoutput.html
print( "%d * %d = %d" %( a, b, (a * b) ) )
# => 4 * 2 = 8

print("{} * {} = {}".format( a, b, a * b ))
# => 4 * 2 = 8

print("{2}, {1} and {0}".format("mango", "bananas", "apple"))
# => apple, bananas and mango

print(1 == 1)
# => True

print( 1 != 1 )
# => False
```

## Multi-line code
The `\` character is used to put sequential code on the next line.

```py
a, b = 1, 2
c = a + \
    b
print( "c =", c )

# => c = 3
```

