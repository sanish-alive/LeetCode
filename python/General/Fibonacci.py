def fibonacci(n):
    if n<=0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sequence = fibonacci(n-1)
        sequence.append(sequence[-1] + sequence[-2])
        return sequence
    
def fibonacciSeries(n, a=0, b=1):
    if n<=0:
        return []
    else:
        return [a]+fibonacciSeries(n-1, b, a+b);
    
    
def fibonacciLastNumber(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacciLastNumber(n-1) + fibonacciLastNumber(n-2)
print(fibonacci(10))
print(fibonacciSeries(10))
print(fibonacciLastNumber(11))