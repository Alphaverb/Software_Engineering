values = input("Введите последовательность чисел: ").split()

list = [int(num) for num in values]
tuple = tuple(list)

print('Список: ', list)
print('Кортеж: ', tuple)
