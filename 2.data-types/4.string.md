```py
# defined with single quotes
a = 'Hello World'
print("'Hello World' =", a)
# => 'Hello World' = Hello World
```

```py
# defined with double quotes
a = "Hello World"
print('"Hello World" =', a)
# => "Hello World" = Hello World
```

```py
# defined with mixed quotes
a = "Hello 'World'"
print('"Hello \'World\'" =', a)
# => "Hello 'World'" = Hello 'World'
```

```py
# special characters
a = "Hello\nWorld" # new line, \t for tab
print('"Hello\\nWorld" =', a)
# => "Hello\nWorld" = Hello
#    World
```

```py
# raw string
a = r"Hello\nWorld"
print('r"Hello\\nWorld" =', a)
# => r"Hello\nWorld" = Hello\nWorld
```

```py
# escape \ character
a = "Hello\\nWorld"
print(r'"Hello\\nWorld" =', a)
# => "Hello\\nWorld" = Hello\nWorld
```

```py
# escape quotes
a = "Hello \"World\""
print(r'"Hello \"World\"" =', a)
# => "Hello \"World\"" = Hello "World"
```

```py
# concat two string (only inline string and not variables)
a = "Hello " "World"
print('"Hello " "World" =', a)
# => "Hello " "World" = Hello World
```

```py
# concat two string using `+` operator
separator = " "
a = "Hello" + separator + "World"
print('"Hello" + separator + "World" =', a)
# => "Hello" + separator + "World" = Hello World
```

```py
# break multi line string using concat
a = ("Hello "
    "World")
print('("Hello "<break>"World") =', a)
# => ("Hello "<break>"World") = Hello World
```

```py
# multi line string (preserve indentation)
a = """Hello
    World"""
print('"""Hello<break>World""" =', a)
# => """Hello<break>World""" = Hello
#                              World
```

```py
# string on next line (\ is code separator)
a = "Hello\
    World"
print('"Hello\\<break>World" =', a)
# => "Hello\<break>World" = Hello    World
```

```py
# repeat a string
a = "hello:" * 3
print('"hello:" * 3 =', a)
# => "hello:" * 3 = hello:hello:hello:
```

```py
# string is a list (learn slicing in list) and hence iterable
a = "Hello World"
print("a[0:6] a[-5:] =", a[0:6], a[-5:])
# => a[0:6] a[-5:] = Hello  World
```

```py
# out of range safety
a = "Hello World"
print("a[0:60] =", a[0:60])
# => a[0:60] = Hello World
```

```py
# concat string slice
a = "Hello World"
print("'B' + a[1:] =", "B" + a[1:])
# => 'B' + a[1:] = Bello World
```

```py
# concat two string slice
a = "Hello World"
a = a[:6] + a[6:]
print("a[:6] + a[6:] =", a)
# => a[:6] + a[6:] = Hello World
```

```py
# string is read only list
a = "Hello World"
a[0] = "B"
print(a)
# => TypeError: 'str' object does not support item assignment
```

```py
# length of a string
a = "Hello World"
print("len(a) =", len(a))
# => len(a) = 11
```

```py
# convert number to a string
a = str(1.25)
print("str(1.25) =", a)
# => str(1.25) = 1.25
```