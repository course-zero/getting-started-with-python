# this is a comment

'''
This is not a
multi line comment (also tripple double-quotes).
This is still compiled by the interpreter
but does nothing.
Hence indentation is very important.
'''

################################
# prints anything
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
print(123) 
print("Hello World!")

# variadic nature
print("Hello", "World!")
print("Hello", "World!", sep=" - ")

# can perform calculation
print( 4 * 2 )

# access variables and calculations
a, b = 4, 2
print( "a * b =", a * b )

# supports formatting
print( "%d * %d = %d" %( a, b, (a * b) ) )

# format using string (read more in string data type)
print("{} * {} = {}".format( a, b, a * b ))

################################

# equality check
print(1 == 1)

# not-equal check
print( 1 != 2 )

################################

# \ is used to put sequential code on the next line
a, b = 1, 2
c = a + \
    b
print( "c =", c )

# python editor
# https://repl.it/languages/python3