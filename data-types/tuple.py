# a tuple is like a list but we can not change the elements, it remains frozen
# a tuple length remains constants
a = (1,2,3,4,5)
print('simple tuple a', a)

# tuple is iterable
print('for loop values of a: ')
for val in a:
    print(val, end=" ")
print('\n')

# tuple can be created without paranthesis
a = 1, 2, 3, 4, 5
print('type(a)', type(a), 'and a', a)

# a single element tuble must end with a comma
a = (1,)
b = (1)

print('single element => type(a)', type(a), 'value: ', a)
print('single element => type(b)', type(b), 'value: ', b)
