n = 20


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


for i in range(2, n):
    fib1 = fibonacci(i)
    fib2 = fibonacci(i-1)
    ratio = fib1/fib2
    print(fib1, "/", fib2, "=", ratio)
