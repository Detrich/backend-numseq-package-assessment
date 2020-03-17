def fib(n):
    """returns the nth number of fibonnaci"""
    a = 0
    b = 1
    if n == 0:
        return a
    elif n == 1: 
        return b
    else:
        for _ in range(1,n):
            c = a + b
            a = b
            b = c
        return b

