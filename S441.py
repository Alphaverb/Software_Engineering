def average(*args):
    if len(args) == 0:
        print('Вы не ввели число!')
        exit()
    print(args)
    result = sum(args) / len(args)
    return result

if __name__ == "__main__":
    result = average(10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
    print(f"Среднее арифметическое: {result}")