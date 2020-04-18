```py
# python supports function recursion
# if a function calls itself, it's a recursive function
# when a function calls itself, code will pause until it returns a value

# get factorial of a number
# !n = n * !(n-1)
def factorialFunc(num):
    if( num == 1 ):
        return 1
    else:
        return num * factorialFunc( num - 1 )
    
result = factorialFunc( 4 ) # 4 * 3 * 2 * 1 = 24
print( 'factorialFunc( 4 ) => ', result )
# => factorialFunc( 4 ) =>  24
```

```py
# count n fibonacci numbers
# fibonacci numbers = 1, 1, 2, 3, 5, 8, ...
def fibonacciSeries( count ):
    result = [1, 1]

    for i in range(count-2):
        result.append( sum( result[-2:] ) )

    return result

print( 'fibonacciSeries(7) => ', fibonacciSeries(7) )
# => fibonacciSeries(7) =>  [1, 1, 2, 3, 5, 8, 13]
```