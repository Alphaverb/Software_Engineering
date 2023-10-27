def average(*args):
    if len(args) == 0:
        print('Вы не ввели число!')
        exit()
    result = sum(args) / len(args)
    return result

if __name__ == "__main__":
    num = input("Введите числа через пробел: ").split()
    arguments = [float(x) for x in num]
    result = average(*arguments)
    print(f"Среднее арифметическое: {result}")