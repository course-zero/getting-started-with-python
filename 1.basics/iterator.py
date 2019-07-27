# an iterator is an object which produces a value on succesive iteration 

# sample iterator class
# https://www.geeksforgeeks.org/iterators-in-python/
class MyItr:
    def __init__(self, limit):
        self.limit = limit
    
    # when iteration is initialized
    def __iter__(self):
        self.current = 0
        return self
    
    # get values sequentially
    def __next__(self):
        if self.current > self.limit:
            raise StopIteration
        else:
            returnVal = self.current
            self.current = self.current + 1
            return returnVal

# create iterator
myItr5 = MyItr(5)

# for loop
print('for loop on interable', end=" :=> ")
for elem in myItr5:
    print( elem, end=" " )
print('')

# convert iterable to a list
print( 'iterator: list(myItr5)', list(myItr5) )

# check element exist
print('iterator: 4 in myItr5', 4 in myItr5)

# convert list to an iterable
itr_list = iter([1,2,3,4,5])
print('itr_list', end=" :=> ")
for elem in itr_list:
    print( elem, end=" " )
print('')

# https://www.geeksforgeeks.org/python-range-method/
# https://stackoverflow.com/questions/31227536/what-is-the-difference-between-range0-2-and-listrange0-2
# https://pynative.com/python-range-function/

# in python 2.x, range() returns a list, which stores entire list in the memory.
# in python 3, range() returns a class of immutable iterable object that lets you iterate over it. This does not store the list in memory. This produces the element on the fly as we iterate over them. (borrowd from: https://stackoverflow.com/questions/31227536/what-is-the-difference-between-range0-2-and-listrange0-2)
# doc: https://docs.python.org/3/library/stdtypes.html#ranges

# range(stop)
a = range(5) # start from 0 to 5 (excluded)
print( 'range(5)', list(a) )

# range(start, stop)
a = range(2, 5) # exclude 5
print( 'range(2, 5)', list(a) )

# range(start,stop,step)
print( 'range(2,10)', list(range(2,10)) ) # default step: 1
print( 'range(2,10,2)', list(range(2,10,2)) ) # ignores 9
print( 'range(2,-10,-2)', list(range(2,-10,-2)) ) # ignores -9
print( 'range(2,10,-2)', list(range(2,10,-2)) ) # empty
#print( 'range(2,10,0)', list(range(2,10,0)) ) # ValueError for step 0

