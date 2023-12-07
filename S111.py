def fib(n):
    fib1 = fib2 = 1
    for i in range(n):
        yield fib1
        fib1, fib2 = fib2, fib1 + fib2

for num in fib(200):
    print(num)