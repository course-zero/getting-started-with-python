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

# sample iterator
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


print( 'list(MyItr(5))', list(MyItr(5)) )
# you cam also use for loop