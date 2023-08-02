# def fibonacci(n):
#     if n<=0:
#         return[]
#     elif n == 1:
#         return [0]
#     elif n == 2:
#         return [0, 1]
#     else:
#         sequence = fibonacci(n-1)
#         sequence.append(sequence[-1] + sequence[-2])
#         return sequence

# fib = fibonacci(15)
# print(fib)


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
    
f = fibonacci(1000)
print(f)