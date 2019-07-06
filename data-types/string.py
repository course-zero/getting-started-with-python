# defined with single quotes
a = 'Hello World'
print("'Hello World' =", a)

# defined with double quotes
a = "Hello World"
print('"Hello World" =', a)

# defined with mixed quotes
a = "Hello 'World'"
print('"Hello \'World\'" =', a)

# special characters
a = "Hello\nWorld" # new line, \t for tab
print('"Hello\\nWorld" =', a)

# raw string
a = r"Hello\nWorld"
print('r"Hello\nWorld" =', a)

# escape \ character
a = "Hello\\nWorld"
print(r'"Hello\\nWorld" =', a)

# escape quotes
a = "Hello \"World\""
print(r'"Hello \"World\"" =', a)

# concat two string (only inline string and not variables)
a = "Hello " "World"
print('"Hello " "World" =', a)

# concat two string using `+` operator
separator = " "
a = "Hello" + separator + "World"
print('"Hello" + separator + "World" =', a)

# break multi line string using concat
a = ("Hello "
    "World")
print('("Hello "<break>"World") =', a)

# multi line string (preserve indentation)
a = """Hello
    World"""
print('"""Hello<break>World""" =', a)

# string on next line (\ is code separator)
a = "Hello\
    World"
print('"Hello\\<break>World" =', a)

# repeat a string
a = "hello:" * 3
print('"hello:" * 3 =', a)

# string is a list (learn slicing in list) and hence iterable
a = "Hello World"
print("a[0:6] a[-5:] =", a[0:6], a[-5:])

# out of range safety
a = "Hello World"
print("a[0:60] =", a[0:60])

# concat string slice
a = "Hello World"
print("'B' + a[1:] =", "B" + a[1:])

# concat two string slice
a = "Hello World"
a = a[:6] + a[6:]
print("a[:6] + a[6:] =", a)

# string is read only list
a = "Hello World"
#a[0] = "B"
#print(a)

# length of a string
a = "Hello World"
print("len(a) =", len(a))

# convert number to a string
a = str(1.25)
print("str(1.25) =", a)