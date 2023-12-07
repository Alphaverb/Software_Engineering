def fib(n):
    fib1 = fib2 = 1
    with open('fib.txt', 'w') as file:
        for i in range(n):
            file.write(str(fib1) + '\n')
            yield fib1
            fib1, fib2 = fib2, fib1 + fib2

for num in fib(200):
    print(num)